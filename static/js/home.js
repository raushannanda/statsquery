var nav = document.getElementById("nav")
var sticky = nav.offsetTop
var dropmenu = document.getElementById("dropmenu")
var menuicon = document.getElementById("mit")
window.onscroll = function(){
    if (window.pageYOffset > sticky) {
        nav.classList.add("sticky")
    }
    else {
        nav.classList.remove("sticky");
    }
}
function showdropmenu(){
    if (dropmenu.classList.contains('hidemenu')){
        dropmenu.classList.remove('hidemenu')
        dropmenu.classList.add('showmenu')
        dropmenu.style.display = "block"
        menuicon.classList.remove("fa-bars")
        menuicon.classList.add("fa-xmark")
    }else if(dropmenu.classList.contains("showmenu")){
        dropmenu.classList.remove('showmenu')
        dropmenu.classList.add('hidemenu')
        dropmenu.style.display = "none"
        menuicon.classList.remove("fa-xmark")
        menuicon.classList.add("fa-bars")
    }
}
