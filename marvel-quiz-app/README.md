# 🦸 Marvel Quiz - Streamlit App

A interactive Marvel Cinematic Universe quiz built with Streamlit that tests your knowledge of the Avengers and ends with a Disney+ recommendation!

## 🎬 Features

- **5 Marvel-themed questions** with multiple choice answers
- **Interactive quiz interface** with progress tracking
- **Score calculation** and detailed results
- **Marvel-themed design** with cosmic backgrounds
- **Disney+ promotion** message at the end
- **Responsive design** for all devices

## 🚀 Local Development

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone or download the project**
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run marvel_quiz.py
   ```

5. **Open your browser to:** `http://localhost:8501`

## 🌐 Streamlit Cloud Deployment

### Option 1: Streamlit Community Cloud (Free)

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial Marvel Quiz commit"
   git remote add origin https://github.com/yourusername/marvel-quiz.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `yourusername/marvel-quiz`
   - Main file path: `marvel_quiz.py`
   - Click "Deploy!"

### Option 2: Manual Streamlit Cloud Setup

1. **Create a GitHub repository**
2. **Upload these files to your repository:**
   - `marvel_quiz.py` (main app file)
   - `requirements.txt` (dependencies)
   - `README.md` (this file)

3. **Deploy on Streamlit Cloud:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Click "New app"
   - Fill in the details:
     - **Repository:** `yourusername/marvel-quiz`
     - **Branch:** `main`
     - **Main file path:** `marvel_quiz.py`
   - Click "Deploy!"

## 📁 Project Structure

```
marvel-quiz/
├── marvel_quiz.py      # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── venv/              # Virtual environment (local only)
```

## 🎯 Quiz Questions

The quiz includes 5 questions about:
1. **Thor's hammer** (Mjolnir)
2. **Vision's Infinity Stone** (Mind Stone)
3. **Captain America's shield** (Vibranium)
4. **Hulk's snap** in Avengers: Endgame
5. **Thanos's home planet** (Titan)

## 🎨 Customization

### Adding More Questions
Edit the `QUIZ_DATA` list in `marvel_quiz.py`:

```python
QUIZ_DATA = [
    {
        "question": "Your question here?",
        "options": ["Option A", "Option B", "Option C", "Option D", "Option E"],
        "correct": 0,  # Index of correct answer (0-4)
        "explanation": "Explanation of the correct answer."
    },
    # Add more questions...
]
```

### Styling
The app uses custom CSS for Marvel theming. Modify the `st.markdown()` sections in the `main()` function to change colors, fonts, and layout.

## 🔧 Troubleshooting

### Common Issues

1. **"streamlit: command not found"**
   - Make sure you're in the virtual environment
   - Run: `pip install streamlit`

2. **Port already in use**
   - Streamlit runs on port 8501 by default
   - Use: `streamlit run marvel_quiz.py --server.port 8502`

3. **Deployment issues**
   - Ensure `requirements.txt` includes all dependencies
   - Check that your main file is named correctly
   - Verify your GitHub repository is public (for free Streamlit Cloud)

## 📱 Mobile Support

The quiz is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🎬 About

This quiz was created to test Marvel fans' knowledge while promoting **Avengers: Infinity War** on Disney+!

## 📄 License

This project is open source and available under the MIT License.

---

**Ready to test your Marvel knowledge? Deploy this quiz and challenge your friends! 🦸‍♂️🦸‍♀️**