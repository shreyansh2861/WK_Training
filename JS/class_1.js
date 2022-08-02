class Person{
    constructor(firstName, lastName, age){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    calcYOB = function (age){
        return 2022-age;
    };
}

const p1 = new Person("Shreyansh","Patil",21);
console.log(p1.calcYOB(p1.age));