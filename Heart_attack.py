from flask import Flask, render_template, request
import pickle

global prediction

app = Flask(__name__)
classifier = pickle.load(open('classifier.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        age = request.form['age']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']

        features = list(map(lambda x: float(x), [age, cp, trestbps, chol, fbs]))

        prediction = classifier.predict([features])
        if prediction == [1]:
            value = 'The Person have Heart Attack'
            return render_template('Positiveresult.html', prediction=value)
        elif prediction == [0]:
            value = 'The Person does not have Heart Attack'
            return render_template('Negativeresult.html', prediction = value)  

    return render_template('index.html', prediction = None)

@app.route('/Details')
def Details():
    return render_template('Details.html')

if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)