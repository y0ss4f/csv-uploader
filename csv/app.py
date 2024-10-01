from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
import os
import pandas as pd
import json
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Database setup
DATABASE = 'data.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS csv_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Age INTEGER,
            Occupation TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('display_table', filename=file.filename))

@app.route('/display/<filename>')
def display_table(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(filepath)
    return render_template('table.html', tables=[df.to_html(classes='table table-striped', header="true")])

@app.route('/save', methods=['POST'])
def save_table():
    data = request.json.get('data')
    if data:
        try:
            # Convert data to DataFrame
            df = pd.DataFrame(data[1:], columns=data[0])  # Use first row as headers
            print("Data to be saved:", df)  # Log the data
            
            # Save to database
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM csv_data')  # Clear the table before inserting new data
            
            for index, row in df.iterrows():
                cursor.execute('INSERT INTO csv_data (Name, Age, Occupation) VALUES (?, ?, ?)', (row['Name'], row['Age'], row['Occupation']))
            
            conn.commit()
            conn.close()
            return jsonify({'message': 'Data saved successfully!'}), 200
        except Exception as e:
            print("Error saving data:", e)  # Log any error
            return jsonify({'message': 'Failed to save data!'}), 400
    return jsonify({'message': 'No data received!'}), 400




@app.route('/export')
def export_data():
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Fetch all data from the csv_data table
    cursor.execute("SELECT Name, Age, Occupation FROM csv_data")
    rows = cursor.fetchall()
    
    # Create a CSV file in memory
    output = "Name,Age,Occupation\n"
    for row in rows:
        output += f"{row[0]},{row[1]},{row[2]}\n"
    
    conn.close()

    # Create a response to return the CSV file
    response = make_response(output)
    response.headers["Content-Disposition"] = "attachment; filename=exported_data.csv"
    response.headers["Content-Type"] = "text/csv"
    return response

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
