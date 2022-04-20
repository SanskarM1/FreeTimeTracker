# Flask helps build API - allows website to access database
import datetime
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
    CREATE TABLE IF NOT EXISTS logged_hours(
        Username varchar(255),
        Categories varchar(255),
        Hours float,
        day date
    );    
    ''')
except sqlite3.Error as e:
    print(f'Failed to create table, Error: {e}')

try:
    connection.execute('''
    CREATE TABLE IF NOT EXISTS goals(
        Username varchar(255),
        Categories varchar(255),
        Hours float,
        day date
    );    
    ''')

except sqlite3.Error as e:
    print(f'Failed to create table, Error: {e}')

try:
    connection.execute('''
    CREATE TABLE IF NOT EXISTS login(
        Username varchar(255),
        Password varchar(255),
    
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
    day = body.get("date", None)

    # categories = body.get("categories", None)
    # pprint.pprint(categories)
    # for category in categories.keys():
    # print(category, categories.get(category))

    # TODO Add information to database

    connection.execute(f'''
    INSERT INTO logged_hours (Username, Categories, Hours, day)
    VALUES ("{username}", "{category}", "{hours}", "{day}")
    ''')

    # for category in categories.keys():
    # connection.execute(f'''
    # INSERT INTO logged_hours (Username, Categories, Hours)
    # VALUES ("{username}", "{category}", {categories.get(category)});
    # ''')

    # connection.execute(f'''
    # INSERT INTO logged_hours (Categories, Hours)
    # VALUES ("entertainment", {5});
    # ''')
    connection.commit()
    cursor = connection.cursor()
    cursor.execute("SELECT username, categories, hours FROM logged_hours;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    return "SUCCESS: INFORMATION ADDED"


@app.route('/getdata', methods=["GET"])
def get_data():
    username = request.args.get('username')

    returninfo = connection.cursor()

    returninfo.execute(f"SELECT username, categories, hours FROM logged_hours WHERE username = '{username}';")

    return jsonify(returninfo.fetchall());


# TODO ADD METHOD TO CLEAR ALL DATA IN DATABASE


@app.route("/signup", methods=["POST"])
def signup():
    body = request.json
    if body is None:
        return "Error: NO USER PROVIDED"
    user = body.get("user", None)
    password = body.get("password", None)

    if user is None or password is None:
        return "Error: INCOMPLETE CREDENTIALS"

    try:
        query = f'''
            INSERT INTO login (Username, Password) VALUES ("{user}", "{password}");
            '''
        connection.execute(query)
        connection.commit()

        return "SUCCESS: USER CREATED"

    except Exception as e:
        print(e)
        return "FAILURE"


@app.route('/weeklyaverage', methods=["GET"])
def weekly_average():
    username = request.args.get('username')
    query = f'''
    SELECT Categories, AVG(hours) 
    FROM logged_hours
    WHERE Username = "{username}" and day > datetime('now', '-5 days')
    GROUP BY Categories;   
    '''
    weeklyaverage1 = connection.cursor()
    weeklyaverage1.execute(query)

    return jsonify(weeklyaverage1.fetchall());

@app.route('/login', methods=["GET"])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    login = connection.cursor()

    login.execute(f'''
    SELECT username, password 
    FROM login 
    WHERE username = "{username}" AND password = "{password}"
    ''')

    print(username)
    print(password)

    #TODO if login.fetchone is none, then login failed, otherwise it worked

    if(login.fetchone()):
        return {
            "login": 0
        }
    else:
        return {
            "login": 1
        }





@app.route('/setgoals', methods=["POST"])
def set_goals():
    body = request.json
    if body is None:
        return "Error: NO DATA PROVIDED"

    print(body)
    username = body.get("username", None)
    category = body.get("category", None)
    hours = body.get("hours", None)
    day = datetime.date.today()

    connection.execute(f'''
        INSERT INTO goals (Username, Categories, Hours, day)
        VALUES ("{username}", "{category}", "{hours}", "{day}")
        ''')

    connection.commit()

    return "GOAL ADDED"


@app.route('/checkprogress', methods=["GET"])
def check_progress():
    username = request.args.get('username')
    category = request.args.get('category')
    query = f'''
    SELECT hours, day 
    FROM goals
    WHERE username = "{username}" AND categories = "{category}"
    ORDER BY day DESC;
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    goal = cursor.fetchone()

    query = f'''
        SELECT SUM(hours) 
        FROM logged_hours
        WHERE Username = "{username}" and Categories = "{category}" and day >= "{goal[1]}";   
        '''
    cursor.execute(query)

    current_hours = cursor.fetchone()

    return {
        "difference": current_hours[0] - goal[0]
    }


@app.route("/comparedata", methods=["GET"])
def comparedata():
    username = request.args.get("username")
    username2 = request.args.get("username2")
    category = request.args.get("category")
    print(username)
    print(username2)
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT SUM(hours)
        FROM logged_hours
        WHERE username = "{username}" AND categories = "{category}" AND day >= datetime('now' , '-7 days')

        ''')

    username1hours = cursor.fetchone()[0]

    cursor.execute(f'''
            SELECT SUM(hours)
            FROM logged_hours
            WHERE username = "{username2}" AND categories = "{category}" AND day >= datetime('now' , '-7 days')

            ''')

    username2hours = cursor.fetchone()[0]

    print(username1hours)
    print(username2hours)

    comparison = username1hours - username2hours

    if (comparison > 0):
        return f"You have {comparison} more hours than {username2}"
    elif (comparison == 0):
        return f"You and {username2} are tied with {username1hours} hours"
    else:
        return f"You have {-comparison} less hours than {username2}"

@app.route("/getusernames", methods=["GET"])
def getusernames():
    cursor = connection.cursor()
    cursor.execute("SELECT Username FROM login")

    return {"usernames" : cursor.fetchall()}



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8081)
