#4) შექმენით პროგრამა სადაც გამოიყენებთ While loop - ს. 
#თქვენი დავალება იქნება ის, რომ მომხამრებელს შემოატანინოთ რიცხვი და თქვენ უნდა გამოიცნოთ ეს რიცხვი, ხოლო ყოველ არ გამოცნობილ რიცხვზე ისევ თავიდან უნდა შეგეკითხოთ და შეიყვანოთ რიცხვი.




user_number =int(input("გთხოვთ შემოიყვანოთ რიცხვი:"))

Right_guess = 10

while Right_guess == user_number:
 print("თქვენ სწორად გაეცით პასუხი ყოჩაღ!")

 while Right_guess >user_number:
  print("თვენ არასწორად გაეცით პასუხი სცადეთ თავიდან")

  while Right_guess <user_number:
   print("თვენ არასწორად გაეცით პასუხი სცადეთ თავიდან")