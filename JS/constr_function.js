// function Student_new(){
//     sName = "A";
//     sAge = 15;
//     console.log(this);
// }

// let s1 = new Student_new();
// console.log(s1);
// console.log(s1.__proto__);

//constructor functions
function Student_New(){
    this.sName = "A";
    this.sAge = 15;
    console.log(this);

}

let s2 = new Student_New();
console.log(s2.sName);
console.log(Student_New.prototype);

