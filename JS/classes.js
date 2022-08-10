class Person {
    constructor(fname,lname,yob){
        this.fname = fname;
        this.lname = lname;
        this.yob = yob;
    }

    calcAge(){
        return 2022-this.yob;
    }
}

// Person.prototype.greet = function (name) {
//     console.log(`Hello ${name}.`);
// }

// const p1 = new Person("Shreyansh", "Patil", 2001);

// console.log(p1);
// console.log(p1.calcAge());
// console.log(p1.__proto__);
// console.log(Person.prototype);


// p1.greet(p1.fname);

// console.log(p1.__proto__ === Person.prototype);

// adding # as in p1.#age or this.#age makes the age variable private