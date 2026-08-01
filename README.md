# 🎓 AI Facial Attendance Tracker

An AI-powered Facial Attendance Tracker that automatically detects and recognizes faces to mark attendance in real time. This project uses Computer Vision and Machine Learning techniques to eliminate manual attendance, reduce proxy attendance, and improve accuracy. Face recognition attendance systems commonly combine OpenCV with machine learning or face-recognition libraries to automate attendance tracking. :contentReference[oaicite:0]{index=0}

---

## 📌 Features

- 👤 Face Registration
- 📷 Real-time Face Detection
- 🧠 Face Recognition using AI
- ✅ Automatic Attendance Marking
- 📅 Date & Time Logging
- 📊 Attendance Report Generation
- 💾 Database Storage
- 🔒 Secure User Authentication
- 📈 Easy-to-use Interface

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Computer Vision:** OpenCV
- **Machine Learning:** face_recognition / Deep Learning
- **Database:** SQLite / MySQL
- **GUI:** Tkinter / CustomTkinter (Optional)
- **Data Handling:** Pandas
- **Model Training:** NumPy

---

## 📂 Project Structure

```
AI-Facial-Attendance-Tracker/
│
├── dataset/                # Face images
├── trainer/                # Trained model
├── attendance/             # Attendance records
├── images/                 # Screenshots
├── models/                 # AI models
├── main.py                 # Main program
├── train_model.py          # Model training
├── attendance.py           # Attendance logic
├── database.py             # Database operations
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/harshsrivastava75/AI-Facial-Attendance-Tracker.git
```

### 2. Open Project

```bash
cd AI-Facial-Attendance-Tracker
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

---

## 📦 Required Libraries

```text
opencv-python
numpy
pandas
face_recognition
dlib
sqlite3
Pillow
scikit-learn
```

Install manually if needed:

```bash
pip install opencv-python numpy pandas face_recognition Pillow scikit-learn
```

---

## 🚀 How It Works

1. Register a new user.
2. Capture multiple face images.
3. Train the AI model.
4. Start the attendance system.
5. The camera detects and recognizes faces.
6. Attendance is automatically recorded with the current date and time.
7. Attendance reports are saved in CSV or the database.

---

## 📊 Output

- Student Name
- Student ID
- Date
- Time
- Attendance Status

Example:

| ID | Name | Date | Time | Status |
|----|------|------|------|--------|
| 101 | John Doe | 31-07-2026 | 09:02 AM | Present |

---

## 🎯 Future Enhancements

- Cloud Database Integration
- Mobile Application
- QR Code Backup Attendance
- Email Notifications
- Face Mask Detection
- Anti-Spoofing Detection
- Multi-Camera Support
- Dashboard Analytics

---

## 💡 Advantages

- Fast Attendance Process
- High Accuracy
- Contactless Attendance
- Eliminates Proxy Attendance
- Saves Time
- Easy Report Generation

---

## 📸 Screenshots

Add your project screenshots here.

```
images/
├── home.png
├── register.png
├── attendance.png
└── report.png
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Harsh Srivastava**

- GitHub: https://github.com/harshsrivastava75
- Email: harshsrivastava7273@gmail.com

---

## ⭐ Support

If you like this project, please ⭐ the repository and share it with others.

---

## 🙏 Acknowledgements

- OpenCV
- Python
- NumPy
- Pandas
- face_recognition Library
- SQLite

---

**Made with ❤️ using Python and Artificial Intelligence**