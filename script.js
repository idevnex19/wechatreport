// 群聊报告交互脚本 - script.js
// 可选：添加一些交互效果
document.addEventListener('DOMContentLoaded', function() {
    // 为卡片添加渐入动画
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
    
    // 词云交互
    const cloudWords = document.querySelectorAll('.cloud-word');
    cloudWords.forEach(word => {
        word.addEventListener('mouseenter', function() {
            this.style.transform = `scale(1.2) translateZ(${parseInt(this.style.transform.match(/\d+/)[0]) + 20}px)`;
        });
        word.addEventListener('mouseleave', function() {
            this.style.transform = this.style.transform.replace(/scale\([\d.]+\)\s*/, '');
        });
    });
    
    // 时段图表交互
    const timeSlots = document.querySelectorAll('.time-slot');
    timeSlots.forEach(slot => {
        slot.addEventListener('click', function() {
            // 可以添加点击展开详情的功能
            console.log('点击了时段：', this.querySelector('.time-hour').textContent);
        });
    });
    
    // 热度条动画
    const heatFills = document.querySelectorAll('.heat-fill');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.width = entry.target.getAttribute('data-width') || '0%';
            }
        });
    });
    
    heatFills.forEach(fill => {
        observer.observe(fill);
    });
});