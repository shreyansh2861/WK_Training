var empType = "permanent";
var salType = empType === "permanent" ? "salary":"stipend";
console.log(salType);


function someFunction(){
    console.log(empType);
}

someFunction();