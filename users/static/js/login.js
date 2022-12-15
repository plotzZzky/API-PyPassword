//LoginTabs
function show_login(tab) {
    set_tabs_inactive();
    document.getElementById("Login").style.display = "block";
    tab.id = "tab-active";
    document.getElementById("Signup").style.display = "none";
}


function show_signup(tab) {
    set_tabs_inactive();
    document.getElementById("Login").style.display = "none";
    tab.id = "tab-active";
    document.getElementById("Signup").style.display = "block";
}

function set_tabs_inactive() {
    var elements = document.getElementsByClassName('tablinks');
    for (var i in elements) {
        if (elements.hasOwnProperty(i)) {
        elements[i].id = " ";
    }
    }
}

