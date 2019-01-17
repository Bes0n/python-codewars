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
      
      #compare number of even or odd numbers and get unique one
      if even_count > odd_count:
        unique_number = unique_odd_number
      else:
        unique_number = unique_even_number
    return unique_number
