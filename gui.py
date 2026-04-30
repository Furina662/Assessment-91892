import tkinter as tk
import json

with open("json/subject.json", "r") as file:
    subject_data = json.load(file)

root = tk.Tk()
root.title("UE Rank Score Calculator")
root.geometry('1000x600')

course_page= tk.Frame(root)
course_page.pack()
tk.Label(course_page, text="please select your course below:", font=("Arial", 16)).pack(pady=20)

for subject_name,subject_data in subject_data["ncea_level_3_standards"].items():

    frame = tk.Frame(root)

    tk.Label(course_page,
             text=subject_name,
             font=("Arial", 14, "bold")).pack(anchor="w")
    
for standard in subject_data["standards"]:
        text = f"{standard['Assessment-standard']} | {standard['Credits']} credits | {standard['Internal-or-External']}"
        tk.Label(
            course_page,
            text=text
        ).pack(anchor="w", padx=20)    

root.mainloop()