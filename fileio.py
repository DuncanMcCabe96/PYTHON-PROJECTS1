import os
import time

# Replace this with the path to your specific directory
directory = '/path/to/your/directory'

# Iterate through all items in the directory
for filename in os.listdir(directory):
    # Form the absolute path
    file_path = os.path.join(directory, filename)
    
    # Check if it is a file and ends with .txt
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        # Get the last modified time
        mtime = os.path.getmtime(file_path)
        
        # Format the mtime into a human-readable format
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        
        # Print the file name and modified time
        print(f"{filename} - Last Modified: {formatted_time}")

