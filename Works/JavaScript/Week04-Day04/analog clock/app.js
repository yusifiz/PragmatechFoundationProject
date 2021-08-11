let hour = document.querySelector('.hourHand')
let minute = document.querySelector('.minuteHand')
let second = document.querySelector('.secondHand')



let deg = 6;
interval = setInterval(()=>{
    let d =new Date()
    let sec = d.getUTCSeconds()*deg;
    let min = d.getUTCMinutes()*deg;
    let hr = d.getHours() * 30;
    
    
    second.style.transform = `rotateZ(${sec}deg)`; 
    minute.style.transform = `rotateZ(${min}deg)`; 
    hour.style.transform = `rotateZ(${(hr) + (min/12)}deg)`
})


