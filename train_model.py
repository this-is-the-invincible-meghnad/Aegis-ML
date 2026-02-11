import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("[1/3] Loading 'dataset.csv'...")

try:
    # Load the CSV file (Real Data Mode)
    df = pd.read_csv('dataset.csv')
    print(f"[+] Successfully loaded {len(df)} training examples.")
except FileNotFoundError:
    print("[-] ERROR: dataset.csv not found! Create it first.")
    exit()

# Separate features (X) and labels (y)
X = df.drop('label', axis=1)
y = df['label']

print("[2/3] Training the Random Forest model...")
# n_estimators=100 means 100 "decision trees" voting
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

print("[3/3] Saving 'aegis_brain.pkl'...")
joblib.dump(model, 'aegis_brain.pkl')
print("DONE! Brain upgraded with external data.")