n = 1
while n < 5:
    print(n)
    n = n + 1

n = 10
while n >= 5:
    print(n)
    n = n - 1

n = 1
numbers = []
while n <= 10:
    numbers.append(n)
    print(numbers)
    n = n + 1
print(n)

# For loop

veg = ["Onion", "Potato", "Tomato"]
for item in veg:
    print(item)

flower = {"Rose", "Marigold", "Jasmine"}
for item in flower:
    print(item)

roll_no = {1: "Amartya", 2: "Anand", 3: "Aniket"}
for i in roll_no:
    print(i)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
great = []
small = []
for i in my_list:
    if i > 5:
        great.append(i)
    else:
        small.append(i)
print(f"First list:{great}")
print(f"Second list: {small}")

# Range (start,stop,step)

for i in range(4):
    print(i)

for i in range(5, 15, 2):
    print(i)

# Break

my_numbers = [1, 5, 3, 7, 3, 2, 5, 6]
for n in my_numbers:
    if n % 2 == 0:
        break
    print(f"The answer is :", {n})

# Continue

for n in range(11):
    if n % 2 == 0:
        continue
    print(n)

# Pass

nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n % 2 == 0:
        pass
    else:
        print(n)


# class EditUserApp(ft.Container):

# 		 def __init__(self, page: ft.Page):
#         super().__init__()
#         self.employee_controller = EmployeeController()
#         self.image_picker_app = ImagePickerApp(self.page)
#         self.image_picker_app.build()
#         self.employee_id_suggestions = ft.Column()
#         self.page = page
#         self.dlg = MyAlertDialog(self.page, "Employee details saved successfully.")
