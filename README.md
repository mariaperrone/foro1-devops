# Crear ambiente
python -m venv .venv

# Activar ambiente
.venv\Scripts\activate

# Instalar Flask
pip install flask

# Instalar requests
pip install requests

# Cómo correr la API:
python app.py

# Cómo consumir la API:
En tu terminal, corre el siguiente comando:

curl -X POST http://127.0.0.1:5000/character -H "Content-Type: application/json" -d '{"character_id": 1}'

- Puedes cambiar character_id por el valor de tu preferencia hasta el 826, luego recibirás el error de "Character not found".
- En caso de no enviar un id, recibirás el error "id not found on request".