from tkmacosx import Button
from timeit import repeat
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
         FigureCanvasTkAgg, NavigationToolbar2Tk
         )
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib
import random
matplotlib.use("TkAgg")


plt.style.use("seaborn-dark")


def make_root() -> tk.Tk:
    '''Creates a root window

    Parameters
    ----------
    None

    Returns
    -------
    root : tk.Tk
    a Tkinter Window
    
    '''
    
    root = tk.Tk()
    root.title("Home")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(background="black")
    return root


def init_window(title: str = "Comparison when unsorted ") -> None:

    '''Creates a window

    Parameters
    ----------
    title : str,optional
    The title of the window

    Returns
    -------
    None
    '''
    root = make_root()

    def run_algorithm(
        algorithm: str,
        array: list = [random.randint(0, 10000) for i in range(5000)],
        n:int=5000,
    ) -> float:
        '''Runs an algorithm out of the list of algorithms
        
        Parameters
        ----------
        algorithm : str
        The name of the algorithm to run
        array : list, optional
        The array to carry out the operation on

        Returns
        -------
        time : float
        Minimum time taken for the algorithm to run on the array
        '''
        if array is None:
            array = [random.randint(0, 10000) for i in range(n)]
        if button_frame:
            button_frame.destroy()
            heading.destroy()
        else:
            pass
        titles = {
            "bubble_sort": "Bubble Sort",
            "insertion_sort": "Insertion Sort",
            "merge_sort": "Merge Sort",
            "quicksort": "Quick Sort",
        }
        stmt = f"{algorithm}({array})"
        # Set up the context and prepare the call to the specified
        # algorithm using the supplied array. Only import the
        # algorithm function if it's not the built-in `sorted()`.
        setup_code = (
            f"from algorithms import {algorithm}"
            if algorithm != "sorted"
            else ""
        )

        # Execute the code ten different times and return the time
        # in seconds that each execution took
        times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
        # Finally, display the name of the algorithm and the
        # minimum time it took to run

        root.title(titles[algorithm])

        algo_name = tk.Label(
            root,
            text=titles[algorithm],
            bg="black",
            fg="#C0C0C0",
            font=("Helvetica", 36),
        )
        algo_name.place(relx=0.5, rely=0.05, anchor=tk.N)
        min_time = tk.Label(
            root,
            text=f"Minimum time to sort {n} elements: \
{ round(min(times),5)/10} seconds",
            bg="black",
            fg="green",
            font=("Helvetica", 26),
        )
        min_time.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        time_complexity = tk.Label(
            root,
            text=f"Time Complexity: {complexity[algorithm]}",
            bg="black",
            fg="#057DCD",
            font=("Helvetica", 26),
        )
        time_complexity.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        description = tk.Label(
            root,
            text=descriptions[algorithm],
            bg="black",
            fg="#C0C0C0",
            font=("Helvetica", 24),
            justify=tk.LEFT,
        )
        description.place(relx=0.5, rely=0.2, anchor=tk.N)

        def back():
            '''Returns to the main menu

            Parameters
            ----------
            None

            Returns
            -------
            None
            '''
            root.destroy()
            init_window()

        back_btn = Button(
            root,
            text="Back",
            command=back,
            bg="#C0C0C0",
            borderless=True,
            fg="black",
            activebackground="black",
            activeforeground="#C0C0C0",
        )
        back_btn.place(x=10, y=10)
        return min(times)/10

    heading = tk.Label(
        root,
        text="Analysis of Sorting Algorithms",
        bg="black",
        fg="white",
        font=("Helvetica", 36),
    )
    heading.place(relx=0.5, rely=0.05, anchor=tk.N)
    button_frame = tk.Frame(root, bg="black")
    button_frame.grid(row=0, column=0)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def get_value(win:tk.Tk,name: str,function:any) -> None:
        '''Gets the value of the input box

        Parameters
        ----------
        win : tk.Tk
        The previous window to pass

        name : str
        The name for creating title for the next window

        function : any
        Used to differentiate between the function to run based on origin of the call

        Returns
        -------
        None
        '''

        n=0
        is_make=id(function) == id(make_graph)
        def submit():
            nonlocal n
            n=int(e1.get())
            root.destroy()
            if is_make :
                make_graph(win,name,n)
            else:
                array = [random.randint(0, 10000) for i in range(n)]
                run_algorithm(function,array,n)
    
        root=make_root()
        tk.Label(root, text="Enter the number of elements you wish to sort",bg=root['bg'],font=("Helvetica", 24)).place(relx=0.5, rely=0.1, anchor=tk.N,)
        e1 = tk.Entry(root,insertbackground="black",bg="black",fg="#C0C0C0",font=("Helvetica", 24))
        e1.place(relx=0.5, rely=0.2, anchor=tk.N)
        submit_btn=Button(root,text="Submit",command=submit,bg="#C0C0C0",borderless=True,fg="black",activebackground="black",activeforeground="#C0C0C0",padx=10,pady=10,font=("Helvetica", 24))
        submit_btn.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        root.mainloop()
        

    def make_graph(win: tk.Tk, name: str, n:int) -> None:
        #print(f"N in make graph is {n}")
        '''Creates a graph of the time taken to sort an array
         
        Parameters
        ----------
        win : tk.Tk 
        The previous window

        name : str
        The title of the window

        Returns
        -------
        None
        '''
       # print("MAKE GRAPH N",n)
        array = [random.randint(0, 10000) for i in range(n)]
        sorted_array = sorted(array)
        if name == "Comparison when fully sorted":
            data = {
                "Bubble Sort": run_algorithm("bubble_sort", sorted_array, n),
                "Insertion Sort": run_algorithm(
                    "insertion_sort", sorted_array,n
                    ),
                "Merge Sort": run_algorithm("merge_sort", sorted_array,n),
                "Quick Sort": run_algorithm("quicksort", sorted_array,n),
            }
        elif name == "Comparison when partially sorted":
            partiallly_sorted_array = sorted_array[: len(array) // 2] + [
                random.randint(0, 10000) for i in range(len(array) // 2)
            ]
            data = {
                "Bubble Sort": run_algorithm(
                    "bubble_sort", partiallly_sorted_array,n
                    ),
                "Insertion Sort": run_algorithm(
                    "insertion_sort", partiallly_sorted_array,n
                ),
                "Merge Sort": run_algorithm(
                    "merge_sort", partiallly_sorted_array,n
                    ),
                "Quick Sort": run_algorithm(
                    "quicksort", partiallly_sorted_array,n
                    ),
            }
        else:
            data = {
                "Bubble Sort": run_algorithm("bubble_sort", array,n),
                "Insertion Sort": run_algorithm("insertion_sort", array,n),
                "Merge Sort": run_algorithm("merge_sort", array,n),
                "Quick Sort": run_algorithm("quicksort", array,n),
            }
        show_graph(root, name, data,n)
    
    unsorted_btn = Button(
        root,
        text=title,
        font=("Helvetica", 20),
        command=lambda: get_value(root, title, make_graph),
        pady=15,
        borderless=True,
        bg="yellow",
        fg="#252930",
        activebackground="white",
        activeforeground="black",
    )
    unsorted_btn.place(anchor=tk.N, relx=0.8, rely=0.7)

    sorted_btn = Button(
        root,
        text="Comparison when fully sorted",
        font=("Helvetica", 20),
        borderless=True,
        command=lambda: get_value(root, "Comparison when fully sorted",make_graph),
        pady=15,
        bg="#32CBF1",
        fg="#252930",
        activebackground="white",
        activeforeground="black",
    )
    sorted_btn.place(anchor=tk.N, relx=0.5, rely=0.7)

    partially_sorted_btn = Button(
        root,
        text="Comparison when partially sorted",
        font=("Helvetica", 20),
        borderless=True,
        command=lambda: get_value(root, "Comparison when partially sorted",make_graph),
        pady=15,
        bg="#6ECB5A",
        fg="#252930",
        activebackground="white",
        activeforeground="black",
    )
    partially_sorted_btn.place(anchor=tk.N, relx=0.2, rely=0.7)
   
    bubble_sort_btn = Button(
        button_frame,
        text="Bubble Sort",
        font=("Helvetica", 20),
        command=lambda: get_value(root,"Bubble Sort","bubble_sort"),
        borderless=True,
        pady=25,
        padx=25,
        bg="#1b1b1b",
        fg="#C0C0C0",
        activebackground="white",
        activeforeground="black",
    )
    bubble_sort_btn.grid(row=0, column=1, sticky="eW")

    insertion_sort_btn = Button(
        button_frame,
        text="Insertion Sort",
        font=("Helvetica", 20),
        command=lambda: get_value(root,"Insertion Sort","insertion_sort"),
        borderless=True,
        pady=25,
        padx=25,
        bg="#1b1b1b",
        fg="#C0C0C0",
        activebackground="white",
        activeforeground="black",
    )
    insertion_sort_btn.grid(row=0, column=2, sticky="eW")

    merge_sort_btn = Button(
        button_frame,
        text="Merge Sort",
        font=("Helvetica", 20),
        command=lambda: get_value(root,"Merge Sort","merge_sort"),
        borderless=True,
        pady=25,
        bg="#1b1b1b",
        fg="#C0C0C0",
        activebackground="white",
        activeforeground="black",
    )
    merge_sort_btn.grid(row=1, column=1, sticky="eW")

    quicksort_btn = Button(
        button_frame,
        text="Quick Sort",
        font=("Helvetica", 20),
        command=lambda: get_value(root,"Quick Sort","quicksort"),
        borderless=True,
        pady=25,
        bg="#1b1b1b",
        fg="#C0C0C0",
        activebackground="white",
        activeforeground="black",
    )
    quicksort_btn.grid(row=1, column=2, sticky="eW")

    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    root.configure(bg="black")
    root.mainloop()


def show_graph(win: tk.Tk, name: str, data: dict,n=5000) -> None:
    '''Shows the graph of the comparison amongst algorithms for a given array
       
    Parameters
    ----------
    win : tk.Tk
        Previous window that is to be destroyed
    name : str
        The title for the new window
    data : dict
        The data to be plotted

    Returns
    -------
    None
    '''
    win.destroy()
    root = make_root()
    root.title(name)
    languages = data.keys()
    time = data.values()

    # create a figure
    figure = Figure(
        figsize=(8, 8), dpi=100, facecolor="black", edgecolor="black"
        )
    # create FigureCanvasTkAgg object
    figure_canvas = FigureCanvasTkAgg(figure, root)
    # create the toolbar
    toolbar = NavigationToolbar2Tk(
        figure_canvas,
        root,
    )
    toolbar.configure(background="black")

    def back():
        '''Returns to the main menu
        
    Parameters
    ----------
    None

    Returns
    -------
    None
        '''
        root.destroy()
        init_window()

    topLeftFrame = tk.Frame(root, bg="black")
    topLeftFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    back_btn = Button(
        topLeftFrame,
        text="Back",
        command=back,
        borderless=True,
        activebackground=root["bg"],
        activeforeground="#C0C0C0",
    )
    back_btn.place(x=10, y=10)
    # create axes
    axes = figure.add_subplot()
    # create the barchart
    axes.bar(languages, time, color="#6669eb")
    axes.set_title(name, fontsize=36, pad=25, color="#C0C0C0")
    axes.set_ylabel(
        f"Time taken to sort {n} elements (seconds)",
        labelpad=15,
        fontsize=26,
        color="#C0C0C0",
    )
    axes.set_xlabel(
        "Sorting Algorithms", labelpad=15, fontsize=26, color="#C0C0C0"
        )
    axes.set_facecolor("black")
    axes.tick_params(axis="y", colors="#C0C0C0")
    axes.tick_params(axis="x", colors="#C0C0C0")

    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()


descriptions = {
    "bubble_sort": """Bubble Sort, sometimes referred to as sinking sort,
is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.""",
    "insertion_sort": "Insertion Sort is a simple sorting algorithm, \
that builds the final sorted array (or list) one item at a time.",
    "merge_sort": """Merge Sort comparison-based sorting algorithm. Most implementations
produce a stable sort, which means that the order of equal elements is the
same in the input and output. Merge sort is a divide and conquer algorithm""",
    "quicksort": "Quicksort is a divide-and-conquer algorithm.\n\
It works by selecting a 'pivot' element from the array \
and partitioning the other elements into two sub-arrays,\n\
according to whether they are less than or greater than the pivot\n\
For this reason, it is sometimes called partition-exchange sort.\n\
The sub-arrays are then sorted recursively. ",
}

complexity = {
    "bubble_sort": "O(n^2)",
    "insertion_sort": "O(n^2)",
    "merge_sort": "O(n log n)",
    "quicksort": "O(n log n)",
}
init_window()
