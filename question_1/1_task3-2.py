# Github repository: https://github.com/19rafsan97/HIT137_Assignment_2

import csv
from transformers import AutoTokenizer
from collections import Counter

def count_unique_tokens_to_csv(file_path, output_csv):
    """
    Tokenizes the text from a file using a pre-trained AutoTokenizer from the
    'transformers' library, counts the frequency of each unique token, and writes
    the top 30 most frequent tokens along with their counts to a CSV file.

    Args:
    file_path (str): The path to the text file containing the input text.
    output_csv (str): The path where the output CSV file will be written.

    The output CSV file will contain two columns:
    1. Token: The token (word or sub-word unit).
    2. Count: The frequency of the token in the input text.
    """
    
    # Load pre-trained tokenizer (you can use any relevant model)
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    
    # Read the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count the frequency of each token
    token_counts = Counter(tokens)

    # Get the top 30 most frequent tokens
    top_30_tokens = token_counts.most_common(30)

    # Write the top 30 tokens and their counts to a CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Token', 'Count'])  # Header row
        writer.writerows(top_30_tokens)  # Write tokens and their counts

# Example usage
file_path = 'question_1/output_text.txt'
output_csv = 'question_1/top_30_tokens.csv'
count_unique_tokens_to_csv(file_path, output_csv)
