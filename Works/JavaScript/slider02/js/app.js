
function showBigImage(elem){
    let imgSrc=elem.querySelector('img').getAttribute('src');
    let bigImage=document.querySelector('.gallery-main-image img')
    bigImage.setAttribute('src',imgSrc)
    console.log(imgSrc)
}