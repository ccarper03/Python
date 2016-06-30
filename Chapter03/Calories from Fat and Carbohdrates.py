__author__ = 'Charles Carper'

# 7. Calories from Fat and Carbohydrates
# A nutritionist who works for a fitness club helps members by evaluating their diets. As part
# of her evaluation, she asks members for the number of fat grams and carbohydrate grams
# that they consumed in a day. Then, she calculates the number of calories that result from
# the fat, using the following formula:
# calories from fat  fat grams  9
# Next, she calculates the number of calories that result from the carbohydrates, using the
# following formula:
# calories from carbs  carb grams  4
# The nutritionist asks you to write a program that will make these calculations.

fat_grams = 0.0
carb_grams = 0.0


fat_grams = float(input('Enter fat grams: '))
calories_from_fat = fat_grams * 9
print("Calories from fat: " + format(calories_from_fat, '3.1f'))
print()

carb_grams = float(input('Enter carbohydrate grams: '))
calories_from_carbs = carb_grams * 4
print("Calories from carbohydrate: " + format(calories_from_carbs, '3.1f'))


