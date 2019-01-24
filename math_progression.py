"""
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write the function findMissing(list), list will always be at least 3 numbers. The missing term will never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7
```

PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!
"""

#My Solution 
def find_missing(sequence):
  length = len(sequence)
  interval = (sequence[length - 1] - sequence[0]) // length
  for n in range(len(sequence) - 1):
    if sequence[n] + interval != sequence[n+1]:
      return (sequence[n]+interval)
    
#Codewars solution
def find_missing(sequence):
    t = sequence
    #sum of 1st and last number times length of all list plus 1 and minus sum of all items. 
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)
            
print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))

