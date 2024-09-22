class PointSystem:
    def __init__(self):
        self.points = 0

    def earn_points(self, amount):
        if amount > 0:
            self.points += amount

    def spend_points(self, amount):
        if amount > 0 and self.points >= amount:
            self.points -= amount

    def final_score(self):
        score = self.points
        # Add recommendation logic based on the final score
        if score >= 90:
            recommendation = "Analytical Thinker: Consider majors like Mathematics, Engineering, or Data Science."
        elif score >= 60:
            recommendation = "Creative Mind: Consider majors like Arts, Literature, or Music."
        elif score >= 30:
            recommendation = "Science and Exploration Enthusiast: Consider majors like Biology, Environmental Science, or Astronomy."
        else:
            recommendation = "Social and Humanitarian Leader: Consider majors like Psychology, Sociology, or Public Health."

        return score, recommendation

def ask_question(question, choice1, choice2):
    print(question)
    print(f"1. {choice1}")
    print(f"2. {choice2}")
    print(f"3. {Neither}")
    while True:
        try:
            answer = int(input("Enter 1, 2, or 3: "))
            if answer in [1, 2, 3]:
                return answer
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    ps = PointSystem()
    questions = [
        ("Would you rather work with numbers or words?", "Numbers", "Words", "Neither"),
        ("Would you rather work in a Lab or an Office?", "Lab", "Office", "Neither"),
        ("Would you rather create an art masterpiece or write a novel?", "Art Masterpiece", "Novel", "Neither"),
        ("Would you rather solve a complex math problem or conduct a scientific experiment?", "Math Problem", "Scientific Experiment", "Neither"),
        ("Would you rather study ancient civilizations or learn about modern politics?", "Ancient Civilizations", "Modern Politics", "Neither"),
        ("Would you rather design a building or create a software program?", "Design Building", "Create Software Program", "Neither"),
        ("Would you rather work with animals or teach children?", "Work with Animals", "Teach Children", "Neither"),
        ("Would you rather have early Mornings or late Nights?", "Early Mornings", "Late Nights", "Neither"),
        ("Would you rather explore space or dive into the ocean's depths?", "Explore Space", "Dive into Ocean", "Neither"),
        ("Would you rather study human behavior or understand how machines work?", "Human Behavior", "Machines", "Neither"),
        ("Would you rather compose a piece of music or act in a play?", "Compose Music", "Act in a Play", "Neither"),
        ("Would you rather manage a sports team or plan a corporate event?", "Manage Sports Team", "Plan Corporate Event", "Neither"),
        ("Would you rather translate foreign languages or study the effects of globalization?", "Translate Languages", "Effects of Globalization", "Neither"),
        ("Would you rather lead a team project or work independently on a research paper?", "Lead Team Project", "Work Independently", "Neither"),
        ("Would you rather develop a new recipe or create a health fitness plan?", "New Recipe", "Health Fitness Plan", "Neither"),
        ("Would you rather study law or explore philosophical ideas?", "Study Law", "Philosophical Ideas", "Neither"),
        ("Would you rather work on environmental conservation or urban development?", "Environmental Conservation", "Urban Development", "Neither"),
        ("Would you rather write code or study cybersecurity?", "Write Code", "Cybersecurity", "Neither"),
        ("Would you rather analyze crime scenes or study social justice issues?", "Analyze Crime Scenes", "Social Justice Issues", "Neither"),
        ("Would you rather focus on physical health or mental health?", "Physical Health", "Mental Health", "Neither"),
        ("Would you rather work in a lab or the field with a community?", "Lab", "Field", "Neither"),
        ("Would you rather be involved in business startups or work on non-profit initiatives?", "Business Startups", "Non-profit Initiatives", "Neither")
    ]

    for question, choice1, choice2 in questions:
        answer = ask_question(question, choice1, choice2)
        if answer == 1:
            ps.earn_points(5)
        elif answer == 2:
            ps.earn_points(3)
        elif: answer == 2:
            ps.earn_points(1)

    score, recommendation = ps.final_score()
    print(f"Final score: {score}")
    print(f"Recommendation: {recommendation}")

if __name__ == "__main__":
    main()
