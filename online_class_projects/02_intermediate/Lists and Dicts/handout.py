# Problem #1: List Practice

def list_practice():
    # Create a list called `fruit_list` that contains the following fruits:
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list.
    print("Length of the fruit list:", len(fruit_list))

    fruit_list.append('mango')
    print("Updated fruit list:", fruit_list)

if __name__ == "__main__":
    list_practice()

    # Problem #2: Index Game

def access_element(data_list, index):
    """Accesses and returns the element at the specified index in a list.

    Args:
        data_list: The list to access.
        index: The index of the element to retrieve.

    Returns:
        The element at the specified index, or an error message if the index is out of range.
    """
    if 0 <= index < len(data_list):
        return data_list[index]
    else:
        return "Error: Index out of range."

def modify_element(data_list, index, new_value):
    """Modifies the element at the specified index in a list.

    Args:
        data_list: The list to modify.
        index: The index of the element to replace.
        new_value: The new value to assign to the element.

    Returns:
        The updated list, or an error message if the index is out of range.
    """
    if 0 <= index < len(data_list):
        data_list[index] = new_value
        return data_list
    else:
        return "Error: Index out of range."

def slice_list(data_list, start_index, end_index):
    """Slices a list and returns a new list containing elements within the specified range.

    Args:
        data_list: The list to slice.
        start_index: The starting index (inclusive).
        end_index: The ending index (exclusive).

    Returns:
        A new list containing the sliced elements, or an appropriate message if indices are invalid.
    """
    if start_index < 0:
        start_index = 0
    if end_index > len(data_list):
        end_index = len(data_list)

    if start_index >= end_index:
        return "Result: Empty slice (start index is greater than or equal to end index)."
    elif 0 <= start_index <= len(data_list) and 0 <= end_index <= len(data_list):
        return data_list[start_index:end_index]
    else:
        return "Error: Invalid start or end index."

def index_game():
    """A simple text-based game to practice list indexing and manipulation."""
    my_list = [10, "hello", 3.14, True, [1, 2]]
    print("\nWelcome to the Index Game!")
    print("Current list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                index = int(input("Enter the index to access: "))
                result = access_element(my_list, index)
                print("Element at index", index, ":", result)
            except ValueError:
                print("Invalid input. Please enter an integer for the index.")
        elif choice == '2':
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                updated_list = modify_element(my_list, index, new_value)
                if isinstance(updated_list, list):
                    my_list = updated_list
                    print("Updated list:", my_list)
                else:
                    print(updated_list)
            except ValueError:
                print("Invalid input. Please enter an integer for the index.")
        elif choice == '3':
            try:
                start_index = int(input("Enter the start index for slicing: "))
                end_index = int(input("Enter the end index for slicing: "))
                result = slice_list(my_list, start_index, end_index)
                print("Slice from", start_index, "to", end_index, ":", result)
            except ValueError:
                print("Invalid input. Please enter integers for the start and end indices.")
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    index_game()