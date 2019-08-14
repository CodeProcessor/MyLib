'''
Created on May 04, 2019

@author: dulan
'''
import matplotlib.pyplot as plt
import numpy as np
import os.path as osp
import os

class Graph(object):
    def __init__(self, save_loc = 'output', filename='untitled'):
        self.save_loc = save_loc
        if not osp.exists(self.save_loc):
            os.makedirs(self.save_loc)
        self.filename = self.set_filename(filename)
        self.ylabel = ''
        self.xlabel = ''
        self.title = ''
        self.legend_1 = None
        self.legend_2 = None

    def set_filename(self, filename):
        self.filename= osp.join(self.save_loc, filename + '.png')

    def set_lables(self, title, xlabel, ylabel_1, ylabel_2=''):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel_1
        self.ylabel_2 = ylabel_2

    def set_legends(self, legend_1, legend_2, legend_3):
        self.legend_1 = legend_1
        self.legend_2 = legend_2
        self.legend_3 = legend_3

    def set_names(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)

    def plot(self, a_list, filename=None):
        self.set_names()
        plt.plot(a_list)
        if filename is not None:
            self.set_filename(filename)
        if self.legend_1 is not None:
            plt.gca().legend((self.legend_1))
        plt.savefig(self.filename+'.png')
        plt.clf()

    def plot_xy(self, x_list, y_list, filename=None):
        self.set_names()
        plt.plot(y_list, x_list)
        if filename is not None:
            self.set_filename(filename)
        plt.savefig(self.filename+'.png')
        plt.clf()

    def plot_2(self, a_list, b_list, filename=None):
        self.set_names()
        plt.plot(a_list)
        plt.plot(b_list)
        if self.legend_1 is not None and self.legend_2 is not None:
            plt.gca().legend((self.legend_1, self.legend_2))
        if filename is not None:
            self.set_filename(filename)
        plt.savefig(self.filename+'.png')
        plt.clf()

    def plot_2sub(self, a_list, b_list, filename=None):
        self.set_names()
        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_title(self.title)
        ax1.set_xlabel(self.xlabel)
        ax1.set_ylabel(self.ylabel, color=color)
        ax1.plot(a_list, color=color, label=self.legend_1)
        ax1.tick_params(axis='y', labelcolor=color)

        color = 'tab:blue'
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        ax2.set_ylabel(self.ylabel_2, color=color)  # we already handled the x-label with ax1
        ax2.plot(b_list, color=color, label=self.legend_2)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()

        if filename is not None:
            self.set_filename(filename)
        plt.savefig(self.filename+'.png')
        plt.clf()

    def plot_3sub(self, a_list, b_list, c_list, filename=None):
        self.set_names()
        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_title(self.title)
        ax1.set_xlabel(self.xlabel)
        ax1.set_ylabel(self.ylabel, color=color)
        ax1.plot(a_list, color=color, label=self.legend_1)
        ax1.tick_params(axis='y', labelcolor=color)

        color = 'tab:blue'
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        ax2.set_ylabel(self.ylabel_2)  # we already handled the x-label with ax1
        ax2.plot(b_list, color=color, label=self.legend_2)
        # ax2.tick_params(axis='y', labelcolor=color)

        color = 'tab:green'
        ax2.plot(c_list, color=color, label=self.legend_3)

        fig.tight_layout()
        ax1.legend()
        ax2.legend()

        if filename is not None:
            self.set_filename(filename)
        plt.savefig(self.filename+'.png')
        plt.clf()


if __name__ == '__main__':
    gr_obj = Graph('hello3')
    # gr_obj.set_lables('this is title', 'x label', 'y label')
    # gr_obj.set_legends('legend 1', 'legend_2', 'legend_3')
    # gr_obj.plot_3sub([1, 2, 3], [10, 25, 30], [5, 35, 30])

    list1 = [1, 0.5, 0.4]
    list2 = [0.5, 0.7, 0.78]
    list3 = [0.5, 0.69, 0.75]
    gr_obj.set_lables('main', 'label1', 'label2', 'label3')
    gr_obj.set_legends('main', 'label1', 'label2')
    gr_obj.plot_3sub(list1, list2, list3, 'plot-xy')
