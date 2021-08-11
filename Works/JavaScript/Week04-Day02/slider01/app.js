var slide = document.getElementsByClassName("sliderImg");

var slideSay = slide.length;

var slideNo = 0;

function back(){
    slideNo--;
    slideShow(slideNo);
}
function next(){
    slideNo++;
    slideShow(slideNo);
}

function slideShow (slideNumber){
    slideNo = slideNumber;
    if(slideNumber >= slideSay){
        slideNo = 0;
    }

    if(slideNumber < 0){
        slideNo = slideSay -1;
    }


    for (i = 0; i< slideSay; i++){
        slide[i].style.display = "none";
    }

    slide[slideNo].style.display = "block";
}