# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def printxtimes(loopNum, firstName, middleName, lastName, streetAddress, city):
    for y in range(loopNum):
        label = "Hi {} {} {} number {} lives on {} street in {} city."
        print(label.format(firstName, middleName, lastName, y, streetAddress, city))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loopNum = 50
    firstName = '1'
    middleName = '2'
    lastName = '3'
    streetAddress = "4"
    city = "6"
    printxtimes(loopNum, firstName, middleName, lastName, streetAddress, city)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
