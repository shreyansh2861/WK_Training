const patientList = [];
let displayPatientList = function (patient) {
  document.getElementById("pList").innerText += ` ${patient}`;
  clearInputs();
};

clearInputs = function () {
  let inputs = document.getElementsByTagName("input");
  for (let input of inputs) {
    if (input.getAttribute("type") != "button") input.value = "";
  }
};

let registerPatients = function () {
  let val = document.getElementById("input").value;
  patientList.push(val);
  console.log(patientList);
  let patientSet = new Set(patientList);
  console.log(patientSet);
  document.getElementById("pList").innerText = "";
  patientSet.forEach(displayPatientList);
};

document.getElementById("register").addEventListener("click", registerPatients);

function showThis() {
  console.log(this);
}
document.getElementById("register").addEventListener("mouseover", showThis);