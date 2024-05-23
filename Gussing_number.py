import random

def display(nw_lwr_rng,nw_hgh_rng):
     num = random.randint(nw_lwr_rng,nw_hgh_rng)

     print("Guess in next 3 attempts")
     
     for i in range(3):
         Guess= int(input(f"Guess {i + 1}: "))
         if Guess == num:
             print("You Won!")
             break
         else:
            print("Oh! You Lost...")  
       
     print("Correct Guess is: ",num)   

def main():
    print("Welcome to Number Guessing Game")
    
    print("Lower range:")
    a = int(input())
    
    print("Higher range:")
    b = int(input())
    display(a, b)

if __name__ == "__main__":
    main()  