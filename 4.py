years = int(input("Введите количество лет: "))
exhibits = int(input("Введите количество экспонатов: "))
a = years*365*8*60//5
b = exhibits//((365*8*60)/5)
print(a,"экспонатов",b,"дней")