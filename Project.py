
import streamlit as st

questions = [
    {
        "question": "Who won the FIFA World Cup in 2018?",
        "options": ["France", "Brazil", "Germany", "Spain"],
        "answer": "France"
    },
    {
        "question": "Which player has won the most Ballon d'Or awards?",
        "options": ["Cristiano Ronaldo", "Lionel Messi", "Michel Platini", "Johan Cruyff"],
        "answer": "Lionel Messi"
    },
    {
        "question": "Which club has won the most Ligue 1 titles?",
        "options": ["Paris Saint Germain", "Olympique Lyonnais", "AS Saint-Etienne", "AS Monaco"],
        "answer": "Paris Saint Germain"
    },
    {
       "question": "Which club has won the most UEFA Champions League titles?",
       "options": ["Real Madrid", "FC Barcelona", "AC Milan", "Bayern Munich"],
       "answer": "Real Madrid"
   },
   {
       "question": "Who holds the record for the most goals scored in a single Premier League season?",
       "options": ["Thierry Henry", "Mohamed Salah", "Alan Shearer", "Cristiano Ronaldo"],
       "answer": "Mohamed Salah"
   },
   {
       "question": "Which player has the most appearances in the history of the English Premier League?",
       "options": ["Ryan Giggs", "Frank Lampard", "Gareth Barry", "Steven Gerrard"],
       "answer": "Gareth Barry"
   },
   {
       "question": "Who is the youngest goalscorer in FIFA World Cup history?",
       "options": ["Pelé", "Kylian Mbappé", "Michael Owen", "Diego Maradona"],
       "answer": "Pelé"
   },
   {
       "question": "Which national team has won the most Copa America titles?",
       "options": ["Brazil", "Argentina", "Uruguay", "Chile"],
       "answer": "Uruguay"
   },
   {
       "question": "Who is the all-time top scorer of the UEFA Champions League?",
       "options": ["Michel Platini", "Cristiano Ronaldo", "Alan Shearer", "Thierry Henry"],
       "answer": "Cristiano Ronaldo"
   },
   {
       "question": "Which country hosted the first-ever FIFA World Cup in 1930?",
       "options": ["Brazil", "Italy", "Uruguay", "France"],
       "answer": "Uruguay"
   }, 
   {
       "question": "Who has the most Ballon d'Or nominations in history?",
       "options": ["Lionel Messi", "Cristiano Ronaldo", "Michel Platini", "Johan Cruyff"],
       "answer": "Lionel Messi"
   },
    {
        "question": "Who was the first Ballon d'Or winner in 1956?",
        "options": ["Stanley Matthews", "Alfredo Di Stefano", "Raymond Kopa", "Omar Sivori"],
        "answer": "Stanley Matthews"
    },
    {
        "question": "Which player won the Ballon d'Or in 1994, becoming the first African recipient?",
        "options": ["George Weah", "Hristo Stoichkov", "Roberto Baggio", "Romário"],
        "answer": "George Weah"
    },
    {
        "question": "Who won the Ballon d'Or in 2018, breaking the Messi-Ronaldo dominance for that year?",
        "options": ["Mbappé", "Luka Modrić", "Antoine Griezmann", "Raphael Varane"],
        "answer": "Luka Modrić"
    },
    {
        "question": "Who is the only goalkeeper to have won the Ballon d'Or?",
        "options": ["Lev Yashin", "Dino Zoff", "Oliver Kahn", "Gianluigi Buffon"],
        "answer": "Lev Yashin"
    },
    {
        "question": "Which year did Cristiano Ronaldo win his first Ballon d'Or?",
        "options": ["2008", "2009", "2010", "2011"],
        "answer": "2008"
    },
    {
        "question": "Who would have surely won the Ballon d'Or in 2020, if not for Covid-19?",
        "options": ["Lionel Messi", "Cristiano Ronaldo", "Robert Lewandowski", "Luka Modric"],
        "answer": "Robert Lewandowski"
    },
    {
        "question": "Which country has produced the most Ballon d'Or winners as of 2022?",
        "options": ["Brazil", "Argentina", "Germany", "France"],
        "answer": "Argentina"
    },
    {
        "question": "Who was the youngest ever Ballon d'Or winner at the age of 20 in 1957?",
        "options": ["Omar Sivori", "Eusébio", "Raymond Kopa", "Ronaldo Nazário"],
        "answer": "Ronaldo Nazário"
    },
    {   "question": "In which stadium is the 2024 Champions League Final being played?",
        "options": ["Parc des Princes", "Santiago Bernabeu", "Wembley", "San Siro"],
        "answer": "Wembley"
    },
    {
        "question": "Which country has won the most FIFA World Cups?",
        "options": ["Germany", "Brazil", "Italy", "Argentina"],
        "answer": "Brazil"
    },
    {
        "question": "Who is the all-time top scorer in the FIFA World Cup?",
        "options": ["Lionel Messi", "Miroslav Klose", "Pelé", "Just Fontaine"],
        "answer": "Miroslav Klose"
    },
    {
        "question": "Which club won the first UEFA Champions League in its current format (1992-93)?",
        "options": ["AC Milan", "FC Barcelona", "Marseille", "Ajax"],
        "answer": "Marseille"
    },
    {
        "question": "Who scored the fastest goal in Premier League history?",
        "options": ["Sadio Mané", "Alan Shearer", "Ledley King", "Shane Long"],
        "answer": "Shane Long"
    },
    {
        "question": "Which national team has won the most African Cup of Nations titles?",
        "options": ["Ivory Coast", "Nigeria", "Cameroon", "Egypt"],
        "answer": "Egypt"
    },
    {
        "question": "Which player holds the record for the most goals in a calendar year?",
        "options": ["Lionel Messi", "Cristiano Ronaldo", "Gerd Müller", "Pelé"],
        "answer": "Lionel Messi"
    },
    {
        "question": "Which club has the most UEFA Europa League titles?",
        "options": ["Sevilla", "Liverpool", "Inter Milan", "Juventus"],
        "answer": "Sevilla"
    },
    {
        "question": "Who won the Golden Boot at the 2014 FIFA World Cup?",
        "options": ["Miroslav Klose", "Thomas Müller", "Lionel Messi", "James Rodríguez"],
        "answer": "James Rodríguez"
    },
    {
        "question": "Who is the only player to have won the Champions League with three different clubs?",
        "options": ["Clarence Seedorf", "Cristiano Ronaldo", "Samuel Eto'o", "Zlatan Ibrahimović"],
        "answer": "Clarence Seedorf"
    },
    {
        "question": "Which country won the first European Championship in 1960?",
        "options": ["Spain", "Soviet Union", "Italy", "France"],
        "answer": "Soviet Union"
    },
    {
        "question": "Which player has the most assists in Premier League history?",
        "options": ["Ryan Giggs", "Cesc Fàbregas", "Frank Lampard", "Wayne Rooney"],
        "answer": "Ryan Giggs"
    },
    {
        "question": "Who was the first non-European player to win the Ballon d'Or?",
        "options": ["Romário", "Pelé", "Diego Maradona", "George Weah"],
        "answer": "George Weah"
    },
    {
        "question": "Which team won the first Premier League title in 1992-93?",
        "options": ["Blackburn Rovers", "Manchester United", "Arsenal", "Chelsea"],
        "answer": "Manchester United"
    },
    {
        "question": "Who scored the 'Hand of God' goal in the 1986 FIFA World Cup?",
        "options": ["Jorge Valdano", "Gary Lineker", "Diego Maradona", "Michel Platini"],
        "answer": "Diego Maradona"
    },
    {
        "question": "Which club is known as 'The Old Lady'?",
        "options": ["Real Madrid", "Juventus", "Manchester United", "Bayern Munich"],
        "answer": "Juventus"
    },
    {
        "question": "Which player has won the most Champions League titles?",
        "options": ["Cristiano Ronaldo", "Paolo Maldini", "Alfredo Di Stéfano", "Francisco Gento"],
        "answer": "Francisco Gento"
    },
    {
        "question": "Which player scored the 'Golden Goal' to win Euro 2000?",
        "options": ["David Trezeguet", "Thierry Henry", "Francesco Totti", "Alessandro Del Piero"],
        "answer": "David Trezeguet"
    },
    {
        "question": "How many goals did Lionel Messi score in 2012",
        "options": ["81", "91", "92", "88"],
        "answer": "91"
    },
    {
        "question": "Which club has won the most Bundesliga titles?",
        "options": ["Hamburg SV", "Borussia Dortmund", "Bayern Munich", "Werder Bremen"],
        "answer": "Bayern Munich"
    },
    {
        "question": "Which player scored the most goals in a single World Cup tournament?",
        "options": ["Gerd Müller", "Ronaldo", "Pelé", "Just Fontaine"],
        "answer": "Just Fontaine"
    }

]

def football_quiz():
    st.title("Football Quiz!")
    
    with st.form("quiz_form"):
        user_answers = {}
        for i, q in enumerate(questions):
            user_answers[i] = st.radio(q["question"], q["options"])


        submit_button = st.form_submit_button(label="Submit Answers")

    if submit_button:
        score = 0
        for i, q in enumerate(questions):
            if user_answers[i] == q["answer"]:
                score += 1

        st.write(f"Your score: {score}/{len(questions)}")
        if score == len(questions):
            st.success("Congratulations! Your football knowledge is amazing!")
        elif score >= (len(questions) / 2):
            st.info("Not terrible, but you can do better!")
        else:
            st.info("Not great, you still have a lot to learn about football...")

if __name__ == "__main__":
    football_quiz()
    
    
