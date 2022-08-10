let f;

const g =  function () {
    const x=5;
    f = function (){
        console.log(x*5);
    };
};

g();
f();

const h = function () {
    const y=9;
    f = function () {
        console.log(y*5);
    };
};

h();
f();

console.dir(f);