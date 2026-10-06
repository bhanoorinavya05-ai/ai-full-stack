import streamlit as st
import pandas as pd
import ollama
from pathlib import Path
from datetime import datetime

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Mess Menu Assistant",
    page_icon="🍽️",
    layout="centered"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🍽️ Mess Menu Assistant")

st.write(
    "Ask questions about the college mess menu "
    "and get quick answers using AI."
)

# --------------------------------------------------
# Find menu.csv in the same folder as this program
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MENU_FILE = BASE_DIR / "menu.csv"


# --------------------------------------------------
# Load Menu
# --------------------------------------------------

@st.cache_data
def load_menu():

    if not MENU_FILE.exists():
        return None

    return pd.read_csv(MENU_FILE)


menu = load_menu()


# --------------------------------------------------
# Check Menu File
# --------------------------------------------------

if menu is None:

    st.error(
        "❌ menu.csv was not found.\n\n"
        "Please keep menu.csv in the same folder as "
        "Mess_Menu_Assistant.py."
    )

    st.stop()


# --------------------------------------------------
# Check Required Columns
# --------------------------------------------------

required_columns = ["Day", "Meal", "Menu"]

for column in required_columns:

    if column not in menu.columns:

        st.error(
            f"❌ The column '{column}' is missing "
            "from menu.csv."
        )

        st.stop()


# --------------------------------------------------
# Display Complete Menu
# --------------------------------------------------

st.subheader("📋 Complete Mess Menu")

st.dataframe(
    menu,
    use_container_width=True
)


# --------------------------------------------------
# Create Menu Context
# --------------------------------------------------

def create_menu_context():

    context = ""

    for _, row in menu.iterrows():

        context += (
            f"Day: {row['Day']}\n"
            f"Meal: {row['Meal']}\n"
            f"Food: {row['Menu']}\n\n"
        )

    return context


menu_context = create_menu_context()


# --------------------------------------------------
# Ask Ollama
# --------------------------------------------------

def ask_ollama(question):

    prompt = f"""
You are a college Mess Menu Assistant.

Answer the user's question ONLY using the menu
information given below.

Do not make up food items.

If the requested information is not available,
say:

"Sorry, that information is not available in
the current mess menu."

MESS MENU INFORMATION:

{menu_context}

USER QUESTION:

{question}

Give a short, clear and friendly answer.
"""

    try:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as error:

        return (
            "❌ Could not connect to Ollama.\n\n"
            "Please make sure Ollama is installed "
            "and the llama3.2 model is available.\n\n"
            f"Error: {error}"
        )


# --------------------------------------------------
# Ask Question
# --------------------------------------------------

st.subheader("💬 Ask the Mess Assistant")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is today's lunch?"
)


if st.button("🤖 Ask Assistant"):

    if question.strip() == "":

        st.warning(
            "Please enter a question first."
        )

    else:

        with st.spinner("🤔 Finding your answer..."):

            answer = ask_ollama(question)

        st.subheader("🤖 Assistant Answer")

        st.write(answer)


# --------------------------------------------------
# Today's Menu
# --------------------------------------------------

st.subheader("📅 Today's Menu")

today = datetime.now().strftime("%A")

today_menu = menu[
    menu["Day"].astype(str).str.lower()
    == today.lower()
]


if not today_menu.empty:

    st.write(f"### {today}")

    for _, row in today_menu.iterrows():

        st.write(
            f"**{row['Meal']} :** {row['Menu']}"
        )

else:

    st.info(
        f"No menu information available for {today}."
    )


# --------------------------------------------------
# Example Questions
# --------------------------------------------------

st.subheader("💡 Example Questions")

st.markdown("""
- What is today's breakfast?
- What is today's lunch?
- What is today's dinner?
- What is available on Monday?
- What are the snacks on Friday?
- Show me Tuesday's complete menu.
- What food is available on Sunday?
""")


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Mess Menu Assistant | Python + Streamlit + Ollama"
)