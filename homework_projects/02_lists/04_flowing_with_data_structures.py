def add_three_copies(lst, data):
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    user_input = input("Enter a message to copy: ")
    my_list = []
    
    print(f"List before: {my_list}")
    add_three_copies(my_list, user_input)
    print(f"List after: {my_list}")

if __name__ == '__main__':
    main()
