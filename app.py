from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/character', methods=['POST'])
def get_character():
    data = request.get_json()
    
    if not data or 'character_id' not in data:
        return jsonify({'error': "id not found on request"}), 400

    id = data['character_id']
    response = requests.get(f'https://rickandmortyapi.com/api/character/{id}')

    if response.status_code == 200:
        character_data = response.json()
        character_info = {
            'name': character_data.get('name'),
            'status': character_data.get('status')
        }
        return jsonify(character_info), 200
    else:
        return jsonify({"error": "Character not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)