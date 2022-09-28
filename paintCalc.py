from itertools import groupby


# retrieve and display header
def header():
    title = open("titlePC.txt", encoding="utf-8")
    print(title.read())
    title.close()


# validate integer or float inputs
def int_check(user_input, maxvalue, minvalue, varType):
    try:
        if varType == 'Float':
            user_input = float(user_input)
            if minvalue < user_input < maxvalue:
                return False
            else:
                print(f"Error: Number needs to be larger than 0 and smaller than {maxvalue}\n" + funky_line)
                return True
        if varType == 'Integer':
            user_input = int(user_input)
            if minvalue < user_input < maxvalue:
                return False
            else:
                print(f"Error: Number needs to be larger than 0 and smaller than {maxvalue}\n" + funky_line)
                return True
    except ValueError:
        print("Error: Please only input a number\n" + funky_line)
        return True


# requests integer inputs from user
def getIntInput(requestString, maxvalue, minvalue):
    not_valid = True
    while not_valid:
        output: str = input(requestString)
        print(funky_line)
        not_valid = int_check(output, maxvalue, minvalue, 'Integer')
    return int(output)


# request float inputs from user
def getFloatIntInput(requestString, maxvalue, minvalue):
    not_valid = True
    while not_valid:
        output: str = input(requestString)
        print(funky_line)
        not_valid = int_check(output, maxvalue, minvalue, 'Float')
    return float(output)


# request optional inputs
def getOptIntInput(requestString, maxvalue, minvalue, assumption):
    not_valid = True
    while not_valid:
        output = input(requestString)
        print(funky_line)
        if output == '':
            output = assumption
            not_valid = False
        else:
            not_valid = int_check(output, maxvalue, minvalue, 'Float')
    return float(output)


# requests number of walls
def wallAmountCollector():
    print(funky_line)
    wall_amount = getIntInput("How many walls do you wish to paint? ¦ Type here --> ", 10, 0)
    return int(wall_amount)


# requests wall measurements and coats for each wall
def wallMeasurementsCollector(wall_amount):
    wall_measurement = []
    for i in range(wall_amount):
        print('\n\n' + funky_line)
        height = getFloatIntInput(f'Enter height for wall {i + 1} in meters ¦ Type here --> ', 1000, 0)
        length = getFloatIntInput(f'Enter length for wall {i + 1} in meters ¦ Type here --> ', 1000, 0)
        coat_count = getIntInput(f'How many coats are required for wall {i + 1} ¦ Type here --> ', 50, 0)
        print(
            f'(OPTIONAL QUESTION!) Of wall {i + 1}, how much of the wall do you estimate to cover? Please exclude windows and doors in'
            f' this estimation!')
        amount_of_wall = getOptIntInput(
            'Give answer in terms of percentage (1-100) ¦ Type here (Leaving blank will assume 100%) --> ', 101, 0, 100)
        wall_measurement.append([height, length, coat_count, amount_of_wall])

    return wall_measurement


# converts meter squared result to litre equivalent
def litreCalculator(total):
    value = total / 10
    return value


# requests number of doors
def doorAmountCollector():
    print('\n')
    print(funky_line)
    door_amount = getIntInput("How many doors are their overall on the walls you wish to paint? ¦ Type here --> ", 20,
                              -1)
    return int(door_amount)


# requests measurements of windows
def windowMeasurementsCollector(window_amount):
    window_measurement = []
    for i in range(window_amount):
        print('\n\n' + funky_line)
        height = getFloatIntInput(f'Enter height for window {i + 1} in meters ¦ Type here --> ', 1000, 0)
        length = getFloatIntInput(f'Enter length for window {i + 1} in meters ¦ Type here --> ', 1000, 0)
        window_measurement.append([height, length])
    return window_measurement


# request number of windows
def windowAmountCollector():
    print('\n')
    print(funky_line)
    window_amount = getIntInput("How many windows are their overall on the walls you wish to paint? ¦ Type here --> ",
                                10, -1)
    return int(window_amount)


# calculates meters squared for window
def windowSquaredCalc(valueDict):
    calculations = []
    for i in range(len(valueDict)):
        height = valueDict['window' + str(i + 1)]['height']
        length = valueDict['window' + str(i + 1)]['length']
        calculations.append(height * length)

    if len(calculations) > 1:
        return litreCalculator(sum(calculations))

    else:
        return litreCalculator(0)


# calculates meters squared for walls
def wallSquaredCalc(valueDict):
    wallTotalList = []
    for i in range(len(valueDict)):
        height = valueDict['wall' + str(i + 1)]['height']
        length = valueDict['wall' + str(i + 1)]['length']
        coats = valueDict['wall' + str(i + 1)]['coats']
        percentage = (valueDict['wall' + str(i + 1)]['percentage']) / 100
        total = height * length
        total = total * coats
        total = total * percentage
        wallTotalList.append(total / 10)
    return sum(wallTotalList)


# retrieve custom character
file = open("linesPC.txt", encoding="utf-8")
funky_line = file.read()
file.close()


# checks if every value in a list is the same
def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def main():
    if __name__ == "__main__":
        # creates a list of the wall measurements
        header()
        wallValuesList = wallMeasurementsCollector(wallAmountCollector())

        # converts valuesList into a more convenient dictionary
        valueDictMaster = {}
        for i in range(len(wallValuesList)):
            valueDictSub = {'height': wallValuesList[i][0],
                            'length': wallValuesList[i][1],
                            'coats': wallValuesList[i][2],
                            'percentage': wallValuesList[i][3]
                            }
            valueDictMaster[f'wall{i + 1}'] = valueDictSub

        # creates a list of coats
        if len(wallValuesList) > 0:
            matchCase = []
            for x in range(len(wallValuesList)):
                matchCase.append(wallValuesList[x][2])

        allSame = all_equal(matchCase)

        # check if all coats are the same or not
        if allSame:
            # gets the amount of doors and then calculate how litres the doors will save
            doorAmount = doorAmountCollector()
            if doorAmount > 0:
                doorLitreReduction = doorAmount * 1.68
            else:
                doorLitreReduction = 0

            # creates a list of window measurements
            windowValuesList = windowMeasurementsCollector(windowAmountCollector())

            # converts window to dictionary and then calculates how many litres the windows will save
            valueWinDictMaster = {}
            if len(windowValuesList) > 0:
                for i in range(len(windowValuesList)):
                    valueWinDictSub = {'height': windowValuesList[i][0],
                                       'length': windowValuesList[i][1],
                                       }
                    valueWinDictMaster[f'window{i + 1}'] = valueWinDictSub
                windowLitreReduction = windowSquaredCalc(valueWinDictMaster)
            else:
                windowLitreReduction = 0
        else:
            doorLitreReduction = 0
            windowLitreReduction = 0

        # calculates the litres that each wall will use
        wallLitreAmount = wallSquaredCalc(valueDictMaster)

        # calculates the total litres
        totalLitreAmount = wallLitreAmount - windowLitreReduction - doorLitreReduction
        totalLitreAmount = round(totalLitreAmount * 1.1)
        if totalLitreAmount > 0:
            dulux5LPrice = round(totalLitreAmount * 6.4)
            dulux2LPrice = round(totalLitreAmount * 8)
            dulux5Ltins = round(totalLitreAmount/5, 1)
            dulux2Ltins = round(totalLitreAmount/2.5, 1)

            print('\n\n' + funky_line)
            print('The prices below are based on the average dulux wall and ceiling paint, prices may vary depending on '
                  'factors such as colour or finish')
            print(f'The total litres estimated to paint the walls: {totalLitreAmount}L')
            print(f"If you buy dulux 5L tins this will potentially cost: £{dulux5LPrice} and you will need {dulux5Ltins} tins.")
            print(f"If you buy dulux 2.5L tins this will potentially cost: £{dulux2LPrice} and you will need {dulux2Ltins} tins.")
            print(funky_line)
        else:
            print('\n\n' + funky_line)
            print('Magically your walls are smaller than the doors or window that are attached, so this will cost you '
                  'nothing hurrah!')
            print(funky_line)

#Program start
main()