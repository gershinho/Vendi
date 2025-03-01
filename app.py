from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import truckdb


app = Flask(__name__)

truckdb.init_db()

app.secret_key = 'gersh'

@app.route('/', methods=['POST', 'GET'])
def truck_register():
    if request.method == 'POST':
        name = request.form['foodTruckName']
        cuisine = request.form['cuisineType']
        number = request.form['phoneNumber']
        hours = request.form['operatingHours']
        email = request.form['email']
        password = request.form['password']
        truck_id = truckdb.insert_truck(name, cuisine, number, hours, email, password)
        session['truck_id'] = truck_id
        return redirect(url_for('map'))
    return render_template('register_truck.html')

@app.route('/map', methods = ['POST', 'GET'])
def map():
    if 'truck_id' not in session:
        return redirect(url_for('truck_register'))
    return render_template('dashboard.html', truck_id=session['truck_id'])

@app.route('/api/update_marker', methods=['POST'])
def update_marker():
    if 'truck_id' not in session:
        return jsonify({"error": "Not logged in"}), 401
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(latitude)
    print(longitude)
    truckdb.update_truck_location(session['truck_id'], latitude, longitude)
    return jsonify({"success": True})



@app.route('/api/get_markers', methods=['GET'])
def get_markers():
    trucks = truckdb.get_all_trucks()
    markers = []
    
    for t in trucks:
        # t structure: (id, foodTruckName, cuisineType, phoneNumber, operatingHours, latitude, longitude, email, password)
        if t[7] is not None and t[8] is not None:  # Only include trucks with a marker
            markers.append({
                "id": t[0],
                "name": t[1],
                "lat": t[7],
                "lng": t[8]
            })
                   
    return markers

if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
