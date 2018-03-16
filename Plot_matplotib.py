import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import time
a

class Plot(object):
    def __init__(self, *args, **kwargs):
        self.xdata = list()
        self.ydata = list()
        self.xerror = list()
        self.yerror = None
        self.color = None
        self.marker = None
        self.size = None
        self.xlabel = None
        self.ylabel = None
        self.label = None
        self.fontsize = 30
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @classmethod
    def get_data(cls, filename):
        xerror = list()
        yerror = list()
        xdata = []
        ydata = []
        data = pd.read_csv(filename)
        for i, col in enumerate(data.columns.values.tolist()):
            if col.startswith('X'):
                xdata.append(data[col])
            if col == 'Yerror':
                yerror.append(data[col])
            if col.startswith('Y'):
                ydata.append(data[col])
        new = cls(xdata=xdata, ydata=ydata, xerror=None, yerror=None)
        return new

    def set_up(self):
        fig = plt.figure(figsize=(14,7))
        # matplotlib.rcParams[]
        plt.setp(fig.gca().spines['bottom'].set_linewidth(2))  # set the linewidth of each axis
        plt.setp(fig.gca().spines['left'].set_linewidth(2))
        plt.setp(fig.gca().spines['right'].set_linewidth(2))
        plt.setp(fig.gca().spines['top'].set_linewidth(2))
        matplotlib.rcParams['xtick.direction'] = 'out'  # x tick out or in (global)
        plt.tight_layout()  # solve the X label doesnot show fully
        plt.tick_params(labelsize=24)  # set the size of axis
        plt.xlabel(self.xlabel, fontsize=self.fontsize), plt.ylabel(self.ylabel, fontsize=self.fontsize)
        plt.gca().axes.tick_params(direction='out', top=True, right=True, length=10, width=2, which='both')  # set the length and width of each tick together

    def plot_2D(self):
        self.set_up()
        # param = {'xtick.direction': 'in', 'figure.autolayout': True}
        # fig.set_size_inches(5.5, 5.5)  # set the size of the figure
        # matplotlib.rc('axes.spines', top=True, right=True) # set the global of tick
        # matplotlib.rcParams.update(param)
        for i in range(len(self.xdata)):
            plt.plot(self.xdata[i], self.ydata[i], 'o-', label=self.label,  markersize=20, markerfacecolor='None', linewidth=3, \
                 )
        # plt.text(10.2, .9, s='test', fontsize=24, rotation=0, wrap=True)  # add test to the plot
        # plt.subplots_adjust(bottom=0)  # adjust the fig if text
        # plt.scatter(self.xdata, self.ydata, marker='o', s=280, c='red', alpha=1, edgecolors=None)



        # plt.errorbar(self.xdata, self.ydata, yerr=self.yerror, barsabove=True, capsize=3, capthick=3, marker='o')
        # plt.fill_between(self.xdata, self.ydata+self.yerror, self.ydata-self.yerror, alpha=0.4, color='red')

        plt.legend(loc=0, fontsize=24, frameon=False)
        plt.savefig('test', dpi=200)
        plt.close()


    def two_Yaxis(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        plt.plot(sth)
        ax2 = ax1.twin()

    def chart(self):
        self.set_up()
        for i in range(len(self.xdata)):
            plt.bar(self.xdata[i], self.ydata[i], width=0.03)
            plt.plot(self.xdata[i], self.ydata[i], linewidth=3)
        plt.tight_layout()
        plt.savefig('test', dpi=200)
        plt.close()


plot = Plot().get_data('test.csv')
plot.chart()





