# add your Student class here!

class Student():
    def __init__(self, name, grade, classes = []):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_name):
        self.classes.append(class_name)
        
    def get_num_classes():
        return len(self.classes)
    
    def summary():
        print(f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes")

    
    


    



