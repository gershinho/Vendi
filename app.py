from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register_truck', methods=['POST', 'GET'])
def register_truck():
    if request.method == 'POST':
        name = request.form['foodTruckName']
        print(name)
    return render_template('register_truck.html')

if __name__ == '__main__':
    app.run(debug=True)
