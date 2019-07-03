def printList(list):
   elements = ""
   for e in list:
      elements += (" " + e)
   print(elements)

primes = [2, 3, 5, 7, 11, 13] #これがlistの宣言
printList(primes)

primes.append(17) #最後に17を追加する
printList(primes)