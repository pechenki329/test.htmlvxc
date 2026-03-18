<!DOCTYPE html>
<html>
<head>
    <title>Sticker Race</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
        }
        .emoji { font-size: 100px; margin: 30px; }
        .sticker {
            width: 100px;
            height: 100px;
            cursor: pointer;
            border: 3px solid white;
            border-radius: 10px;
            margin: 10px;
        }
        .sticker:hover { border-color: gold; transform: scale(1.1); }
        button {
            background: gold;
            color: black;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            font-size: 18px;
            cursor: pointer;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Кто быстрее подберет стикер?</h1>
    <div class="emoji" id="emoji">😊</div>
    <div id="stickers"></div>
    <div id="message"></div>
    <button onclick="newRound()">Следующий раунд</button>

    <script>
        let tg = Telegram.WebApp;
        tg.expand();

        const stickers = {
            '😊': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f60a.png',
            '😂': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f602.png'
        };

        let currentCorrect = stickers['😊'];

        function newRound() {
            document.getElementById('emoji').textContent = '😊';
            currentCorrect = stickers['😊'];
            showStickers();
        }

        function showStickers() {
            let html = '';
            html += '<img src="' + stickers['😊'] + '" class="sticker" onclick="check(true)">';
            html += '<img src="' + stickers['😂'] + '" class="sticker" onclick="check(false)">';
            document.getElementById('stickers').innerHTML = html;
        }

        function check(isCorrect) {
            if (isCorrect) {
                document.getElementById('message').innerHTML = '✅ Правильно!';
            } else {
                document.getElementById('message').innerHTML = '❌ Неправильно!';
            }
        }

        newRound();
    </script>
</body>
</html>
