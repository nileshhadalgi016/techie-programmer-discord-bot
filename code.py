
import sys
    
sys.stdout = open('output.txt', 'wt')
try:
    print(""" techie_programmer bro
    
    I'm go through the tutorial you shared 
    
    I think it will work 😅 """)

except Exception as e: print(e)

            