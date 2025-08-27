# content.py

"""
This file holds the educational content for the EduBridge application.
Content is now structured by class (from 1 to 8), then by subject.
"""

LESSON_CONTENT = {
    # --- CLASS 1 CONTENT ---
    "1": {
        "science": [
            {
                "id": "c1s1",
                "title": "Our Body Parts",
                "content": "We have many body parts like eyes to see, ears to hear, a nose to smell, and hands to hold things. Each part is very important.",
                "quiz": [
                    {"question": "Which part helps us to see?", "options": ["Ear", "Nose", "Eyes"], "answer": "Eyes"},
                    {"question": "What do we use to hold a pencil?", "options": ["Feet", "Hands", "Head"], "answer": "Hands"}
                ]
            }
        ],
        "mathematics": [
            {
                "id": "c1m1",
                "title": "Counting Numbers 1-10",
                "content": "Let's learn to count! One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten.",
                "quiz": [
                    {"question": "What comes after 5?", "options": ["6", "7", "4"], "answer": "6"},
                    {"question": "How many fingers are on one hand?", "options": ["10", "5", "2"], "answer": "5"}
                ]
            }
        ],
        "social science": [
            {
                "id": "c1ss1",
                "title": "My Family",
                "content": "A family is a group of people who live together. We have parents, and sometimes brothers or sisters. We love and help our family.",
                "quiz": [
                    {"question": "Who are the main members of a small family?", "options": ["Parents and children", "Only friends", "Only teachers"], "answer": "Parents and children"}
                ]
            }
        ],
        "computer": [
            {
                "id": "c1c1",
                "title": "What is a Computer?",
                "content": "A computer is an electronic machine that helps us draw, play games, and watch videos. The main parts are the monitor, keyboard, and mouse.",
                "quiz": [
                    {"question": "Which part looks like a TV screen?", "options": ["Mouse", "Keyboard", "Monitor"], "answer": "Monitor"}
                ]
            }
        ],
        "general knowledge": [
            {
                "id": "c1gk1",
                "title": "Colors of the Rainbow",
                "content": "A rainbow has seven beautiful colors: Violet, Indigo, Blue, Green, Yellow, Orange, and Red.",
                "quiz": [
                    {"question": "Which color is NOT in the rainbow?", "options": ["Red", "Blue", "Black"], "answer": "Black"}
                ]
            }
        ]
    },
    # --- CLASS 2 CONTENT ---
    "2": {
        "science": [
            {
                "id": "c2s1",
                "title": "Types of Plants",
                "content": "There are different types of plants. Big and strong plants are called trees. Small plants are called shrubs and herbs.",
                "quiz": [
                    {"question": "A very big and tall plant is called a...", "options": ["Herb", "Tree", "Shrub"], "answer": "Tree"}
                ]
            }
        ],
        "mathematics": [
            {
                "id": "c2m1",
                "title": "Simple Addition",
                "content": "Addition means putting numbers together. For example, if you have 3 pencils and you get 2 more, you have 3 + 2 = 5 pencils.",
                "quiz": [
                    {"question": "What is 4 + 5?", "options": ["8", "9", "10"], "answer": "9"}
                ]
            }
        ],
        "social science": [
            {
                "id": "c2ss1",
                "title": "Festivals We Celebrate",
                "content": "Festivals are happy times when we celebrate with family and friends. Examples are Diwali, Eid, and Christmas.",
                "quiz": [
                    {"question": "Which festival is known as the festival of lights?", "options": ["Eid", "Christmas", "Diwali"], "answer": "Diwali"}
                ]
            }
        ],
        "computer": [
            {
                "id": "c2c1",
                "title": "Uses of a Keyboard",
                "content": "A keyboard has many buttons called keys. We use them to type letters, numbers, and symbols on the computer.",
                "quiz": [
                    {"question": "What do we use to type our name on a computer?", "options": ["Mouse", "Keyboard", "Monitor"], "answer": "Keyboard"}
                ]
            }
        ],
        "general knowledge": [
            {
                "id": "c2gk1",
                "title": "Our National Animal",
                "content": "The national animal of India is the Tiger. It is a symbol of strength and courage.",
                "quiz": [
                    {"question": "What is the national animal of India?", "options": ["Lion", "Elephant", "Tiger"], "answer": "Tiger"}
                ]
            }
        ]
    },
    # --- You can add content for Class 3, 4, 5, 6, 7, 8 here ---
    # "3": { ... },
    # "4": { ... },
}