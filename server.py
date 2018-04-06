from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def PagePrincipale():
 return render_template('PagePrincipale.html')


@app.route("/hello")
def hello():
 return 'Hello, peeps'


if __name__ == "__main__":
 app.run(debug=True)