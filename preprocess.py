import pandas as pd
import numpy as np
import joblib
import os

from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_data(file_path):

    df = pd.read_csv(file_path)

    # Numerical Features
    num_cols = [

        'error_count',
        'duration',
        'test_failed',
        'coverage',
        'cpu_usage',
        'memory_usage',
        'past_failures'
    ]

    # Text Feature
    text_col = 'log_text'

    # Target Columns
    target_cols = [

        'Failure_Risk',
        'Performance_Risk',
        'Test_Risk',
        'Security_Risk'
    ]

    # Fill missing values
    df[num_cols] = df[num_cols].fillna(0)

    df[text_col] = df[text_col].fillna("")

    # Scale numerical data
    scaler = StandardScaler()

    X_num = scaler.fit_transform(
        df[num_cols]
    )

    # TF-IDF vectorization
    tfidf = TfidfVectorizer(
        max_features=1000
    )

    X_text = tfidf.fit_transform(
        df[text_col]
    ).toarray()

    # Combine features
    X = np.hstack((
        X_num,
        X_text
    ))

    y = df[target_cols]

    # Create model folder
    os.makedirs(
        "model",
        exist_ok=True
    )

    # Remove old scaler
    if os.path.exists("model/scaler.pkl"):

        os.remove("model/scaler.pkl")

    # Remove old tfidf
    if os.path.exists("model/tfidf.pkl"):

        os.remove("model/tfidf.pkl")

    # Save preprocessors
    joblib.dump(
        scaler,
        "model/scaler.pkl"
    )

    joblib.dump(
        tfidf,
        "model/tfidf.pkl"
    )

    return X, y