# Emotion Detector using Machine Learning

A simple Emotion Detection web app built using **Machine Learning**, **Streamlit**, and **LinearSVC**.
The model predicts human emotions from text input such as joy, sadness, anger, fear, love, and surprise.

---

## 🚀 Features

* Predict emotions from text
* Streamlit web interface
* Machine Learning model using LinearSVC
* Label encoding support
* Fast and lightweight application

---

## 📂 Project Structure

```bash
Emotion-Detector/
│
├── app/
│   └── app.py
│
├── data/
│   └── train.txt
│
├── notebook/
│   └── Emotion-detetctor.ipynb
│
├── src/
│   ├── emotion_detector_model.pkl
│   └── emotion_encoder.pkl
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🧠 Technologies Used

* Python
* Scikit-learn
* Streamlit
* Joblib
* NLP

---

## 📊 Dataset

The dataset contains text sentences with labeled emotions like:

* Joy
* Sadness
* Anger
* Fear
* Love
* Surprise

Example dataset sample:
`i feel amazing;joy` 

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/emotion-detector.git
cd emotion-detector
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 💻 Streamlit App

The application takes user text input and predicts the emotion using the trained model. 

Example:

```python
prediction = model.predict([text])
emotion = encoder.inverse_transform(prediction)
```

---

## 🧪 Example Inputs

| Text                    | Predicted Emotion |
| ----------------------- | ----------------- |
| I am very happy today   | Joy               |
| I feel lonely and sad   | Sadness           |
| I am really angry       | Anger             |
| I am scared about exams | Fear              |

---

## 📸 Output

```bash
Predicted Emotion: Joy
```

---

## 📌 Future Improvements

* Deep Learning implementation
* BERT/Transformer model
* Better UI design
* Deployment on Streamlit Cloud
* Real-time sentiment analytics

---

## 👨‍💻 Author

Ujjwal Kumar

---

## ⭐ If you like this project

Give this repository a star on GitHub ⭐
