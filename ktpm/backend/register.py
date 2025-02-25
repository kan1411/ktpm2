from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Cho phép mọi nguồn

logging.basicConfig(level=logging.DEBUG)

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="register"
    )
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            role VARCHAR(10) NOT NULL,
            area VARCHAR(255) NOT NULL,
            phone VARCHAR (20) NOT NULL,
            academic VARCHAR(255) NOT NULL
        )
    """)
    db.commit()
except mysql.connector.Error as err:
    app.logger.error(f"Error: {err}")

@app.route('/checkUser', methods=['POST'])
def check_user():
    cursor = db.cursor()
    try:
        data = request.json
        app.logger.debug(f"Received data for checkUser: {data}")
        
        if not data:
            return jsonify({"error": "No data provided"}), 400

        username = data.get('username')
        phone = data.get('phone')

        query = "SELECT * FROM users WHERE username = %s OR phone = %s"
        cursor.execute(query, (username, phone))
        results = cursor.fetchall()

        if results:
            existing_user = any(user[1] == username for user in results)
            existing_phone = any(user[7] == phone for user in results)

            if existing_user:
                return jsonify({"message": "Username đã tồn tại!"}), 400
            if existing_phone:
                return jsonify({"message": "Phone đã tồn tại!"}), 400

        return jsonify({"message": "Username và Phone hợp lệ."}), 200
    except mysql.connector.Error as err:
        app.logger.error(f"Lỗi khi kiểm tra: {err}")
        return jsonify({"message": f"Lỗi khi kiểm tra: {err}"}), 500
    finally:
        cursor.close()

@app.route('/register', methods=['POST'])
def register():
    cursor = db.cursor()
    try:
        data = request.json 
        app.logger.debug(f"Received data for register: {data}")
        
        if not data:
            return jsonify({"error": "No data provided"}), 400

        username = data.get('username')
        password = data.get('password')  
        name = data.get('name')
        gender = data.get('gender')
        role = data.get('role')
        area = data.get('area')
        phone = data.get('phone')
        academic = data.get('academic')

        query = "SELECT * FROM users WHERE username = %s OR phone = %s"
        cursor.execute(query, (username, phone))
        results = cursor.fetchall()

        if results:
            existing_user = any(user[1] == username for user in results)
            existing_phone = any(user[7] == phone for user in results)

            if existing_user:
                return jsonify({"message": "Username đã tồn tại!"}), 400
            if existing_phone:
                return jsonify({"message": "Phone đã tồn tại!"}), 400

        query = """
            INSERT INTO users (username, password, name, gender, role, area, phone, academic)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (username, password, name, gender, role, area, phone, academic)
        cursor.execute(query, values)
        db.commit()
        response = {'message': 'Đăng ký thành công rồi, bạn giỏi quá!!!'}
    except mysql.connector.Error as err:
        app.logger.error(f"Lỗi khi đăng ký: {err}")
        response = {'message': f'Lỗi khi đăng ký: {err}'}
    finally:
        cursor.close()
    return jsonify(response)

if db.is_connected():
    app.logger.info("Kết nối thành công đến cơ sở dữ liệu MySQL.")
else:
    app.logger.error("Kết nối không thành công đến cơ sở dữ liệu MySQL.")

if __name__ == '__main__':
    app.run(debug=True)
