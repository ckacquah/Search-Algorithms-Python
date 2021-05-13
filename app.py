# Author: Acquah Cyril Kofi
# Index N0: 10686868
# Date: 2/14/2021
# Copyright (C) 2021

import graph
import tkinter

from tkinter import ttk
from tree import *

WINDOW_WIDTH = 570
WINDOW_HEIGHT = 460
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400


class Application:
    def __init__(self):
        # init tk
        self.root = tkinter.Tk()

        self.graph = None
        self.header = None
        self.footer = None
        self.go_button = None
        self.statistics = {}
        self.destination = None
        self.destination_entry = None
        self.destination_value = None
        self.algorithm = None
        self.algorithm_type = None
        self.algorithm_value = None
        self.algorithm_type_value = None
        self.choose_algorithm = None
        self.choose_algorithm_type = None
        self.createHeader()
        self.createGraph()
        self.createFooter()

    def run(self):
        self.root.title("Tree Searching")
        self.root.configure(background="white")
        self.root.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.root.mainloop()

    def getGraph(self):
        return self.graph

    def getDestination(self):
        return self.destination.get()

    def createGraph(self):
        self.graph = graph.Graph(self.root, CANVAS_HEIGHT, CANVAS_WIDTH, 10)
        self.graph.setXLabels(0, 200)
        self.graph.setYLabels(200, 0)
        self.graph.getCanvas().grid(row=1, columnspan=6)

    def getAlgorithm(self):
        algo = self.algorithm.get()
        if algo == "Breath First":
            return BREATH_FIRST
        elif algo == "Depth First":
            return DEPTH_FIRST
        elif algo == "Uniform Cost":
            return UNIFORM_COST

    def createHeader(self):
        self.header = tkinter.Frame(self.root)
        self.header.grid(row=0, column=0)

        tkinter.Label(self.header, text="Algorithm").grid(row=0, column=1)
        tkinter.Label(self.header, text="Destination").grid(row=0, column=3)

        algorithm_types = ("Uninformed", "Informed")
        self.algorithm_type = tkinter.StringVar()
        self.algorithm_type_value = tkinter.StringVar().get()
        self.choose_algorithm_type = tkinter.ttk.Combobox(
            self.header, textvariable=self.algorithm_type_value, state="readonly")
        self.choose_algorithm_type["values"] = algorithm_types
        self.choose_algorithm_type.grid(row=0, column=0)
        self.choose_algorithm_type.current(0)

        algorithms = ("Breath First",  "Depth First", "Uniform Cost")
        self.algorithm = tkinter.StringVar()
        self.algorithm_value = tkinter.StringVar().get()
        self.choose_algorithm = tkinter.ttk.Combobox(
            self.header, textvariable=self.algorithm, state="readonly")
        self.choose_algorithm["values"] = algorithms
        self.choose_algorithm.grid(row=0, column=2)
        self.choose_algorithm.current(0)

        self.destination = tkinter.StringVar()
        self.destination.set("Mankessim")
        self.destination_value = self.destination.get()
        self.destination_entry = tkinter.Entry(
            self.header, textvariable=self.destination)
        self.destination_entry.grid(row=0, column=4)

        self.go_button = tkinter.Button(self.header, text="Go")
        self.go_button.grid(row=0, column=5)

    def onClick(self, callback):
        self.go_button.bind('<Button-1>', callback)

    def createFooter(self):
        footer_feilds = [
            ("Algorithm:",      "N/A", "name"),
            ("Start:",          "N/A", "start"),
            ("End:",            "N/A", "end"),
            ("Nodes Visited:",  "N/A", "visited"),
            ("Runtime:",        "N/A", "time"),
        ]
        self.footer = tkinter.Frame(self.root)
        self.footer.grid(row=2, column=0)

        i = 0
        for n in footer_feilds:
            row = 0
            column = i
            key = n[0]
            value = n[1]
            _key = n[2]
            titleFont = ('', 10, 'bold')
            valueFont = ('', 10, 'normal')
            str_value = tkinter.StringVar()
            str_value.set(str(value))
            widget = tkinter.Label(self.footer, text=str(key))
            widget.grid(row=row, column=column)
            widget.config(font=titleFont)
            widget.config(fg="black", bg="#62C2CC")
            widget = tkinter.Label(self.footer, textvariable=str_value)
            widget.grid(row=row, column=column+1)
            widget.config(font=valueFont)
            widget.config(fg="#423f3e", bg="#62C2CC")
            self.statistics.update({_key: str_value})
            i += 2

    def updateFooter(self, map):
        keys = list(map.keys())
        for key in keys:
            if key != "node":
                self.statistics[key].set(str(map[key]))
