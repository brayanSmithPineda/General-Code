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

// const score = {
//     Looses : 0,
//     Wins : 0,
//     Ties: 0
// };

const score = JSON.parse(localStorage.getItem('score')) || {Looses: 0, Wins:0, Ties:0};

//We show the score right after we refrest or star the page, if we do not write this line of code the result will no show if we refresh the page
updateScoreElement();

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

function updateScoreElement (){
    document.querySelector('.js-score').innerHTML = `
    Wins: ${score.Wins}, Looses: ${score.Looses}, Ties: ${score.Ties}`;
    
}