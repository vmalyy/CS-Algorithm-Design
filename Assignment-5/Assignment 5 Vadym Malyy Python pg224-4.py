#Global constant
number = 0
total = 0

#Asking to input positive numbers or negative to stop and disply sum.
def main():
       global number,total
       while number >= 0:
              #Ask for input. Set validation to only input int.
              total = total + number
              try:     
                     number = int(input('Please input positive numbers or negative to stop:'))
              except ValueError:
                     print('Error: Please select an integer')
                     number=0
              if number < 0:
                     print ('The sum of numbers is:',total)   
main()
	   
       
