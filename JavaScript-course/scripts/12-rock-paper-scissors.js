function generateComputerMove(){
    const randNum = Math.random();
    if (randNum <= 0.33){
        computerMove = 'rock';
    } else if (randNum > 0.33 && randNum <= 0.66) {
        computerMove = 'paper';
    } else {
        computerMove = 'scissors';
    }
    return computerMove;
}

function updateScoreElement (){
    document.querySelector('.js-score').innerHTML = `
    Wins: ${score.Wins}, Looses: ${score.Looses}, Ties: ${score.Ties}`;
    
}
// const score = {
//     Looses : 0,
//     Wins : 0,
//     Ties: 0
// };

const score = JSON.parse(localStorage.getItem('score')) || {Looses: 0, Wins:0, Ties:0};

//We show the score right after we refrest or star the page, if we do not write this line of code the result will no show if we refresh the page
updateScoreElement();

//Event Listener to run the function everytime we click on the button, is like the onclick attribute

const rockButton = document.querySelector('.js-rock-button');
const paperButton = document.querySelector('.js-paper-button');
const scissorButton = document.querySelector('.js-scissors-button');

rockButton.addEventListener('click', () => {
    playGame('rock');
})

rockButton.addEventListener('click', () => {
    playGame('rock');
})
paperButton.addEventListener('click', () => {
    playGame('paper');
})
scissorButton.addEventListener('click', () => {
    playGame('scissors');
})

//Playing the game with keydown using addEventListener, we use the body with the dom, This means that regardless of where the focus is on the page, pressing the keys r, p, or s will trigger the corresponding game action.

document.body.addEventListener('keydown', (event) => {
    if(event.key === 'r'){
        playGame('rock');
    }else if(event.key === 'p'){
        playGame('paper');
    }else if(event.key === 's'){
        playGame('scissors');
    };
})

document.querySelector('.js-reset-score-button')
    .addEventListener('click', () => {
        score.Wins = 0;
        score.Looses = 0;
        score.Ties = 0;
        localStorage.removeItem('score');

        //We write the updateScoreElement function to reset the score immediatily we click the button, if we do not write this line the webpage will displate the old score until we play again
        updateScoreElement();
    });
    
function playGame(myMove){
    const computerMove = generateComputerMove();
    
    if (myMove === 'rock') {
        if (computerMove === 'rock'){
            result = 'Tie';
        } else if (computerMove === 'paper'){
            result = 'You loose';
        } else {
            result = 'You win';
        }
    } else if (myMove === 'paper') {
        if (computerMove === 'rock'){
            result = 'You win';
        } else if (computerMove === 'paper'){
            result = 'Tie';
        } else {
            result = 'You loose';
        }
    } else {
        if (computerMove === 'rock'){
            result = 'You loose';
        } else if (computerMove === 'paper'){
            result = 'You win';
        } else {
            result = 'Tie';
        }
    }

    if (result === 'Tie'){
        score.Ties++;
    } else if (result === 'You win'){
        score.Wins++;
    } else {
        score.Looses++;
    }

    localStorage.setItem('score', JSON.stringify(score)); // we save the object score into local Storage and we name it score

    document.querySelector('.js-result').innerHTML = result;
    document.querySelector('.js-moves').innerHTML = `You <img src="/Influcer-Marketing-App/Images/${myMove}-emoji.png" class = "emoji">  <img src="/Influcer-Marketing-App/Images/${computerMove}-emoji.png" class = "emoji"> Computer`;

    //With this code we ensure the score is show every time we play the game, if we don´t do that the result will only show at the beggining
    updateScoreElement();
}

let isAutoPlaying = false;
let intervalId;
function autoplay(){
    if(!isAutoPlaying){
        intervalId = setInterval(() => {
            const myMove = generateComputerMove();
            playGame(myMove);
        },1000);
        isAutoPlaying = true;
    } else {
        clearInterval(intervalId);
        isAutoPlaying;
    }
     
}