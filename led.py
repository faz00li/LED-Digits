import sys
################################################################################
#   LED representations of binary digits.
#   Dictionary of LED digits
################################################################################
zero = [
    ["#", "#", "#"],
    ["#", " ", "#"],
    ["#", " ", "#"],
    ["#", " ", "#"],
    ["#", "#", "#"]
]

one = [
    [" ", " ", "#"],
    [" ", " ", "#"],
    [" ", " ", "#"],
    [" ", " ", "#"],
    [" ", " ", "#"]
]

dig_dic = { 0: zero, 1: one }

################################################################################
#  LED related functions
################################################################################
def printDigit(digit: list):
    for i in range(5):
        print(digit[i])
    print()

################################################################################
#   Obtain binary number in the form of a string from the CLI.
#   Validate input.
################################################################################
args = sys.argv[1]
if args.isdigit() == False:
    print("Binary number must consist of 0 and 1s.")
    exit(0)

print("The binary number is: ", args)
digits = []
for c in args:
    digits.append(int(c))

print("The parsed binary number as a list is: ", digits)

led_digits = []
for i in range(len(digits)):
    x = tuple(dig_dic[digits[i]])
    led_digits.append(x)

print(led_digits)

segment = ""
line = ""

rank = 0
for rank in range(5):
    print("Number of digits: ", len(digits))
    for i in range(len(digits)):
        x = led_digits[i][rank]
        print(x)
        segment = segment + line.join(x)
    print(segment)
    print()
    segment = ""
    line = ""

# rank = 1
# for i in range(len(digits)):
#     print(led_digits[i][rank], end=".")
# print()

# rank = 2
# for i in range(len(digits)):
#     print(led_digits[i][rank], end=".")
# print()






################################################################################
#   Program Execution
################################################################################


# Parse args - seperate each character

