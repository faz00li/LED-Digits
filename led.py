import sys
from ledigits import zero, one, two, three, four, five, six, seven, eight, nine

ledig_dic = { 0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine }

################################################################################
#  LED related functions
################################################################################
def printDigit(digit: list):
    for i in range(5):
        print(digit[i])
    print()

################################################################################
#   Obtain number in the form of a string from the CLI.
#   Validate input.
################################################################################
args = sys.argv[1]
if args.isdigit() == False:
    print("Number must consist of digits 0 to 9.")
    exit(0)

print("The number is: ", args)
digits = []
# Turn string digits to integers in list in order to use led dictionary
for c in args: 
    digits.append(int(c))

print("The parsed number as a list is: ", digits)

################################################################################
#   Program Execution
#   Create list of digits as tuples
################################################################################
led_digits = []
for i in range(len(digits)):
    x = tuple(ledig_dic[digits[i]])
    led_digits.append(x)

segment = ""
line = ""

print("Number of digits: ", len(digits))
for rank in range(5):
    for i in range(len(digits)):
        x = led_digits[i][rank]
        segment = segment + " " + str(x).strip("[']")
    print(segment)
    segment = ""
    line = ""


