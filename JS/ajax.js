const getCountryData = function (cName) {
    // making AJAX request
    const request = new XMLHttpRequest();
    // console.log(request);
  
    request.open("GET", `https://restcountries.com/v3.1/name/${cName}`);
    // async call hence data is not returned immediately
    request.send();
    console.log(request);
    console.log(request.responseText);
  
    // // need to add event handler which will be called once the data is returned
    request.addEventListener("load", function () {
      const textData = this.responseText;
      // console.log(textData);
      const [data] = JSON.parse(textData);
      // console.log(data);
      // console.log(data.continents[0]);
      const minData = {
        name: data.name.common,
        region: data.region,
        population: data.population,
        language: data.languages[Object.keys(data.languages)[0]],
        currency: data.currencies[Object.keys(data.currencies)[0]].name,
      };
      console.log(minData);
    });
  };
  
  getCountryData("india");
  // getCountryData("sri lanka");