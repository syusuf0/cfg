def calculate_classes(n_students):
    """
    Function to calculate and print the proposed number of classes and allocation.

    Parameters:
    n_students (int): The number of students.
    """
    # ensure a minimum of 2 classes
    n_classes = max(2, round(n_students / 30))

    # calculate the number of students in each class as evenly as possible
    students_per_class = n_students // n_classes
    remainder = n_students % n_classes

    # create the allocation dictionary
    allocation = {}
    for i in range(n_classes):
        allocation[f'Class {i + 1}'] = students_per_class + (i < remainder)

    print(f"Proposed Allocation: {n_classes} classes")
    print(allocation)


# example usage
calculate_classes(31)
calculate_classes(59)
calculate_classes(87)
