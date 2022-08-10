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
console.log(s2.__proto__);
console.log(Student_New.prototype);


Student_New.prototype.nationality = "Indian";
console.log(s2.nationality);

const s3 = new Student_New("B",13);
console.log(s3.nationality);

console.log(Student_New.prototype);

Student_New.prototype.calcYOB = function (){
    return 2022-this.sAge;
};

console.log(s3.calcYOB());

console.log(Student_New.prototype);