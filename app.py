from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        data = request.json.get('data', [])
        if not isinstance(data, list):
            return jsonify({"is_success": False, "error": "Invalid input format"}), 400
        
        user_id = "john_doe_17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_lowercase = [max([x for x in alphabets if x.islower()], default="")]

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }
        return jsonify(response)

    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
