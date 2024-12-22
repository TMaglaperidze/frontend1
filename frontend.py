from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

BACKEND_1_URL = "http://localhost:5001/status"
BACKEND_2_URL = "http://localhost:5002/status"

def check_backend_status():
    try:
        response_1 = requests.get(BACKEND_1_URL, timeout=2)
        response_2 = requests.get(BACKEND_2_URL, timeout=2)

        status_1 = response_1.json()
        status_2 = response_2.json()

        return {
            "service_1": {"status": status_1.get("status"), "name": status_1.get("service_name")},
            "service_2": {"status": status_2.get("status"), "name": status_2.get("service_name")},
        }
    except Exception as e:
        return {"error": str(e)}

@app.route('/status', methods=['GET'])
def status():
    return jsonify(check_backend_status()), 200

if __name__ == '__main__':
    time.sleep(2)  # Give backend services time to start
    print("Checking backend services...")
    app.run(host='0.0.0.0', port=5000)
