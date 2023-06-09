import pandas as pd

def get_recommendations(title, cosine_sim, df):
    
    # I want this function to be case-insensitive
    # The user should be able to enter values in whatever case they like and they should get recommendations
    # Hence I convert everything to lowercase and then compare
    # Convert the title to lower case
    title = title.lower()

    # Convert all the titles in the DataFrame to lower case for comparison
    df['title_lower'] = df['title'].str.lower()
    
    #if the book title is not found in the dataset, return False
    if title not in df['title_lower'].values:
        return False
    
    # Create a new Series with lower case titles as index
    indices_lower = pd.Series(df.index, index=df['title_lower']).drop_duplicates()

    # Match the book with the corresponding index
    idx = indices_lower[title]

    # Get the pairwise similarity scores of all books with that book
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the books based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar books
    sim_scores = sim_scores[1:11] #Starting from 1 because 0 would be the book itself

    # Get the book indices
    book_indices = [i[0] for i in sim_scores]

    # Remove the 'title_lower' column
    df = df.drop(columns=['title_lower'])

    # Return the top 10 most similar books
    return df.iloc[book_indices]
