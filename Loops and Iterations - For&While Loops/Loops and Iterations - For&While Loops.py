nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. break
for num in nums:
    if num == 5:
        print("Founded!")
        break
    else:
        print("\n This is not 5")

# 2. continue
for num in nums:
    if num == 5:
        print("Founded!")
        continue
    else:
        print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

#  Range
for i in range(1, 10):
    print(i)

#  While Loop
i = 1
while i < 10:
    print(i)
    i += 1

#  While Loop with break
i = 1
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

# Infinite Loop
i = 1
while True:
    # if i == 5:
    #     break
    print(i)
    i += 1