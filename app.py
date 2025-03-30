from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow CORS for all domains (you can restrict this to specific domains later)
CORS(app, resources={r"/*": {"origins": "*"}})

entries = []

@app.route('/all-entries', methods=['GET'])
def all_entries():
    return jsonify(entries), 200

@app.route('/new-entry', methods=['POST'])
def new_entry():
    data = request.get_json()
    print("Received new entry:", data)
    entries.append(data)
    return jsonify({"message": "Entry added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
