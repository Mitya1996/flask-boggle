let score = 0;
let guesses = []
let time = 5
let highScore = 0

$('#submit-btn').on('click', handleGuess);

async function handleGuess(e) {
    e.preventDefault();

    let guess = $('#word').val();
    let res = await axios.get('/guess', { params: { guess: guess } });
    response = res.data.response;
    $('#response').text(response); //set innertext  

    //do not increment score if already guessed
    let alreadyGuessed = guesses.find(e => e == guess);
    guesses.push(guess)
    if(alreadyGuessed) {
        alert('Already Guessed'); 
    }
    //if 'ok' then score++ and rerender score
    else if(response == 'ok') {
        score += guess.length;
        $('#score').text(score);
    }
}


let timerInterval = setInterval(function() {
    if(time <= 1) {
        clearInterval(timerInterval);
        $('#submit-btn').attr('disabled', true); //disable further guesses
        updateHighScore();
        alert('Times Up!');
    }
    time--;
    $('#timer').text(time);
}, 1000);

function updateHighScore() {
    if(score > highScore) {
        highScore = score;
        $('#high-score').text(highScore);
    }
}