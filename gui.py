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
#===============================================================
#display subjects and standards
for subject_name,subject_data in data["ncea_level_3_standards"].items():

    frame = tk.Frame(root)
    frame.grid_columnconfigure(0, weight=1)
    tk.Label(frame,
             text=subject_name,
             anchor="center",
             font=("Arial", 20, "bold")).grid(row=0, column=0, sticky="ew")
    
    for i, standard in enumerate(subject_data["standards"]):
            text = f"{standard['Assessment-standard']} | {standard['Credits']} credits | {standard['Internal-or-External']}"
            tk.Label(
                frame,
                text=text
            ).grid(row=i+1, column=0, sticky="w", padx=20)
            
    tk.Button(
        frame,
        text="Back",
        command=lambda f=frame: switch_to_course_page(f)
    ).grid(row=len(subject_data["standards"]) + 1, column=0, pady=20)

    pages[subject_name] = frame
#===============================================================
# switch pages
def switch_to_standard_page(choosen_subject):
    course_page.grid_forget()
    pages[choosen_subject].grid(row=0, column=0, sticky="nsew")

def switch_to_course_page(current_frame):
    current_frame.grid_forget()
    course_page.grid(row=0, column=0, sticky="nsew")
#===============================================================
#add buttons
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