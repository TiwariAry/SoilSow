from flask import Flask, request, render_template
import numpy as np
import joblib

import google.generativeai as genai

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Load trained model and label encoder
model = joblib.load("crop_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

# Home
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input from form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
        prediction = model.predict(features)[0]
        crop = label_encoder.inverse_transform([prediction])[0].capitalize()

        print(crop)

        prompt = f"""
        Given the following soil and weather conditions:
        - Nitrogen: {N}
        - Phosphorus: {P}
        - Potassium: {K}
        - Temperature: {temp}°C
        - Humidity: {humidity}%
        - pH: {ph}
        - Rainfall: {rainfall}mm

        The predicted crop is: {crop}.
        
        Please explain in one detailed and well-written paragraph why this crop is suitable for these conditions. Avoid using bullet points or numbering. Use simple, friendly, and natural language.
        Also, give me the name of the possible locations in India where these conditions are present in seperate paragraph. Start this paragraph with ';' symbol.
        """

        response = gemini_model.generate_content(prompt)
        explanation = response.text.strip()
        crop_explanation, location_prediction = explanation.split(';')

        return render_template("result.html", result=f"Recommended Crop: {crop}", crop_explanation=crop_explanation, location_prediction=location_prediction)

    except Exception as e:
        return render_template("index.html", result=f"Error: {str(e)}")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)