import sqlite3

DATABASE = 'food_truck.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS trucks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        foodTruckName TEXT,
                        cuisineType TEXT,
                        phoneNumber TEXT,
                        operatingHours TEXT,
                        latitude REAL,
                        longitude REAL,
                        email TEXT,  
                        password TEXT)''')
    conn.commit()
    conn.close()
    
# def clear_all_trucks():
#     conn = sqlite3.connect(DATABASE)
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM trucks")
#     conn.commit()
#     conn.close()
# clear_all_trucks() 

def insert_truck(name, cuisine, number, hours, email, password):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trucks (foodTruckName, cuisineType, phoneNumber, operatingHours, email, password) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, cuisine, number, hours, email, password))
    truck_id = cursor.lastrowid  # Get the truck's unique id
    conn.commit()
    conn.close()
    return truck_id

def update_truck_location(truck_id, latitude, longitude):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE trucks SET latitude = ?, longitude = ? WHERE id = ?", (latitude, longitude, truck_id))
    conn.commit()
    conn.close()

def delete_marker(truck_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE trucks SET latitude = NULL, longitude = NULL WHERE id = ?", (truck_id,))
    conn.commit()
    conn.close()

def get_all_trucks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trucks")
    trucks = cursor.fetchall()
    conn.close()
    return trucks
def get_truck_by_id(truck_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trucks WHERE id = ?", (truck_id,))
    truck = cursor.fetchone()
    conn.close()
    return truck
    
def get_truck_by_email(email):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trucks WHERE email = ?", (email,))
    truck = cursor.fetchone()
    conn.close()
    return truck

