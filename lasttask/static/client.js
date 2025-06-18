(function () {
    const info = document.createElement("div");
    info.innerText = "Загрузка данных...";
    info.style.position = "fixed";
    info.style.bottom = "10px";
    info.style.right = "10px";
    info.style.padding = "5px";
    info.style.background = "#fff";
    info.style.border = "1px solid #ccc";
    info.style.fontSize = "12px";
    document.body.appendChild(info);

    const data = {
        timestamp: Date.now(),
        userAgent: navigator.userAgent,
        screen: { w: window.screen.width, h: window.screen.height }
    };

    fetch("https://your-domain/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    }).then(()=>{ info.innerText="Загружено"; })
      .catch(()=>{ info.innerText="Ошибка"; });
})();
