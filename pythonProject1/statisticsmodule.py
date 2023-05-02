#Import mode,median and mean functions from statistics module
from statistics import mode,median,mean
#define function named improved_avg
def improved_avg():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    num3=int(input("Enter the third number: "))
    num4=int(input("Enter the fourth number: "))
    num5=int(input("Enter the fifth number: "))
    #store 5 numbers in a list
    list=[num1,num2,num3,num4,num5]

    #use mean,median,mode functions
    meanvalue=mean(list)
    medianvalue=median(list)
    modevalue=mode(list)

    #print mean,median and mode values of the number
    print("The mean is: ",meanvalue)
    print("The median is: ",medianvalue)
    print("The mode is: ",modevalue)
#call def function
improved_avg()