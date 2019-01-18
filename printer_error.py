"""
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.

You have to write a function printer_error which given a string will output the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from a to z.

#Examples:

"""
s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"

"""
#My Code

def printer_error(s):
  s = list(s)
  error_codes = list('nopqrstuvwxyz')
  error_number = 0
#nested loop to list color codes and then search for used colors in error if they exist. if exist count error
  for color_codes in s:
    for error in error_codes:
      if error in color_codes:
        error_number += 1
  #output in format errors/total output
  return "{}/{}".format(error_number,len(s))

print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))


#best solutions

def printer_error(s):
  nom = len([c for c in s if c not in 'abcdefghijklm'])
  return '{}/{}'.format(nom, len(s))


from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
    
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
    
def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)
    # your code
