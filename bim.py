# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_num = float(height)
weight_num = int(weight)

# result = weight_num / (height_num * height_num)
result = weight_num / height_num ** 2

bmi = round(result)
# bmi2 = int(result)

print(bmi)
# print(bmi2)


# print(height_num)
# print(weight_num)
# print(result)