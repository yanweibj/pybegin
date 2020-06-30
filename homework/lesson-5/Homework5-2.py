'''
2. 在控制台中录入5个学生信息(姓名／年龄／性别)
数据结构：列表中嵌套字典
[
    {
        "name":xx,
        "age":xx,
        "sex":xx,
    },
    {
        "name":xx,
        "age":xx,
        "sex":xx,
    }
    .......
]
'''
list01 = list()
print("请在控制台输入5个学生的信息：")
for i in range(5):
    print("请输入第%d个学生的信息：" %(i+1))
    student={}
    student["name"] = input("姓名：")
    student["age"] = input("年龄：")
    student["sex"] = input("性别：")
    list01.append(student)

for student in list01:
    print(student)