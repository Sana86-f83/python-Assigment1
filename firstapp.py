import streamlit as st

# Function to display the Growth Mindset Challenge page
def growth_mindset():
    st.title("🌱 Growth Mindset Challenge")
    st.write("""
    **A growth mindset** is the belief that your abilities and intelligence can be developed through hard work, perseverance, 
    and learning from your mistakes. 🚀  

    ### 🌟 Why Adopt a Growth Mindset?
    - 🔥 **Embrace Challenges**: View obstacles as opportunities to learn rather than setbacks.
    - 🎯 **Learn from Mistakes**: Making mistakes is a natural part of learning.
    - 💪 **Persist Through Difficulties**: Stay determined, even when things get tough.
    - 🏆 **Celebrate Effort**: Recognize and reward the effort you put into learning.
    - 🔍 **Keep an Open Mind**: Stay curious and be willing to adapt.  

    **Remember, your journey in education isn’t just about proving your intelligence—it’s about developing it.** ✨
    """)

# Define Quiz Questions
quizzes = {
    "HTML": [
        {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Machine Learning", "Hyper Tool Multi Language"], "answer": "Hyper Text Markup Language"},
        {"question": "Which tag is used for the largest heading?", "options": ["<h6>", "<h1>", "<h3>"], "answer": "<h1>"},
        {"question": "Which tag is used to create a hyperlink?", "options": ["<a>", "<link>", "<href>"], "answer": "<a>"},
        {"question": "Which tag is used to insert an image?", "options": ["<img>", "<pic>", "<image>"], "answer": "<img>"},
        {"question": "What is the correct file extension for HTML?", "options": [".html", ".htm", ".web"], "answer": ".html"},
    ],
    "CSS": [
        {"question": "Which property is used to change text color?", "options": ["color", "font-size", "background"], "answer": "color"},
        {"question": "What does CSS stand for?", "options": ["Cascading Style Sheet", "Computer Style System", "Creative Styling Software"], "answer": "Cascading Style Sheet"},
        {"question": "Which CSS property controls text size?", "options": ["font-size", "text-size", "size"], "answer": "font-size"},
        {"question": "Which CSS property makes an element invisible?", "options": ["visibility: hidden", "display: none", "both"], "answer": "both"},
        {"question": "Which unit is used for responsive design?", "options": ["px", "em", "%"], "answer": "%"},
    ],
    "JavaScript": [
        {"question": "Which keyword is used to declare a variable in JavaScript?", "options": ["var", "define", "let"], "answer": "var"},
        {"question": "Which symbol is used for comments in JavaScript?", "options": ["//", "<!-- -->", "/* */"], "answer": "//"},
        {"question": "Which function is used to print output in JavaScript?", "options": ["print()", "console.log()", "log()"], "answer": "console.log()"},
        {"question": "Which operator is used for strict equality?", "options": ["==", "===", "="], "answer": "==="},
        {"question": "Which method converts a string to an integer?", "options": ["parseInt()", "int()", "Number()"], "answer": "parseInt()"},
    ],
    "TypeScript": [
        {"question": "Which of these is a valid TypeScript type?", "options": ["number", "int", "float"], "answer": "number"},
        {"question": "Which command is used to compile TypeScript?", "options": ["tsc", "node", "compile-ts"], "answer": "tsc"},
        {"question": "Which TypeScript feature is not in JavaScript?", "options": ["Interfaces", "Objects", "Functions"], "answer": "Interfaces"},
        {"question": "Which symbol is used for optional properties?", "options": ["?", "!", ":"], "answer": "?"},
        {"question": "How do you specify a return type for a function?", "options": [":type", "= type", "<type>"], "answer": ":type"},
    ],
    "Tailwind CSS": [
        {"question": "Which class is used for padding in Tailwind?", "options": ["p-4", "margin-4", "pad-4"], "answer": "p-4"},
        {"question": "Which prefix is used for responsive classes?", "options": ["sm:", "res:", "rsp:"], "answer": "sm:"},
        {"question": "Which utility is used for flexbox layout?", "options": ["flex", "grid", "block"], "answer": "flex"},
        {"question": "Which class sets text color to red?", "options": ["text-red-500", "color-red", "text-danger"], "answer": "text-red-500"},
        {"question": "Which class sets background to blue?", "options": ["bg-blue-500", "background-blue", "bg-primary"], "answer": "bg-blue-500"},
    ],
            "Next.js": [
            {"question": "Which command is used to create a new Next.js app?", "options": ["npx create-next-app", "npm init next", "yarn start next"], "answer": "npx create-next-app"},
            {"question": "Which function is used to fetch data in Next.js?", "options": ["getStaticProps", "useState", "fetchData"], "answer": "getStaticProps"},
            {"question": "Which Next.js feature supports server-side rendering?", "options": ["getServerSideProps", "getStaticProps", "fetchData"], "answer": "getServerSideProps"},
            {"question": "Which file is the entry point of a Next.js app?", "options": ["index.js", "_app.js", "main.js"], "answer": "_app.js"},
            {"question": "Which command starts a Next.js development server?", "options": ["npm run dev", "npm start", "next start"], "answer": "npm run dev"},
        ],

}

# Function to display the Feedback Page
def feedback_page():
    st.title("📝 Feedback")
    st.write("We would love to hear your thoughts about this app! Please provide your feedback below:")
    
    feedback = st.text_area("Enter your feedback here...")
    likes   =  st.feedback("stars")

    
    if st.button("Submit Feedback"):
        st.success("✅ Thank you for your feedback! We appreciate your time.")

# Sidebar Navigation
st.sidebar.title("📖 Learning Hub")
page = st.sidebar.radio("Go to", ["🌱 Growth Mindset Challenge", "🧠 Quiz", "📝 Feedback"])

# Navigation Logic
if page == "🌱 Growth Mindset Challenge":
    growth_mindset()
elif page == "🧠 Quiz":
    language = st.sidebar.selectbox("Select a programming language", ["Select a Language"] + list(quizzes.keys()))
    if language and language != "Select a Language":
        st.title(f"🧠 {language} Quiz")
        score = 0
        user_answers = {}
        for q in quizzes[language]:
            user_answers[q["question"]] = st.radio(q["question"], q["options"], index=None, key=q["question"])
        if st.button("✅ Submit All Answers"):
            for q in quizzes[language]:
                if user_answers[q["question"]] == q["answer"]:
                    score += 1
                    st.success(f"✅ Correct! {q['question']}")
                    st.balloons()
                    
                else:
                    st.error(f"❌ Wrong answer. The correct answer is: **{q['answer']}**")
            total_questions = len(quizzes[language])
            st.write(f"🏆 **Your Final Score: {score}/{total_questions}**")
elif page == "📝 Feedback":
    feedback_page()

# Footer
st.markdown("---")
st.markdown("<h5 style='text-align: center; color:yellow'>Made by Sana Faisal</h5>", unsafe_allow_html=True)
