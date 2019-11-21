#TASK1
#Conditions to be satisfied:
#    1. Takes even length of number and the number must be equal to or greater than 6
#    2. Finding the middle value of given observations - median 

#creating a data structure to store the numbers
even_list = []
num = int(input("Length of elements: "))  #first takes the length of numbers
if (num >= 6):                            #checking the condition whether it is equal or greater than 6
   if (num % 2) == 0:                     #checks whether it is an even number
       for i in range(0,num):             #if the given unput is an even number then for each value in the range
          number = int(input("Enter number:"))  #for each element in the row assigning an integer value
          even_list.append(number)             #lastly putting the results into the main data
even_list.sort()                               #to properly arrange the data
#for even number of values middle most value is found by taking adding the middle 2 values and dividing by 2
median_1 = even_list[n//2]                     
median_2 = even_list[n//2 - 1] 
median = (median_1 + median_2)/2                # this gives the middle value of the given set of observations
print("Median" + str(median))  
