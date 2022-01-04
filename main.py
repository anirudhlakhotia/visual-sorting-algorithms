import tkinter as tk
from tkinter import font
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
plt.style.use('seaborn-dark')

root=tk.Tk()
root.title('Dashboard')
root.geometry("550x350")

data = {
            'Bubble Sort': 73.21,
            'Insertion Sort': 56.71,
            'Merge Sort': 0.619,
            'Tim Sort': 0.512,
            'Quick Sort': 0.116,
        }
languages = data.keys()
popularity = data.values()

def init_window(title="Sorting Algorithms v/s Time taken to sort 1000 elements ",data=data):
    btn=tk.Button(root,text=title,command=lambda:show_graph(title,data))
    btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    root.mainloop()


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
    axes.set_ylabel('Time taken to sort 1000 elements (seconds)',labelpad=15,fontsize=12)
    axes.set_xlabel('Sorting Algorithms',labelpad=15, fontsize=12)
    
    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    root.title(name)
    root.mainloop()
#show_graph('Sorting Algorithms v/s Popularity', data)
init_window()