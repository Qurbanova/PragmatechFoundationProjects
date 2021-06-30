#IDENTITY OPERATORS "İS" and "IS NOT"
x = ["alma", "banan"]
y = ["alma", "banan"]
z = x
print(x is z)
# nəticə-> TRUE, çünki z x ilə eyni obyektdir.

print(x is not z)
# nəticə-> FALSE. Çünki x ilə z eyni obyektdir.

print(x is not y)
# nəticə TRUE. Çünki x ilə y fərqli obyeklerdir, içərisindəki elementlerin eyni olmasına baxmayaraq.

print(x is y)
# Nəticə--> FALSE. Bu obyeklerin elementleri eyni olsa da,özleri ferqli elementlerdir. Onun üçün də eyni(bərabər) sayıla bilməzlər.

print(x==y)
#Bu doğrudur.İdentity oparatorlarından fərqli olaraq Comparison operatoru ilə müqayisədə x və y bərabərdir, çünki daxildindəki elementler bərabərdirlər.

print(x != y)
#Bu isə yanlışdır. Comparison oparatoru ilə müqayisə olunduqda x və y bərabərdir. Çünki onların elementləri bərabərdir.


#Membership Operators
x = ["alma", "banan"]
print("banan" in x)

# Nəticə doğrudur.Çünki belə bir element bu obyektin daxilində mövcuddur.


print ('armud' not in x)
#Nəticə doğrudur. Çünki belə bir element obyektin daxilində mövcud deyil.

x=[2,3,5,15,23]
print(3 in x)
print(10 not in x)

def LoginCheck():
    username= input('Username : ')
    password=input('Password : ')
    print('butun melumatlar daxil edilmelidir')

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

def myfunc():
    global x
    x = "fantastic"
        
myfunc()
print("Python is " + x)
