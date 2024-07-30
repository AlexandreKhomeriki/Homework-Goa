#დაწერეთ პითონის პროგრამა, რომელიც ითვლის მართკუთხედის პერიმეტრს. პროგრამამ უნდა სთხოვოს მომხმარებელს მართკუთხედის სიგანე და სიმაღლე.


# Prompt the user to enter the width of the rectangle
width = (input("Please enter the width of the rectangle: "))

# Prompt the user to enter the height of the rectangle
height = (input("Please enter the height of the rectangle: "))

# Calculate the perimeter of the rectangle
perimeter = 2 * (width + height)

# Print the perimeter of the rectangle
print("The perimeter of the rectangle with width {width} and height {height} is {perimeter}.")