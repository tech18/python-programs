#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write A program to accept Four digit number from user and count zero , odd and even digits from the entered number.

#input the number, as string by default to bypass if someones inputs 0000
num = (input('Enter the 4 digit number'))

#use len function to find the length
num_length = int (len(num))

#using try except to detect the input error
try :
    #check if the length more than 4 or not
    if (num_length == 4) :
        #convert the string to number
        num = int (num)
        #print(f"The length of the number is {num_length}\n")
        #declaring standard values
        i = 1
        even_count = 0
        odd_count = 0
        zero_count = 0
        #extracting the numbers and finding 0, even and odd numbers
        while (i <= num_length) :
            #finding the last number of the digit using % operator.
            #This gives the remainder which is nothing but the last digit of the number
            digit = int (num % 10)
            if (digit == 0) :
                zero_count +=1
            elif (digit %2 == 0) :
                even_count +=1
            else :
                odd_count +=1
            i += 1
            num /= 10
            
        print (f"Count of even numbers: {even_count}\n")
        print (f"Count of odd numbers: {odd_count}\n")
        print (f"Count of zero numbers: {zero_count}\n")

    else :
        print ("Please enter 4 digit number only")

except ValueError:
    print("Please enter valid 4 digit number only! (No decimals or strings allowed please!)")
    


# In[ ]:




