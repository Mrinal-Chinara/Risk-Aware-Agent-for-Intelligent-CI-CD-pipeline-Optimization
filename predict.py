import numpy as np
import joblib

model = joblib.load("model/model.pkl")

scaler = joblib.load("model/scaler.pkl")

tfidf = joblib.load("model/tfidf.pkl")

RISK_LABELS = [
    "Failure",
    "Performance",
    "Test",
    "Security"
]

def severity(prob):

    if prob > 0.8:
        return "HIGH"

    elif prob > 0.5:
        return "MEDIUM"

    return "LOW"

def predict_risk(input_num, input_text):

    num_scaled = scaler.transform([input_num])

    text_vec = tfidf.transform(
        [input_text]
    ).toarray()

    final_input = np.hstack((
        num_scaled,
        text_vec
    ))

    prediction = model.predict(final_input)

    probabilities = []

    for estimator in model.estimators_:

        prob = estimator.predict_proba(
            final_input
        )[0][1]

        probabilities.append(prob)

    result = {}

    for i, label in enumerate(RISK_LABELS):

        result[label] = {
            "prediction": int(
                prediction[0][i]
            ),
            "probability": float(
                probabilities[i]
            ),
            "severity": severity(
                probabilities[i]
            )
        }

    return result