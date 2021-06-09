/*console.log('Hello, World!');

const getRandomNumber = (max) => {
    return Math.floor(Math.random() * (max + 1));
}

console.log(getRandomNumber(10));
console.log(getRandomNumber(100));

const getCurrentTime = () => {
    const currentDate = new Date();
    return currentDate.getHours() + ":" + currentDate.getMinutes() + ":" + currentDate.getSeconds();
}

console.log(`The current time is ${getCurrentTime()}.`);*/

const appearanceHeading = document.getElementById("facts__heading");
appearanceHeading.textContent = "Qualities and Traits of a Crab";

const importantFact = document.getElementById("facts__fact--important");
importantFact.className = `${importantFact.className} highlight`;

const newAppearanceFact = document.createElement("li");
newAppearanceFact.textContent = "covered in sand (when on a sandy beach)";

const appearanceList = document.getElementById("facts__list");
appearanceList.appendChild(newAppearanceFact);