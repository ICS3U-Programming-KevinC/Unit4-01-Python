# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Nov. 11, 2022
# This program sums up all of the digits from 0 to the user input


def main():
    # initialize all required variables
    counter = 0
    sum = 0
    user_num_str = input("Please enter a positive integer: ")

    # check if the input is a valid integer
    try:
        user_num_int = int(user_num_str)
    except:
        print("Please enter a valid integer")
    else:

        # check if the number is positive
        if user_num_int < 0:
            print("Please enter a positive integer")
        else:

            # repeats until counter is counter is greater than the input
            while counter <= user_num_int:

                # adds counter to the sum
                sum += counter

                # increment counter by 1
                counter += 1

                # tell the user hoe many times the code runs through the loop
                print(f"Tracking through the loop {counter} times")

            # output the result of the program
            print(f"The sum of all numbers from 0 to {user_num_int} is {sum}")


if __name__ == "__main__":
    main()
