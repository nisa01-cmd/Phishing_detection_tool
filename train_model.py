
import pandas as pd
import re
import whois
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

def get_domain_age_days(url):
    try:
        domain = re.findall(r'https?://(?:www\.)?([^/]+)', url)[0]
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        return (datetime.now() - creation_date).days if creation_date else 0
    except:
        return 0

def extract_features(url):
    return [
        len(url),
        1 if '@' in url else 0,
        1 if '-' in url else 0,
        1 if '//' in url else 0,
        1 if re.match(r'https?://\d+\.\d+\.\d+\.\d+', url) else 0,
        1 if any(w in url.lower() for w in ['login', 'secure', 'update', 'verify']) else 0,
        get_domain_age_days(url)
    ]

df = pd.read_csv("phishing_dataset.csv")
X = [extract_features(url) for url in df['url']]
y = LabelEncoder().fit_transform(df['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'phishing_model_with_domain.pkl')
print("✅ Model trained and saved as 'phishing_model_with_domain.pkl'")
