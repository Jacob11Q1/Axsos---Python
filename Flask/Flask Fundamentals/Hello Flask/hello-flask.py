from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index.html template with phrase and times variables."""
    return render_template("index.html", phrase="hello", times=5)

if __name__ == "__main__":
    app.run(debug=True)

# ============================
# Root Route: Render Home Page
# ============================
# @app.route('/')
# def hello_world():
#     """Render the index.html template"""
#     return render_template('index.html')

# def hello_world():
#     return 'Hellow World!'