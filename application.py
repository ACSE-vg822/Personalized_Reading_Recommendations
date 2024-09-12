from flask import Flask, render_template, request
import numpy as np
import pandas as pd

#from Utilities.similarity_matrix import compute_similarity_matrix
from Utilities.recommendation import get_recommendations

application = Flask(__name__)
app = application


@app.route('/', methods=['GET', 'POST'])
def process_input():
    if request.method == 'POST':
        user_input = request.form['input']
        result = get_recommendations(user_input)
        
        if result is False:
            return render_template('not_found.html')  # Render not_found.html template if result is False
        
        # Select only the second column from the DataFrame and render as HTML
        result_table = result.iloc[:, [1]].to_html(index=False)  # Only the second column
        return render_template('result.html', table=result_table)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
