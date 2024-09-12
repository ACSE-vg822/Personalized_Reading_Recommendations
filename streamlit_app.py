import streamlit as st
import base64
import pandas as pd
from Utilities.recommendation import get_recommendations


# Custom CSS for background and styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        /* background-image: url("static/index_image.png"); */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    h1 {
        color: #4CAF50;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .recommendations-table {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        margin: 20px 0;
    }
    .recommendations-table table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }
    .recommendations-table td, .recommendations-table th {
        border: 1px solid #ddd;
        padding: 8px;
    }
    .recommendations-table th {
        display: none;
    }
    .recommendations-table tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    .recommendations-table tr:hover {
        background-color: #ddd;
    }
    .recommendations-table td {
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the app
st.title("📚 Book Recommendation System")

#st.image('static/index_image.png', use_column_width=True)

# Prompt the user for input
user_input = st.text_input("Enter the title of a book you like:")

# Show example text under the input field
st.markdown("For example: *Macbeth, Orlando, Pride and Prejudice, A Room of One's Own*")

# Add space between elements
st.markdown("<br>", unsafe_allow_html=True)

# Show recommendations only if input is provided
if user_input:
    result = get_recommendations(user_input)
    
    if result is False:
        st.error("🚫 Sorry, this book is not available in our database.")
    else:
        st.success("🎉 Here are some book recommendations based on your input:")
        
        # Prepare the list of recommended books
        book_list = result.iloc[:, 1].tolist()  # Extract the second column with book titles

        # Render the table without the header and index
        html_table = """
        <div class="recommendations-table">
        <table>
        <tbody>
        """
        for book in book_list:
            html_table += f"<tr><td>{book}</td></tr>"
        html_table += """
        </tbody>
        </table>
        </div>
        """
        st.markdown(html_table, unsafe_allow_html=True)
