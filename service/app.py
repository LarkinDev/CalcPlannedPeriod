from flask import Flask
from flask import request
import joblib

app = Flask(__name__)
model = None


@app.route('/service', methods=['GET'])
def predict():
    content = request.json()
    work_hourse = model.predict()


if __name__ == '__main__':
    model = joblib.load('model.sav')
    app.run(debug=True)
