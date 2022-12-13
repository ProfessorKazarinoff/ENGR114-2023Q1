# plot_data.py

import matplotlib.pyplot as plt

def plot_data(wd,a):
    # dictionary that produces the unit needed in the y-axis label
    unit_d = {'humidity':'%','temperature':'F','rainfall':'in/min','pressure':'Hg'}
    unit = unit_d[a[0]]

    # fig, ax
    fig, ax = plt.subplots()

    # plot
    ax.plot(wd)

    # customize
    ax.set_title(f"Plot of temperature in Natick, MA using past {a[1]} data points")
    ax.set_ylabel(f"{a[0]} ({unit})")
    ax.set_xlabel("Data Point Number")

    # show the plot
    plt.show()