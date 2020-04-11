from flask import Flask , render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carte')
def carte():
    return render_template('carte.html')

@app.route('/formtest')
def formtest():
    return render_template('formtest.html')

if __name__ == '__main__':
    app.run(debug=True)
