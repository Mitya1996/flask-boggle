let score;
let guesses = []
const gameTime = 10
let highScore //todo make this as a get request from backend
let numPlayed

newGame();
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

function newGame() {
    $('#submit-btn').attr('disabled', false);  
    $('#reset-btn').attr('disabled', true);
    $('#alert').empty();  
    let time = gameTime;
    updateNumPlayed();
    updateHighScore();
    initScore();
    initHighScore();

    let timerInterval = setInterval(function() {
        if(time <= 1) {
            clearInterval(timerInterval);
            $('#submit-btn').attr('disabled', true); //disable further guesses
            $('#reset-btn').attr('disabled', false); //allow reset
            updateHighScore();
            customAlert('Times Up!');
        }
        time--;
        $('#timer').text(time);
    }, 1000);
}

function initScore() {
    score = 0;
    $('#score').text(score);
}

async function initHighScore() {
    axios.get('/updateHighScore')
    .then(function (response) {
        // handle success
        console.log(response);
        highScore = response.data.high_score;
        $('#high-score').text(highScore);
    })
    .catch(function (error) {
        // handle error
        console.log(error);
    })
    .then(function () {
        // always executed
    });
}

async function initNumPlayed() {
    axios.get('/updateNumPlayed')
    .then(function (response) {
        // handle success
        console.log(response);
        numPlayed = response.data.num_played;
        $('#num-played').text(numPlayed);
    })
    .catch(function (error) {
        // handle error
        console.log(error);
    })
    .then(function () {
        // always executed
    });
}

async function updateHighScore() {
    if(!highScore) {
        initHighScore();
    }
    if(score > highScore) {
        highScore = score;
        $('#high-score').text(highScore);
        //update on back end (or save to flask session cookie rather)
        await axios.post('/updateHighScore', {
            newHighScore: highScore,
          })
          .then(function (response) {
            console.log(response);
            highScore = response.data.session_HS;
            $('#high-score').text(highScore);
          })
          .catch(function (error) {
            console.log(error);
          });
    }
}

async function updateNumPlayed() {
    await axios.post('/updateNumPlayed', {
        'incrementOne': 'true',
    })
    .then(function (response) {
        console.log(response);
        numPlayed = response.data.num_played;
        $('#num-played').text(numPlayed);
    })
    .catch(function (error) {
        console.log(error);
    });
}

function customAlert(msg) {
    let alert = `<div class="alert alert-warning alert-dismissible fade show" role="alert">
    <strong>${msg}</strong>
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>`
    $('#alert').html(alert);
}