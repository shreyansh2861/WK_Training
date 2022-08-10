let person = {
    fname: "Shreyansh",
    lname: "Patil",
    title: "Master.",

    displayName: function (){
        console.log(`${this.title} ${this.fname} ${this.lname}`);
    },
};

person.displayName();

let person1 = {
    fname: "Arnav",
    lname: "Patil",
    title: "Master.",
};

person.displayName.call(person1);

let p1new = person.displayName.bind(person1);

p1new();