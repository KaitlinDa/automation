import os
import shutil
from rich.console import Console

console = Console()

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        console.print(f"Folder '{folder_name}' created.", style="green")
    else:
        console.print(f"Folder '{folder_name}' already exists.", style="yellow")

def handle_deleted_user(user_folder, temp_folder):
    create_folder(temp_folder) 
    shutil.move(user_folder, temp_folder)
    console.print(f"Moved documents from '{user_folder}' to '{temp_folder}'.", style="purple")

def sort_documents(source_folder):
    docs_folder = os.path.join(source_folder, "documents")
    mail_folder = os.path.join(source_folder, "mail")
    logs_folder = os.path.join(source_folder, "logs")

    create_folder(docs_folder)
    create_folder(mail_folder)
    create_folder(logs_folder)

    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if file.endswith(".txt"):
            shutil.move(file_path, os.path.join(docs_folder, file))
        elif file.endswith(".mail"):
            shutil.move(file_path, os.path.join(mail_folder, file))
        elif file.endswith(".log"):
            shutil.move(file_path, os.path.join(logs_folder, file))
    console.print(f"Documents in '{source_folder}' sorted.", style="magenta")

def parse_log_file(log_folder):
    for log_file_name in os.listdir(log_folder):
        if log_file_name.endswith(".log"):
            log_file_path = os.path.join(log_folder, log_file_name)
            errors_path = os.path.join(log_folder, "errors.log")
            warnings_path = os.path.join(log_folder, "warnings.log")

            with open(log_file_path, 'r') as log_file, \
                open(errors_path, 'a') as errors_file, \
                open(warnings_path, 'a') as warnings_file:
                for line in log_file:
                    if "ERROR" in line:
                        errors_file.write(line)
                    elif "WARNING" in line:
                        warnings_file.write(line)
            console.print(f"Log file '{log_file_name}' parsed for errors and warnings.", style="red")

def main_menu():
    while True:
        console.print("\nTasks:", style="bold underline")
        console.print("1. Create new folder", style="bold")
        console.print("2. Handle deleted user 'user2'", style="bold")
        console.print("3. Sort documents in 'user1' and 'user2'", style="bold")
        console.print("4. Parse log file for errors and warnings in 'user1/logs' folder", style="bold")
        console.print("5. Exit", style="bold")
        choice = console.input("Enter your choice (1-5): ")

        if choice == '1':
            folder_name = console.input("Enter the name of the new folder: ")
            create_folder(folder_name)
        elif choice == '2':
            handle_deleted_user("user2", "temp")
        elif choice == '3':
            sort_documents("user1")
            sort_documents("user2")
        elif choice == '4':
            log_folder = "user1/logs"
            parse_log_file(log_folder)
        elif choice == '5':
            console.print("Exiting the application.", style="red")
            break
        else:
            console.print("Invalid choice. Please enter a number between 1-5.", style="red")

if __name__ == "__main__":
    main_menu()
