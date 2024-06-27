
console.log("hello")

const hide = document.getElementById("hide-nav")
const show = document.getElementById("show-nav")
const nav = document.getElementById("nav-menu")
const listitem = document.querySelectorAll(".nav-item li")
const cont = document.querySelector(".nav-co")
const bar = document.querySelector(".bar")

hide.addEventListener("click", function(){
    nav.style.width= "0px"
    nav.style.display = "none"
     show.style.display ="block"
})

show.addEventListener("click", function(){
    nav.style.width = "200px"
    show.style.display ="none"
    nav.style.display = "block"
})

listitem.forEach(item=> {
    item.addEventListener("click", function(){
        // listitem.forEach(li=> li.classList.add("hide"));
        cont.classList.add("hide")
        bar.classList.add("show")

        // this.classList.add("active")
    })
})