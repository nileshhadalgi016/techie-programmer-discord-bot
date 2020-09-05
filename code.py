
import sys
    
sys.stdout = open('output.txt', 'wt')
def n(a) :
      if a%2==0:
            return "Even Number"
print(n(4))
            