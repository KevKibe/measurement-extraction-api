from flask import Flask, request, jsonify
from measurement import extract_measurements

app = Flask(__name__)

@app.route('/extract_measurements', methods=['POST'])
def handle_extraction():
    # Assuming images are sent as files in the request
    front_image = request.files['front_image']
    side_image = request.files['side_image']

    # Perform measurement extraction
    measurements = extract_measurements(front_image, side_image)

    # Return the measurements as JSON response
    return jsonify(measurements)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
