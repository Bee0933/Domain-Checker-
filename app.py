from flask import Flask

app = Flask(__name__, template_folder='#', static_folder='#')


@app.route('/')
def home_page():
    pass


