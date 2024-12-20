#!/usr/bin/env python
import sys
import warnings
import os
from typing import List

from code_doc_ai.crew import CodeDocAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

print('Hi, please select the programming language to scan:')
print('1. Visual Basic')
print('2. C#') 
print('3. Java')
print('4. Python')

while True:
    try:
        choice = int(input('Enter your choice (1-4): '))
        if choice == 1:
            scaning_code = 'Visual Basic'
            covert_from = 'vb'
        elif choice == 2:
            scaning_code = 'C#'
            covert_from = 'cs' 
        elif choice == 3:
            scaning_code = 'Java'
            covert_from = 'java'
        elif choice == 4:
            scaning_code = 'Python'
            covert_from = 'py'
        else:
            print('Invalid choice. Please try again.')
            continue
        break
    except ValueError:
        print('Please enter a valid number.')

print(f'\nYou selected {scaning_code} (.{covert_from})')

print('\nPlease select the language to convert to:')
print('1. C#')
print('2. Java') 
print('3. Python')

while True:
    try:
        choice = int(input('Enter your choice (1-3): '))
        if choice == 1:
            covert_type = 'C#'
            covert_to = 'cs'
        elif choice == 2:
            covert_type = 'Java'
            covert_to = 'java'
        elif choice == 3:
            covert_type = 'Python' 
            covert_to = 'py'
        else:
            print('Invalid choice. Please try again.')
            continue
        break
    except ValueError:
        print('Please enter a valid number.')

print(f'\nYou selected {covert_type} (.{covert_to})')

def get_files_to_scan(directory: str) -> List[str]:
    f"""Get all {covert_from} files from the directory."""
    scaned_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(f'.{covert_from}'):
                scaned_files.append(os.path.join(root, file))
    return scaned_files

def display_file_menu(files: List[str]) -> str:
    """Display a menu of files and get user selection."""
    print(f"\nAvailable {covert_from} files:")
    print("0. Convert all files")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    while True:
        try:
            choice = int(input(f"\nEnter the number of the file to convert (0 for all files): "))
            if 0 <= choice <= len(files):
                return files[choice - 1] if choice > 0 else "all"
            print(f"Invalid selection. Please try again.")
        except ValueError:
            print(f"Please enter a valid number.")

def run():
    f"""
        Run the crew to scan app-for-scanning application and convert it to {covert_type} code then save it to output-app directory.
    """
    scan_directory = 'app-for-scanning'
    scaned_files = get_files_to_scan(scan_directory)
    
    if not scaned_files:
        print(f"No {covert_from} files found in {scan_directory}")
        return
    
    selected_file = display_file_menu(scaned_files)
    
    inputs = {
        'scan_directory': 'app-for-scanning',
        'code_directory': 'output-app',
        'covert_from': f'{scaning_code} (.{covert_from})',
        'covert_type': f'{covert_type} (.{covert_to})',
        'selected_file': selected_file,
        'covert_to': covert_to
    }
    
    crew_ai = CodeDocAi(inputs=inputs)
    crew_ai.crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
