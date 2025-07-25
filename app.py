from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Grab values from form
        values = request.form.values()
        if not all(values) or any(v.strip() == '' for v in values):
            return render_template('index.html', prediction_text="⚠️ Please enter all values before submitting.")

        # Convert to float and make prediction
        features = [float(v) for v in values]
        prediction = model.predict([features])[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        return render_template('index.html', prediction_text=f"🩺 Result: {result}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
