import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np


class Index:
    """
    A simple search index using TF-IDF and cosine similarity for text fields and exact matching for keyword fields.

    Attributes:
        text_fields (list): List of text field names to index.
        keyword_fields (list): List of keyword field names to index.
        vectorizers (dict): Dictionary of TfidfVectorizer instances for each text field.
        keyword_df (pd.DataFrame): DataFrame containing keyword field data.
        text_matrices (dict): Dictionary of TF-IDF matrices for each text field.
        docs (list): List of documents indexed.
    """

    def __init__(self, text_fields, keyword_fields, vectorizer_params={}):
        """
        Initializes the Index with specified text and keyword fields.

        Args:
            text_fields (list): List of text field names to index.
            keyword_fields (list): List of keyword field names to index.
            vectorizer_params (dict): Optional parameters to pass to TfidfVectorizer.
        """
        self.text_fields = text_fields
        self.keyword_fields = keyword_fields

        self.vectorizers = {field: TfidfVectorizer(**vectorizer_params) for field in text_fields}
        self.keyword_df = None
        self.text_matrices = {}
        self.docs = []

    def fit(self, docs):
        """
        Fits the index with the provided documents.

        Args:
            docs (list of dict): List of documents to index. Each document is a dictionary.
        """
        self.docs = docs
        keyword_data = {field: [] for field in self.keyword_fields}

        for field in self.text_fields:
            texts = [doc.get(field, '') for doc in docs]
            self.text_matrices[field] = self.vectorizers[field].fit_transform(texts)

        for doc in docs:
            for field in self.keyword_fields:
                keyword_data[field].append(doc.get(field, ''))

        self.keyword_df = pd.DataFrame(keyword_data)

        return self

    def search(self, query, filter_dict={}, boost_dict={}, num_results=10):
        """
        Searches the index with the given query, filters, and boost parameters.

        Args:
            query (str): The search query string.
            filter_dict (dict): Dictionary of keyword fields to filter by. Keys are field names and values are the values to filter by.
            boost_dict (dict): Dictionary of boost scores for text fields. Keys are field names and values are the boost scores.
            num_results (int): The number of top results to return. Defaults to 10.

        Returns:
            list of dict: List of documents matching the search criteria, ranked by relevance.
        """
        query_vecs = {field: self.vectorizers[field].transform([query]) for field in self.text_fields}
        scores = np.zeros(len(self.docs))

        # Compute cosine similarity for each text field and apply boost
        for field, query_vec in query_vecs.items():
            sim = cosine_similarity(query_vec, self.text_matrices[field]).flatten()
            boost = boost_dict.get(field, 1)
            scores += sim * boost

        # Apply keyword filters
        for field, value in filter_dict.items():
            if field in self.keyword_fields:
                mask = self.keyword_df[field] == value
                scores = scores * mask.to_numpy()

        # Use argpartition to get top num_results indices
        top_indices = np.argpartition(scores, -num_results)[-num_results:]
        top_indices = top_indices[np.argsort(-scores[top_indices])]

        # Filter out zero-score results
        top_docs = [self.docs[i] for i in top_indices if scores[i] > 0]

        return top_docs



class VectorSearch:
    """
    A vector search index using cosine similarity for vector search and exact matching for keyword fields.
    
    Takes a 2D numpy array of vectors and a list of payload documents, providing efficient
    similarity search with keyword filtering and boosting capabilities.
    """
    
    def __init__(self, keyword_fields):
        """
        Initialize the VectorSearch index.
        
        Args:
            keyword_fields (list): List of keyword field names to index for exact matching.
        """
        self.keyword_fields = keyword_fields
        self.vectors = None  # 2D numpy array of vectors
        self.keyword_df = None  # DataFrame containing keyword field data
        self.docs = []  # List of documents (payload)
        
    def fit(self, vectors, payload):
        """
        Fits the index with the provided vectors and payload documents.
        
        Args:
            vectors (np.ndarray): 2D numpy array of shape (n_docs, vector_dimension).
            payload (list of dict): List of documents to use as payload. Each document is a dictionary.
        """
        if len(vectors) != len(payload):
            raise ValueError("Number of vectors must match number of payload documents")
            
        self.vectors = vectors
        self.docs = payload
        
        # Create keyword DataFrame
        keyword_data = {field: [] for field in self.keyword_fields}
        for doc in payload:
            for field in self.keyword_fields:
                keyword_data[field].append(doc.get(field, ''))
        self.keyword_df = pd.DataFrame(keyword_data)
        
        return self
        
    def search(self, query_vector, filter_dict=None, num_results=10, output_ids=False):
        """
        Searches the index with the given query vector and filters.
        
        Args:
            query_vector (np.ndarray): 1D numpy array of shape (vector_dimension,) for the query.
            filter_dict (dict): Dictionary of keyword fields to filter by. Keys are field names 
                              and values are the values to filter by.
            num_results (int): The number of top results to return. Defaults to 10.
            output_ids (bool): If True, adds an '_id' field to each document containing its index. 
                             Defaults to False.
            
        Returns:
            list of dict: List of documents matching the search criteria, ranked by relevance.
                         If output_ids is True, each document will have an additional '_id' field.
        """
        if filter_dict is None:
            filter_dict = {}
            
        if not self.docs or self.vectors is None:
            return []
            
        # Reshape query vector for cosine similarity
        query_vector_2d = query_vector.reshape(1, -1)
        
        # Compute cosine similarity
        scores = cosine_similarity(query_vector_2d, self.vectors).flatten()
        
        # Apply keyword filters
        for field, value in filter_dict.items():
            if field in self.keyword_fields:
                mask = self.keyword_df[field] == value
                scores = scores * mask.to_numpy()
        
        # Get number of non-zero scores
        non_zero_mask = scores > 0
        non_zero_count = np.sum(non_zero_mask)
        
        if non_zero_count == 0:
            return []
            
        # Ensure num_results doesn't exceed the number of non-zero scores
        num_results = min(num_results, non_zero_count)
        
        # Get indices of non-zero scores
        non_zero_indices = np.where(non_zero_mask)[0]
        
        # Sort non-zero scores in descending order
        sorted_indices = non_zero_indices[np.argsort(-scores[non_zero_indices])]
        
        # Take top num_results
        top_indices = sorted_indices[:num_results]
        
        # Return corresponding documents
        if output_ids:
            return [{**self.docs[i], '_id': int(i)} for i in top_indices]
        return [self.docs[i] for i in top_indices] 