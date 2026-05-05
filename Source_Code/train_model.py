import os
import pickle
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from feature_extractor import extract_features

X, y = [], []

def load(folder, label):
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r", errors="ignore") as f:
            code = f.read()
            X.append(extract_features(code))
            y.append(label)

load("dataset/ai_code", 1)
load("dataset/human_code", 0)

svm = SVC(probability=True)
rf = RandomForestClassifier()

svm.fit(X, y)
rf.fit(X, y)

os.makedirs("models", exist_ok=True)

pickle.dump(svm, open("models/svm.pkl", "wb"))
pickle.dump(rf, open("models/rf.pkl", "wb"))

print("Models trained and saved!")