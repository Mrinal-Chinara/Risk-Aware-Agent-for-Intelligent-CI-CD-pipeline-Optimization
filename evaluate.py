import joblib
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from preprocess import preprocess_data

def evaluate():
    X, y = preprocess_data("data/augmented_dataset.csv")

    # Same split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = joblib.load("model/model.pkl")

    y_pred = model.predict(X_test)

    print("\n📊 Classification Report:\n")
    print(classification_report(y_test, y_pred, zero_division=0))

if __name__ == "__main__":
    evaluate()