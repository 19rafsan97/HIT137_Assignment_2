# Github repository: https://github.com/19rafsan97/HIT137_Assignment_2

import pandas as pd
import argparse

# Function to process CSV files and write to a text file
def process_csv_files(csv_files, output_file):
    """
    Processes a list of CSV files, extracts the content from the 'TEXT' column
    (or 'SHORT-TEXT' column renamed to 'TEXT'), and writes the extracted text 
    into a specified output text file.

    Parameters:
    -----------
    csv_files : list of str
        A list of file paths for the CSV files to be processed.

    output_file : str
        The file path for the output text file where the extracted text will be written.

    """
    # Open a new .txt file to write the content
    with open(output_file, 'w') as txt_file:
        for csv_file in csv_files:
            # Read the CSV file
            df = pd.read_csv(csv_file, low_memory=False)

            # Check for 'SHORT-TEXT' column and rename it to 'TEXT' for consistency
            if 'SHORT-TEXT' in df.columns:
                df.rename(columns={'SHORT-TEXT': 'TEXT'}, inplace=True)

            # Extract the 'TEXT' column and write each row to the .txt file
            if 'TEXT' in df.columns:
                for text in df['TEXT']:
                    txt_file.write(str(text) + '\n')
            else:
                print(f"Column 'TEXT' not found in {csv_file}")

# Main function to handle argument parsing
def main():
    parser = argparse.ArgumentParser(description="Process CSV files and extract text content.")
    parser.add_argument('--csv1', required=True, help="First CSV file")
    parser.add_argument('--csv2', required=True, help="Second CSV file")
    parser.add_argument('--csv3', required=True, help="Third CSV file")
    parser.add_argument('--csv4', required=True, help="Fourth CSV file")
    parser.add_argument('--output', type=str, default='question_1/output_text.txt', help="Output text file (default: output_text.txt)")

    args = parser.parse_args()

    # Create a list of the CSV files from the arguments
    csv_files = [args.csv1, args.csv2, args.csv3, args.csv4]

    # Call the processing function
    process_csv_files(csv_files, args.output)

if __name__ == "__main__":
    main()
