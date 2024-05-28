1. Automatic Answer Checker System

def get_answers(prompt):
    """Function to get answers from user input."""
    answers = []
    while True:
        answer = input(prompt)
        if answer == '':  # Empty input to stop
            break
        answers.append(answer)
    return answers

def check_answers(correct_answers, student_answers):
    """Function to check the student's answers against the correct answers."""
    correct = 0
    incorrect = 0
    unanswered = 0
    
    for i in range(len(correct_answers)):
        if i >= len(student_answers) or student_answers[i] == '':
            unanswered += 1
        elif student_answers[i] == correct_answers[i]:
            correct += 1
        else:
            incorrect += 1
    
    return correct, incorrect, unanswered

# Get correct answers from user
correct_answers = get_answers("Enter the correct answer (press enter to stop): ")

# Get student's answers from user
student_answers = get_answers("Enter the student's answer (press enter to stop): ")

# Check the answers
correct, incorrect, unanswered = check_answers(correct_answers, student_answers)

# Display the results
print(f"Student's Score: {correct} out of {len(correct_answers)}")
print(f"Correct Answers: {correct}")
print(f"Incorrect Answers: {incorrect}")
print(f"Unanswered Questions: {unanswered}")


2. Online AI Shopping Assistant with M-Wallet System
    
class ShoppingAssistant:
    def __init__(self):
        self.preferences = []
        self.products = {
            'electronics': ['Smartphone', 'Laptop', 'Headphones'],
            'fashion': ['T-shirt', 'Jeans', 'Sneakers'],
            'books': ['Novel', 'Biography', 'Science Fiction']
        }

    def get_user_preferences(self):
        self.preferences = input("Enter your shopping preferences (e.g., electronics, fashion, books): ").split(', ')
    
    def recommend_products(self):
        recommendations = []
        for preference in self.preferences:
            if preference in self.products:
                recommendations.extend(self.products[preference])
        return recommendations

# Create an instance of ShoppingAssistant
assistant = ShoppingAssistant()
assistant.get_user_preferences()
recommended_products = assistant.recommend_products()

# Display the recommended products
print("Recommended Products: ", recommended_products)


3. Intelligent Tourist System Project

import json

class TouristDestination:
    def __init__(self, name, location, type, rating):
        self.name = name
        self.location = location
        self.type = type
        self.rating = rating

class TouristDestinations:
    def __init__(self):
        self.destinations = []
    
    def load_destinations(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                destination = TouristDestination(item['name'], item['location'], item['type'], item['rating'])
                self.destinations.append(destination)
    
    def get_recommendations(self, interests):
        recommendations = [dest for dest in self.destinations if dest.type in interests]
        recommendations.sort(key=lambda x: x.rating, reverse=True)
        return recommendations

# Usage example:
destinations = TouristDestinations()
destinations.load_destinations('destinations.json')

tourist_interests = ['beach', 'museum']
recommended_destinations = destinations.get_recommendations(tourist_interests)

for destination in recommended_destinations:
    print(f"{destination.name} in {destination.location}, Type: {destination.type}, Rating: {destination.rating}")


4. Online Plagiarism Checker


def check_plagiarism(input_text):
    """Dummy function to simulate plagiarism checking."""
    database_texts = [
        "This is a sample text for checking plagiarism.",
        "Another text to check the similarity with the input.",
        "Yet another example of text in the database."
    ]
    similarity_percentages = [70, 45, 30]  # Dummy similarity percentages
    
    return list(zip(database_texts, similarity_percentages))

# Get text input from user
input_text = input("Enter the text to check for plagiarism: ")

# Check for plagiarism
results = check_plagiarism(input_text)

# Display the results
for text, similarity in results:
    print(f"Similarity: {similarity}%, Text: {text}")


5. Teacher Automatic Time-Table Software

class Teacher:
    def __init__(self, name):
        self.name = name

class Subject:
    def __init__(self, name):
        self.name = name

def generate_time_table(teachers, subjects, classroom_availability):
    """Dummy function to simulate timetable generation."""
    timetable = {}
    for teacher in teachers:
        timetable[teacher.name] = {}
        for subject in subjects:
            timetable[teacher.name][subject.name] = classroom_availability[0]  # Assign first available classroom
    
    return timetable

# Input information from user
teachers = [Teacher(name) for name in input("Enter teacher names (comma-separated): ").split(', ')]
subjects = [Subject(name) for name in input("Enter subject names (comma-separated): ").split(', ')]
classroom_availability = input("Enter available classrooms (comma-separated): ").split(', ')

# Generate timetable
timetable = generate_time_table(teachers, subjects, classroom_availability)

# Display the timetable
for teacher, subjects in timetable.items():
    print(f"Teacher: {teacher}")
    for subject, classroom in subjects.items():
        print(f"  Subject: {subject}, Classroom: {classroom}")
