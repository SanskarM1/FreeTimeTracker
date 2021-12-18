# Flask helps build API - allows website to access database
import sqlite3

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Opens the database as a SQLite connection , creates it if it doesnt exist
connection = sqlite3.connect('database.db', check_same_thread=False)

# TODO Create Table!! + error handling

try:
    connection.execute('''
    CREATE TABLE logged_hours(
        Username varchar(255),
        Categories varchar(255),
        Hours float
    );    
    ''')
except sqlite3.Error as e:
    print(f'Failed to create table, Error: {e}')


@app.route("/inputdata", methods=["POST"])
def log_hours():
    body = request.json
    if body is None:
        return "Error: NO DATA PROVIDED"

    print(body)
    username = body.get("username", None)
    category = body.get("category", None)
    hours = body.get("hours", None)

    #categories = body.get("categories", None)
    # pprint.pprint(categories)
    #for category in categories.keys():
        #print(category, categories.get(category))

    # TODO Add information to database

    connection.execute(f'''
    INSERT INTO logged_hours (Username, Categories, Hours)
    VALUES ("{username}", "{category}", "{hours}")
    ''')

    #for category in categories.keys():
        #connection.execute(f'''
        #INSERT INTO logged_hours (Username, Categories, Hours)
        #VALUES ("{username}", "{category}", {categories.get(category)});
        #''')

    # connection.execute(f'''
    # INSERT INTO logged_hours (Categories, Hours)
    # VALUES ("entertainment", {5});
    # ''')
    connection.commit()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM logged_hours;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    return "SUCCESS: INFORMATION ADDED"


@app.route('/getdata', methods=["GET"])
def get_data():
    username = request.args.get('username')
    # Todo GET INFO FROM DATABASE
    # Have a way for user to enter in username info and get information for specific user
    returninfo = connection.cursor()
    returninfo.execute("SELECT * FROM logged_hours;")
    rows = returninfo.fetchall()
    information_list = []
    for row in rows:
        if row[2] == username:
            print(row)
            information_list.append(row)


    # Transformation step --> translate info from database to API

    # return transform data
    return jsonify(information_list)


# TODO ADD METHOD TO CLEAR ALL DATA IN DATABASE

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8081)


@app.route("/createuser", methods=["POST"])
def post():
    body = request.json
    if body is None:
        return "Error: NO USER PROVIDED"
    user = body.get("username", None)
    password = body.get("password", None)

    if user is None or password is None:
        return "Error: INCOMPLETE CREDENTIALS"

    # TODO Create user in database

    return "SUCCESS: USER CREATED"
