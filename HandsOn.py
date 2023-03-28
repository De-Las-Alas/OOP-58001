class Person:
    def __init__(self, name, pre, mid, fin):
        self.name = name
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def grade(self):
        avg = (self.__pre + self.__mid + self.__fin) / 3
        return avg


'#different attempt at trying to make the grades hidden behind words that only say your current standing'
'#if avg >= 70 and avg <= 100: print(f"{self.__name}, PASSED!")'
'#elif avg < 70 and avg >= 65: print(f"{self.__name}, REMEDIAL!")'
'#elif avg <= 0 or avg > 100: print(f"{self.__name}, CODE ERROR!")'
'#else: print(f"{self.__name}, FAILED!")'

std1 = Person("Student1", float(input("Enter Pre Grade for STD1: ")),
              float(input("Enter Mid Grade for STD1: ")), float(input("Enter Fin Grade for STD1: ")))
Person.pre = 50
Person.mid = 50
Person.fin = 50

std2 = Person("Student2", float(input("Enter Pre Grade for STD2: ")),
              float(input("Enter Mid Grade for STD2: ")), float(input("Enter Fin Grade for STD2: ")))
Person.pre = 50
Person.mid = 50
Person.fin = 50

std3 = Person("Student3", float(input("Enter Pre Grade for STD3: ")),
              float(input("Enter Mid Grade for STD3: ")), float(input("Enter Fin Grade for STD3: ")))
Person.pre = 50
Person.mid = 50
Person.fin = 50

print("Name: ", std1.name, " Average Grade: ", std1.grade())
print("Name: ", std2.name, " Average Grade: ", std2.grade())
print("Name: ", std3.name, " Average Grade: ", std3.grade())
