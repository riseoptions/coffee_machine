import os

# Define the project structure
project_structure = {
    "coffee_machine_project": [
        "main.py",
        "coffee_machine.py",
        "beverage.py",
        "ingredient_manager.py",
        {"tests": ["test_coffee_machine.py", "test_ingredient_manager.py"]}
    ]
}

# Function to create the project structure
def create_project_structure(base_path, structure):
    for folder, contents in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for item in contents:
            if isinstance(item, dict):  # If the item is a folder with contents
                create_project_structure(folder_path, item)
            else:  # If the item is a file
                file_path = os.path.join(folder_path, item)
                with open(file_path, 'w') as file:
                    pass  # Create an empty file

# Base path for the project
base_path = "./"

# Create the project structure
create_project_structure(base_path, project_structure)

"Project structure created successfully!"
