def add_patient(patients):
    print("Adding a new patient...")
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    
    patient = {
        'name': name,
        'age': age,
        'illness': illness
    }
    
    patients.append(patient)
    print(f"Patient '{name}' added successfully!\n")


def display_all(patients):
    print("\nList of all patients:")
    if patients:
        for index, patient in enumerate(patients, start=1):
            print(f"{index}. Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
    else:
        print("No patients in the list.\n")


def search_patient(patients):
    search_name = input("Enter patient's name to search: ")
    found = False
    for patient in patients:
        if patient['name'].lower() == search_name.lower():
            print("\nPatient found. Details:")
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}\n")
            found = True
            break
    if not found:
        print(f"Patient with name '{search_name}' not found.\n")


def remove_patient(patients):
    remove_name = input("Enter patient's name to remove: ")
    removed = False
    for patient in patients:
        if patient['name'].lower() == remove_name.lower():
            patients.remove(patient)
            print(f"Patient '{remove_name}' removed successfully.\n")
            removed = True
            break
    if not removed:
        print(f"Patient with name '{remove_name}' not found.\n")


def main():
    patients = []
    
    while True:
        print("Hospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_all(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            remove_patient(patients)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
