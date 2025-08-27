# Import our custom modules
from agents import LearnAgent, ExplainAgent, TestAgent, CoachAgent, ParentAgent, speak
from content import LESSON_CONTENT
import database

# Import standard library modules
import time

def main():
    """
    The main function to run the EduBridge application.
    """
    # --- Initialization ---
    database.setup_database() # Creates the db file and table if they don't exist
    db_conn = database.create_connection()
    
    # Instantiate all our AI agents
    learn_agent = LearnAgent()
    explain_agent = ExplainAgent()
    test_agent = TestAgent()
    coach_agent = CoachAgent()
    parent_agent = ParentAgent()

    # --- Application Start ---
    speak("Welcome to EduBridge! Your personal AI learning partner.")
    student_name = input("What is your name? ")
    speak(f"Hello, {student_name}! I am excited to help you learn today.")
    
    coach_agent.motivate()

    # --- Main Application Loop ---
    while True:
        # --- Subject Selection ---
        speak("Which subject would you like to study today?")
        subjects = list(LESSON_CONTENT.keys())
        for i, subject in enumerate(subjects):
            print(f"{i + 1}. {subject.capitalize()}")
        
        try:
            choice = int(input("Enter the number of the subject: "))
            selected_subject = subjects[choice - 1]
        except (ValueError, IndexError):
            speak("That's not a valid choice. Please try again.")
            continue
            
        # --- Lesson Selection ---
        speak(f"Great! Here are the lessons for {selected_subject.capitalize()}:")
        lessons = LESSON_CONTENT[selected_subject]
        for i, lesson in enumerate(lessons):
            print(f"{i + 1}. {lesson['title']}")
        
        try:
            choice = int(input("Enter the number of the lesson: "))
            selected_lesson = lessons[choice - 1]
        except (ValueError, IndexError):
            speak("That's not a valid choice. Please try again.")
            continue

        # --- Learning Phase ---
        learn_agent.teach(selected_lesson)
        
        # --- Interaction Menu ---
        while True:
            speak("What would you like to do next?")
            print("1. Explain the lesson again")
            print("2. Take the quiz")
            print("3. Hear some motivation")
            
            action = input("Enter your choice (1, 2, or 3): ")

            if action == '1':
                explain_agent.explain(selected_lesson)
            elif action == '2':
                score, total = test_agent.give_quiz(selected_lesson)
                
                # Save progress to the database
                database.save_progress(db_conn, student_name, selected_lesson['id'], score, total)
                
                # Provide feedback and reporting
                coach_agent.praise(score, total)
                time.sleep(1) # Pause for effect
                parent_agent.report_progress(student_name, selected_lesson['title'], score, total)
                break # Exit interaction menu to go back to lesson selection
            elif action == '3':
                coach_agent.motivate()
            else:
                speak("That is not a valid choice, please select 1, 2, or 3.")

        # --- Continue or Exit ---
        speak("Would you like to choose another lesson?")
        another = input("Type 'yes' to continue or anything else to exit: ").lower()
        if another != 'yes':
            break

    # --- Application End ---
    db_conn.close() # Close the database connection
    speak(f"Thank you for learning with EduBridge, {student_name}! Have a great day!")


if __name__ == "__main__":
    main()