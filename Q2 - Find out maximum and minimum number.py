#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Write a program to accept ‘n’ numbers from user , store these numbers into an array. Find out maximum and minimum number from an Array.

#function to check whether the input is number or not (also validates float)
def numCheck (string) :
    temp = str(string)
    if (temp.isnumeric() or temp.replace('.','',1).isdigit()) :
        return True
    else :
        return False
    
#function to collect numbers and return as a list
def collectNum (length) :
        i = 0
        num_list =[]
        while (i < length) :
            temp = str((input(f'\n Enter the number#{i+1}   :')))
            if not (numCheck(temp)) :
                print('Please enter numbers only')
            else :
                num_list.append(float(temp))
                i += 1
        print(f'\nThe entered number are: {num_list}')
        return num_list

cont = True
num_list = []
while (cont) :
    
    #How many numbers the user wants to input
    num_len = int(input("\nHow many numbers would you like to enter?"))
    if numCheck(num_len) :
        num_list = collectNum(int(num_len))
        
        #finding maximum and minimum in a list using max and min inbuilt function
        max_num = max(num_list)
        min_num = min(num_list)
        print(f"Largest number is {max_num}\n")
        print(f"Smallest number is {min_num}\n")
        cont = False
            
    else :
        print('Please enter numbers only')
        cont = True


# In[ ]:




