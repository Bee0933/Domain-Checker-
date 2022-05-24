from utils import predict
from flask import Flask, render_template, url_for, request, redirect

# app = Flask(__name__, template_folder='#', static_folder='#')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        input_url = request.form['input_url']
        prediction = predict(input_url)
        return render_template('predict.html', prediction=prediction)
    else:
        return render_template('index.html')
        

if __name__ == '__main__':
    app.run(debug=False)
