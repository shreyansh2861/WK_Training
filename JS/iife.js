// immediately invoked function expression

const calcSum = function (num1, num2){
    return num1 + num2;
};

console.log(calcSum(1,2));

(function(num1,num2){
    console.log(num1 + num2);
})(3,4);