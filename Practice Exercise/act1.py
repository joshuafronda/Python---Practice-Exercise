#String Searching Operations
text = "Welcome to Joshua Fronda's Python class!"

first_o = text.find('o')
last_o = text.rfind('o')

print(f"First 'o' found at index: {first_o}")
print(f"Last 'o' found at index: {last_o}")

#Output: 
#First 'o' found at index: 4
#Last 'o' found at index: 31