const redButton = document.querySelector('#red');
let repeatText = ''
  let responsebox = document.querySelector('#response-box');

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', (e) => {
  console.log("You clicked the red button!");

  responsebox.style.backgroundColor = 'red';



  repeatText = repeatText + 'red';
  responsebox.innerHTML = repeatText;});



//---------------------------------------------------
const greenButton = document.querySelector('#green');

// Use addEventListener to respond to a click event.
greenButton.addEventListener('click', (e) => {
  console.log("You clicked the green button!");

   responsebox.style.backgroundColor = 'green';

   repeatText = repeatText + 'green';
   responsebox.innerHTML = repeatText;

});

//------------------------------------------------------


const blueButton = document.querySelector('#blue');

// Use addEventListener to respond to a click event.
blueButton.addEventListener('click', (e) => {
  console.log("You clicked the blue button!");

   responsebox.style.backgroundColor = 'blue';

 repeatText = repeatText + 'blue';
 responsebox.innerHTML = repeatText;

});
