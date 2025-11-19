from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Flask</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: white;
            text-align: center;
        }
        .container {
            padding: 80px 20px;
        }
        h1 { font-size: 3rem; margin-bottom: 10px; }
        p { font-size: 1.3rem; opacity: 0.9; }
        .button {
            padding: 12px 20px;
            margin-top: 20px;
            font-size: 1rem;
            background-color: white;
            color: #0077ff;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.2s ease;
        }
        .button:hover {
            background-color: #cce5ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bienvenido a mi aplicación Flask</h1>
        <p>Esta aplicación está detrás de Traefik con HTTPS automático.</p>
        <a class="button" href="#">Explorar más</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
