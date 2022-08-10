let num_array = [1, 2, 3];

let sq_array = [];
let num_square = function (num) {
    sq_array.push(num*num);
};
num_array.forEach(num_square);
console.log(sq_array);

let num_square_map = function (num){
    return num*num;
};
console.log(num_array.map(num_square_map));

let check_if_positive = function (x){
    return x % 2 == 0;
};

console.log(num_array.filter(check_if_positive));

const findMax = function (x,y) {
    return x > y ? x : y ;
};

// console.log(num_array.map(num_square));