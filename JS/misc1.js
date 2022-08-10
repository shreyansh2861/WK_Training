// const Person =  function(sname, sage){
//     this.sname = sname;
//     this.sage = sage;
// };

// Person.species = "Humans";

// Person.greet = function (){
//     console.log("Hello");
// };

// p1 = new Person("Shreyansh", 21);

// console.log(Person.species);
// Person.greet();

// console.log(p1.species);
// // p1.greet;


class Person{
    static species = "Humans";
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    static greet1(){
        console.log("Hola");
    }
}

// Person.species = "Humans";


Person.greet = function(){
    console.log("Hello");
};

p1 = new Person("Shreyansh", 21);

console.log(p1.species);
console.log(Person.species);

Person.greet();
Person.greet1();

// p1.greet();
// p1.greet1();

class student extends Person{
    constructor(name, age, sclass){
        super(name, age);
        this.sclass = sclass;
    }


}

s1 = new student("A",14, 9);

console.log(s1);


