import os
os.system("cls")
print("SET")
s = {"salom", 21, 3, 'qalaysan', 23.34, 11,22,True}
print(s)

                #!   P O P 
print("POP")
s.pop()             # 0-index ochirib beradi
print(s)

                #!   R E M O V E
print("Remove")
s.remove(22)       # berilgan qiymatni ochirib beradi(yoq bolsa error beradi)
print(s)

                #!  D I S C A R D
print("Discard")
s.discard(11)       # berilgan  qiymatni ochirib beradi (error bermasdam)
print(s)

                    #!  C L E A R
print("Clear")
s.clear()               # butun set ni boshatib (tozalab) beradi
print(s)