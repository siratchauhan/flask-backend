from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded user details
user_id = "sirat_05082004"
email = "siratchauhan8@gmail.com"
roll_number = "2221345"

@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    try:
        data = request.json.get('data', [])
        
        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        # Find the highest alphabet (case insensitive)
        highest_alphabet = max(alphabets, key=lambda x: x.lower()) if alphabets else []
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)