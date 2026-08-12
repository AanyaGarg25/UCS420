# q1

roll = input("Enter your roll no.: ")

l = []
for i in roll:
    l.append(int(i) * 10)

print(l)

l.append(0)
print(l)

l.insert(0, 3)
print(l)

l.remove(3)
print(l)

l.pop()
l.pop(4)
print(l)

l.sort()
print("List in ascending order:", l)

l.sort(reverse=True)
print("List in descending order:", l)

print("Slicing:", l[:3], l[-3:])

avg = sum(l) / len(l)

new_l = [x for x in l if x > avg]

print("Average:", avg)
print(new_l)


# q2

scores = tuple(l[:8])

print("Original tuple:", scores)

highest = max(scores)
lowest = min(scores)

print("Highest no.:", highest)
print("Index of highest:", scores.index(highest))
print("Lowest no.:", lowest)
print("Occurrences of lowest:", scores.count(lowest))

reversed_list = list(scores[::-1])

print("Reversed list:", reversed_list)

n = int(input("Enter a number to be searched: "))

if n in scores:
    print("First occurrence index:", scores.index(n))
else:
    print("The number is not present")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)


# q3

import random as r

r.seed(1024170172)

List = [r.randint(100, 900) for i in range(100)]

print(List)

odd_count = 0

for i in List:
    if i % 2 != 0:
        odd_count += 1

print("Odd numbers in the list:", odd_count)

even_count = 0

for i in List:
    if i % 2 == 0:
        even_count += 1

print("Even numbers in the list:", even_count)

prime_count = 0
Prime_list = []

for i in List:
    prime = True

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime = False
            break

    if prime and i > 1:
        prime_count += 1
        Prime_list.append(i)

print("Prime count =", prime_count)
print("Prime list =", Prime_list)

most_freq = List[0]
max_count = 0

for i in List:
    count = List.count(i)

    if count > max_count:
        max_count = count
        most_freq = i

print("Most frequent number =", most_freq)
print("Frequency =", max_count)


# q4

roll = input("Enter roll number: ")

A = {int(digit) * 7 for digit in roll[:8]}
B = {int(digit) * 9 for digit in roll[:8]}

print("A =", A)
print("B =", B)

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("A - B:", A.difference(B))
print("B - A:", B.difference(A))

print("Symmetric Difference:", A.symmetric_difference(B))

print("A subset of B?", A.issubset(B))
print("B superset of A?", B.issuperset(A))

x = int(input("Enter a value to remove from A: "))

A.discard(x)

print("Updated A =", A)


# q5

my_dict = {
    "name": "Aanya",
    "roll_no": "12345678",
    "branch": "CSE",
    "age": 20,
    "city": "Delhi"
}

my_dict["location"] = my_dict.pop("city")
print("After renaming city:", my_dict)

my_dict["cgpa"] = 8.53
print("After adding cgpa:", my_dict)

my_dict["age"] += 1
print("After updating age:", my_dict)

dict1 = my_dict.copy()
removed = dict1.pop("branch")
print("Using pop():", dict1)

dict2 = my_dict.copy()
del dict2["branch"]
print("Using del:", dict2)

for key, value in my_dict.items():
    print(key, "→", value)

if "email" in my_dict:
    print(my_dict["email"])
else:
    print("Email key not found")

friend_dict = {
    "name": "Riya",
    "roll_no": "87654321",
    "branch": "ECE",
    "age": 21,
    "city": "Delhi"
}

merged = {**my_dict, **friend_dict}

print("Merged Dictionary:", merged)

string_dict = {k: v for k, v in my_dict.items() if type(v) == str}

print("Only string values:", string_dict)