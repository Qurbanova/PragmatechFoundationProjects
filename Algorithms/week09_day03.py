#Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.
#Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.
#Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.
#Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki, 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.

# a=5
# b=3
# print(a+b)
# #LISTS-> REMOVE METHODS
# mylist=[2, 4,6, 'gunel']
# print(len(mylist))
# #mylist.remove(2)
# print(mylist)
# #mylist.pop(3)
# #del mylist[1]
# #del mylist
# #mylist.clear()
# print(mylist)
#ADD METHODS
# mylist=[2, 4,6, 'gunel']
# mylist.append('banan')
# mylist.insert(2, 'apple')
# herlist=[11,22,33]
# mylist.extend(herlist)
# mylist[3]='code'
# mylist[1:3] = ["blackcurrant", "watermelon"]
# print(mylist)
# for x in mylist:
#     print(x)
   
# thislist=mylist.copy()
# print(mylist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[]
# for x in fruits:
#     if 'i'or'o' in x:
#         newlist.append(x)
# newlist=[x for x in fruits if 'a' in x]

# print(newlist)


#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
def meyve_secimi(fruits):
   for x in fruits:
      if 'a' in x:
         newlist.append(x)
   print(newlist)
meyve_secimi(["apple", "banana", "cherry", "kiwi", "mango"])  




