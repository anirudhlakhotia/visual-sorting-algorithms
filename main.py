import platform

if platform.system() == "Darwin":
    from tkmacosx import Button
else:
    from tkinter import Button
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib
import random
matplotlib.use('TkAgg')
from timeit import repeat
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk)

plt.style.use('seaborn-dark')
def make_root():
    root=tk.Tk()
    root.title('Home')
    root.geometry("550x450")
    return root

def init_window(title="Comparison when unsorted "):
    root=make_root()
    def run_algorithm(algorithm,array = [random.randint(0, 10000) for i in range(5000)]):
        if button_frame:
            button_frame.destroy()
        else:
            pass
        titles={"bubble_sort":"Bubble Sort","insertion_sort":"Insertion Sort","merge_sort":"Merge Sort","quicksort":"Quick Sort"}
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

        root.title(titles[algorithm])
        root.geometry("550x550")
        lbl=tk.Label(root,text=titles[algorithm],bg='black',fg='white',font=("Helvetica", 28))
        lbl.place(relx=0.5, rely=0.05, anchor=tk.N)
        lbl2=tk.Label(root,text=f"Minimum time to sort 5000 elements: {round(min(times),5)} seconds" ,bg='black',fg='green',font=("Helvetica", 16))
        lbl2.place(relx=0.5, rely=0.55, anchor=tk.N)
        lbl4=tk.Label(root,text=f"Time Complexity: {complexity[algorithm]}" ,bg='black',fg='#48d2ff',font=("Helvetica", 16))
        lbl4.place(relx=0.5, rely=0.5, anchor=tk.N)
        lbl3=tk.Label(root,text=descriptions[algorithm],bg='black',fg='white',font=("Helvetica", 12),justify=tk.LEFT)
        lbl3.place(relx=0.5,rely=0.3,anchor=tk.N)
        def back():
            root.destroy()
            init_window()
        back_btn=Button(root,text="Back",command=back,bg='white',fg='black',activebackground='black',activeforeground='white')
        back_btn.place(x=10,y=10)
        return min(times)


    button_frame = tk.Frame(root,bg='black')
    button_frame.grid(row=0,column=0)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def make_graph(win,name):
        array=[random.randint(0, 10000) for i in range(5000)]
        sorted_array=sorted(array)
        if name == "Comparison when fully sorted":
            data={
                'Bubble Sort': run_algorithm('bubble_sort',sorted_array),
                'Insertion Sort': run_algorithm('insertion_sort',sorted_array),
                'Merge Sort': run_algorithm('merge_sort',sorted_array),
                'Quick Sort': run_algorithm('quicksort',sorted_array)
                 }
        elif name == "Comparison when partially sorted":
            partiallly_sorted_array=sorted_array[:len(array)//2]+[random.randint(0, 10000) for i in range(len(array)//2)]
            data={
                'Bubble Sort': run_algorithm('bubble_sort',partiallly_sorted_array),
                'Insertion Sort': run_algorithm('insertion_sort',partiallly_sorted_array),
                'Merge Sort': run_algorithm('merge_sort',partiallly_sorted_array),
                'Quick Sort': run_algorithm('quicksort',partiallly_sorted_array)
            }
        else:
             data = {
                'Bubble Sort': run_algorithm('bubble_sort',array),
                'Insertion Sort': run_algorithm('insertion_sort',array),
                'Merge Sort': run_algorithm('merge_sort',array),
                'Quick Sort': run_algorithm('quicksort',array)
                    }
        show_graph(root,name,data)
        
    btn=Button(root,text=title,command=lambda:make_graph(root,title),pady=5,bg="black",fg="white",activebackground='white',activeforeground='black')
    sorted_btn=Button(root,text="Comparison when fully sorted",command=lambda:make_graph(root,"Comparison when fully sorted"),pady=5,bg="black",fg="white",activebackground='white',activeforeground='black')
    sorted_btn.place(anchor=tk.N,relx=0.5,rely=0.65)
    partially_sorted_btn=Button(root,text="Comparison when partially sorted",command=lambda:make_graph(root,"Comparison when partially sorted"),pady=5,bg="black",fg="white",activebackground='white',activeforeground='black')
    partially_sorted_btn.place(anchor=tk.N,relx=0.5,rely=0.75)
    btn.place(anchor=tk.N,relx=0.5,rely=0.85)
    btn2=Button(button_frame,text="Bubble Sort",command=lambda:run_algorithm("bubble_sort"),pady=10,bg="black",fg="white",activebackground='white',activeforeground='black')
    btn2.grid(row=0,column=1,sticky="eW")
    btn3=Button(button_frame,text="Insertion Sort",command=lambda:run_algorithm("insertion_sort"),pady=10,bg="black",fg="white",activebackground='white',activeforeground='black')
    btn3.grid(row=0,column=2,sticky="eW")
    btn4=Button(button_frame,text="Merge Sort",command=lambda:run_algorithm("merge_sort"),pady=10,bg="black",fg="white",activebackground='white',activeforeground='black')
    btn4.grid(row=1,column=1,sticky="eW")
    btn5=Button(button_frame,text="Quick Sort",command=lambda:run_algorithm("quicksort"),pady=10,bg="black",fg="white",activebackground='white',activeforeground='black')
    btn5.grid(row=1,column=2,sticky="eW")
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    root.configure(bg='black')
    root.mainloop()
    


def show_graph(win,name, data):
    win.destroy()
    root=tk.Tk()
    root.title(name)
    root.geometry("650x450")
    root.configure(bg='black')
    languages=data.keys()
    time=data.values()

    # create a figure
    figure = Figure(figsize=(8, 8), dpi=100, facecolor='black', edgecolor='black')
    # create FigureCanvasTkAgg object
    figure_canvas = FigureCanvasTkAgg(figure, root)
    # create the toolbar
    toolbar=NavigationToolbar2Tk(figure_canvas, root,)
    toolbar.configure(background='black')
    def back():
        root.destroy()
        init_window()
    topLeftFrame = tk.Frame(root,bg='black')
    topLeftFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
    back_btn=Button(topLeftFrame,text="Back",command=back,activebackground=root['bg'],activeforeground="white")
    back_btn.place(x=10,y=10)
    # create axes
    axes = figure.add_subplot()
    # create the barchart
    axes.bar(languages, time,color='#6669eb')
    axes.set_title(name, fontsize=16,pad=25,color='white')
    axes.set_ylabel('Time taken to sort 5000 elements (seconds)',labelpad=15,fontsize=12,color='white')
    axes.set_xlabel('Sorting Algorithms',labelpad=15, fontsize=12,color='white')
    axes.set_facecolor('black')
    axes.tick_params(axis='y', colors='white')
    axes.tick_params(axis='x', colors='white')

    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    back_btn=Button(root,text="Back",command=back,bg='white',fg='black',activebackground='black',activeforeground='white')
    back_btn.place(x=10,y=10)
 
    root.mainloop()
descriptions={"bubble_sort":'''Bubble Sort, sometimes referred to as sinking sort,
is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.'''
,"insertion_sort":'''Insertion Sort is a simple sorting algorithm,that builds the final sorted array (or list) one item at a time. ''',
"merge_sort":'''Merge Sort comparison-based sorting algorithm. Most implementations
produce a stable sort, which means that the order of equal elements is the
same in the input and output. Merge sort is a divide and conquer algorithm''',
"quicksort":''' Quicksort is a divide-and-conquer algorithm.\n It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays,\n according to whether they are less than or greater than the pivot
 For this reason, it is sometimes called partition-exchange sort.\n The sub-arrays are then sorted recursively. '''}
complexity={"bubble_sort":"O(n^2)","insertion_sort":"O(n^2)","merge_sort":"O(n log n)","quicksort":"O(n log n)"}
init_window()