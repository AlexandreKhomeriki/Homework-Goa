print("        Wellcome  to  GOA Shop        ")
print(" In GOA you are going to learn programing ")
print("""
>in GOA we have different type of classes<
1> Speed 1
2> Speed 2
3> Speed 3
in Speed 1 there is 1 class in a week in Speed 2 there are two classes  and in speed 3 there are 3 classes in a week<
4> exit the shop
""")

class_Speed = int(input("class speed"))


    
goa_shop = True

while goa_shop:
    if class_Speed ==1:
        yes_no = input ("these class costs 18 lari< are you shure u want to buy these course [ yes/no] >")
        if yes_no == "yes":
            print ( "you have sacsesfuly bought a Speed 1 course  <3 ")
            goa_shop = False
        elif yes_no == "no":
            print ( "you dint bought a cours in GOA ")
        else:
            print ( "you had to answer yes or no")  
    elif class_Speed ==2:            
        yes_no = input ("these class costs 26 lari< are you shure u want to buy these course [ yes/no] >")
        if yes_no == "yes":
            print ( """you have sacsesfuly bought a Speed 2 course  <3
                          now you can lern faster than speed 1
                    """)
            goa_shop = False
        elif yes_no == "no":
            print ( "you dint bought a cours in GOA ")
        else:
            print ( "you had to answer yes or no")        
    elif class_Speed ==3:
        yes_no = input ("these class costs 30 lari< are you shure u want to buy these course [ yes/no] >")
        if yes_no == "yes":
            print ( """you have sacsesfuly bought a Speed 3 course  <3
                          now you can lern faster than speed 2 and speed 1
                    """)
            goa_shop = False
        elif yes_no == "no":
            print ( "you dint bought a cours in GOA ")
        else:
            print ( "you had to answer yes or no")  
    elif class_Speed ==4:
           goa_shop = False
        
    else: 
        print ("you had to anwer 1 , 2, 3 or 4 ")