let loadS = document.querySelector(".load")


window.addEventListener('load',()=>{
    var el = document.createElement("div");
    loadS.appendChild(el);
    
    var frames, duplicate, x, y;
    duplicate = loadS.innerHTML;
    loadS.innerHTML = duplicate.repeat(10);
    frames = loadS.children;
    setInterval(() => {
        x = document.documentElement.clientWidth -1, y = document.documentElement.clientHeight -100;
        for(var i = 0; i < frames.length; i++){
            frames[i].setAttribute("style","position:absolute; height:100px; width1px;left:" + Math.random() * x + "px;top:" + Math.random() * +y +"px;");
        }
    },1);
})