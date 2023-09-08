
def get_input():
     while True:
        number = input("Enter a number to 'FizzBuzz' ")
        if number.isdigit() or number.replace(".","").isnumeric():
            return int(float(number))
            break
        else:
            print("Not a valid entry, please try again.")
            continue
            
          
def fizzbuzz_all_in_one(number):
    for num in range(1,number):
        if num % 3 == 0 and num % 5 == 0:  
             print(num,"FizzBuzz")
        elif num % 5 == 0:
            print(num,"Buzz")
        elif num % 3 == 0:
            print(num,"Fizz")
        else:
                print(num)
    return "Complete"


def fizzbuzz():
     number = get_input()
     fizzbuzz_all_in_one(number)
