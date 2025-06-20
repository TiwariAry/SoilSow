# 🌾 SoilSow: Intelligent Crop Recommendation System

**SoilSow** is an AI-powered web application that recommends the most suitable crop based on user-provided soil and weather conditions, and explains the recommendation using natural language via the Gemini API.

🌐 **Live App**: [SoilSow](https://soilsow.onrender.com/)  
<br/>

![image](https://github.com/user-attachments/assets/42456621-ce19-4f8e-926a-d475225e94aa)
![image](https://github.com/user-attachments/assets/4a6fc803-b654-455d-973e-4ecafe4dfda8)

---

## 📸 Features

- 🌱 Predicts the best crop based on:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH
  - Rainfall
- 🤖 Uses a trained machine learning model (`Random Forest`) for prediction.
- 💬 Integrated with **Gemini Pro (Google Generative AI)** to generate:
  - A detailed explanation for the recommended crop.
  - A list of possible Indian regions matching the input conditions.
- 📦 Web interface built with **Flask**, styled using custom CSS.
- ☁️ Deployed on **Render** for public access.

---

## 🧠 Model Training Notebook

Model was trained on crop recommendation dataset.

📓 [Google Colab Notebook](https://colab.research.google.com/drive/1ynNjzuv4nNz5uEhVCslWmjVg17Cj6QHd?usp=sharing)

---

## 🌿 System Overview

![image](https://github.com/user-attachments/assets/4f4575a6-5c7d-4556-a509-61a13a26a057)

---

## 🗂️ Project Structure

```bash
SoilSow/
│
├── app.py                  # Main Flask application: routing, prediction logic, and Gemini API interaction
├── .env                    # Stores environment variables securely
├── crop_model.pkl          # Trained machine learning model used for crop prediction
├── label_encoder.pkl       # Encoder to map predicted numerical labels back to crop names
├── requirements.txt        # Python dependencies needed to run the app
├── Procfile                # Specifies command to run the app on Render
│
├── templates/              # Folder for HTML templates rendered by Flask
│   ├── index.html          # Main form where users input soil and climate parameters
│   └── result.html         # Page displaying predicted crop and AI-generated explanation
│
├── static/                 # Folder for static assets like stylesheets and images
│   ├── indexStyle.css      # CSS styling for index.html (input form)
│   ├── resultStyle.css     # CSS styling for result.html (prediction and explanation)
│   ├── bg.jpg              # Background image used in the web UI
│   └── favicon.ico         # Favicon shown in the browser tab

```

---

## 🚀 How It Works

### 🌱 Input & Prediction
1. User enters soil and weather parameters (Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall) into the form.
2. The input is sent via POST request to the `/predict` route on the Flask backend.
3. The backend uses a trained Random Forest model to predict the most suitable crop based on the input features.
4. The predicted crop label is decoded using the label encoder.

### 🤖 AI Explanation (Gemini API)
1. The backend generates a detailed prompt including input parameters and predicted crop.
2. This prompt is sent to the Google Gemini generative AI API.
3. Gemini returns a detailed natural language explanation of why the predicted crop is suitable for the given conditions, along with possible Indian regions where these conditions exist.
4. The Flask backend sends the prediction and AI explanation to the frontend.

### 📄 Display Results
1. The results page renders the recommended crop along with the AI-generated explanation and location suggestions.
2. User can review the recommendation and understand the reasoning behind it.

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/TiwariAry/SoilSow.git
cd SoilSow
```

#### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

---

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Setup Environment Variables
Create a .env file in the root directory and add your Gemini API Key:
```bash
GEMINI_API_KEY=your_gemini_api_key
```

#### 5. Run the App
```bash
python app.py
```

---

## 🧠 Learnings & Highlights

- Integrated **Gemini 2.5 Flash** API for natural language crop recommendations
- Trained and deployed a **Random Forest** model for crop prediction using soil and climate data
- Built a user-friendly web interface using **Flask**, **HTML/CSS**, and **Jinja2 templating**
- Secured API keys using environment variables and deployed the app seamlessly on **Render**
- Gained experience in serving machine learning models in production with dynamic input handling

---

## 📣 Future Enhancements

- 🌾 Add support for **multiple crop suggestions** with confidence levels
- 📍 Integrate **location-based auto-detection** using IP or browser geolocation
- 🌐 Multilingual support for farmers in regional Indian languages
- 🧠 Enhance AI response with **visual graphs** or **nutrient charts**
- 🗃️ Add a **crop history dashboard** to track previous predictions

---

## 🤝 Contributing

Pull requests are welcome! For significant changes, please open an issue first to discuss what you would like to change.  
Let’s grow **SoilSow** together into a smarter, farmer-friendly recommendation system! 🌱

---

## 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).  
Feel free to fork, modify, and build on it.

---

## 👨‍💻 Author

**Aryan Tiwari**  
📫 [LinkedIn](https://www.linkedin.com/in/aryan-tiwari-6844a9250)  
💻 [GitHub](https://github.com/TiwariAry)

---
