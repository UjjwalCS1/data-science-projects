import streamlit as st
import joblib

# Load model and encoder
model = joblib.load("../src/emotion_detector_model.pkl")
encoder = joblib.load("../src/emotion_encoder.pkl")

# App title
st.title("Emotion Detector using LinearSVC")

# User input
text = st.text_area("Enter your text")

# Prediction button
if st.button("Predict Emotion"):

    prediction = model.predict([text])

    emotion = encoder.inverse_transform(prediction)

    st.success(f"Predicted Emotion: {emotion[0]}")
