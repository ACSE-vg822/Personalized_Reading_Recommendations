import numpy as np
import pandas as pd

# Load the cosine similarity matrix from the .npy file
cosine_sim = np.load('File_dump/cosine_sim.npy')
indices = pd.read_pickle('File_dump/indices.pkl')
df = pd.read_pickle('File_dump/df.pkl')

def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the book that matches the title
    idx = indices[title]

    # Get the pairwise similarity scores of all books with that book
    sim_scores = list(enumerate(cosine_sim[idx].flatten()))

    # Sort the books based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar books
    sim_scores = sim_scores[1:11]

    # Get the book indices
    book_indices = [i[0] for i in sim_scores]
    
    # Return the top 10 most similar books
    return df.iloc[book_indices]

#print(get_recommendations('A Short History of Nearly Everything'))

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_input():
    if request.method == 'POST':
        user_input = request.form['input']
        result = get_recommendations(user_input)
        result_table = result.to_html()
        return render_template('result.html', table=result_table)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
