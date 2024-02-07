# Measurement Extraction API Documentation
The Measurement Extraction API is a Flask-based web service that allows users to extract body measurements from front and side images of a person. This documentation provides information on how to interact with the API, the available endpoints, and their functionalities.

Base URL
The base URL for accessing the Measurement Extraction API is http://localhost:5000 when running locally. For production deployment, replace localhost with the appropriate domain name.

Endpoints
Extract Measurements
Endpoint: /extract_measurements (POST)

Description: Extracts body measurements from front and side images of a person.

Request Format:

HTTP Method: POST
Content-Type: multipart/form-data
Request Parameters:

front_image: Front image of the person (image file)
side_image: Side image of the person (image file)
Response Format:

Content-Type: application/json
Response Parameters:

height: Height of the person in centimeters.
chest: Chest measurement of the person in centimeters.
waist: Waist measurement of the person in centimeters.
hip: Hip measurement of the person in centimeters.
shoulder_width: Shoulder width of the person in centimeters.
arm_length: Arm length of the person in centimeters.
leg_length: Leg length of the person in centimeters.
neck_circumference: Neck circumference of the person in centimeters.
head_circumference: Head circumference of the person in centimeters.
foot_length: Foot length of the person in centimeters.
wrist_circumference: Wrist circumference of the person in centimeters.
bicep_circumference: Bicep circumference of the person in centimeters.
