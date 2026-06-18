import tkinter as tk
from tkinter import messagebox
imprtant database
import sqlite3
TOTAL_SEATS = 13

WINDOW_TITLE = "Booking System"
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 620

COLOR_FREE = "#7DC688"
COLOR_BOOKED = "#FF9E99"
COLOR_DRIVER = "#999999"


root = None

set_buttons = {} # halkani waa buttons ka kuraasta icons ka aan u iticmaalnayo

def make_seat_button(parent, seat_number):
    
    btn = tk.Button(parent, text=str(seat_number), width=5, height=2, font=("Arial", 10, "bold"),
                    relief="raised", command=lambda n=seat_number: on_seat_click(n))
    return btn
def build_bus_layout():
    container = tk.Frame(root, padx=20, pady=20)
    container.pack(fill=tk.BOTH, expand=True)

front_row = tk.Frame(container)
front_row.pack(pady=(0, 10))

driver_label = tk.Label(front_row, text="Driver", bg=COLOR_DRIVER, width=10, height=3,font=("Arial", 10, "bold"), relief="raised")
driver_label.grid(row=0, column=0, padx=5)
seat_one = make_seat_button(front_row, 1)
seat_one.grid(row=0, column=1, padx=5)
seat_buttons[1] = seat_one #kurisiga koowaad

divider = tk.frame(container, height=2, bg="black")
divider.pack()

passenger_section = tk.Frame(container)
passenger_section.pack()

rows_layout = [
    [2, 3,4],
    [5, 6,7],
    [8, 9,10],
    [11,12,13]
]
for row_index, seat_number in enumerate(rows_layout):
    left_a,left_b,right = seat_numbers
    btn_a = make_seat_button(passenger_section, left_a)
    btn_a.grid(row=row_index, column=0, padx=34, pady=3)
    seat_buttons[left_a] = btn_a

    btn_b = make_seat_button(passenger_section, left_b)
    btn_b.grid(row=row_index, column=1, padx=34, pady=3)
    seat_buttons[left_b] = btn_b
# waa space kii u dhaxeyey
    aisle = tk.Frame(passenger_section, width=30)
    aisle.grid(row=row_index, column=2)

    btn_r = make_seat_button(passenger_section, right)
    btn_r.grid(row=row_index, column=3, padx=34, pady=3
    seat_buttons[right] = btn_r
# button kii confirm ka samaynayey
button_bar = tk.Frame(container, pady=15)
button_bar.pack()


refresh_btn = tk.Button(button_bar, text="Refresh", width=12, command=refresh_seats,)

refresh_btn.grid(row=0, column=0, padx=5)

def refresh_seats():
    try:
        booked = set(database.get_booked_seat_number())
    except Exception as e:
        messagebox.showerror("database muu soo akhrisan: ", str(e))
        return
    for seat_num, btn in seat_buttons.items():
        if seat_num in booked:
            btn.config(bg=COLOR_BOOKED, )
        else:
            btn.config(bg=COLOR_FREE,)

def on+seat_click(seat_number):
    try:
        booked = set(database.get_booked_seat_number())
    except Exception as e:
        messagebox.showerror("database muu soo akhrisan: ", str(e))
        return
 
    satus = "Booked" if seat_number in booked else "Free"
    print(f"Cliked seat {seat_number}. Status: {status}") 


 def main():
    global root

    database.init_database()  # Initialize the database 
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.resizable(False, False) # size ka window ka ma badali karno
    build_bus_layout()
    refresh_seats()  # Refresh seat status on startup
    root.mainloop()

if __name__ == "__main__":
    main()   
 
