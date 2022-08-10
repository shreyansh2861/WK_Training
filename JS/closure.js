function parentfn(){
    const parentVar = 10;

    return function childfn(){
        console.log(parentVar*10);
    };
}

const chFn1 = parentfn();

chFn1();

let chFn2;

function parentFn1(){
    const parentVar = 10;

    chFn2 = function(){
        console.log(parentVar*10);
    };
}

parentFn1();