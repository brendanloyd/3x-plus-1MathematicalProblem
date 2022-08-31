# python
# Brendan Loyd
# HomeWork 1 4500
# 08-25-2021
# External files: None

# this file explores the 3x + 1 mathematical problem using python.

# this function handles even case numbers. The function will divide the number by 2. Handling the case if the number is
# odd, until the number reaches one. Counting the steps along the way.
def even_case(number):
    count = 0
    print("We will divide x / 2(x is your number), printing results until we reach 1.")
    while number != 1:
        if number % 2 != 0:
            print("Odd number encountered, instead we will 3x + 1.")
            number = number * 3 + 1
            count += 1
            print("3x + 1 =", number)
        count += 1
        number = number / 2
        print("x / 2 =", number)
    print("Congrats! Your number has been reduced to", number, " in:", count, "steps.")
    input("Press Enter to continue...")


# this function handles odd case numbers. The function will multiply the number by 3 and add one. Handling the number
# when it becomes an even case and if it were to become odd again. Counting the steps along the way.
def odd_case(number):
    count = 0
    print("We will start my using 3x + 1(your number being x)")
    count += 1      # this portion is included to handle if the number is 1
    number = number * 3 + 1
    while number != 1:
        if number % 2 != 0:
            print("Odd number encountered, repeating 3x + 1")
            number = number * 3 + 1
            count += 1
            print("3x + 1 =", number)
        number = number / 2
        count += 1
        print("x / 2 =", number)
    print("Congrats! Your number has been reduced in:", count, "steps.")
    input("Press Enter to continue...")


# Very similar to the even and odd functions this function handles the array of numbers input my the user 
# and finds the shortest, longest, total and average run at the end.
def array_handling(my_array):
    shortest_run = 100000000
    longest_run = 0
    total_run = 0
    for x in my_array:  # cycling through the array
        count = 0
        if x == 1:  # this portion is included to handle if the number is 1
            x = x * 3 + 1
            count += 1
            total_run += 1
        while x != 1:
            if x % 2 != 0:
                x = x * 3 + 1
                count += 1
                total_run += 1
            else:
                x /= 2
                count += 1
                total_run += 1
        if count < shortest_run:
            shortest_run = count
        if count > longest_run:
            longest_run = count
    average_run = total_run / len(my_array)

    # printing results
    print("shortest run is", shortest_run)
    print("longest run is", longest_run)
    print("total run is", total_run)
    print("average run is", average_run)
    input("Press Enter to continue...")


# this is the main function that prompts the user with the menu, handles the different cases
# and calls supporting functions
def main():
    ans = True
    while ans:
        print("""
        Hello welcome to the program! In this program, for option 1 depending the number you enter, even or odd,
        I will either divide by 2 or multiply by 3 and add 1, respectively. Each time I will reevaluate the number
        and decide to, again, divide by 2 or multiply by 3 and add 1. The process will be recorded and displayed back
        to you. The goal is to determine how many steps it takes to reduce the number to 1. 
        Option 2 works similarly to option 1, however, you input a range of numbers and I find the shortest, longest, 
        total,and average count to display back to you. Enjoy!
        
        1. Designate a number to start the process.
        2. Designate a range of numbers to use with the process.
        3. Quit the program.
        """)
        choice = input()  # gets input from user
        if choice == "1":   # if choice is 1, the program will take a single number
            print("Enter an integer to start the process")
            while True:
                try:
                    number = int(input())
                    break
                except ValueError:
                    print("That was not an integer. try again.")
            if number % 2 == 0:
                even_case(number)
            else:
                odd_case(number)

        elif choice == "2":  # if choice is 2, the program will take in a range of numbers and store in an array
            print("Enter the smallest integer in the range.")
            while True:
                try:
                    small_int = int(input())
                    break
                except ValueError:
                    print("That was not an integer. try again.")
            print("Enter the largest integer in the range.")
            while True:
                try:
                    large_int = int(input())
                    break
                except ValueError:
                    print("That was not an integer. try again.")
            size = large_int - small_int
            int_array = []
            for x in range(size + 1):
                int_array.append(small_int)
                small_int = small_int + 1

            array_handling(int_array)

        elif choice == "3":  # if the choice is 3, it will exit the program. Making the user hit enter before exit
            ans = False  # message is displayed.
            input("Press Enter to continue...")
            print("you chose option 3. Have a good day!")
        else:
            print("Not a valid choice, please try again.")


# calls main to start the program.
main()
