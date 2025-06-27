
import tkinter as tk
from tkinter import messagebox
import re
import whois
from datetime import datetime
import joblib
import numpy as np

model = joblib.load('phishing_model_with_domain.pkl')

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
    return np.array([
        [
            len(url),
            1 if '@' in url else 0,
            1 if '-' in url else 0,
            1 if '//' in url else 0,
            1 if re.match(r'https?://\d+\.\d+\.\d+\.\d+', url) else 0,
            1 if any(w in url.lower() for w in ['login', 'secure', 'update', 'verify']) else 0,
            get_domain_age_days(url)
        ]
    ])

def check_url():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    features = extract_features(url)
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0][prediction] * 100
    age_days = features[0][-1]
    verdict = "Phishing 🔴" if prediction == 1 else "Legitimate 🟢"
    age_info = f"Domain age: {age_days} days" if age_days > 0 else "Domain age: Unknown"
    result = f"{verdict}\nConfidence: {confidence:.2f}%\n{age_info}"
    result_label.config(text=result, fg="red" if prediction == 1 else "green")

window = tk.Tk()
window.title("Phishing URL Detector")
window.geometry("500x300")
window.configure(bg="#f4f4f4")

title = tk.Label(window, text="ML Phishing URL Detector", font=("Arial", 18, "bold"), bg="#f4f4f4")
title.pack(pady=15)

url_entry = tk.Entry(window, width=50, font=("Arial", 12))
url_entry.pack(pady=10)

check_button = tk.Button(window, text="Check URL", command=check_url, font=("Arial", 12), bg="#2a9d8f", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14), bg="#f4f4f4")
result_label.pack(pady=15)

window.mainloop()
