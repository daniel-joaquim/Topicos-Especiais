let timerInterval;

function startTimer() {
    fetch('/start', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
            if (data.status === 'started') {
                timerInterval = setInterval(updateTimer, 1000);
            }
        });
}

function pauseTimer() {
    fetch('/pause', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
            if (data.status === 'paused') {
                clearInterval(timerInterval);
            }
        });
}

function resetTimer() {
    fetch('/reset', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
            if (data.status === 'reset') {
                clearInterval(timerInterval);
                document.getElementById('timer').innerText = '00:00:00';
            }
        });
}

function updateTimer() {
    fetch('/time')
        .then(response => response.json())
        .then(data => {
            document.getElementById('timer').innerText = data.time;
        });
}
