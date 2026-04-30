import tkinter as tk
import json

with open("json/subject.json", "r") as file:
    data = json.load(file)

root = tk.Tk()
root.title("UE Rank Score Calculator")
root.geometry('1000x600')
#===============================================================

course_page= tk.Frame(root)
course_page.pack(fill="both", expand=True)

tk.Label(course_page, text="please select your course below:", font=("Arial", 16)).pack(pady=20)

pages = {}
#===============================================================
#display subjects and standards
for subject_name,subject_data in data["ncea_level_3_standards"].items():

    frame = tk.Frame(root)

    tk.Label(frame,
             text=subject_name,
             font=("Arial", 14, "bold")).pack(anchor="w")
    
    for standard in subject_data["standards"]:
            text = f"{standard['Assessment-standard']} | {standard['Credits']} credits | {standard['Internal-or-External']}"
            tk.Label(
                frame,
                text=text
            ).pack(anchor="w", padx=20)

    pages[subject_name] = frame
#===============================================================
# switch pages
def switch_to_standard_page(choosen_subject):
    course_page.pack_forget()
    pages[choosen_subject].pack(fill="both", expand=True)

def switch_to_course_page(current_frame):
    current_frame.pack_forget()
    course_page.pack(fill="both", expand=True)
#===============================================================
#add buttons
for subject_name in pages:
    tk.Button(
        course_page,
        text=subject_name,
        command=lambda n=subject_name: switch_to_standard_page(n)
    ).pack(pady=5)
    
root.mainloop()