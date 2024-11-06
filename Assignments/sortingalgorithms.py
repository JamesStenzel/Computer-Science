import random
import statistics
numbers = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),]
a = len(numbers)
a = a-1
steps = 0
for j in range(a):
    for i in range(a):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            steps += 1
print(numbers)
print(steps)
def quicksort():
    numbers = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
    b = numbers[-1]
    lpos = 0
    rpos = len(numbers)-1
    for j in range(len(numbers)-1):
        #find l
        #l is first number from left that is smaller
        #r in fist number in list from right that is larger
        for n in numbers:
            if n > b:
                lpos = n
                break
        #find r
        for i in range(len(numbers)-1, -1, -1):
            if numbers[i] < b:
                rpos = i
                break

        if lpos > rpos:
            numbers[lpos], numbers[-1], numbers[-1], numbers[lpos]
            break
        else:
            numbers[lpos], numbers[rpos] = numbers[rpos], numbers[lpos]
    print(numbers)
quicksort()
    


    