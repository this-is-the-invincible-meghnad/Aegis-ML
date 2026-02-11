import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("[1/3] Creating ADVANCED training data...")


# 1 = Open, 0 = Closed
data = {
    '21':   [0, 1, 0, 0, 1, 0, 0, 1], # FTP
    '22':   [1, 1, 1, 0, 0, 1, 0, 0], # SSH
    '23':   [0, 0, 1, 0, 1, 0, 0, 1], # Telnet (Unsafe)
    '80':   [1, 1, 1, 1, 0, 1, 1, 0], # HTTP
    '443':  [1, 1, 0, 1, 0, 1, 1, 0], # HTTPS
    '445':  [0, 0, 1, 1, 1, 0, 0, 1], # SMB (Critical Risk)
    '3389': [0, 0, 0, 0, 1, 0, 0, 1], # RDP
    'label': [
        'SAFE', 'SAFE', 'DANGEROUS', 'DANGEROUS', 'DANGEROUS', 
        'SAFE', 'SAFE', 'DANGEROUS'
    ]
}

df = pd.DataFrame(data)
X = df.drop('label', axis=1)
y = df['label']

print("[2/3] Training the Aggressive Model...")
# We use n_estimators=200 for a bigger brain
model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)

print("[3/3] Saving 'aegis_brain.pkl'...")
joblib.dump(model, 'aegis_brain.pkl')
print("DONE! Brain upgraded.")