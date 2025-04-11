def main():
    number_count = {}  # Initialize an empty dictionary to store the count of each number

    while True:
        number = input("Enter a number: ")
        
        if number == "":  
            break
        
      
        number = int(number)
        
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1
    
    for number, count in number_count.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()
