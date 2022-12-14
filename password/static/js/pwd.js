function setPreview(json) {
    var title = document.getElementById('title');
    var user = document.getElementById('usuario');
    var password = document.getElementById('password');
    var url = document.getElementById('url');
    var page = document.getElementById('tpage');
    var text = JSON.parse(json);
    title.value = text.title;
    user.value = text.user;
    password.value = text.password;
    if (text.url == undefined){
        url.value = '';
    } else {
        url.value = text.url;
    }

    page.innerHTML = text.title;
}

function cleanPreview() {
    var title = document.getElementById('title');
    var user = document.getElementById('usuario');
    var password = document.getElementById('password');
    var url = document.getElementById('url');
    var page = document.getElementById('tpage');
    title.value = "";
    user.value = "";
    password.value = "";
    url.value = "https://wwww.";
    page.innerHTML = "Nova senha";
}

function copyPwd() {
    var value = document.getElementById('pwd').innerText;
    navigator.clipboard.writeText(value)
}

function copyPassword() {
    var value = document.getElementById('password').value;
    navigator.clipboard.writeText(value)
}