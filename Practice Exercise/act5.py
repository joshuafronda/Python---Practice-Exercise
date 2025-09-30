x = 10
y = 25

print(f"Is x less than y? {x < y}")   # True
print(f"Is x divisible by 5 and y odd? {(x % 5 == 0) and (y % 2 == 1)}")  # True and True = True
print(f"Is x divisible by 4 or y greater than 30? {(x % 4 == 0) or (y > 30)}")  # True or False = True
print(f"Is x NOT greater than y? {not (x > y)}")  # not False = True
