# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def print_hello(name):
    print(f'Hello, {name}'.title())


def merge_str(str1, str2):
    print(str1.title() + str2.upper())


def print_list(mags):
    for magician in mags:
        print(magician + ', that was a good trick!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hello('python')
    merge_str('hello, ', 'world')
    motors = ['honda', 'yamaha', 'suzuki']
    motor = motors.pop()
    print(motors)
    print_hi(motor)
    magicians = ['jimmy', 'tommy', 'jack']
    print_list(magicians)
    print(list(range(1, 16, 3)))
    squares = [value ** 3 for value in range(1, 11)]
    print(squares[-3:])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
