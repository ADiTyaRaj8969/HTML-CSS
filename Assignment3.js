const quizData = [
  {
    question: "What is the capital of France?",
    options: ["Berlin", "Madrid", "Paris", "Rome"],
    correct: "Paris",
  },
  {
    question: "Who wrote 'Romeo and Juliet'?",
    options: ["Shakespeare", "Dickens", "Hemingway", "Tolkien"],
    correct: "Shakespeare",
  },
  {
    question: "What is 2 + 2?",
    options: ["3", "4", "5", "6"],
    correct: "4",
  },
  {
    question: "What is the largest planet in our solar system?",
    options: ["Earth", "Mars", "Jupiter", "Saturn"],
    correct: "Jupiter",
  },
  {
    question: "Which element has the chemical symbol 'O'?",
    options: ["Oxygen", "Osmium", "Ozone", "Oganesson"],
    correct: "Oxygen",
  },
  {
    question: "Who was the first president of the United States?",
    options: [
      "Abraham Lincoln",
      "George Washington",
      "Thomas Jefferson",
      "John Adams",
    ],
    correct: "George Washington",
  },
];

let currentQuestionIndex = 0;
let score = 0;

function loadQuiz() {
  const quizContainer = document.getElementById("quiz");
  quizContainer.innerHTML = ""; // Clear previous content

  // Get current question data
  const currentQuestion = quizData[currentQuestionIndex];

  // Create question element
  const questionElement = document.createElement("div");
  questionElement.classList.add("question");
  questionElement.textContent = currentQuestion.question;

  // Create options
  const optionsElement = document.createElement("div");
  optionsElement.classList.add("options");

  currentQuestion.options.forEach((option) => {
    const optionElement = document.createElement("label");
    optionElement.classList.add("option");
    optionElement.innerHTML = `
      <input type="radio" name="option" value="${option}">
      ${option}
    `;
    optionsElement.appendChild(optionElement);
  });

  quizContainer.appendChild(questionElement);
  quizContainer.appendChild(optionsElement);
}

function submitQuiz() {
  const selectedOption = document.querySelector('input[name="option"]:checked');

  if (!selectedOption) {
    alert("Please select an option");
    return;
  }

  const answer = selectedOption.value;
  const correctAnswer = quizData[currentQuestionIndex].correct;

  if (answer === correctAnswer) {
    score++;
  }

  // Go to the next question or end the quiz
  currentQuestionIndex++;

  if (currentQuestionIndex < quizData.length) {
    loadQuiz();
  } else {
    showResult();
  }
}

function showResult() {
  const resultContainer = document.getElementById("result");
  resultContainer.textContent = `Your score is: ${score} out of ${quizData.length}`;
  document.getElementById("submit").style.display = "none"; // Hide submit button
}

loadQuiz(); // Initial call to load the first question
