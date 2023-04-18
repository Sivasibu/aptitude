// Define the timer values
let minutes = 0;
let seconds = 0;




// Update the timer display and the input field
const timer = document.getElementById('displaytimer');
const inputtag = document.getElementById('timer');
timer.innerHTML = "<b>Timer: " + minutes + " minutes " + seconds + " seconds</b>";
inputtag.value = minutes;

// Define the function to update the timer every second
const updateTimer = () => {
  seconds += 1;
  if (seconds == 60) {
    minutes += 1;
    seconds = 0;
  }
  
  // Update the timer display and the input field
  timer.innerHTML = "<b>Timer: " + minutes + " minutes " + seconds + " seconds</b>";
  inputtag.value = minutes;
  
  // Store the timer value in the local storage
  localStorage.setItem('timer', minutes + ':' + seconds);
  
  // Check if 40 minutes have passed
  if (minutes == 40 && seconds == 0) {
    clearInterval(intervalID); // Stop the timer
    window.location.href = "/result/"; // Go to the result page
  }
};

// Update the timer every second
let intervalID = setInterval(updateTimer, 1000);

// Save the timer value in the local storage before leaving the page
window.onunload = () => {
  localStorage.setItem('timer', minutes + ':' + seconds);
};

// Restore the timer value from the local storage when loading the page
window.onload = () => {
  let storedTime = localStorage.getItem('timer');
  if (storedTime !== null) {
    let timeArray = storedTime.split(':');
    minutes = parseInt(timeArray[0]);
    seconds = parseInt(timeArray[1]);
    timer.innerHTML = "<b>Timer: " + minutes + " minutes " + seconds + " seconds</b>";
    inputtag.value = minutes;
  }
};

// Stop the timer when the submit button is clicked
const submitButton = document.getElementById('submit');
submitButton.addEventListener('click', () => {
  clearInterval(intervalID);
});

// Refresh the timer when the start button is clicked
const startButton = document.getElementById('start');
startButton.addEventListener('click', () => {
  clearInterval(intervalID); // Stop the timer
  minutes = 0; // Reset the timer values to 0
  seconds = 0;
  timer.innerHTML = "<b>Timer: " + minutes + " minutes " + seconds + " seconds</b>"; // Update the timer display
  inputtag.value = minutes; // Update the input field
  intervalID = setInterval(updateTimer, 1000); // Start the timer again
});

      