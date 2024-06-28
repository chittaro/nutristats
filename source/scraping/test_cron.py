from datetime import date

path = 'home/chittaro/python/nutristats/source/data/'
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print(d1)


#with open('/home/chittaro/python/nutristats/source/data/input2.txt', 'a') as file:
#    file.write('wroted it\n')
