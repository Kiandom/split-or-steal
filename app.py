<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Split or Steal Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }

        #game-container {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
        }

        .player-container {
            border: 1px solid #ccc;
            padding: 10px;
            width: 200px;
        }

        #result-container {
            border: 1px solid #ccc;
            padding: 10px;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Split or Steal Game!</h1>
    <div id="game-container">
        <div class="player-container" id="player1">
            <h2>Player 1</h2>
            <button onclick="makeDecision(1, 'split')">Split</button>
            <button onclick="makeDecision(1, 'steal')">Steal</button>
        </div>
        <div class="player-container" id="player2">
            <h2>Player 2</h2>
            <button onclick="makeDecision(2, 'split')">Split</button>
            <button onclick="makeDecision(2, 'steal')">Steal</button>
        </div>
    </div>
    <div id="result-container">
        <h2>Results</h2>
        <p id="result"></p>
    </div>

    <script>
        function makeDecision(playerNum, decision) {
            disableButtons(playerNum);
            checkResults();
        }

        function disableButtons(playerNum) {
            document.getElementById(`player${playerNum}`).querySelectorAll('button').forEach(button => {
                button.disabled = true;
            });
        }

        function checkResults() {
            // Simulate server-side logic by generating random results
            const decisions = ['split', 'steal'];
            const player1Decision = decisions[Math.floor(Math.random() * 2)];
            const player2Decision = decisions[Math.floor(Math.random() * 2)];

            displayResults(player1Decision, player2Decision);
        }

        function displayResults(player1Decision, player2Decision) {
            const resultText = `Player 1: ${player1Decision}\nPlayer 2: ${player2Decision}\nHost: `;
            document.getElementById('result').innerText = resultText;
        }
    </script>
</body>
</html>
