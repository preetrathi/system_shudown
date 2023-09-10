import os
import tkinter as tk

# Function to change button color on hover
def on_enter(event):
    event.widget.config(bg='lightgreen')

# Function to change button color back to default
def on_leave(event):
    event.widget.config(bg='SystemButtonFace')

# Define button texts and associated command functions
buttons = [
    ("Restart", lambda: os.system("shutdown /r /t 1")),
    ("Restart Time", lambda: os.system("shutdown /r /t 20")),
    ("Log Out", lambda: os.system("shutdown -l")),
    ("Shut Down", lambda: os.system("shutdown /s /t 1")),
]

# Create a Tkinter window
st = tk.Tk()
st.title("Shut Down App")
st.geometry("500x500")
st.config(bg='lightblue')

# Create and place buttons
button_height = 50
button_width = 200
y_position = 60

for button_text, command_function in buttons:
    button = tk.Button(
        st,
        text=button_text,
        font=('Times New Roman', 25, 'bold'),
        relief=tk.RAISED,
        cursor='plus',
        command=command_function
    )
    button.place(x=150, y=y_position, height=button_height, width=button_width)
    y_position += 110  # Adjust the vertical position for the next button

    # Bind the hover events to the button
    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)

# Start the Tkinter main loop
st.mainloop()
d