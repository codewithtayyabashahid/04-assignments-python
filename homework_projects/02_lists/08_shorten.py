MAX_LENGTH = 3

def get_first_element(lst):
    print(f"The first element is: {lst[0]}")

def get_last_element(lst):
    print(f"The last element is: {lst[-1]}")

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def main():
    user_list = []
    while True:
        element = input("Enter a value: ")
        if element == "":
            break
        user_list.append(element)
    
    print(f"Here's the list: {user_list}")
    
    if user_list:
        get_first_element(user_list)
        get_last_element(user_list)
        shorten(user_list)
        print(f"Shortened list: {user_list}")

if __name__ == '__main__':
    main()