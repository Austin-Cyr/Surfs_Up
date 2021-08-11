from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello world'
    print("Hello world")
    return "Welcome to my Home page!"

@app.route("/about")
def about():
    print("Server rec'd request for 'about' page...")
    return "Welcome to my About page!"

if __name__ == "__main__":
    app.run(debug=True)