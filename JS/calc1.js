let expression = "";
function display(clicked_id) {
  expression += document.getElementById(clicked_id).value;
  document.getElementById("screen").value = expression;
}

function getResult() {
  result = eval(expression);
  document.getElementById("screen").value = result;
}

function clearResult() {
  expression = "";
  document.getElementById("screen").value = expression;
}

window.onerror = function () {
  expression = "Invalid Expression";
  document.getElementById("screen").value = expression;
};

// document.addEventListener("click", display);