import os
import json
import sys
from datetime import datetime

class SubjectInfo:
    def __init__(self):
        self.name = None
        self.dob = None
        self.hand = None
        self.hand_type = None
        self.subjects_dir = "subjects"  # Directory where files will be saved and loaded from

        # Ensure the 'subjects' directory exists
        if not os.path.exists(self.subjects_dir):
            os.makedirs(self.subjects_dir)

    def get_missing_fields(self):
        """Return a list of missing fields."""
        missing_fields = []
        if not self.name:
            missing_fields.append("Name")
        if not self.dob:
            missing_fields.append("Date of Birth")
        if not self.hand:
            missing_fields.append("Dominant Hand")
        if not self.hand_type:
            missing_fields.append("Hand Type")
        return missing_fields

    def generate_filename(self):
        """Generate the filename in the format: name_date_of_birth.json, replacing spaces with underscores."""
        if self.name and self.dob:
            # Replace spaces in the name with underscores
            name_with_underscores = self.name.replace(" ", "_")
            # Format the filename
            dob_formatted = self.dob.replace("-", "")  # Remove hyphens from the DOB for the filename
            filename = f"{name_with_underscores}_{dob_formatted}.json"
            return filename
        return None

    def check_if_file_exists(self, filename):
        """Check if the file exists and handle renaming if necessary."""
        file_path = os.path.join(self.subjects_dir, filename)
        if os.path.exists(file_path):
            # Ask user if they want to overwrite or create a new file with a number suffix
            while True:
                overwrite = input(f"\nThe file {filename} already exists. Do you want to overwrite it? (y/n): ").lower()
                if overwrite == 'y':
                    return file_path  # Overwrite the file
                elif overwrite == 'n':
                    # Create a new file name with _1, _2, etc.
                    i = 1
                    new_filename = filename.replace(".json", f"_{i}.json")
                    new_file_path = os.path.join(self.subjects_dir, new_filename)
                    while os.path.exists(new_file_path):
                        i += 1
                        new_filename = filename.replace(".json", f"_{i}.json")
                        new_file_path = os.path.join(self.subjects_dir, new_filename)
                    return new_file_path
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        else:
            return file_path  # No file exists, so we can create it

    def save_to_file(self, filename=None):
        """Save subject information to a JSON file."""
        missing_fields = self.get_missing_fields()
        
        if missing_fields:
            print("\nMissing Information: Cannot save the file.")
            for field in missing_fields:
                print(f"- {field}")
            return  # Don't proceed with saving if any field is missing

        # Generate the filename if not passed
        if not filename:
            filename = self.generate_filename()

        if filename:
            # Check if the file already exists and decide whether to overwrite or create a new one
            file_path = self.check_if_file_exists(filename)

            # Prepare data for saving
            json_output = self.generate_json()
            if json_output:
                try:
                    # Save the JSON data to the chosen file
                    with open(file_path, 'w') as f:
                        f.write(json_output)
                    print(f"\nSubject information has been saved to {file_path}")
                except IOError as e:
                    print(f"An error occurred while saving the file: {e}")
            else:
                print("\nError: Unable to generate JSON output.")
        else:
            print("\nError: Cannot generate a filename. Make sure name and date of birth are entered.")

    def generate_json(self):
        """Generate a JSON representation of the subject's information."""
        if self.name and self.dob and self.hand and self.hand_type:
            # Calculate age
            age = self.calculate_age()

            # Create a dictionary for the JSON output
            output_data = {
                "name": self.name,
                "date_of_birth": self.dob,
                "age": age if age is not None else "Unknown",
                "left_handed": self.is_left_handed(),
                "hand_type": self.hand_type
            }

            # Convert dictionary to JSON format and return
            return json.dumps(output_data, indent=4)
        else:
            return None

    def calculate_age(self):
        """Calculate age based on date of birth."""
        if self.dob:
            dob_date = datetime.strptime(self.dob, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
            return age
        return None

    def is_left_handed(self):
        """Return if the subject is left-handed."""
        return self.hand == 'left'

    def input_name(self):
        """Input the name of the subject."""
        self.name = input("\nEnter the name of the subject: ")

    def input_date_of_birth(self):
        """Input the date of birth of the subject."""
        self.dob = input("\nEnter the date of birth (YYYY-MM-DD): ")

    def select_hand(self):
        """Input the dominant hand (left or right)."""
        while True:
            hand = input("\nIs the subject left-handed or right-handed? (left/right): ").lower()
            if hand in ['left', 'right']:
                self.hand = hand  # Store the hand in the subject object
                return
            else:
                print("Invalid input. Please enter 'left' or 'right'.")

    def select_hand_type(self):
        """Select the hand type (fire, water, earth, air)."""
        hand_types = ['fire', 'water', 'earth', 'air']
        while True:
            hand_type = input("\nSelect the hand type (fire, water, earth, air): ").lower()
            if hand_type in hand_types:
                self.hand_type = hand_type  # Store the hand type in the subject object
                return
            else:
                print("Invalid input. Please choose from 'fire', 'water', 'earth', or 'air'.")

    def display_information(self):
        """Display the entered subject information and show missing fields."""
        print("\nSubject Information:")
        
        # Display entered information
        print(f"Name: {self.name if self.name else 'Not entered'}")
        print(f"Date of Birth: {self.dob if self.dob else 'Not entered'}")
        print(f"Dominant Hand: {self.hand.capitalize() if self.hand else 'Not entered'}")
        print(f"Hand Type: {self.hand_type.capitalize() if self.hand_type else 'Not entered'}")
        
        # Get the missing fields using the common method
        missing_fields = self.get_missing_fields()
        
        # Display the missing fields
        if missing_fields:
            print("\nMissing Information:")
            for field in missing_fields:
                print(f"- {field}")
        else:
            print("\nAll information has been entered.")

    def show_menu(self):
        """Show the main menu with options."""
        print("#" * 40)
        print("#" + " " * 12 + "Hand Analysis Data Entry" + " " * 12 + "#")
        print("#" * 40)
        print("#" + " " * 4 + "Please choose an option from the menu below:" + " " * 4 + "#")
        print("#" * 40)
        print("# 1. Enter Name                          #")
        print("# 2. Enter Date of Birth                 #")
        print("# 3. Select Hand (Left or Right)         #")
        print("# 4. Select Hand Type (Fire, Water, Earth, Air) #")
        print("# 5. Display Information                 #")
        print("# 6. Generate JSON Output                #")
        print("# 7. Save Information to File            #")
        print("# 8. Load Information from File          #")
        print("# 9. Show All Subjects                   #")
        print("# 10. Exit                               #")
        print("#" * 40)

    def clear_screen(self):
        """Clear the screen depending on the OS."""
        if sys.platform == "win32":  # For Windows
            os.system("cls")
        else:  # For macOS and Linux
            os.system("clear")

    def load_from_file(self, filename):
        """Load subject information from a JSON file."""
        try:
            file_path = os.path.join(self.subjects_dir, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.name = data.get("name")
                self.dob = data.get("date_of_birth")
                self.hand = data.get("left_handed")
                self.hand_type = data.get("hand_type")
                print(f"\nSuccessfully loaded information from {file_path}")
        except FileNotFoundError:
            print(f"\nError: The file {filename} was not found.")
        except json.JSONDecodeError:
            print("\nError: The file could not be parsed as JSON. Please check the file format.")
        except KeyError as e:
            print(f"\nError: Missing expected key in the loaded file: {e}")

    def show_all_subjects(self):
        """List all subject files in the 'subjects' directory."""
        try:
            files = os.listdir(self.subjects_dir)
            json_files = [f for f in files if f.endswith('.json')]

            if not json_files:
                print("\nNo subject files found in the directory.")
                return

            print("\nList of Subjects:")
            for idx, file in enumerate(json_files, 1):
                print(f"{idx}. {file.replace('.json', '')}")

            # Select a subject to load
            try:
                choice = int(input("\nSelect a subject file to load (enter the number): "))
                if 1 <= choice <= len(json_files):
                    selected_file = json_files[choice - 1]
                    self.load_from_file(selected_file)
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"\nError occurred: {e}")


# Main program loop
def main():
    subject = SubjectInfo()
    
    while True:
        subject.show_menu()
        choice = input("\nSelect an option: ")

        if choice == '1':
            subject.input_name()
        elif choice == '2':
            subject.input_date_of_birth()
        elif choice == '3':
            subject.select_hand()
        elif choice == '4':
            subject.select_hand_type()
        elif choice == '5':
            subject.display_information()
        elif choice == '6':
            subject.generate_json()
        elif choice == '7':
            subject.save_to_file()
        elif choice == '8':
            filename = input("\nEnter the filename to load (e.g., JohnDoe_19900101.json): ")
            subject.load_from_file(filename)
        elif choice == '9':
            subject.show_all_subjects()
        elif choice == '10':
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice, please try again.")

        input("\nPress any key to continue...")
        subject.clear_screen()

if __name__ == "__main__":
    main()

