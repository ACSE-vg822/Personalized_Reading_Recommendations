from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from similarity_matrix import compute_similarity_matrix
from recommendation import get_recommendations

indices = pd.read_pickle('File_dump/indices.pkl')
df = pd.read_pickle('File_dump/df.pkl')
cosine_sim = compute_similarity_matrix(df)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_input():
    if request.method == 'POST':
        user_input = request.form['input']
        result = get_recommendations(user_input, cosine_sim, indices, df)
        result_table = result.to_html()
        return render_template('result.html', table=result_table)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
