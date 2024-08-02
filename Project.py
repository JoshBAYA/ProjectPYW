
import streamlit as st

questions = [
    {
        "question": "Would you rather work with numbers or words?",
        "options": ["Numbers", "Words", "Germany"],
        "answer": "Numbers"
    },
    {
        "question": "Would you rather work in a Lab or an Office?",
        "options": ["Lab", "Office", "Neither"],
        "answer": "Office"
    },
    {
        "question": "Would you rather create an art masterpiece or write a novel?",
        "options": ["Create an art masterpiece", "Write a novel", "Neither"],
        "answer": "Create an art masterpiece"
    },
    {
       "question": "Would you rather solve a complex math problem or conduct a scientific experiment?",
       "options": ["Solve a complex math problem", "Conduct a scientific experiment", "Neither"],
       "answer": "Conduct a scientific experiment"
   },
   {
       "question": "Would you rather study ancient civilizations or learn about modern politics?",
       "options": ["Ancient civilizations", "Modern politics", "Neither"],
       "answer": "Modern politics"
   },
   {
       "question": "Would you rather design a building or create a software program?",
       "options": ["Design a building", "Create a software program", "Neither"],
       "answer": "Create a software program"
   },
   {
       "question": "Would you rather work with animals or teach children?",
       "options": ["Work with animals", "Teach children", "Neither"],
       "answer": "Teach children"
   },
   {
       "question": "Would you rather have early Mornings or late Nights?",
       "options": ["Late nights", "Early morning", "Neither"],
       "answer": "Early morning"
   },
   {
       "question": "Would you rather explore space or dive into the ocean's depths?",
       "options": ["Explore space", "Dive into the ocean's depths", "Neither"],
       "answer": "Neither"
   },
   {
       "question": "Would you rather study human behavior or understand how machines work?",
       "options": ["Study human behavior", "Understand how machines work", "Neither"],
       "answer": "Understand how machines work"
   }, 
   {
       "question": "Would you rather compose a piece of music or act in a play?",
       "options": ["Compose a piece of music", "Act in a play", "Neither"],
       "answer": "Compose a piece of music"
   },
    {
        "question": "Would you rather manage a sports team or plan a corporate event?",
        "options": ["Manage a sports team", "Plan a corporate event", "Neither"],
        "answer": "Neither"
    },
    {
        "question": "Would you rather translate foreign languages or study the effects of globalization?",
        "options": ["Translate foreign languages", "Study the effects of globalization", "Neither"],
        "answer": "Study the effects of globalization"
    },
    {
        "question": "Would you rather lead a team project or work independently on a research paper?",
        "options": ["Lead a team project", "Work independently on a research paper", "Neither"],
        "answer": "Work independently on a research paper"
    },
    {
        "question": "Would you rather develop a new recipe or create a health fitness plan?",
        "options": ["Develop a new recipe", "Create a health fitness plan", "Neither"],
        "answer": "Develop a new recipe"
    },
    {
        "question": "Would you rather study law or explore philosophical ideas?",
        "options": ["Study law", "Explore philosophical ideas", "Neither"],
        "answer": "Explore philosophical ideas"
    },
    {
        "question": "Would you rather work on environmental conservation or urban development?",
        "options": ["Environmental conservation", "Urban development", "Neither"],
        "answer": "Urban development"
    },
    {
        "question": "Would you rather write code or study Cybersecurity?",
        "options": ["Write Code", "Study Cybersecurity", "Neither"],
        "answer": "Write Code"
    },
    {
        "question": "Would you rather analyze crime scenes or study social justice issues?",
        "options": ["Analyze crime scenes", "Study social justice issues", "Neither"],
        "answer": "Neither"
    },
    {   "question": "Would you rather focus on physical health or mental health?",
        "options": ["Physical health", "Mental health", "Neither"],
        "answer": "Mental health"
    },
    {
        "question": "Would you rather work in a lab or in the field with a community?",
        "options": ["Work in a lab", "In the field with a community", "Neither"],
        "answer": "In the field with a community"
    },
    {
        "question": "Would you rather be involved in business startups or work on non-profit initiatives?",
        "options": ["Business startups", "Non-profit initiatives", "Neither"],
        "answer": "Business startups"
    },

]

def football_quiz():
    st.title("College Major Finder Quiz")
    
    with st.form("quiz_form"):
        user_answers = {}
        for i, q in enumerate(questions):
            user_answers[i] = st.radio(q["question"], q["options"])


        submit_button = st.form_submit_button(label="Submit Answers")

    class PointSystem:
    def __init__(self):
        self.points = 0

    def earn_points(self, amount):
        if amount > 0:
            self.points += amount
            print(f"Earned {amount} points. Total points: {self.points}")
        else:
            print("Amount should be positive.")

    def spend_points(self, amount):
        if amount > 0:
            if self.points >= amount:
                self.points -= amount
                print(f"Spent {amount} points. Total points: {self.points}")
            else:
                print("Not enough points.")
        else:
            print("Amount should be positive.")

    def check_points(self):
        print(f"Total points: {self.points}")

    def final_score(self):
        if self.points >= 100:
            recommendation = "Excellent! Keep up the great work!"
        elif self.points >= 50:
            recommendation = "Good job! You're doing well!"
        elif self.points >= 20:
            recommendation = "Not bad, but there's room for improvement."
        else:
            recommendation = "You need to work harder."

        return self.points, recommendation

# Example usage
if __name__ == "__main__":
    ps = PointSystem()
    ps.earn_points(40)
    ps.spend_points(10)
    ps.check_points()
    
    score, recommendation = ps.final_score()
    print(f"Final score: {score}")
    print(f"Recommendation: {recommendation}")
if __name__ == "__main__":
    football_quiz()
    
    
