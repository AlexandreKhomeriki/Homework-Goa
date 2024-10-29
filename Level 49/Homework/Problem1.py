# პროექტის აღწერა
# პრობლემა დაწერეთ პროგრამა, რომელიც ითვლის სტუდენტების ნიშნებს და განსაზღვრავს საუკეთესო სტუდენტს. მომხმარებელი შეიყვანს სტუდენტების სახელებსა და მათ ნიშანს, პროგრამა კი გამოთვლის საშუალო ნიშანს თითოეული სტუდენტისთვის და გამოაცხადებს საუკეთესოს.
# Function to find the best student
def find_best_student():
    students = {}
    
    print(" Best student?")
    
    while True:
        name = input("Enter name (Type done when finished: ")
        if name.lower() == 'done':
            break
            
        try:
            grade = float(input(f"  what is  {name} grade? "))
            students[name] = grade
        except ValueError:
            print("Not valid try again.")
            continue

    if not students:
        print("U didnt enter anything so comeback when ur ready!")
        return


    best_student = max(students, key=students.get)
    best_grade = students[best_student]

    print(f" The best student is: {best_student} With grade of  {best_grade:.2f}")


find_best_student()
