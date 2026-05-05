import pickle
from feature_extractor import extract_features

svm = pickle.load(open("models/svm.pkl", "rb"))
rf = pickle.load(open("models/rf.pkl", "rb"))

def predict(code):
    features = extract_features(code)

    svm_pred = svm.predict([features])[0]
    rf_pred = rf.predict([features])[0]

    final = round((svm_pred + rf_pred) / 2)

    label = "AI Generated" if final == 1 else "Human Written"

    return label, features