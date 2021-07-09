# 1)Write a Python function to sum all the numbers in a list. Sample List : (8, 2, 3, 0, 7) Expected Output : 20 
# 2)Write a Python function to multiply all the numbers in a list. Sample List : (8, 2, 3, -1, 7) Expected Output : -336
# 3)Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None. Expected Output: returnDay(1) --> Sunday
# 4)-Write a function called lastElement. This function takes one parameter (a list) and returns the last value in the list. It should return None if the list is empty. Example Output lastElement([1,2,3]) # 3 lastElement([]) # None 
# 5)Write a Python program to print the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8]
                    #GOOD LUCK FOR ME ! 

#FUNCTIONS
def my_function():
    print('hello from a function!')

my_function() 

''' def lst():
    lst=[]
    mylist=[8, 2, 3, 0, 7]
    num=0
    num+=1
    if num in mylist:
        lst.append(mylist)
print("Sum of elements in given list is :", sum(lst)) '''


''' mylist=[8, 2, 3, 0, 7]
Sum=sum(mylist)
print(Sum) '''

''' def hasil(my_list):
    netice=1
    for i in my_list:
        netice=netice*i
    return(netice)
hasil([8, 2, 3, -1, 7]) '''


''' def hefteninGunleri(eded):
    hefteninGunleri={
        1:'Sunday', 
        2:'Monday',
        3:'Tuesday',
        4:'Wensday',
        5:'Thursday',
        6:'Friday',
        7:'Saturday'  
    }
    if 1<=eded<=7:
        return(hefteninGunleri[eded])
    else:
        return None
eded=int(input("Bir gun qeyd edin 1-7 arasi: "))
x=hefteninGunleri(eded)
if x[0]=='F':
    print('cume gunu') '''

def last_element(my_list):
  if len(my_list)>0:
      for i in my_list:
        #i=my_list[-1]
        return(i)
last_element([1,2,3])
print(last_element)



    


''' def topla(my_list):
    cem=0
    for i in my_list:
        cem+=i
    return cem
print(topla([8,2,3,0,7]))
 '''

#lst = []
#num = int(input('How many numbers: '))
#for n in range(num):
  #  numbers = int(input('Enter number '))
 #   lst.append(numbers)
#print("Sum of elements in given list is :", sum(lst))


''' def my_function(fname, fsurname):
      print(fname + "  " +fsurname +" Refsnes")

my_function("Emil","Quliyev")

def my_function(*kids):
      print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") '''