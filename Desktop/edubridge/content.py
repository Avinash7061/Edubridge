

"""
This file holds the educational content for the EduBridge application.
It simulates an offline content database for subjects like Math and Science.
Each subject has a list of lessons, and each lesson has content and a quiz.
"""

LESSON_CONTENT = {
    "math": [
        {
            "id": "m1",
            "title": "Introduction to Addition",
            "content": "Addition is how we find the total number of items when we put two groups together. For example, if you have 2 apples and you get 3 more, you have 5 apples in total.",
            "quiz": [
                {
                    "question": "What is 2 + 2?",
                    "options": ["3", "4", "5", "6"],
                    "answer": "4"
                },
                {
                    "question": "If you have 5 candies and get 1 more, how many do you have?",
                    "options": ["4", "5", "6", "7"],
                    "answer": "6"
                }
            ]
        },
        {
            "id": "m2",
            "title": "Introduction to Subtraction",
            "content": "Subtraction is taking away a number from another. If you have 5 apples and you eat 2, you are left with 3 apples.",
            "quiz": [
                {
                    "question": "What is 5 - 3?",
                    "options": ["1", "2", "3", "4"],
                    "answer": "2"
                },
                {
                    "question": "If you have 10 coins and lose 4, how many are left?",
                    "options": ["5", "6", "7", "8"],
                    "answer": "6"
                }
            ]
        }
    ],
    "science": [
        {
            "id": "s1",
            "title": "Living and Non-Living Things",
            "content": "Living things can breathe, eat, grow, and move. Examples are plants, animals, and humans. Non-living things cannot do these things, like a rock or a chair.",
            "quiz": [
                {
                    "question": "Which of the following is a living thing?",
                    "options": ["Car", "Tree", "Book", "Toy"],
                    "answer": "Tree"
                },
                {
                    "question": "Which of these is a non-living thing?",
                    "options": ["Dog", "Fish", "Stone", "Bird"],
                    "answer": "Stone"
                }
            ]
        }
    ]
}

def get_lesson(subject, lesson_id):
    """
    Retrieves a specific lesson from the content database.
    
    Args:
        subject (str): The subject of the lesson (e.g., 'math').
        lesson_id (str): The unique ID of the lesson.
        
    Returns:
        dict: The lesson dictionary if found, otherwise None.
    """
    if subject in LESSON_CONTENT:
        for lesson in LESSON_CONTENT[subject]:
            if lesson['id'] == lesson_id:
                return lesson
    return None