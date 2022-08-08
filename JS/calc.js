function displayVal(){
    var val = document.getElementById("one").value;
    document.getElementById("screen").value = val;
    var rand_array = ["one", 1, "two", 2, "three", 3, "four", 4];
    console.log(rand_array);
    last_elem = rand_array.pop();
    first_elem = rand_array.shift();
    console.log(rand_array);
}