// Rock-paper-scissors game

function game(answer) {
    prompt('Welcome user, this is a basic JS rock-paper-scissors game');
    var answer = prompt('Please, only use characters, otherwise this wont work. Which option do you choose?": Rock, paper or scissors.');
    answer = toUpperCase(answer);

    switch(answer){
        case Rock:
            console.log('JavaScript chooses paper');
            console.log('You lose.');
            break;
        case Paper:
            console.log('Javascript chooses scissors');
            console.log('You lose.');
            break;
        case Scissors:
            console.log('JavaScript chooses paper');
            console.log('You win!');
            break;
        default:
            console.log('You probably missed a letter, try again.')
    }
    


}   