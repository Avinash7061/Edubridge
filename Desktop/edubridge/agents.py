# agents.py --- EduBridge AI Agents
import pyttsx3

# --- Voice Engine Setup ---
# This sets up the text-to-speech engine that works offline.
try:
    engine = pyttsx3.init()
except ImportError:
    print("pyttsx3 library not found. Voice features will be disabled.")
    engine = None
except RuntimeError:
    print("Failed to initialize pyttsx3. Voice features may not work.")
    engine = None

def speak(text):
    """
    A helper function to make the application speak.
    It uses the pyttsx3 engine. If the engine is not available,
    it will simply print the text.
    """
    print(f"\n(EduBridge Voice): {text}\n")
    if engine:
        engine.say(text)
        engine.runAndWait()

# --- AI Agent Definitions ---

class LearnAgent:
    """
    The LearnAgent is responsible for teaching lessons to the student.
    It presents the content of a lesson in a clear, simple way.
    """
    def teach(self, lesson):
        speak(f"Today's lesson is on: {lesson['title']}")
        speak(lesson['content'])
        speak("I hope you understood the lesson well!")

class ExplainAgent:
    """
    The ExplainAgent helps by simplifying or re-explaining concepts.
    For now, it will just re-read the lesson content.
    In a more advanced version, it could offer simpler examples.
    """
    def explain(self, lesson):
        speak("Of course, let me explain that again for you.")
        speak(lesson['content'])
        speak("If you still have questions, don't hesitate to ask!")

class TestAgent:
    """
    The TestAgent checks the student's knowledge by giving a quiz.
    It asks questions, gets the user's answer, and provides feedback.
    """
    def give_quiz(self, lesson):
        score = 0
        quiz_questions = lesson['quiz']
        total_questions = len(quiz_questions)

        speak(f"Let's start the quiz for: {lesson['title']}. There are {total_questions} questions.")

        for i, q in enumerate(quiz_questions):
            speak(f"Question {i + 1}: {q['question']}")
            
            # Display options
            for idx, option in enumerate(q['options']):
                print(f"{idx + 1}. {option}")
            
            # Get user input
            while True:
                try:
                    choice = int(input("Enter the number of your answer: "))
                    if 1 <= choice <= len(q['options']):
                        break
                    else:
                        print("Invalid choice. Please enter a number from the options.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            user_answer = q['options'][choice - 1]

            # Check answer
            if user_answer == q['answer']:
                speak("That's correct! Well done!")
                score += 1
            else:
                speak(f"Not quite. The correct answer was: {q['answer']}")
        
        speak(f"You have completed the quiz. Your score is {score} out of {total_questions}.")
        return score, total_questions

class CoachAgent:
    """
    The CoachAgent motivates the student to keep learning.
    It provides encouragement before and after activities.
    """
    def motivate(self):
        speak("Remember, every lesson you learn brings you one step closer to your dreams. Keep up the great work!")

    def praise(self, score, total):
        if score == total:
            speak("Fantastic job! You got a perfect score! I'm proud of you.")
        elif score >= total / 2:
            speak(f"Good effort! You are learning and improving, which is what matters most.")
        else:
            speak("Don't worry about the score. The most important thing is that you tried. Let's review the lesson and try again!")

class ParentAgent:
    """
    The ParentAgent informs parents about their child's progress.
    In this simulation, it will print a message to the console.
    """
    def report_progress(self, student_name, lesson_title, score, total):
        message = f"Hello, this is an update from EduBridge for {student_name}. Your child has just completed the lesson '{lesson_title}' and scored {score} out of {total}. Please continue to encourage them."
        speak(message)
        print("--- (This message would be sent as a voice note to the parent) ---")