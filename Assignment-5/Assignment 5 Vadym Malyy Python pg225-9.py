
def numberDays():
    global daysWorked
    try:     
        daysWorked = int(input("Please enter the days worked:"))
    except ValueError:
        print('Error: Please select an integer')
        numberDays()
    
def setCalculation():
    print('Day(s)\t$ Earned')
    print('------------')
    total = 0.0
    for number in range(1,daysWorked +1):
        square = float((2**(number-1))/100)
        total = total + square
        print(number,'      ',square)
    print ('total       ',"%.2f" % total)
    
def main():
    numberDays()
    setCalculation()
        
main()
