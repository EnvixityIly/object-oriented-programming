class student:
    grade = 8
    print("Hellow I am a swudent uf grade", grade)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    
zabir = student('ZHR', 35)
radoya = student("Ra", 12)
tabid = student("Reyna", 1)
    
print(zabir.name, zabir.age)
print(tabid.name, tabid.age)
print(radoya.name, radoya.age)