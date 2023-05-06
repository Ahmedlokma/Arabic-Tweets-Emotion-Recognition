import os
import csv

# Path to the directory containing the txt files
dir_path = '/Users/ahmedlokma/Desktop/neg'


# Output CSV file name
output_file = 'output.csv'

# Determine if file exists
file_exists = os.path.isfile(os.path.join(dir_path, output_file))

# Open output CSV file in append mode if it exists, otherwise create it
with open(output_file, 'a', newline='') as f:
    writer = csv.writer(f)

    # Add column header row if file does not exist
    if not file_exists:
        writer.writerow(['sentence', 'sentiment'])

    # Loop through all txt files in directory
    for filename in os.listdir(dir_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(dir_path, filename)

            # Open the txt file and read the sentence
            with open(filepath, 'r') as txt_file:
                sentence = txt_file.read().strip()

                # Write the sentence and sentiment to the output CSV file
                writer.writerow([sentence, 'positive'])

# Print the output file path
print(f"Output file path: {os.path.join(dir_path, output_file)}")