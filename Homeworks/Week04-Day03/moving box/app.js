let box = document.querySelector('.box')
let bigBox = document.querySelector('.box-container')
let btnRight = document.querySelector('.btn-right')
let btnUp = document.querySelector('.btn-up')
let btnDown = document.querySelector('.btn-down')
let btnLeft = document.querySelector('.btn-left')
marginValRight = 0;
marginValLeft = 0;
marginValUp = 0;
marginValDown = 0;


btnRight.addEventListener('click',function(){
    let moveBox = document.querySelector('.box').style.marginLeft = `${marginValRight}px`
    let moveForm = document.querySelector('.box').style.transition = "all .5s"
    marginValRight +=20;

})
btnLeft.addEventListener('click',function(){
    let moveBox = document.querySelector('.box').style.marginRight = `${marginValLeft}px`
    let moveForm = document.querySelector('.box').style.transition = "all .5s"
    marginValLeft +=20;

})
btnUp.addEventListener('click',function(){
    let moveBox = document.querySelector('.box').style.marginBottom = `${marginValUp}px`
    let moveForm = document.querySelector('.box').style.transition = "all .5s"
    marginValUp +=20;

})
btnDown.addEventListener('click',function(){
    let moveBox = document.querySelector('.box').style.marginTop = `${marginValDown}px`
    let moveForm = document.querySelector('.box').style.transition = "all .5s"
    marginValDown +=20;

})