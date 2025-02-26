import streamlit as st
import time
from datetime import date
import authentication  # Importing authentication module



# Function to display the Growth Mindset Challenge page

# Session state to track login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = ""
    
# Track which form is open
if "form_state" not in st.session_state:
    st.session_state.form_state = None

# Sidebar Buttons for Authentication
st.title("User Authentication")

if not st.session_state.logged_in:
    col1, col2 = st.columns(2)  # Create two equal columns

    with col1:
        if st.button("Sign Up"):
            st.session_state.form_state = "signup"

    with col2:
        if st.button("Sign In"):
            st.session_state.form_state = "signin"

    # **Show the relevant form based on session state**
    if st.session_state.form_state == "signup":
        authentication.signup_page()  # Show signup form
    
    if st.session_state.form_state == "signin":
        authentication.signin_page()  # Show signin form

else:
    st.success(f"Logged in as {st.session_state.user_email}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_email = ""
        st.session_state.form_state = None  # Reset form state
        st.rerun()

        # home page
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
    st.title("📞 Contact Us")
    st.write("We would love to hear your thoughts about this app! Please provide your feedback below:")

    # Input fields
    name = st.text_input("Enter Your Name", "")
    email = st.text_input("Enter your Email")
    feedback_date = st.date_input("Enter Date", value=date.today())
    feedback = st.text_area("Enter your Comment here...")

    # Rating slider
    rating = st.feedback("stars")

    # Submit button logic
    if st.button("Submit Feedback"):
        if feedback.strip():
            with open("feedback.txt", "a", encoding="utf-8") as file:
                file.write(f"Name: {name}\nEmail: {email}\n Date: {feedback_date}\nFeedback: {feedback}\nRating: {rating}\n" + "-"*50 + "\n")

            st.success("✅ Thank you for your feedback! We appreciate your time.")

            # Display feedback below
            st.write("### Submitted Feedback")
            st.write(f"**Name:** {name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Date:** {feedback_date}")
            st.write(f"**Feedback:** {feedback}")
            st.write(f"**Rating:** {rating}")

        else:
            st.warning("⚠️ Please enter some feedback before submitting.")
            

# AboutMe page function
def Aboutme(): 
    st.title("📌 About Me")
    st.write("👋 Hello! I'm Sana Faisal, an aspiring Cloud AI Engineer passionate about Python, TypeScript, Next.js, and AI development.")           

    # Rounded image
    st.image("images/aboutpage.jpg", caption="My Profile", width=450)  # Width adjust kar sakte ho

    st.header("🚀 My Journey:")
    st.markdown("""
    - 💡 **Always eager to learn new technologies.**  
    - 🔍 **Exploring the world of Artificial Intelligence & Cloud Computing.**  
    - 🎯 **Focused on web development, AI solutions, and cloud-based applications.**  
    """)

    st.header("🌟 Skills & Expertise")
    st.markdown("""
    - 💻 Web Development (HTML, CSS, JavaScript, Tailwind CSS, TypeScript, Next.js)  
    - 📡 Cloud & AI (Python, Machine Learning, AI Engineering)  
    - 📈 Digital Marketing & SEO (Shopify, WordPress, Marketing Strategies)  
    - 📩 Let’s Connect! I’d love to collaborate on exciting tech projects! 🚀🔗  
    """)

     
# Sidebar Navigation
# Custom CSS for Sidebar Styling
st.markdown("""
    <style>
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #1A1A2E, #16213E); /* Gradient Background */
            padding-top: 20px;
            border-right: 2px solid #0F3460;
        }

        /* Sidebar Title Styling */
        [data-testid="stSidebar"] h1 {
            color: #00FFD1;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            text-transform: uppercase;
            text-shadow: 0px 0px 15px rgba(0, 255, 209, 0.9);
        }

        /* SelectBox Styling */
        select {
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: 2px solid #00FFD1;
            padding: 12px;
            border-radius: 12px;
            width: 100%;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }

        /* SelectBox Hover Effect */
        select:hover {
            background: #00FFD1;
            color: black;
            font-weight: bold;
        }

        /* Option Styling */
        option {
            background: #16213E;
            color: white;
            font-size: 16px;
            font-weight: bold;
        }

        /* Option Hover Effect */
        select option:hover {
            background: #00FFD1 !important;
            color: black !important;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with Styling and Emoji
st.sidebar.title("✨ Sana Faisal 🚀")
st.sidebar.subheader("🌟 Welcome to my Streamlit App! 🎉")

st.sidebar.title("📚 Learning Hub 🌟")
st.sidebar.markdown("----")

# Ensure session state is initialized
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Navigation (Only Show if Logged In)
if st.session_state.logged_in:
    page = st.sidebar.selectbox("🔍 Explore:", ["🏠 Home", "📌 About Me", "🧠 Quiz Section", "📞 Contact Us"])

    # Navigation Logic
    if page == "🏠 Home":
        growth_mindset()

    elif page == "📌 About Me":
        Aboutme()

    elif page == "🧠 Quiz Section":
        language = st.sidebar.selectbox("Select a programming language", ["Select a Language"] + list(quizzes.keys()))

        if language == "Select a Language":
            st.title("🧠 Programming Quiz")
            st.write("📢 **Please select a language from the sidebar to start the quiz.**")
        else:
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
                    else:
                        st.error(f"❌ Incorrect! The correct answer is: {q['answer']}")

                st.write(f"### 🎯 Your Final Score: {score} / {len(quizzes[language])}")
                if score == len(quizzes[language]):
                    st.balloons()
                elif score >= len(quizzes[language]) / 2:
                    st.success("🔥 Good job! Keep practicing.")
                else:
                    st.warning("📚 Keep learning! You'll improve with time.")

    elif page == "📞 Contact Us":
        feedback_page()

else:
    st.warning("Please Sign In to access the pages.")

# Footer
st.markdown("----")
st.markdown(
    """
    <div style="text-align: center; margin-top: 10px; padding: 20px; color: yellow; font-size: 18px;">
        🚀 Made with ❤️ by <b>Sana Faisal</b> | © 2025 All Rights Reserved.<br>
        Follow me on <a href="https://www.linkedin.com/in/sana-faisal-developer/" target="_blank" style="color:lightblue;">LinkedIn</a> | Visit: <a href="https://fusiontrend.pk" target="_blank" style="color:lightblue;">FusionTrend.pk</a>
    </div>
    """,
    unsafe_allow_html=True
)




















