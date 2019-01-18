"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

"""

#My Solution

def iq_test(numbers):
    #your code here
    split_numbers = numbers.split(' ')
    #initial count of even and odd numbers in the list
    even_count = 0
    odd_count = 0
    
    #gathering unique numbers
    unique_even_number = 0 
    unique_odd_number = 0
    unique_number = 0
    
    #go through the list
    for number in split_numbers:
      if int(number) % 2 == 0:
        even_count += 1
        if even_count == 1:
          unique_even_number = split_numbers.index(number) + 1
      else:
        odd_count += 1
        if odd_count == 1:
          unique_odd_number = split_numbers.index(number) + 1
      
      #compare count of even or odd numbers and get unique one (which is equal 1) 
      if even_count > odd_count:
        unique_number = unique_odd_number
      else:
        unique_number = unique_even_number
return unique_number


#Best Practice solution: 

def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1
