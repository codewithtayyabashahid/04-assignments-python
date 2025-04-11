def get_first_element(lst):
    print(f"The first element is: {lst[0]}")

def get_last_element(lst):
    print(f"The last element is: {lst[-1]}")

def main():
    num_elements = int(input("Enter the number of elements in the list: "))
    user_list = []
    
    for _ in range(num_elements):
        element = input("Enter an element: ")
        user_list.append(element)
    
    get_first_element(user_list)
    get_last_element(user_list)

if __name__ == '__main__':
    main()
