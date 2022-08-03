import datetime

def timed_greeting(func):
    hour = datetime.datetime.now().hour
    if 1 <= hour < 22:
        func("Shreyansh")
        print("What a lovely evening it is !!")

@timed_greeting
def greeting(name):
    print(f"Greetings {name}")

"""
def greeting1(func):
    func()
    print("How Are You ?")


@greeting1
def greeting():
    print(f'Hello World')

greeting1(greeting)
"""