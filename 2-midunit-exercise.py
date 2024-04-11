# Author: Lakshya Rai   

def calculate_rectangle_area(length, width):
    area = length * width
    return area

def print_even_numbers_up_to(n):
    print("Even numbers up to", n, ":")
    for i in range(2, n + 1, 2):
        print(i)

def countdown(start):
    print("Countdown from", start, ":")
    while start > 0:
        print(start)
        start -= 1
        if start == 0:
            print("Blast off!")

if __name__ == "__main__":
    length = 5
    width = 3
    area = calculate_rectangle_area(length, width)
    print("Area of rectangle with length", length, "and width", width, "is:", area)

    n = 10
    print_even_numbers_up_to(n)

    start = 5
    countdown(start)

