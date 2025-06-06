import re
import os
import datetime
import json
import asyncio
from contextlib import AsyncExitStack
from mcp import ClientSession
from mcp.client.sse import sse_client
from google import genai
from dotenv import load_dotenv
# 配置环境变量
MCP_BASE_URL = os.environ["MCP_BASE_URL"]
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
GROUP_MAP = json.loads(os.environ["GROUP_MAP_JSON"])

PROMPT_FILE = ".github/scripts/prompt.md"
DAILY_DIR = "daily"

client = genai.Client(api_key=GOOGLE_API_KEY)

# 加载 Prompt
def load_prompt():
    with open(PROMPT_FILE, encoding="utf-8") as f:
        return f.read()
    
# 请求 MCP 获取群聊记录 
def fetch_chat_log(talker: str, time: str) -> str:
    """
    请求 MCP 获取群聊记录
    
    Args:
        talker: 群聊名称或联系人名称
        time: 时间范围，如 "2024-01-01"
        
    Returns:
        str: 聊天记录文本
    """
    
    async def _fetch():
        exit_stack = AsyncExitStack()
        
        try:
            # 1. 连接到SSE服务器
            print(f"尝试连接到: {MCP_BASE_URL}")
            sse_cm = sse_client(MCP_BASE_URL)
            streams = await exit_stack.enter_async_context(sse_cm)
            print("SSE 流已获取。")
            
            # 2. 创建ClientSession
            session_cm = ClientSession(streams[0], streams[1])
            session = await exit_stack.enter_async_context(session_cm)
            print("ClientSession 已创建。")
            
            # 3. 初始化Session
            await session.initialize()
            print("Session 已初始化。")
            
            # 4. 调用chatlog工具
            result = await session.call_tool("chatlog", {
                "time": time,
                "talker": talker
            })
            
            # 5. 提取结果
            if result.content and len(result.content) > 0:
                return result.content[0].text
            else:
                return "未找到聊天记录"
                
        except Exception as e:
            return f"错误: {str(e)}"
        finally:
            # 清理资源
            await exit_stack.aclose()
    
    try:
        return asyncio.run(_fetch())
    except Exception as e:
        return f"执行错误: {str(e)}"
    

def extract_html_from_markdown(markdown_content: str) -> str:
    """
    从Markdown内容中提取HTML代码块
    支持多种格式的HTML代码块
    """
    
    # 方法1: 提取 ```html 代码块
    html_pattern = r'```html\s*\n(.*?)\n```'
    match = re.search(html_pattern, markdown_content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    # 方法2: 提取普通 ``` 代码块（如果内容看起来像HTML）
    code_pattern = r'```\s*\n(.*?)\n```'
    matches = re.findall(code_pattern, markdown_content, re.DOTALL)
    for code_block in matches:
        # 检查是否包含HTML标签
        if re.search(r'<html|<HTML|<!DOCTYPE', code_block, re.IGNORECASE):
            return code_block.strip()
    
    # 方法3: 查找从<!DOCTYPE或<html开始的完整HTML文档
    html_doc_pattern = r'(<!DOCTYPE[^>]*>.*?</html>|<html.*?</html>)'
    match = re.search(html_doc_pattern, markdown_content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    # 方法4: 如果没有找到明显的HTML，返回原内容（可能整个就是HTML）
    # 检查内容是否直接就是HTML
    if re.search(r'<html|<!DOCTYPE', markdown_content, re.IGNORECASE):
        return markdown_content.strip()
    
    # 如果都没找到，抛出异常
    raise ValueError("未找到有效的HTML内容")

def generate_html(prompt: str) -> str:
    """生成HTML报告并提取HTML内容"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20", 
        contents=prompt
    )
    
    # 从返回的markdown中提取HTML
    try:
        html_content = extract_html_from_markdown(response.text)
        return html_content
    except ValueError as e:
        print(f"⚠️ HTML提取失败: {e}")
        print("📝 原始响应内容预览:")
        print(response.text[:500] + "..." if len(response.text) > 500 else response.text)
        
        # 如果提取失败，可以选择返回原内容或抛出异常
        return response.text  # 或者 raise e

# 保存 HTML 文件
def save_html(content: str, filename: str):
    os.makedirs(DAILY_DIR, exist_ok=True)
    with open(os.path.join(DAILY_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

def main():
    date_str = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    prompt_template = load_prompt()

    for group_name, file_prefix in GROUP_MAP.items():
        print(f"⏳ 生成群聊：{group_name}")
        try:
            chat_log = fetch_chat_log(group_name, date_str)
            full_prompt = f"{group_name}{date_str}的聊天记录```\n{chat_log}\n\n```{prompt_template}"
            html = generate_html(full_prompt)
            filename = f"{file_prefix}_{date_str}.html"
            save_html(html, filename)
            print(f"✅ 成功生成 {filename}")
        except Exception as e:
            print(f"❌ 群聊 {group_name} 处理失败：{e}")

if __name__ == "__main__":
    main()
