from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your OpenCage API key (FREE at https://opencagedata.com/)
OPENCAGE_API_KEY = "be513fc9c21a4a0e885fb5bfa10d3e22"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/geocode", methods=["POST"])
def geocode():
    data = request.get_json()
    city = data.get("city")

    if not city:
        return jsonify({"error": "City not provided"}), 400

    geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={OPENCAGE_API_KEY}"
    response = requests.get(geocode_url).json()

    if response["results"]:
        location = response["results"][0]["geometry"]
        return jsonify({"lat": location["lat"], "lng": location["lng"]})
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
