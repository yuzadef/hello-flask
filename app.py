from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World! This is a test for Git VCS."


if __name__ == "__main__":
<<<<<<< Updated upstream
    app.run(debug=False)
=======
    app.run(debug=True)
# test
>>>>>>> Stashed changes
