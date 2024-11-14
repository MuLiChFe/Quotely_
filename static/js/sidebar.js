// sidebar.js
document.addEventListener('DOMContentLoaded', function() {
    const offcanvas = document.getElementById('offcanvasScrolling');
    const hoverButton = document.getElementById('hoverButton');

    // 当鼠标进入 offcanvas 区域时保持显示
    offcanvas.addEventListener('mouseenter', function() {
        offcanvas.classList.remove('hiding');
        offcanvas.classList.add('show');  // 显示 offcanvas
    });

    // 当鼠标离开 offcanvas 区域时隐藏
    offcanvas.addEventListener('mouseleave', function() {
        offcanvas.classList.remove('show'); // 隐藏 offcanvas
        offcanvas.classList.add('hiding');
    });

    // 当鼠标进入按钮区域时，确保 offcanvas 可见
    hoverButton.addEventListener('mouseenter', function() {
        offcanvas.classList.remove('hiding')
        offcanvas.classList.add('show');  // 显示 offcanvas
    });
});
