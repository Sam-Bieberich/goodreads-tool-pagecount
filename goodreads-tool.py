#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
import os


####################DEFINITIONS########################
# Filters the CSV to make it so that only the books that are in a unique bookshelf will be in the new file 
def filter_csv(file_path):
    # Read the CSV file
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Remove the first row (header)
        header = next(csv_reader)
        
        # Find the index of the 17th column (assuming 0-based index)
        column_17_index = 16
        
        # Filter rows with string value in the 17th column and not in the exclusion list
        filtered_rows = [row for row in csv_reader if len(row) > column_17_index 
                                                    and isinstance(row[column_17_index], str)
                                                    and row[column_17_index].lower() not in ["read", "to-read", "currently-reading"]
                                                    and row[column_17_index] != ""]  # Exclude empty string
    
    # Create the path for the filtered file using os.path
    filtered_file_path = os.path.join(os.path.dirname(file_path), 'filtered_' + os.path.basename(file_path))
    
    # Write the filtered data back to the CSV file
    with open(filtered_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write the filtered rows
        csv_writer.writerows(filtered_rows)

        
def create_dictionary_from_csv(csv_file_path):
    data_dict = {}

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) >= 17 and len(row) >= 12:  # Ensure columns exist
                key = row[16]  # 17th column
                value = int(row[11])  # 12th column

                if key in data_dict:
                    data_dict[key] += value
                else:
                    data_dict[key] = value

    return data_dict

######################FILL IN#############################
# Read the CSV again and make a dictionary
csv_file_path = 'fill in the filepath here'
filter_csv(csv_file_path)

result_dict = create_dictionary_from_csv(csv_file_path)

print(result_dict)



# In[ ]:




