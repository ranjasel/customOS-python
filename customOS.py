import json
import time

files = {}
SAVE_PATH = "files.json"

def normalize_filename(name):
    # Returns a cleaned filename, or None if invalid.
    name = name.strip().lower()
    if not name or name.startswith(".") or name.strip(".") == "":
        return None
    if not name.endswith(".txt"):
        name += ".txt"
    return name

def load_file():
    try:
        with open(SAVE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_file():
    with open(SAVE_PATH, "w") as f:
            json.dump(files, f)

def create_file():
    while True:
        create_file_name = normalize_filename(input("\nEnter file name (without .txt): ")) # get file name

        if create_file_name is None: # invalid file name
            time.sleep(0.5)
            print("Invalid file name, retry")
            continue

        elif create_file_name in files: # check if file already exists
            print("File name already exists, retry.")
            continue

        # create file
        files[create_file_name] = ""
        save_file()
        break
    
    # confirmation message
    time.sleep(0.5)
    print(f"File '{create_file_name}' has been created successfully.") 

def write_file():
    while True:
        if not files: # check if any file exists
            time.sleep(0.25)
            print("No files available. Create a file first.")
            return

        print("\nAvailable files:") 
        for file in files: # print name of avail. files
            time.sleep(0.2)
            print(f"» {file}")

        write_file_choose = normalize_filename(input("\nEnter file name (without .txt): "))

        if write_file_choose is None: # invalid file name
            time.sleep(0.5)
            print("Invalid file name, retry")
            continue

        if write_file_choose in files: # check if file exists
            time.sleep(0.5)
            print(f"File '{write_file_choose}' found.")

            append_or_rewrite = input("\nWould you like to rewrite or add content (add/rewrite): ").lower().strip() # check user choice

            if append_or_rewrite == "rewrite":
                time.sleep(0.5)
                add_file_content = input("Enter content to be added (WARNING: This will replace old content.): ") # get content
                files[write_file_choose] = add_file_content # replace content

                time.sleep(0.5)
                save_file()
                print("Content rewritten successfully.")
                return
            
            elif append_or_rewrite == "add":
                add_file_content = input("Enter content to be added: ") # get content
                if files[write_file_choose]:
                    files[write_file_choose] += "\n" + add_file_content
                else:
                    files[write_file_choose] = add_file_content

                time.sleep(0.5)
                save_file()
                print("Content added successfully.")
                return
            
            else:
                time.sleep(0.25)
                print("Invalid command, retry.")
                continue               

        else:
            time.sleep(0.25)
            print("File doesn't exist, retry.")
            continue

def view_file():
    while True:
        if not files: # check if any file exists
            time.sleep(0.25)
            print("No files available. Create a file first.")
            return

        print("Available files:") 
        for file in files: # print name of avail. files
            time.sleep(0.2)
            print(f"» {file}")

        view_file_choose = normalize_filename(input("\nEnter file name (without .txt): "))

        if view_file_choose is None: # invalid file name
            time.sleep(0.5)
            print("Invalid file name, retry")
            continue

        if view_file_choose in files: # check if file exists
            time.sleep(0.5)
            print(f"File '{view_file_choose}' found.") 
            time.sleep(0.25)
            print(f"\n--- {view_file_choose} ---")
            if files[view_file_choose]:
                print(files[view_file_choose]) # print file content
            else:
                print("Empty file")
            print("----------------------")

            input("\nEnter to continue.")
            return
        
        else:
            print("File not found, retry.")
            continue

def delete_file():
    while True:
        if not files: # check if any file exists
            time.sleep(0.25)
            print("No files available. Create a file first.")
            return

        print("Available files:") 
        for file in files: # print name of avail. files
            time.sleep(0.2)
            print(f"» {file}")

        delete_file_choose = normalize_filename(input("\nEnter file name (without .txt): "))

        if delete_file_choose is None: # invalid file name
            time.sleep(0.5)
            print("Invalid file name, retry")
            continue

        if delete_file_choose in files: # check if file exists
            time.sleep(0.5)
            print(f"File '{delete_file_choose}' found.") 

            delete_yes_no = input(f"\nWould you like to delete '{delete_file_choose}'? (yes/no): ").lower().strip()
            if delete_yes_no == "yes":
                del files[delete_file_choose]
                time.sleep(0.5)
                save_file()
                print(f"File '{delete_file_choose}' has been deleted successfully.")
                return
            elif delete_yes_no == "no":
                input("Press Enter to cancel deletion.")
                return
            else:
                print("Invalid option, retry.")
                continue

        else:
            time.sleep(0.25)
            print("Invalid file name, retry.")
            continue

files = load_file()

print("Welcome to CustomOS")

while True:
    time.sleep(0.5)
    print("\n==file management== \n1. create file\n2. write content\n3. view file\n4. delete file\n5. exit program".title())
    time.sleep(0.5)
    user_input = input("\nWhat would you like to do: ").strip().lower()

    if user_input in ["1","create","create file"]:
        create_file()

    elif user_input in ["2" , "write" , "write file"]:
        write_file()

    elif user_input in ["3" , "view" , "view file"]:
        view_file()
        
    elif user_input in ["4" , "delete" , "delete file"]:
        delete_file()

    elif user_input in ["5" , "exit" , "exit program"]:
        break
    else:
        if not user_input:
            print("Empty Input, retry.")
            continue
        else:
            print("Invalid Option, retry.")
            continue

# exit
print("You've exited the program.")