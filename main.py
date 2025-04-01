from activity.student import Student
from activity.comparison import get_student_with_more_classes

# First instance
samara = Student("Samara", "junior", [
    "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition"
])
samara.add_class("Painting")
print(samara.get_num_classes())  # => 7
print(samara.summary())          # => "Samara is a junior enrolled in 7 classes"

# Second instance
claire = Student("Claire", "freshman", [
    "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science"
])
claire.add_class("Painting")
print(claire.get_num_classes())  # => 6
print(claire.summary())          # => "Claire is a freshman enrolled in 6 classes"

# Comparison
winner = get_student_with_more_classes(claire, samara)
print(winner.name)  # => Samara