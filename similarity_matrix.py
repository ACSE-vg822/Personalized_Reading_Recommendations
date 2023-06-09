import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# This is the best combination of features so far
# (Commented below) I tried many permutations and combinations of features, but title+authors gave the best performance

def compute_similarity_matrix(df):
    
    # Combines 'title' and 'authors' into a new column 'content'
    # This column will be used to compute the similarity matrix
    df['content'] = df['title'] + ' ' + df['authors'] #+ ' ' + df['ratings_count'].astype(str) + ' ' + df['text_reviews_count'].astype(str)
    
    # Initialize the TfidfVectorizer
    # TfidfVectorizer will convert the 'content' column into a matrix of TF-IDF features
    # stop_words='english' will remove all common words ('a', 'an', 'the', etc.) hence reducing noise in the data
    tfidf = TfidfVectorizer(stop_words='english')
    
    # Apply the vectorizer to the 'content' column
    # This step transforms the text into a matrix of TF-IDF features
    tfidf_matrix = tfidf.fit_transform(df['content'])
    
    # Compute the cosine similarity matrix from the TF-IDF matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    # Return the computed cosine similarity matrix
    return cosine_sim




"""def compute_similarity_matrix(df):
    # Convert 'average_rating' to categorical bins
    bins = [1, 2, 3, 4, 5]
    labels = ['1-2', '2-3', '3-4', '4-5']
    df['average_rating_cat'] = pd.cut(df['average_rating'], bins=bins, labels=labels, include_lowest=True)

    # Concatenate 'average_rating_cat', 'average_rating', 'ratings_count' and 'language_code' (all converted to string)
    df['new_content'] = df['average_rating_cat'].astype(str) + ' ' + df['average_rating'].astype(str) + ' ' + df['ratings_count'].astype(str) + ' ' + df['language_code'].astype(str)

    # Create a new TF-IDF Vectorizer
    tfidf_new = TfidfVectorizer(stop_words='english')

    # Construct the new TF-IDF matrix
    tfidf_matrix_new = tfidf_new.fit_transform(df['new_content'])

    # Compute the new cosine similarity matrix
    cosine_sim_new = linear_kernel(tfidf_matrix_new, tfidf_matrix_new)

    # Now, for the original content-based cosine similarity
    df['content'] = df['title'] + ' ' + df['authors']
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Compute the average of the old and new cosine similarity matrices
    cosine_sim_avg = (cosine_sim + cosine_sim_new) / 2

    return cosine_sim_avg"""

"""def compute_similarity_matrix(df):
    # Convert 'average_rating' to categorical bins
    bins = [1, 2, 3, 4, 5]
    labels = ['1-2', '2-3', '3-4', '4-5']
    df['average_rating_cat'] = pd.cut(df['average_rating'], bins=bins, labels=labels, include_lowest=True)

    # Concatenate all desired features (converted to string)
    df['all_content'] = df['title'] + ' ' + df['authors'] + ' ' + df['average_rating_cat'].astype(str) + ' ' + df['average_rating'].astype(str) + ' ' + df['ratings_count'].astype(str) + ' ' + df['language_code'].astype(str)

    # Create a new TF-IDF Vectorizer
    tfidf_all = TfidfVectorizer(stop_words='english')

    # Construct the new TF-IDF matrix
    tfidf_matrix_all = tfidf_all.fit_transform(df['all_content'])

    # Compute the new cosine similarity matrix
    cosine_sim_all = linear_kernel(tfidf_matrix_all, tfidf_matrix_all)

    return cosine_sim_all"""



