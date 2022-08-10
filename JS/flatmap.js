const num_array = [1, 2, [3, 4, 5]];

const sqr = function (num){
    return num*num;
};

const array1 = num_array.flat();
console.log(array1.flat());

const sq_array = num_array.map(sqr);
console.log(sq_array);

const sq_array1 = num_array.flatMap(sqr);
console.log(sq_array1);

const str_array = ["this is a sample string", "which will be flattened"];

console.log(str_array.flatMap((s)=>s.split(" ")));