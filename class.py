from datetime import date
class Individual():
    def __init__(self,name):
        self.name=name
        self.birthday=None
    def get_name(self):
        return self.name
    def add_birthday(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
        return (self.day,self.month,self.year)
    def get_age(self):
        a=date.today()
        b=a.year
        age=b-self.year
        return age
    def __str__(self):
        return str(Individual)
       
class AU_Employee(Individual):
    new=1
    def __init__(self, name):
        super().__init__(name)
    def get_unique_id(self):
        self.id=AU_Employee.new
        AU_Employee.new+=1
        return self.id
class Faculty(AU_Employee):
    def __init__(self,name):
        super().__init__(name)               

class EN_Faculty(Faculty):
    def __init__(self,name,faculty_name,classroom_year):
        super().__init__(name)
        self.faculty_name=faculty_name
        self.classroom_year=classroom_year
    def give_class(self):
        return "Btech 1st year"
    def give_year(self):
        return self.classroom_year
              
class Design_Faculty(Faculty):
    def __init__(self,name,faculty_name,classroom_year):
        super().__init__(name)
        self.faculty_name=faculty_name
        self.classroom_year=classroom_year 
    def give_class(self):
        return "Bdes 1st year"
    def give_year(self):
        return self.classroom_year                 
        
class Roaster_Au():
    def __init__(self):
        self._faculty=[]
        self.c={}
    def add_faculty(self,faculty):
        self.faculty=faculty
        if faculty not in self._faculty:
            self.c[faculty]=[]
        return self.c
    def add_course(self,course,factl):
        (self.c[factl]).append(course)
        return self.c 
    def get_courses(self,fact):
        self.fact=fact
        try:
            if self.fact not in self.c:
                raise ValueError("No such Faculty Found")
            else:
                return self.c[self.fact]
        except ValueError:
                print(("No such Faculty Found"))        
F1=Faculty("Sparsh")
F2=Faculty("Gourav")
F3=Faculty("Navni")
F4=Faculty("Abhay")
a=Roaster_Au()
(a.add_faculty(F1))
(a.add_course("ITC",F1))
(a.add_faculty(F2)) 
(a.add_course("DT",F2))
(a.add_faculty(F3)) 
(a.add_course("POE",F3))
(a.add_faculty(F4)) 
(a.add_course("FOP",F4))
print(a.get_courses(F3))
