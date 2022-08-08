emp_list = [1981, 1977];
for(emp in emp_list){
    console.log(emp);
}

for(i in emp_list){
    console.log(emp_list[i]);
}

function getAges(list_dobs){
    const ages = [];
    for (dob of list_dobs){
        ages.push(2022-dob);
    }
    return ages;
}

console.log(getAges(emp_list))

function CalAge(dob){
    return 2022-dob;
}

const newAges = [];

newAges.push(emp_list.forEach(CalAge));

console.log(newAges);