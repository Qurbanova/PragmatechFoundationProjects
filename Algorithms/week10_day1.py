# # Bunlar təkrar özüm üçün işlədiyim kodlardır, baxmaya bilərsiniz.45-ci sətirdən başlayır tasklar.
# for x in range(6):
#     if x==3:
#         break
#     print(x)
# else:
#     print('Finally finished!')


# def my_function(fname):
#     print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(country):
#     print('I am from' + ' '+country)
# my_function("India")
# my_function("Brazil")


# def my_function(**std):
#     print("Student's first name is" + "  "+ std["sname"] +'  '+ "and the student id is" + "  "+ std["sid"])
# my_function(sname='Gunel', sid='one')

# def my_function(*fruit):
#     print("My fav fruit is"+"  "+ fruit[2])
# my_function('apple','banana', 'cherry')


# def my_function(fruits):
#     for x in fruits:
#         print(x)
# my_function(["apple", "banana", "cherry"])
     
def my_function(x):
       return 5 * x

print('The result is',(my_function(3)))
print(my_function(5))
print(my_function(9))


# x=lambda a, b:b%a
# print(x(6,3))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# #TASKLR BURADAN BASHLAYIR.
# # lamda funksiyadan və filter-dən istifadə edərək listin 4-ə qalıqsız bölünən elementlərini çapa verin
# my_list= [5,8,17,24,100,65,48]
# y = list(filter(lambda i: i % 4==0, my_list))
# print(y)
# # stringin uzunluğunu len metodundan istifadə etmədən hesablayan funksiya yazın

# def my_func(my_word):
#     i=0
#     for x in my_word:
#         i+=1
#     return i
# print(my_func('hello'))

# # Düzbucaqlının sahəsini hesablayan funksiya yazın. En və uzunu inputdan alın
# x=int(input('Düzbucaqlının eni: '))  
# y=int(input("Düzbucaqlının uzunluğu:  "))
# print("Düzbucaqlının sahəsi:  ",x*y)


# # ** Bonus olaraq: İnputdan 3 ədəd alın hansı ki bu ədədlər kvadrat tənliyin əmsalları olacaq (a, b, c). ax²+bx+c=0 [https://az.wikipedia.org/wiki/Kvadrat_t%C9%99nlik]. Daxil edilən əmsallara uyğun olaraq tənliyin köklərini hesablayan funksiya yazın.

def sahe(x,y):
    try:
        x=int(x)
        y=int(y)
        return x*y
    except:
        return("noninteger")
  
a=input('Düzbuc44aqlının eni: ')  
b=input("Düzbucaqlının uzunluğu:  ")
print(sahe(a,b))