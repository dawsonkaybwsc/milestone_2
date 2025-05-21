import time

print("hello")
feeling_are = input("How are you feeling? ") 
print("you are feeling", feeling_are)
time.sleep(2)
print("what is 5 times 7?")
your_answer = input("Answer: ")
print("your guess was", your_answer)
if int(your_answer) > 5 * 7:
    print("you're wrong, it is 35, try again")
if int(your_answer) < 5 * 7:
    print("you're wrong, it is 35, try again")
if int(your_answer) > 100:
    print("answer the question properly")
if int(your_answer) == 5 * 7:
    time.sleep(2)
    print("you're right! It is", 5 * 7)
time.sleep(3)
print("next question")
time.sleep(2)
print("what is your name?")
name = input("Your name: ")
time.sleep(2)
print("okay, what is your age", name)
age = input("Your age: ")
time.sleep(2)
print("okay so your name is", name, "your age is", age, "and your're feeling", feeling_are, "thank you for sharing", name,)
