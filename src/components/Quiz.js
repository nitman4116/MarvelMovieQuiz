import React, { useState } from 'react';
import './Quiz.css';
import { quizData } from '../data/quizData';

const Quiz = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [showResults, setShowResults] = useState(false);
  const [score, setScore] = useState(0);

  const handleAnswerSelect = (questionId, answerIndex) => {
    setSelectedAnswers({
      ...selectedAnswers,
      [questionId]: answerIndex
    });
  };

  const handleNextQuestion = () => {
    if (currentQuestion < quizData.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      calculateScore();
      setShowResults(true);
    }
  };

  const calculateScore = () => {
    let correctAnswers = 0;
    quizData.forEach(question => {
      if (selectedAnswers[question.id] === question.correctAnswer) {
        correctAnswers++;
      }
    });
    setScore(correctAnswers);
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setSelectedAnswers({});
    setShowResults(false);
    setScore(0);
  };

  if (showResults) {
    return (
      <div className="quiz-container">
        <div className="results-screen">
          <div className="results-content">
            <h1 className="results-title">Quiz Complete!</h1>
            <div className="score-display">
              <h2>Your Score: {score}/{quizData.length}</h2>
              <div className="score-percentage">
                {Math.round((score / quizData.length) * 100)}%
              </div>
            </div>
            <div className="disney-message">
              <h3>🎬 Go watch Avengers: Infinity War now on Disney+! 🎬</h3>
              <p>Experience the epic battle that changed the Marvel Cinematic Universe forever!</p>
            </div>
            <button className="retry-button" onClick={resetQuiz}>
              Take Quiz Again
            </button>
          </div>
        </div>
      </div>
    );
  }

  const question = quizData[currentQuestion];
  const isAnswerSelected = selectedAnswers[question.id] !== undefined;

  return (
    <div className="quiz-container">
      <div className="quiz-header">
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${((currentQuestion + 1) / quizData.length) * 100}%` }}
          ></div>
        </div>
        <div className="question-counter">
          Question {currentQuestion + 1} of {quizData.length}
        </div>
      </div>

      <div className="question-container">
        <h2 className="question-text">{question.question}</h2>
        
        <div className="options-container">
          {question.options.map((option, index) => (
            <button
              key={index}
              className={`option-button ${
                selectedAnswers[question.id] === index ? 'selected' : ''
              }`}
              onClick={() => handleAnswerSelect(question.id, index)}
            >
              <span className="option-letter">{String.fromCharCode(65 + index)}</span>
              <span className="option-text">{option}</span>
            </button>
          ))}
        </div>

        <div className="quiz-navigation">
          <button 
            className="next-button"
            onClick={handleNextQuestion}
            disabled={!isAnswerSelected}
          >
            {currentQuestion === quizData.length - 1 ? 'Finish Quiz' : 'Next Question'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default Quiz;