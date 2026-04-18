# 🎨 Image Color Palette Generator

A web app that extracts dominant colors from an uploaded image using machine learning.

---
## 🌐 Live Demo

👉 https://image-color-palette-generator-7e5z.onrender.com/

---

## 🖼️ Preview

### Homepage
![Homepage](./static/screenshots/homepage.png)

### Example Output 1
![Preview 1](./static/screenshots/preview_1.png)

### Example Output 2
![Preview 2](./static/screenshots/preview_2.png)

---

## 🚀 Features

- Upload an image  
- Choose number of colors  
- Extract dominant colors using KMeans  
- Copy HEX codes  

---

## 🛠️ Tech Stack

- Flask  
- NumPy  
- Pillow  
- scikit-learn  

---

## ▶️ Run Locally

pip install -r requirements.txt  
python app.py  

Open in browser:  
http://127.0.0.1:5000/

---

## 📁 Project Structure

```
.
├── static/
│   ├── css/
│   ├── uploads/
│   └── screenshots/
├── templates/
│   └── index.html
├── app.py
├── utils.py
├── requirements.txt
├── .env
└── .gitignore
```

---
## ✅ Improvements

- Added validation for uploaded files  
- Handles invalid/non-image uploads gracefully  
- Improved user experience with error messages  

---

## ⭐️ Show Your Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 👤 Author

**Sijan Thapa**  
GitHub: https://github.com/FermiumParadox