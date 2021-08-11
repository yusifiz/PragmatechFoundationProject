// 1-den 100-e qeder ededlerin cemi:
let cem=0;

for(var i=0; i<=100;i++){
    cem=cem+i;
}

console.log('1-den 100-e qeder ededlerin cemi: '+cem)


// Paraqrafdakı simvolların sayı
let info='Bu sahəyə yeni başlayanlar üçün programlaşdırma həddindən artıq qarışıq və çətin gələ bilər. İnternetdə tonlarla qaynaqları görüb gözünüz qorxa bilər. Düşünə bilərsiniz ki, bu qədər konsepti necə öyrənə bilərəm və yaxud bu mənim nə qədər zamanımı alar. Əfsanələrə görə, əgər riyaziyyatı yaxşı bilmirsinizsə sizin bu sahədə uğurlu ola bilməyiniz mümkün deyil. Və yaxud bu sahədə ali təhsiliniz yoxdursa heç bir yerdə iş tapa bilməyəcəksiniz. Əslində isə bu sahəyə giriş etdikdən sonra heç də elə olmadığını görəcəksiniz.';
let a = info.length
console.log('Paraqrafdakı simvolların sayı: '+a)

// Paraqrafdakı 's' hərfərinin sayı

let b = info.match(/s/g)
console.log('Paraqrafdakı s hərfərinin sayı: ' +b.length)

// Paraqrafdakı sözlərin sayı

let c = info.split(" ")
console.log('Paraqrafdakı sözlərin sayı: ' +c.length)

// Paraqrafdakı hərflərin sayı
console.log('Paraqrafdakı hərflərin sayı: ' + (a - c.length))

// arr massivindəki tək ədədlər

let arr=[1,3,4,6,89,12,67,34,89,123];
let x
const tekEded = arr.filter((arr) => {
    return  arr%2 == 1;
})

console.log('arr massivindəki tək ədədlər:' +tekEded);

// arr massivindəki ədədlərin cəmi

let cem1 =0; 
arr.forEach((arr) => {
    return cem1 = cem1 + arr;
})

console.log('arr massivindəki ədədlərin cəmi: ' +cem1)

// arr massivinəki ədədlərin kvadratı

let kvadrat ; 
arr.forEach((arr) => {
    kvadrat= arr**2;
    return console.log('arr massivinəki ədədlərin kvadratı: ' +kvadrat)
})

// arr massivindəki ən böyük ədəd

arr.sort(function(a,b){
    return b-a;
})
console.log('arr massivindəki ən böyük ədəd: ' +arr[0]);
