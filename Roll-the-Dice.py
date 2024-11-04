import numpy as np

dice = [1, 2, 3, 4, 5, 6]

def roll_the_dice(rows, cells):
    return np.random.choice(dice, size=(rows, cells))

def count_occurrences(matrix, number):
    indices = np.where(matrix == number)
    return list(zip(indices[0], indices[1]))

def find_min_max(matrix):
    return np.min(matrix), np.max(matrix)

def print_menu():
    print("what do you need to do?\n\t1-Calculate the number of each number in the dice\n\t2-min and max of all roll the dices\n\t3-print Matrix of rolled dice\n\t4-change matrix\n\t5-exit") 

def main():
    rows = int(input("please enter your rows :"))
    cells = int(input("please enter your cells :"))
    matrix_dice = roll_the_dice(rows, cells)

    while True:
        print_menu()
        try:
            user_choice = int(input("enter your choice's number:"))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if user_choice == 1:
            try:
                number = int(input("enter a number:"))
                indices = count_occurrences(matrix_dice, number)
                if indices:
                    print("Occurrences at positions:", indices)
                else:
                    print(f"No occurrences of {number} found.")
            except ValueError:
                print("Invalid number, try again.")
                
        elif user_choice == 2:
            matrix_min, matrix_max = find_min_max(matrix_dice)
            print(f"Minimum value in matrix: {matrix_min}")
            print(f"Maximum value in matrix: {matrix_max}")

        elif user_choice == 3:
            print(f"Your matrix:\n{matrix_dice}")
            
        elif user_choice == 4:
            rows = int(input("please enter new rows:"))
            cells = int(input("please enter new cells:"))
            matrix_dice = roll_the_dice(rows, cells)
            print(f"Your new matrix:\n{matrix_dice}")
            
        elif user_choice == 5:
            print("Exiting program. Good Luck!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()