a = int(input(">> "))
if a%3 == 0:
   if a%7 == 0:
      print("3と7の両方で割り切れる")
   else:
      print("3のみで割り切れる")
else:
   if a%7 == 0:
      print("7のみで割り切れる")
   else:
      print("3でも7でも割り切れない")