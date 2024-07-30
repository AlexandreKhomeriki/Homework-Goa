# შექმენით ცვლადები სადაც შეინახავთ თქვენს თავზე ინფორმაციას (სახელი, გვარი, ასაკი, ქვეყანა, ქალაქი, საყვარელი ფერი, საყვარელი მანქანა, საყვარელი საჭმელი, საყვარელი სპორტი და ა.შ) შემდეგ შემოტანილი მნიშვნელობებით ააწყვეტ ერთი დიდი წინადადება.


# Define variables to get a sentence
first_name = "Alexandre"
last_name = "Khomeriki"
age = 13
country = "Georgia"
city = "Tbilisi"
favorite_color = "black"
favorite_car = "Porsche Spyder 918"
favorite_food = "khinkali"
favorite_sport = "football"

# Construct a sentence with the entered answers 
sentence = (
    "My name is {first_name} {last_name}. "
    "I am {age} years old. "
    "I live in {city}, {country}. "
    "My favorite color is {favorite_color}. "
    "My favorite car is the {favorite_car}. "
    "My favorite food is {favorite_food}. "
    "My favorite sport is {favorite_sport}."
)

# Output the sentence
print(sentence)