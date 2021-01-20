'''
 ###############################################
#    #######################################    #
####    ########   Simple Calculator   ##########    ####
#   #######################################     #
###############################################
##                                           ##
  ##########################################
  ############  Version 2  #################
  ##########################################
 ##                                          ##
'''
'''
The version 2 of SimpleCalc.py adds extra functionality but due to my limited
approach, has to remove to some functions as well, which hope so will be added
along with these new functions in the later version.
This version can tell total number of inputs, their summation and and average,
no matter how many inputs you give it, but as the same time this version unable
to calculate multiple and devision of the numbers.
'''
sum = 0
count = 0

while True:
    num = input('Input your number: ')
    if num == 'done':
        print('goodbye')
        break
    try:
        fnum = float(num)
    except:
        print('bad input')
        continue
    sum = sum + fnum
    count = count + 1

print('----Total Inputs:', count)
print('----Sum:', sum)
print('----Average:', sum/count)
