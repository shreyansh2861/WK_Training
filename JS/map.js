const question = new Map([
    ["Shreyansh",100],
    ["Arnav",101],
    ["Parshwa",102],
    [true,"back to office"],
    [
        [1,2],
        ["hello", "world"],
    ],
]);

// console.log(question);
// console.log(question.get(true));
itr = question.keys();
console.log(itr.next().value);
console.log(itr.next().value);
console.log(itr.next().value);
console.log(itr.next().value);