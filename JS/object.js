const student = {
    sname: "Shreyansh",
    sage: 21,
    // greet: function (){
    //     console.log("Good Morning");
    // }
};

student.fav_game = "Cricket";

console.log(student);

student.greet = function () {
    console.log("Good morning");
};
student.greet();

const calcAge = (yob, curr_yr) =>  curr_yr-yob;

console.log(calcAge(2001, 2022));


function process_emp(emp_lis, calcAge){
    const ages = [];
    curr_yr1=2022
    for(emp in emp_lis){
        ages.push[calcAge(emp,curr_yr1)];
    }
    return ages;
}

console.log(process_emp([1997,1998,2003,1978], calcAge));