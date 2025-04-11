import random

DONE_LIKELIHOOD = 0.2  # 20% chance to stop early

def done():
    """Returns True with likelihood DONE_LIKELIHOOD, simulating an early stop condition."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():  
            return  
        print(i, end=" ")  

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  
    print("\nI'm done.")  


if __name__ == '__main__':
    main()
