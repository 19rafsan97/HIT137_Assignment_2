# Github repository: https://github.com/19rafsan97/HIT137_Assignment_2

import pandas as pd
from collections import Counter

# Read the text file
with open('output_text.txt', 'r') as file:
    text = file.read()

# Tokenize the text into words
words = text.split()

# Count occurrences of each word
word_counts = Counter(words)

# Get the Top 30 most common words
top_30_words = word_counts.most_common(30)

# Save the Top 30 words and counts into a CSV file
df_top_words = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
df_top_words.to_csv('question_1/top_30_words.csv', index=False)
