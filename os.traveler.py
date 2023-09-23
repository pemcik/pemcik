
import os

def traverse_directory(directory):
    for root, subdirectories, files in os.walk(directory):
        print(f"Current Directory: {root}")

        # Print all files in the current directory
        for file in files:
            print(f"File: {file}")

        # Print all subdirectories in the current directory
        for subdirectory in subdirectories:
            print(f"Directory: {subdirectory}")

if __name__ == "__main__":
    directory_to_traverse = input("Enter the directory path to traverse: ")
    traverse_directory(directory_to_traverse)