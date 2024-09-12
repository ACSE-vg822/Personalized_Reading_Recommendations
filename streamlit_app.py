import streamlit as st
import numpy as np
import pandas as pd
from Utilities.recommendation import get_recommendations

# Title of the app
st.title("Book Recommendation System")

# Prompt the user for input
user_input = st.text_input("What's your favorite title? :)")

# Check if input is provided
if user_input:
    result = get_recommendations(user_input)
    
    if result is False:
        st.error("Sorry, this book is not available in our database :(")
    else:
        # Show the recommended books
        st.write("Here are some recommendations for you:")
        # Display the recommendations as a table (only the second column)
        st.table(result.iloc[:, [1]])

