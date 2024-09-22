kilometri = 1.000000
mili = 0.621371

print("1.kilometr tu mill")
print("2.mill tu kilometr")
choose = input("choose: ")

if choose == "1":
    choose1 = int(input("enter your kilometr: "))
    print(choose1 * mili)
elif choose == "2":
    choose2 = int(input("enter your mill: "))
    print(choose2 * kilometri)