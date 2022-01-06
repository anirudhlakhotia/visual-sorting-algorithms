import tkinter as tk
from tkinter import Label, font
import matplotlib.pyplot as plt
import matplotlib
import random
matplotlib.use('TkAgg')
from timeit import repeat
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
plt.style.use('seaborn-dark')

root=tk.Tk()
root.title('Dashboard')
root.geometry("550x350")
array = [random.randint(0, 10000) for i in range(10000)]
data = {
            'Bubble Sort': 73.21,
            'Insertion Sort': 56.71,
            'Merge Sort': 0.619,
            'Quick Sort': 0.116,
        }
languages = data.keys()
popularity = data.values()

def init_window(title="Sorting Algorithms v/s Time taken to sort 10000 elements ",data=data):
    button_frame = tk.Frame(root, background="red")
    button_frame.grid(row=0,column=0)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    btn=tk.Button(root,text=title,command=lambda:show_graph(title,data),pady=5)
    btn.grid(row=1,column=0)
    btn.grid_rowconfigure(0, weight=2)
    btn.grid_columnconfigure(0, weight=1)
    btn2=tk.Button(button_frame,text="Bubble Sort",command=lambda:run_algorithm())
    btn2.grid(row=0,column=1,sticky="eW")
    btn3=tk.Button(button_frame,text="Insertion Sort",command=lambda:run_algorithm())
    btn3.grid(row=0,column=2,sticky="eW")
    btn4=tk.Button(button_frame,text="Merge Sort",command=lambda:run_algorithm())
    btn4.grid(row=1,column=1,sticky="eW")
    btn5=tk.Button(button_frame,text="Quick Sort",command=lambda:run_algorithm())
    btn5.grid(row=1,column=2,sticky="eW")
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    root.mainloop()


def run_algorithm(algorithm="bubble_sort",array=array):
    stmt = f"{algorithm}({array})"
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from algorithms import {algorithm}" \
        if algorithm != "sorted" else ""

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    global root
    root.destroy()
    root=tk.Tk()
    root.title(algorithm)
    lbl=tk.Label(root,text=f"Algorithm: {algorithm}")
    lbl.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
    lbl2=tk.Label(root,text=f"Minimum execution time: {min(times)}")
    lbl2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
def show_graph(name, data):
    global root
    root.destroy()
    root=tk.Tk()
    root.title(name)

    languages=data.keys()
    popularity=data.values()

    # create a figure
    figure = Figure(figsize=(8, 8), dpi=100)
    # create FigureCanvasTkAgg object
    figure_canvas = FigureCanvasTkAgg(figure, root)
    # create the toolbar
    NavigationToolbar2Tk(figure_canvas, root)

    # create axes
    axes = figure.add_subplot()
    # create the barchart
    axes.bar(languages, popularity)
    axes.set_title(name, fontsize=16,pad=25)
    axes.set_ylabel('Time taken to sort 10000 elements (seconds)',labelpad=15,fontsize=12)
    axes.set_xlabel('Sorting Algorithms',labelpad=15, fontsize=12)
    
    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    root.title(name)
    root.mainloop()
#show_graph('Sorting Algorithms v/s Popularity', data)

init_window()