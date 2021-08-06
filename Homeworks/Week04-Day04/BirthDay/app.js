let birthD = document.querySelector('.bday p')


setInterval(()=>{
    let birthDay = new Date(2002, 0, 10, 12, 30, 0);
    let today = new Date();
    let a = today - birthDay;
    let second = Math.round(a/1000); 
    let minute = Math.round(second/60);
    let hour = Math.round(minute/60);
    let day = Math.round(hour/24);
    let month = Math.round(day/30.4);
    let year = Math.floor(month/12);
    
    birthD.innerHTML = `${year + " Year <br>"} ${month + "  Month<br>"} ${day + "  Day<br>"} ${hour + "  Hour<br>"} ${minute + " Minute<br>"} ${second + "  Second"}`

    
})