#Using the yield statement to function as return statemnt but with a psuedo break built into its implementation
def odds(start=1):
     ''' return all odd numbers from start upwards'''
     if int(start) % 2 == 0: start = int(start) + 1
     while True:
          yield start
          start += 2

#Generator functions can be used as incrementors in the for/while loop construct          
for n in odds ():
      if n > 7: break
      else: print(n)
