#encoding:utf-8
import time
from Mysql import Base
# class Base():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

    # def tt1(self):
    #     print ("%s is %d years old" %(self.name,self.age))

class Grate(Base):
    def talk(self):
        # Base(name='wwg',age=18
        print ("%s is %d years old" %(self.name,self.age))

if __name__=="__main__":
    s=Grate("wwg",18)
    s.talk()

# pp=Grate()
# pp.talk(name='wwg',age=18)