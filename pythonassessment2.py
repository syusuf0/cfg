def calculate_classes(n_students):
    """
    Function to calculate and print the proposed number of classes and allocation.

    Parameters:
    n_students (int): The number of students.
    """
    # makes sure there is  a minimum of 2 classes
    n_classes = max(2, round(n_students / 30))

    # making sure there is equal amount of student per class
    students_per_class = n_students // n_classes
    remainder = n_students % n_classes

    # construct an allocation dictionary
    allocation = {}
    for i in range(n_classes):
        allocation[f'Class {i + 1}'] = students_per_class + (i < remainder)

    print(f"Proposed Allocation: {n_classes} classes")
    print(allocation)


print("Script started")

# test inputs
calculate_classes(33)
calculate_classes(67)
calculate_classes(94)

print("Script ended")

