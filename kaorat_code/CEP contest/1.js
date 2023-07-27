// block scope (let/constant)

// var x=10
// if (x==10){
//     let y=20
//     console.log(y)
// }
// // console.log("y="+y)

// fullname=(fname,lname)=>fname+lname

// console.log(fullname("kao","rat"))

sum=(...num)=>{
    let total=0
    for(let i of num) total+=i
    return total
}
console.log(sum(50,1000))