# Personalized_Reading_Recommendations
This is a book recommendation system implemented in Python, using content-based filtering.

# Overview
The recommendation system takes as input a book title, and outputs a list of books that are similar to the input book. The similarity is determined based on the book's title and authors. As advised in the problem statement, data has been taken from this link: https://www.kaggle.com/jealousleopard/goodreadsbooks

# System Requirements
Python 3.7+
Then create the environment as instructed further below

# Project Structure
    Dataset/: This directory contains the original dataset.
    File_dump/: This directory contains all the pickle files.
    templates/: This directory contains the html files for the user interface.
    Utilities/: This directory contains two utility scripts as follows:
                similarity_matrix.py: This script contains a function to compute the cosine similarity matrix for the books data.
                recommendation.py: This script contains a function to generate book recommendations based on the similarity matrix.
    Data_Cleaning.ipynb: This is the Jupyter Notebook where we clean the dataset.
    Model_and_Evaluation.ipynb: This is the Jupyter Notebook where we create and evaluate the model.

# !Attention!
Ideally we'd want to save our cosine matrix after the first run and then resuse it for recommendations over and over again. However, the pickle file of cosine matrix was ~818MB in size and couldn't be pushed to GitHub. Hence, the code at the moment is desgined that it runs by creating the model all over again for every run. **However, clear instructions have been provided as to how the user can create and save the matrix locally and reuse it every time. User is advised to go through the instructions carefully.**

# Setup
1. Clone the repository in your local computer: https://github.com/ACSE-vg822/Personalized_Reading_Recommendations.git
2. Create the environment: conda env create -f environment.yml. Then activate it: conda activate book_rec
3. Go to 'Model_and_Evaluation.ipynb' and run all cells. This will ensure the a pickle file of cosine similarity matrix is saved in the File_dump/ directory.
4. Now go to app.py and follow the intructions of commenting/uncommenting specific lines.

**Note: User can skip 3 and 4 if they want, and directly go to 5. However, in that case a new model will be created for every run, which is time and computation expensive :(**

5. In the command-line, go to the top most level of the directory and run this command: flask run 

6. Paste this link in your browser: http://127.0.0.1:5000() 
(Link to handle cases where some other program might be using this address: https://flask.palletsprojects.com/en/2.3.x/server/#address-already-in-use)

Enjoy reading! :)