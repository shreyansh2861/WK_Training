document.querySelector("#clk").addEventListener("click", () => {
    const  request = new XMLHttpRequest();
    request.open("GET",`https://restcountrie.com/v3.1/name/india`);
    request.send();
    console.log(request.responseText);
});