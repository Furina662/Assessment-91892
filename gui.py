import tkinter as tk
import json

with open("json/subject.json", "r") as file:
    data = json.load(file)

root = tk.Tk()
root.title("UE Rank Score Calculator")
root.geometry('1600x900')
#===============================================================
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
course_page= tk.Frame(root)
course_page.grid(row=0, column=0)

tk.Label(course_page, text="Please select your course below:", font=("Arial", 25, "bold")).grid(row=0, column=0, columnspan=3, sticky="ew")

pages = {}
drop_down_vars = {}
#===============================================================
#saved subject function
def saved_grades_function():
    global saved_grades_list
    saved_grades_list = {}
    for (subject, standard), var in drop_down_vars.items():
        grade = var.get()
        if grade == 'Not Attempted':
            continue
        if subject not in saved_grades_list:
            saved_grades_list[subject] = {}
        saved_grades_list[subject][standard] = grade
    print(saved_grades_list)
#===============================================================
# switch pages
def switch_to_standard_page(choosen_subject):
    course_page.grid_forget()
    pages[choosen_subject].grid(row=0, column=0, sticky="nsew")

def switch_to_course_page(current_frame):
    current_frame.grid_forget()
    course_page.grid(row=0, column=0, sticky="nsew")
#===============================================================
#display subjects and standards
for subject_name,subject_data in data["ncea_level_3_standards"].items():

    frame = tk.Frame(root)
    frame.grid_columnconfigure((0,1,2,3), weight=1)

    grade = [
            "Not Attempted",
            "Not Achieved",  
            "Achieved",  
            "Merit",  
            "Excellence" 
            ]

    tk.Label(frame,
             text=subject_name,
             anchor="center",
             font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, sticky="ew")
    
    tk.Label(frame, text="Assessment", anchor="center", font=("Arial", 14, "bold")).grid(row=1, column=0, sticky="nsew")
    tk.Label(frame, text="Credits", anchor="center", font=("Arial", 14, "bold")).grid(row=1, column=1, sticky="nsew")
    tk.Label(frame, text="Type", anchor="center", font=("Arial", 14, "bold")).grid(row=1, column=2, sticky="nsew")
    tk.Label(frame, text="Grade", anchor="center", font=("Arial", 14, "bold")).grid(row=1, column=3, sticky="nsew")


    for i, standard in enumerate(subject_data["standards"]):
        tk.Label(frame,
                text=standard['Assessment-standard'],
                anchor="center",
                pady=10,
                font=("Arial", 16)).grid(row=i+2, column=0, sticky="nsew")

        tk.Label(frame,
                text=standard['Credits'],
                anchor="center",
                pady=10,
                font=("Arial", 16)).grid(row=i+2, column=1, sticky="nsew")

        tk.Label(frame,
                text=standard['Internal-or-External'],
                anchor="center",
                pady=10,
                font=("Arial", 16)).grid(row=i+2, column=2, sticky="nsew")
        var = tk.StringVar()
        var.set("Not Attempted")
        drop_down_menu = tk.OptionMenu(frame, var, *grade)
        drop_down_menu.config(
            font=("Arial", 14)
        )
        drop_down_menu["menu"].config(
            font=("Arial", 20)
            )
        drop_down_menu.grid(
            row=i+2,
            column=3,
            sticky="nsew"
        )
        drop_down_vars[(subject_name, standard['Assessment-standard'])] = var
    tk.Button(
        frame,
        text="Back",
        font=("Arial", 14, "bold"),
        command=lambda f=frame: switch_to_course_page(f)
    ).grid(row=len(subject_data["standards"]) + 2, column=3)
    
    tk.Button(
        frame,
        text="Save Grades",
        font=("Arial", 14, "bold"),
        command=saved_grades_function
    ).grid(row=len(subject_data["standards"]) + 3, column=3)
    pages[subject_name] = frame

#===============================================================
#add buttons in course page
row = 1
col = 0
for subject_name in pages:
    tk.Button(
        course_page,
        text=subject_name,
        width=50,
        font=("Arial", 13, "bold"),
        height=2,
        command=lambda n=subject_name: switch_to_standard_page(n)
    ).grid(row=row, column=col, padx=10, pady=10)

    col += 1
    if col == 3:
        col = 0
        row += 1

root.mainloop()