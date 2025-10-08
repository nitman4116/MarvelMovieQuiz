import streamlit as st
import random

# Marvel Quiz Data
QUIZ_DATA = [
    {
        "question": "What is the name of Thor's hammer?",
        "options": ["Mjolnir", "Stormbreaker", "Gungnir", "Hofund", "Jarnbjorn"],
        "correct": 0,
        "explanation": "Mjolnir is Thor's iconic hammer, forged in the heart of a dying star."
    },
    {
        "question": "Which Infinity Stone is located in Vision's forehead?",
        "options": ["Power Stone", "Space Stone", "Mind Stone", "Reality Stone", "Time Stone"],
        "correct": 2,
        "explanation": "The Mind Stone gives Vision his consciousness and powers."
    },
    {
        "question": "What is Captain America's shield made of?",
        "options": ["Adamantium", "Vibranium", "Uru", "Carbonadium", "Promethium"],
        "correct": 1,
        "explanation": "Captain America's shield is made of Vibranium, the strongest metal on Earth."
    },
    {
        "question": "Which Avenger was the first to snap their fingers with the Infinity Gauntlet?",
        "options": ["Iron Man", "Hulk", "Captain America", "Thor", "Doctor Strange"],
        "correct": 1,
        "explanation": "Hulk was the first to snap his fingers to bring back everyone who was dusted."
    },
    {
        "question": "What is the name of the planet where Thanos grew up?",
        "options": ["Titan", "Xandar", "Knowhere", "Sakaar", "Vormir"],
        "correct": 0,
        "explanation": "Thanos is from Titan, a moon of Saturn that was destroyed by overpopulation."
    }
]

def initialize_session_state():
    """Initialize session state variables"""
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    if 'score' not in st.session_state:
        st.session_state.score = 0

def reset_quiz():
    """Reset the quiz to start over"""
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.quiz_completed = False
    st.session_state.score = 0

def calculate_score():
    """Calculate the final score"""
    score = 0
    for i, question in enumerate(QUIZ_DATA):
        if st.session_state.answers.get(i) == question['correct']:
            score += 1
    st.session_state.score = score
    return score

def display_question():
    """Display the current question"""
    question = QUIZ_DATA[st.session_state.current_question]
    
    st.markdown(f"### Question {st.session_state.current_question + 1} of {len(QUIZ_DATA)}")
    st.markdown(f"**{question['question']}**")
    
    # Display options
    selected_option = st.radio(
        "Choose your answer:",
        question['options'],
        key=f"question_{st.session_state.current_question}",
        index=None
    )
    
    # Store the answer
    if selected_option is not None:
        option_index = question['options'].index(selected_option)
        st.session_state.answers[st.session_state.current_question] = option_index
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button("← Previous", key="prev_btn"):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col3:
        if selected_option is not None:
            if st.session_state.current_question < len(QUIZ_DATA) - 1:
                if st.button("Next →", key="next_btn"):
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("Finish Quiz", key="finish_btn"):
                    calculate_score()
                    st.session_state.quiz_completed = True
                    st.rerun()

def display_results():
    """Display the quiz results"""
    score = st.session_state.score
    total_questions = len(QUIZ_DATA)
    percentage = (score / total_questions) * 100
    
    st.markdown("## 🎬 Quiz Complete!")
    
    # Score display
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"### Your Score: {score}/{total_questions}")
        st.markdown(f"### {percentage:.0f}%")
    
    # Disney+ message
    st.markdown("---")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
        <h2 style="color: white; margin: 0;">🎬 Go watch Avengers: Infinity War now on Disney+! 🎬</h2>
        <p style="color: white; margin: 10px 0 0 0;">Experience the epic battle that changed the Marvel Cinematic Universe forever!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Detailed results
    st.markdown("### 📊 Detailed Results:")
    for i, question in enumerate(QUIZ_DATA):
        user_answer = st.session_state.answers.get(i)
        correct_answer = question['correct']
        is_correct = user_answer == correct_answer
        
        status = "✅" if is_correct else "❌"
        st.markdown(f"{status} **Question {i+1}:** {question['question']}")
        st.markdown(f"   Your answer: {question['options'][user_answer] if user_answer is not None else 'Not answered'}")
        st.markdown(f"   Correct answer: {question['options'][correct_answer]}")
        if not is_correct:
            st.markdown(f"   💡 {question['explanation']}")
        st.markdown("---")
    
    # Retry button
    if st.button("🔄 Take Quiz Again", key="retry_btn"):
        reset_quiz()
        st.rerun()

def main():
    """Main Streamlit app"""
    st.set_page_config(
        page_title="Marvel Quiz",
        page_icon="🦸",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for Marvel theme
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #0f0f23, #1a1a2e, #16213e);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 30px;
    }
    .main-header h1 {
        color: #4ecdc4;
        font-size: 3rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .main-header p {
        color: #ffffff;
        font-size: 1.2rem;
        margin: 10px 0 0 0;
    }
    .question-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 20px 0;
    }
    .progress-bar {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1);
        height: 8px;
        border-radius: 4px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🦸 Marvel Quiz 🦸</h1>
        <p>Test your knowledge of the Marvel Cinematic Universe!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress bar
    if not st.session_state.quiz_completed:
        progress = (st.session_state.current_question + 1) / len(QUIZ_DATA)
        st.markdown(f"Progress: {st.session_state.current_question + 1}/{len(QUIZ_DATA)}")
        st.markdown(f"""
        <div class="progress-bar" style="width: {progress * 100}%;"></div>
        """, unsafe_allow_html=True)
    
    # Main content
    if st.session_state.quiz_completed:
        display_results()
    else:
        display_question()
    
    # Sidebar with quiz info
    with st.sidebar:
        st.markdown("### 🎯 Quiz Info")
        st.markdown(f"**Questions:** {len(QUIZ_DATA)}")
        st.markdown(f"**Current:** {st.session_state.current_question + 1}")
        
        if st.session_state.quiz_completed:
            st.markdown(f"**Score:** {st.session_state.score}/{len(QUIZ_DATA)}")
        
        st.markdown("---")
        st.markdown("### 🎬 About")
        st.markdown("Test your Marvel knowledge and get ready to watch Avengers: Infinity War on Disney+!")

if __name__ == "__main__":
    main()
