const patientList = [];
let displayPatientList = function (patient) {
  document.getElementById("pList").innerText += ` ${patient.Name}`;
  console.log(patient);
  clearInputs();
};

clearInputs = function () {
  let inputs = document.getElementsByTagName("input");
  for (let input of inputs) {
    if (input.getAttribute("type") != "button") input.value = "";
  }
};
// randomID = function () {
//   let id =
// };

let registerPatients = function () {
  let patient = {};
  let patientIDSet = new Set();
  for (patient of patientList) {
    patientIDSet.add(patient.ID);
  }
  patient.ID = (() => Math.floor(Math.random() * 10000) + 1)();
  patient.Name = document.getElementById("name").value;
  patient.Age = document.getElementById("age").value;
  patient.Mobile = document.getElementById("mobile").value;
  patient.City = document.getElementById("city").value;
  patientList.push(patient);
  console.log(patientList);

  console.log(patientSet);
  document.getElementById("pList").innerText = "";
  patientSet.forEach(displayPatientList);
};

document.getElementById("register").addEventListener("click", registerPatients);

function showThis() {
  console.log(this);
}
document.getElementById("register").addEventListener("mouseover", showThis);