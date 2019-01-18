#My solution

import math

#check is square root equal to the multiplied value. if not return -1 
def find_next_square(sq):
  n = int(math.sqrt(sq))
  if n * n == sq:
    return (n + 1)**2
  else:
    return -1
    
#Best practice 

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
    
    
def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2
