RATE = 100
print("Введіть кількість учнів які вчаться на оцінки 12,11,10,9,8,7,6,5,4,3,2,1,0")
mark = []
mark.insert(0,0)
for i in range(1,13):
    x = int(input("Введіть кількість учнів,які вчаться на  {}: " .format(i)))
    mark.insert(i,x)
print ("Успішність учнів у %")
sumExpert = 0
for i in range(10,13):
    sumExpert += mark[i]
sumAdvanced = 0
for i in range(7,10):
            sumAdvanced += mark[i]
sumBasic = 0
for i in range(4,7):
            sumBasic += mark[i]
sumEntry = 0
for i in range(1,4):
            sumEntry += mark[i]
generalSum = sumExpert + sumAdvanced + sumBasic + sumEntry 
def showResult():
    print("Високий рівень {}%" .format(rExpert))
    print("Достатній рівень {}%" .format(rAdvanced))
    print("Середній рівень {}%" .format(rBasic))
    print("Низький рівень {}%" .format(rEntry))
if generalSum != 0:
   rExpert=sumExpert*RATE/generalSum
   rAdvanced=sumAdvanced*RATE/generalSum
   rBasic=sumBasic*RATE/generalSum
   rEntry=sumEntry*RATE/generalSum
   sumaRate=rExpert+rAdvanced+rBasic+rEntry
   if sumaRate == RATE:
      print showResult()
      print("Готово")
   else:
        print("не 100%")
        rDifference=RATE-sumaRate
        rAdvanced+=rDifference
        print showResult()
        print("Різниця: {} % додана до достатнього рівня" .format(rDifference))
else:
    print("На нуль ділити не можна!") 
