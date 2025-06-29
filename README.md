# 🔐 Phishing URL Detector using Machine Learning + Domain Intelligence

This project is a smart and interactive tool that detects phishing websites based on the structure of a URL and the domain's age using Machine Learning and WHOIS data. It provides real-time results via a user-friendly Python GUI built with Tkinter.

---

## 📌 Features

✅ Detects whether a URL is **Phishing** or **Legitimate**  
✅ Displays a **confidence score** (%) from a trained Random Forest model  
✅ Shows **domain age** (in days) using WHOIS lookups  
✅ Built with a simple and clean **Tkinter GUI**  
✅ Fully offline, privacy-respecting model once trained  
✅ Expandable to support browser plugins, web versions, and more

---

## 💻 Tech Stack

- **Frontend GUI**: Python Tkinter  
- **ML Backend**: Scikit-learn (RandomForestClassifier)  
- **Data Extraction**: Regex, WHOIS (`python-whois`)  
- **Model Saving/Loading**: Joblib  
- **Dataset**: Custom CSV file with URLs and labels (phishing or legitimate)

---

## 📁 Folder Structure

```

Phishing\_URL\_Detector\_Project/
│
├── phishing\_dataset.csv              # Sample dataset
├── train\_model.py                    # Script to train and save model
├── main\_gui.py                       # Tkinter GUI app to check URLs
├── phishing\_model\_with\_domain.pkl    # Model file (generated after training)
└── README.md                         # Project details

````

---

## 🧠 Dataset

The sample dataset `phishing_dataset.csv` includes:
- 10 real-looking phishing URLs
- 10 legitimate popular URLs  
Each URL is labeled as either `phishing` or `legitimate`.

---

## ⚙️ How it Works

1. **Feature Extraction**:
   - URL length
   - Use of '@' symbol
   - Presence of hyphens (`-`)
   - Use of double slashes after domain
   - Use of IP addresses
   - Suspicious keywords like `login`, `secure`, `update`, `verify`
   - **Domain age (in days)** from WHOIS data

2. **Model Training**:
   - A `RandomForestClassifier` is trained using the features above.
   - The trained model is saved as `phishing_model_with_domain.pkl`.

3. **Prediction**:
   - The GUI takes user input and passes it to the model.
   - It displays prediction (Phishing/Legitimate), model confidence %, and domain age.

---

## 🚀 How to Run

### 🔧 1. Install Required Packages
```bash
pip install pandas scikit-learn joblib python-whois tk
````

### 📊 2. Train the Model

```bash
python train_model.py
```

This creates `phishing_model_with_domain.pkl`.

### 🖥️ 3. Launch the GUI

```bash
python main_gui.py
```

Then enter any URL in the input box and click **“Check URL”**.

---

## 📝 Notes

* WHOIS lookup may fail for some domains (especially newly created or obscure ones).
* This is a lightweight model suitable for educational/demo purposes.
* You can improve accuracy by:

  * Expanding the dataset
  * Adding more URL-based features
  * Integrating browser-based metadata

---

## 🙌 Author

**Nisarga**
[LinkedIn](www.linkedin.com/in/nisarga-gondane-b45a7a315) | [GitHub](https://github.com/nisa01-cmd)
Built with 💻, ☕, and curiosity for online safety.

---

## 🛡️ License

This project is open for educational use. If you build on this work, kindly give credit.

```


