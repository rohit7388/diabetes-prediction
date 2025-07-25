@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs from form
        values = request.form.values()
        if not all(values) or any(v.strip() == '' for v in values):
            return render_template('index.html', prediction_text="⚠️ Please enter all values before submitting.")

        # Convert inputs to float and predict
        features = [float(x) for x in values]
        prediction = model.predict([features])[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        return render_template('index.html', prediction_text=f'Result: {result}')

    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")
