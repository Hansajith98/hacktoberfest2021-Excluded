setInterval(() => {
    let i = document.getElementById("timer").innerHTML
    i = parseInt(i)
    i += 1;
    document.getElementById("timer").innerHTML = i
}, 1000)

document.addEventListener('visibilitychange', () => {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/play/switch", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        winsw: true
    }));
})