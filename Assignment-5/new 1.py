# Ryan Beardall Lab 8-1 10/31/13
#program calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day and continues to double each day. 
accumulatedPay = []
payPerDay = []
days = []
#User enters days worked to find out ho much money user will have
def numberDays():
    global daysWorked
    daysWorked = (input("Enter the days worked "))
    return daysWorked
def salaryOnDay(daysWorked):
    return float((2**(daysWorked-1))/100)
def calculations():
    earnings = 0
    for i in range (1, daysWorked + 1):
        salary = salaryOnDay(i)       
        currRow = [0, 0, 0]
        currRow[0] = i
        currRow[1] = salary
        earnings += salary
        currRow[2] = earnings
        days.append(currRow)
#program prints matrix
def main():
    numberDays()
    calculations()   
    for el in days:
        print (el)
main()
