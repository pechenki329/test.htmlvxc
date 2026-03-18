<!DOCTYPE html>
<html>
<head>
    <title>Sticker Race</title>
    <meta charset="utf-8">
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
        }
        h1 { font-size: 28px; }
        .emoji { font-size: 100px; margin: 30px; }
        .stickers { display: flex; justify-content: center; gap: 20px; }
        .sticker {
            width: 100px;
            height: 100px;
            cursor: pointer;
            border: 3px solid white;
            border-radius: 10px;
        }
        .sticker:hover { border-color: gold; }
        .message { font-size: 24px; margin: 20px; }
        button {
            background: gold;
            color: black;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Кто быстрее подберет стикер?</h1>
    <div class="emoji" id="emoji">😊</div>
    <div class="stickers" id="stickers"></div>
    <div class="message" id="message"></div>
    <button onclick="window.newRound()">Следующий раунд</button>

    <script>
        let tg = Telegram.WebApp;
        tg.expand();

        const stickers = {
            '😊': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f60a.png',
            '😂': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f602.png'
        };

        let currentCorrect = stickers['😊'];

        function showStickers() {
            document.getElementById('stickers').innerHTML = 
                '<img src="' + stickers['😊'] + '" class="sticker" onclick="check(true)">' +
                '<img src="' + stickers['😂'] + '" class="sticker" onclick="check(false)">';
        }

        window.check = function(isCorrect) {
            if (isCorrect) {
                document.getElementById('message').innerHTML = '✅ Правильно!';
            } else {
                document.getElementById('message').innerHTML = '❌ Неправильно!';
            }
        };

        window.newRound = function() {
            document.getElementById('emoji').textContent = '😊';
            currentCorrect = stickers['😊'];
            document.getElementById('message').innerHTML = '';
            showStickers();
        };

        // Запуск
        window.newRound();
    </script>
</body>
</html>
