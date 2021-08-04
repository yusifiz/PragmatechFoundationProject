let box = document.querySelector('.box')
let bigBox = document.querySelector('.box-container')
let btnRight = document.querySelector('.btn-right')
let btnUp = document.querySelector('.btn-up')
let btnDown = document.querySelector('.btn-down')
let btnLeft = document.querySelector('.btn-left')
marginVal = 0;



btnRight.addEventListener('click',function(){
    let moveBox = document.querySelector('.box').style.marginLeft = `${marginVal}px`
    let moveForm = document.querySelector('.box').style.transition = "all .5s"
    marginVal +=20;

})
btnLeft.addEventListener('click',function(){
    let moveBox = document.querySelector('.box').style.marginRight = `${marginVal}px`
    let moveForm = document.querySelector('.box').style.transition = "all .5s"
    marginVal +=20;

})
btnUp.addEventListener('click',function(){
    let moveBox = document.querySelector('.box').style.marginBottom = `${marginVal}px`
    let moveForm = document.querySelector('.box').style.transition = "all .5s"
    marginVal +=20;

})
btnDown.addEventListener('click',function(){
    let moveBox = document.querySelector('.box').style.marginTop = `${marginVal}px`
    let moveForm = document.querySelector('.box').style.transition = "all .5s"
    marginVal +=20;

})