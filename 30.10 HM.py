# a.
students: int = int(input("Enter amount of students: "))
full_classes = students // 30
remaining_students = students % 30

print(f"amounts of full classes of 30 students: {full_classes}")
print(f"the last class have: {remaining_students}")

# b.
while True:
    try:
        number: int = int(input("enter a number: "))
        if 10 <= number <= 99:
            ahadot = number // 10
            asarot = number % 10
            if asarot > ahadot:
                reverse_number = asarot * 10 + ahadot
                print(f"the opposite number is: {reverse_number}")
            else:
                print(f"the number stays: {number}")
            break
        else:
            print("the number isn't between 10 - 99")
    except ValueError:
        print("Put in only numbers!")

# c.
for number in range(2, 201):
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)

# d.
counts = {'a': 0,'b': 0,'c': 0,'d': 0}

while True:
    answer: str = str(input("mark 'a' / 'b' / 'c' / 'd': "))
    if answer == 'x':
        break
    elif answer in counts:
        counts[answer] += 1
    else:
        print("please enter one of the options")
print(f"amounts of answers a: {counts['a']}")
print(f"amounts of answers b: {counts['b']}")
print(f"amounts of answers c: {counts['c']}")
print(f"amounts of answers b: {counts['d']}")

max_counts = max(counts, key=counts.get)
min_counts = min(counts, key=counts.get)

print(f"the large amounts of time that the answer repeats: {max_counts} ({counts[max_counts]}")
print(f"the small amounts of time that the answer repeats: {min_counts} ({counts[min_counts]}")