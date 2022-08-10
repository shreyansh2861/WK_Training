const Person = function(sname, sage){
    this.sname = sname;
    this.sage = sage;
};

const student = function(personal, school){
    this.personal = personal;
    this.school = school;
};

const per1 = new Person("A", 15);
const st1 = new student(per1,"REMS");

console.log(st1.personal.sname);

Person.prototype.favSport = "Cricket";

const Person1 = {
    pname: "Someone",
    age: 0,
};

p1 = Object.create(Person1);

console.log(p1.name);

console.log(Person1.__proto__);