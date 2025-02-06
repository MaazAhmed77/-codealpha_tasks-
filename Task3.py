import os
import shutil

# Define file categories and their extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.ppt'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []
}

# Function to organize files
def organize_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist!")
        return

    # Create category folders if they don't exist
    for category in FILE_CATEGORIES:
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Walk through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Identify the file type based on its extension
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                # Move the file to the appropriate folder
                category_folder = os.path.join(directory, category)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved: {filename} -> {category}")
                moved = True
                break
        
        # If the file doesn't match any category, move it to 'Others'
        if not moved:
            shutil.move(file_path, os.path.join(directory, 'Others', filename))
            print(f"Moved: {filename} -> Others")

# Run the function
if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
