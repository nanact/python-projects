import matplotlib.pyplot as plt

students_names = ["sanjay","Rahui","Karen","Wasim","Ramesh","Ajay","Sartaj","Priya"]
student_marks = [35,50,20,45,25,40,25,40]

marks_perc = []
for x in student_marks:
    res = (x/50)*100
    marks_perc.append(res)
    
print(marks_perc)

def marks_line_chart():
    plt.plot(students_names,student_marks,mec = "r",ms = 9,linewidth = "20.5",color = "r",linestyle = "-.")
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()
    
marks_line_chart()

def pencentage_bar_chart():
    plt.bar(students_names,marks_perc)
    plt.title("Students' Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Student Percentage")
    plt.show()
    
pencentage_bar_chart()