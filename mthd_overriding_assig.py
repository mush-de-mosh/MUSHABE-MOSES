class Employee:
    def introduce_self(self):
        print("I am an employee in this place..")
        
#subclasses to override the above method
class SecretaryDash(Employee):
    def introduce_self(self):
        print("I am a secretary in this company") 
        
class DirectoryDash(Employee):
    def introduce_self(self):
        print('''I am here not only as an employee but 
              i head all the employees in this company...''')   
        
#calling these methods
mush = DirectoryDash()
mush.introduce_self()

mayya = SecretaryDash()
mayya.introduce_self()    
