import pandas as pd
import os

input_directory = 'C:/Users/Tejas/Desktop/project/CSV_Files'  # Replace with your actual directory path

output_directory = './cleaned.csv'  # Output directory for cleaned files

# Make sure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to clean CSV files
def clean_csv(input_file, output_file):
    try:
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file)
        
        # Remove rows with missing values (NaN) in any column
        df.dropna(inplace=True)
        
        # Drop any unnecessary columns (example: 'Unnamed: 0' for index column)
        df.drop(columns=['Unnamed: 0'], errors='ignore', inplace=True)
        
        # Convert specific columns to the correct data types (example: 'Age' to integer)
        if 'Age' in df.columns:
            df['Age'] = df['Age'].astype(int)
        
        # Save the cleaned DataFrame to a new CSV file
        df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to: {output_file}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Main function to clean all CSV files in the input directory
def clean_all_csv_files():
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, filename)
            clean_csv(input_file, output_file)

if __name__ == "__main__":
    clean_all_csv_files()
