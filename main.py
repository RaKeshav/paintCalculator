from abc import ABC, abstractmethod
from collections import deque
from collections import ChainMap

if __name__ == '__main__':
    Name = str("Keshav")
    Game = "Valorant"
    Rank = "Diamond"
    Lines = ["Hello my name is ", " I spend a lot of my free time playing the game ", " my rank is "]

    # print(Lines[0] + Name + Lines[1] + Game + Lines[2] + Rank)

    # print(str(Name))

numb = 14
letter = 'Y'
string = 'Hello!'
decimal = 2.5
bigger_numb = 307
negative_numb = -1
huge_numb = 438000000
boolean = False

# print('\n', int(numb), str(string), float(decimal), int(bigger_numb), int(negative_numb), int(huge_numb), bool(boolean))

# print(10 * 5)
# print(10 / 5)
# x = 10
# X = x + 1

print('\n')

x, y = 50, 10
if x >= y:
    print('Greater')

x, y = 50, 50
if x == y:
    print('Equal')

x, y = 50, 50
if x == y:
    print('Equal')
else:
    print('Unequal')

x = [50, 51]
y = [51, 49]

for i in range(0, 1):
    if x[i] == y[i]:
        print('Equal')
    else:
        print('Unequal')

x = [50, 57, 5]
y = 50

for x in x:
    if x == y:
        print('1')
    elif x > y:
        print('2')
    else:
        print('3')

day = 2
match day:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")

day = 4
match day:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3 | 4 | 5 | 6 | 7:
        print("Weekday")

c = 1
while c <= 6:
    print(c)
    c += 1

for x in range(0, 6):
    print(x)
    if x == 3:
        break

print('\n')

x = 3
while x != 9:
    print(x)
    x += 1
    if x == 6:
        x += 1

print('\n')

list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]

for j in range(0, len(list1)):
    print(list1[j])
    for k in range(0, len(list2)):
        print(list2[k])

print('\n')

values = [2, 5, 5, 6, 8, 10, 4, 5]
a = 0
while values[a] <= values[a + 1]:
    print(values[a])
    a = a + 1

print('\n')

values = [2, 1, 5, 3, 8, 10, 13, 5]
b = 0
while b <= values[b]:
    print(values[b])
    b += 1

print('\n')


def getTotal(num1, num2): return num1 + num2


print(getTotal(50, 3))

print('\n')


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def print_info(self):
        print("Model: " + self.model)
        print("Color: " + self.color)


if __name__ == "__main__":
    my_car = Car("Bugatti", "Red")
    my_car.print_info()

print('\n')


class Flower(ABC):
    @abstractmethod
    def bloom(self):
        print("Red flower")

    def grow(self):
        print("Growing...")


class Dandelion(Flower):
    def bloom(self):
        print("Yellow flower")


if __name__ == "__main__":
    dandy = Dandelion()
    dandy.grow()
    dandy.bloom()

print('\n')

results = {
    "Jack": [60, 105, 70],
    "Brandon": [102, 81, 3],
    "Serban": [120, 0, 70],
    "Dan P": [119, 60, 90]
}

for k in results:
    value = max(results[k])
    print(k, value)

print('\n')


def average(aList):
    return round(sum(aList) / len(aList))


resultsAverage = results

for k in results:
    resultsAverage[k] = average(results[k])

print(resultsAverage)

print('\n')


def reverseQueue(queue):

    stack = []

    while (queue):
        stack.append(queue[0])
        queue.popleft()

    while len(stack) != 0:
        queue.append(stack[-1])
        stack.pop()


# Driver code
if __name__ == '__main__':
    queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    reverseQueue(queue)
    print(queue)

print('\n')



