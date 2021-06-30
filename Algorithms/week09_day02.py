#Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin
x='Hello Python!'
print(x)

#ad və soyad dəyişkənləri yaradın və onlara istədiyiniz kiçik hərflərdən ibarət dəyər verin. Sonra tam_ad adlı dəyərdə ad və soyadın ilk hərflərini böyük şəkildə çapa verərək həmin şəxsə Salam verin.
ad='gunel'
soyad='qurbanova'
tam_ad=ad[0]+soyad[0]
print('Salam'+ "  " + tam_ad.upper())

#İki ədədi iki müxtəlif dəyişkənə mənimsədin sonra isə onların bir birlərinə olan qüvvətini tapın (Riyazi operatorları research edin həll etmək üçün bu taski)
a=5
b=4
print(a**b)
print(b**a)

#y = “4.92” stringini integere çevirin.
#/This is Casting./
y=float('4.92')
print(int(y))


#İstifadəçidən havanın temperaturunu soruşun. 10 dərəcədən aşağı olarsa temperatur, ekrana soyuq, 20 dərəcə olarsa, Normal, 30 dərəcədən yüksək olarsa İsti sözü yazılsın.

#'Proqramlaşdırma' sözündə 'x' hərfinin olub-olmamasının yoxlayın
#This is membership operator.
text='Proqramlashdirma'
if 'x' in text:
    print('Beli, var.')
else:
    print('Xeyr, yoxdur.')


#İki dənə string tipində dəyişkən yaradıb onları başqa bir string dəyərdə birləşdirib saxlayın və həmin string dəyəri ekrana yazdırın.
a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
