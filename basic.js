// 

// function hello(x,y){
// console.log(typeof(y),x);
// }

// hello("nitish",22);



//important array functions
// forEach function
// let arr=[1,2,3,4,5];
// arr.forEach(function print(el){
//     console.log(el);
// })

// //or

// let arr=[1,2,3,4,5];
// function print(el){
//     console.log(el);
// }
// arr.forEach(print);

// let arr=[{
//     name:"nitish",
//     class:11
// },{
//     name:"nitish",
//     class:12
// }];

// arr.forEach((obj)=>{
//     console.log(obj.name);
// })

let arr=[1,23,3,40,5];
arr.every((num)=>{
    console.log(num%10 ==0);
})