
$('#submit-btn').on('click', handleGuess);

async function handleGuess(e) {
    e.preventDefault();
    let guess = $('#word').val();
    let res = await axios.get('/guess', { params: { guess: guess } });
    response = res.data.response
    $('#response').text(response); //set innertext of 
}

