input = input("write what you want here:")
t = str(input)
s = t.lower()
k = s[::-1]
f = k.replace(" ", "")
r = s.replace(" ", "")
vowels = ["a" , "u" , "o" , "e" , "i"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
spaces = [" "]
exclude = ["!" , "?" , "," , "."]

how_many_letters = 0
capital_number = 0
vowels_number = 0
numbers_number = 0
words_number = 1
palindrome = False

for char in t :
    if char.isalpha():
        how_many_letters += 1
    if char in vowels:
        vowels_number += 1
    if char in numbers:
        numbers_number += 1
    if char in spaces:
        words_number += 1
    if char in exclude:
        words_number -= 1
for c in t:
    if c.isupper():
        capital_number +=1

if f == r:
    palindrome = True
else :
    palindrome = False

print("there are {} letters in your input".format(how_many_letters)
+"\n there are {} capital letters in your input.".format(capital_number)
+"\nthere are {} vowels in your input".format(vowels_number)
+"\nthere are {} numbers in your input".format(numbers_number)
+"\nthere are {} words in your input".format(words_number)
+"\n help me please")

if palindrome == True:
    print("your text is palindrome")
else:
    print("your text isn't palindrome")
