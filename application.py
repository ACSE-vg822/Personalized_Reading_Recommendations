from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

from Utilities.similarity_matrix import compute_similarity_matrix
from Utilities.recommendation import get_recommendations


# Once the user has run all cells in 'Model_and_Evaluation.ipynb', they should comment # 1 and uncomment # 2 and # 3
# This is to ensure that we don't create a new model each time, hence saving time and computaional capacity
# After running that jupyter notebook, the model is saved as a pickle file and can be loaded here
# cosine_sim.pkl is a big file and couldn't be pushed to GitHub, hence I am adding the instructions here

# cosine_sim = compute_similarity_matrix(df) # 1


with open('File_dump/cosine_sim.pkl', 'rb') as f: # 2
    cosine_sim = pickle.load(f)                   # 3

with open('File_dump/df.pkl', 'rb') as f:
    df = pickle.load(f)
    
application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def process_input():
    if request.method == 'POST':
        user_input = request.form['input']
        result = get_recommendations(user_input, cosine_sim, df)
        
        if result is False:
            return render_template('not_found.html')  # Render not_found.html template if result is False
        
        # Select only the second column from the DataFrame and render as HTML
        result_table = result.iloc[:, [1]].to_html(index=False)  # Only the second column
        return render_template('result.html', table=result_table)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
