# 🧠 AI-Powered Code Reviewer

A simple web app built with **Flask** that allows users to upload Python code files and get instant feedback using **pylint**. It highlights potential issues and helps developers write cleaner, more professional code.

---

## 🚀 Features

- Upload python codes and analyze them instantly
- Displays:
  - Linting feedback from `pylint`
  - "✅ Code is proper ✅" if no issues are found
  - "⚠️ Issues found in code ⚠️" with detailed feedback
- Automatically deletes the uploaded file after analysis

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Linting Engine**: `pylint`

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Adhiperumbar/Code_reviewer.git
   cd Code_reviewer

2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python app.py

5. Open your browser and go to
http://localhost:5000


📁 Project Structure
Code_reviewer/
│
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md


📌 Future Improvements
Support for other languages (JS, C++, etc.)
Highlight specific lines of code with issues
Authentication and history tracking for users
Frontend enhancements (loading spinner, file validation)

👩‍💻 Author
Adhiperumbar
