# 群聊报告生成器

## 任务描述
根据[我提供的]聊天记录，智能生成对应时间范围的报告（日报/周报/月报），输出为精美的HTML页面，适合截图分享。每个话题都将配备犀利有趣的深度评论。

## 报告类型自动识别
系统将根据您提供的时间范围自动选择报告类型：
- **日报**：当指定"今日"、"今天"或具体某一天时，提取 8-12 个核心话题
- **周报**：当指定"本周"、"这周"、"近一周"、"最近7天"时，提取 12-16 个重要话题  
- **月报**：当指定"本月"、"这个月"、"近一个月"、"最近30天"时，提取 16-24 个热门话题

## 深度评论系统
为每个话题生成一条犀利有趣的深度评论，风格特点：
- **人设**：年轻人，批判现实，思考深刻，语言风趣
- **风格**：融合Oscar Wilde、鲁迅、王朔、刘震云的表达方式
- **特色**：一针见血的隐喻，辛辣讽刺，抓住事物本质
- **表达**：用一句话通过隐喻和讽刺揭示话题的深层含义

### 评论示例
- 委婉 → "刺向他人时，决定在剑刃上撒上止痛药。"
- 内卷 → "所有人都在电梯里跳舞，以为这样能更快到达楼顶。"
- 摸鱼 → "在老板的眼皮底下练习如何优雅地浪费时间。"

## 自动提取信息
系统将自动从聊天记录中提取：
- **群名称**：从聊天记录的系统通知或常见群聊信息中提取
- **时间信息**：根据您指定的时间范围和聊天记录中的时间戳确定
- **报告标题**：根据时间范围自动生成（如"群日报"、"群周报"、"群月报"）

## 聊天记录支持格式
支持多种常见格式：

**基本消息格式:**
```
昵称(ID) 时间
消息内容
```

**示例:**
```
为"人民"币服务(dong349154) 05:28:11
![图片](http:///image/26c946122149f8a8a135e50e58d621e3)
```

**图片和链接格式:**
- 图片会以 `![图片](URL)` 的形式出现在消息内容中
- 链接会以 `[链接|链接描述 URL]` 或直接 `URL` 的形式出现在消息内容中

**合并转发消息格式:**
```
[合并转发|群聊的聊天记录]
 原始发送者昵称 时间
 消息内容
```

**动画表情格式:**
```
[动画表情]
```

**引用消息格式:**
```
> 昵称(ID) 时间
> 消息内容
```

## 输出要求
使用以下HTML模板结构，生成完整的HTML页面：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[群名称][报告类型] - [时间范围]</title>
    <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
    <div class="container">
        <!-- 头部信息 - 根据报告类型动态调整 -->
        <header>
            <div class="report-type">[日报/周报/月报]</div>
            <h1>[群名称]群聊[报告类型]</h1>
            <p class="date">[具体日期/时间范围]</p>
            <div class="meta-info">
                <div class="meta-info-item">
                    <span class="meta-icon">💬</span>
                    <span>总消息数：<strong>[数量]</strong></span>
                </div>
                <div class="meta-info-item">
                    <span class="meta-icon">👥</span>
                    <span>活跃用户：<strong>[数量]</strong></span>
                </div>
                <div class="meta-info-item">
                    <span class="meta-icon">⏱️</span>
                    <span>统计周期：<strong>[时间范围]</strong></span>
                </div>
            </div>
        </header>

        <!-- 1. 讨论热点 -->
        <section class="hot-topics">
            <h2>📊 [时间范围]讨论热点</h2>
            <div class="card-grid card-grid-2">
                <!-- 话题卡片模板 - 根据报告类型重复相应数量 -->
                <div class="card topic-card">
                    <div class="topic-card-header">
                        <h3>[热点话题名称]</h3>
                        <div class="topic-heat">
                            🔥 <span>[热度值]</span>
                        </div>
                    </div>
                    <span class="badge badge-primary">[话题分类]</span>
                    <p class="topic-summary">[话题简要总结，50-100字]</p>
                    
                    <div class="deep-comment">
                        <div class="comment-header">
                            <span class="comment-icon">🎯</span>
                            <span class="comment-label">评论</span>
                        </div>
                        <div class="comment-content">
                            <p class="comment-text">[犀利有趣的一句话深度评论]</p>
                        </div>
                    </div>
                    
                    <div class="topic-keywords">
                        <span class="keyword">#[关键词1]</span>
                        <span class="keyword">#[关键词2]</span>
                        <span class="keyword">#[关键词3]</span>
                    </div>
                    <div class="topic-stats">
                        <span class="badge badge-info">💬 [消息数]条讨论</span>
                        <span class="badge badge-info">👥 [参与人数]人参与</span>
                        <span class="badge badge-info">🕐 [讨论时长]</span>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- 2. 数据统计与可视化 -->
        <section class="analytics">
            <h2>📈 数据统计与分析</h2>
            
            <!-- 统计卡片 -->
            <div class="analytics-grid">
                <div class="stat-card">
                    <div class="stat-label">总消息数</div>
                    <div class="stat-number">[数量]</div>
                    <div class="stat-change">较[上期]增长 [百分比]%</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">活跃用户</div>
                    <div class="stat-number">[数量]</div>
                    <div class="stat-change">参与率 [百分比]%</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">平均响应时间</div>
                    <div class="stat-number">[时间]</div>
                    <div class="stat-change">分钟</div>
                </div>
            </div>
            
            <!-- 话题热度分布 -->
            <h3>🔥 话题热度分布</h3>
            <div class="heat-distribution">
                <div class="heat-item">
                    <div class="heat-header">
                        <span class="heat-topic">[话题名称]</span>
                        <span class="heat-percentage">[百分比]%</span>
                    </div>
                    <div class="heat-bar">
                        <div class="heat-fill" style="width: [百分比]%; background: linear-gradient(90deg, #667eea, #764ba2);"></div>
                    </div>
                    <div class="heat-stats">
                        <span>[消息数]条消息</span> · <span>[参与人数]人参与</span>
                    </div>
                </div>
            </div>
            
            <!-- 活跃度排行榜 -->
            <h3>🏆 活跃度排行榜</h3>
            <div class="participants-ranking">
                <div class="participant-card">
                    <div class="participant-rank rank-1">1</div>
                    <div class="participant-info">
                        <div class="participant-name">[群友昵称]</div>
                        <div class="participant-stats">
                            <span>💬 [消息数]条</span>
                            <span>⏱️ 平均[响应时间]分钟</span>
                            <span>🎯 参与[话题数]个话题</span>
                        </div>
                        <div class="participant-traits">
                            <span class="badge badge-secondary">[特征1]</span>
                            <span class="badge badge-secondary">[特征2]</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 时段活跃度分析 - 仅限日报/周报 -->
            <h3>⏰ 时段活跃度分析</h3>
            <div class="time-activity">
                <div class="time-chart">
                    <div class="time-slot" style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(102, 126, 234, 0.3));">
                        <div class="time-hour">00</div>
                        <div class="time-count">[消息数]</div>
                    </div>
                    <!-- 继续添加其他23个时段... -->
                </div>
            </div>
            
            <!-- 熬夜冠军 -->
            <h3>🌙 熬夜冠军</h3>
            <div class="night-owl-card card">
                <div class="owl-content">
                    <div class="owl-crown">👑</div>
                    <div class="owl-info">
                        <h4>[熬夜冠军昵称]</h4>
                        <p class="owl-title">"[称号，如：午夜守护者]"</p>
                        <div class="owl-stats">
                            <span>🕐 最晚活跃：[时间]</span>
                            <span>🌙 深夜消息：[数量]条</span>
                        </div>
                        <p class="owl-quote">"[最后一条深夜消息]"</p>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- 3. 词云展示 -->
        <section class="word-cloud">
            <h2>☁️ 热词云图</h2>
            <div class="cloud-container">
                <div class="cloud-3d">
                    <div class="cloud-layer">
                        <!-- 词云示例 - 根据实际词频和重要性调整大小和颜色 -->
                        <span class="cloud-word" style="left: 40%; top: 20%; font-size: 36px; color: #667eea; transform: translateZ(100px);">[热词1]</span>
                        <span class="cloud-word" style="left: 60%; top: 30%; font-size: 28px; color: #764ba2; transform: translateZ(80px);">[热词2]</span>
                        <!-- 建议40-60个词汇，分布在不同层次 -->
                    </div>
                </div>
                
                <div class="cloud-legend">
                    <div class="legend-item">
                        <span class="legend-dot" style="background-color: #667eea;"></span>
                        <span>[分类1] 相关</span>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- 4. 报告总结 -->
        <section class="summary">
            <h2>📝 [时间范围]总结</h2>
            <div class="card">
                <h3>核心洞察</h3>
                <ul>
                    <li><strong>[洞察点1]：</strong>[具体说明]</li>
                    <li><strong>[洞察点2]：</strong>[具体说明]</li>
                    <li><strong>[洞察点3]：</strong>[具体说明]</li>
                </ul>
                
                <h3>趋势分析</h3>
                <p>[根据报告类型，分析日/周/月的趋势变化]</p>
                
                <h3>建议与展望</h3>
                <p>[基于数据分析给出的建议]</p>
            </div>
        </section>
        
        <!-- 页脚信息 -->
        <footer>
            <div class="footer-info">
                <span>📊 数据来源：[群名称]</span>
                <span>📅 统计周期：[具体时间范围]</span>
                <span>🕐 生成时间：[当前时间]</span>
            </div>
            <p class="disclaimer">
                免责声明：本报告基于群聊公开讨论内容自动生成，仅供参考。如有不当内容，请联系管理员处理。
            </p>
        </footer>
    </div>

    <script src="../assets/script.js"></script>
</body>
</html>
```