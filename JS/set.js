const list = ['A','B','C'];

const set = new Set(list);

console.log(list);
console.log(set);

function display(item){
    console.log(item);
}

set.forEach(display);

//using iterator

let itr = set.values();

//console.log(itr.next().value);
itr.next();
while(itr!=undefined){
    console.log(itr.next().value);
}