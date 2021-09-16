const axios = require("axios");

const YOUR_API_KEY = "87e54692536c26";

const wonders = [
    "Great Wall of China",
    "Petra",
    "Colosseum",
    "Chichen Itza",
    "Machu Picchu",
    "Taj Mahal",
    "Christ the Redeemer",
  ];

const locations = {};

const findLatitudeAndLongitude = (query) => {
    let lat;
    let lon;
    axios.get("https://us1.locationiq.com/v1/search.php",{
        params: {
            key: YOUR_API_KEY,
            q: query,
            format: "json",
          }
    }).then((response)=>{
        lat = response.data[0].lat;
        lon = response.data[0].lon;
        locations[query] = {lat, lon};
    }).catch((error)=>{
        console.log("we caught an error!", error)
    });
}


function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
   
async function findLocations() {
    for (query of wonders){
        findLatitudeAndLongitude(query)
        await sleep(500);
    }
    console.log(locations)
}

findLocations();

