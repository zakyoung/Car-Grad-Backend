from flask import Flask, request, jsonify
from flask_cors import CORS
from entryHelpers import create_entry_from_request, create_entry_from_object_in_database
from databaseExchange import get_all_entries
import logging
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/all-entries', methods=['GET'])
def all_entries():
    entries = get_all_entries()
    entries_as_dicts = [entry.to_dict() for entry in entries]
    return jsonify(entries_as_dicts), 200

@app.route('/new-entry', methods=['POST'])
def new_entry():
    entry = create_entry_from_request(request)
    if create_entry_from_object_in_database(entry):
        return jsonify({"message": "Entry added successfully"}), 201
    else:
        logging.error("There was an issue adding the entry to the database")
        return jsonify({"message": "There was an issue adding the entry"}), 400

if __name__ == '__main__':
    app.run(debug=True)
