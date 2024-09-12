# 📚 Book Recommendation System

A simple book recommendation system built using Streamlit and a similarity matrix to suggest books based on a user's input. The system uses a dataset of books and provides recommendations based on the most similar titles.

Hosted on Streamlit: https://personalizedreadingrecommendations-5ceie6kslmwvvk97zqeuzk.streamlit.app/

## 🚀 Features

- **Book Recommendations**: Users can input the title of a book, and the system will recommend similar books.
- **Interactive Interface**: Built using Streamlit, the app provides a clean, user-friendly interface for input and displaying recommendations.
- **Real-Time Results**: The app instantly displays recommendations based on the entered book title.
- **Example Searches**: Suggestions provided for sample book titles to help users start.

## 🎨 Technologies Used

- **Streamlit**: For the web interface.
- **Pandas**: To manage and manipulate the book dataset.
- **Similarity Matrix**: For calculating book similarities based on titles.
- **Python**: The core programming language used for the app.

## 🛠️ Installation

To run the project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Create a virtual environment** (Optional but recommended):

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate   # On Windows use: myenv\Scripts\activate
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:

    ```bash
    streamlit run streamlit_app.py
    ```

5. **Navigate to your browser**:

    The app will be locally hosted and can be found by following the link displayed in the terminal

## 📁 Folder Structure

```bash
/Personalized_Reading_Recommendations/
    ├── streamlit_app.py              # Main Streamlit app file
    ├── Data_Cleaning.ipynb           # Notebook for data cleaning
    ├── Model_and_evaluation.ipynb    # Notebook for training and evaluation
    ├── Utilities/
    │   ├── recommendation.py         # Contains the recommendation function
    │   ├── similarity_matrix.py      # Computing similarity matrix 
    ├── File_dump/
    │   ├── cosine_sim.pkl            # Pre-computed similarity matrix
    │   ├── df.pkl                    # Cleaned dataset of books
    ├── requirements.txt              # Project dependencies
    ├── static/
    │   ├── index_image.png           # Optional image for the background
    ├── README.md                     # Project README file

## 🔍 How to Use

1. **Enter a Book Title**: You can input any book title (e.g., *Macbeth*, *Pride and Prejudice*, *Orlando*).
2. **View Recommendations**: Based on your input, the app will provide a list of similar books.
3. **Example Queries**: If you're not sure what to search for, try one of the example queries under the input field.

## ⚡ Example Book Titles

- *Macbeth*
- *Orlando*
- *Pride and Prejudice*
- *A Room of One's Own*

## 🤔 Issues or Improvements?

Feel free to open an issue or create a pull request with improvements or bug fixes.
