from __future__ import division
import matplotlib.pyplot as plt
import sys

def loadData(cpu_data, memory_data, memory_rate_data, file):
    f = open(file)
    for line in f:
        tokens = line.split("\t")
        cpu_data.append(float(tokens[0]))
        memory_data.append(int(tokens[1])/(1024*1024))
        memory_rate_data.append(float(tokens[2]))
        
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.itervalues():
        sp.set_visible(False)

def displayData(x, cpu_data, memory_data, memory_rate_data):
    fig = plt.figure()
    fig.subplots_adjust(right=0.75)
    
    host = fig.add_subplot(111)
    par1 = host.twinx()
    par2 = host.twinx()
    par2.spines["right"].set_position(("axes", 1.05))
    make_patch_spines_invisible(par2)
    par2.spines["right"].set_visible(True)

    p1, = host.plot(x, cpu_data, "b-", label="CPU")
    p2, = par1.plot(x, memory_rate_data, "r-", label="Memory")
    p3, = par2.plot(x, memory_data, "g-", label="Memory Size")

    host.set_ylim(0, max(cpu_data)*1.5)
    par1.set_ylim(0, max(memory_rate_data)*1.5)
    par2.set_ylim(0, max(memory_data)*1.5)

    host.set_xlabel("Time(s)")
    host.set_ylabel("CPU Percentage(%)")
    par1.set_ylabel("Memory Percentage(%)")
    par2.set_ylabel("Memory Size(MB)")

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=8)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)

    lines = [p1, p3, p2]

    host.legend(lines, [l.get_label() for l in lines])

    plt.show()

def process(args):
    file = args[1]
    if file == None:
        print "please input your data file as args"
    #file = "data/pid-7507-benchmark.tsv"
    cpu = []
    memory_data=[]
    memory_rate_data=[]

    print "Loading Data..."
    loadData(cpu, memory_data, memory_rate_data, file)

    num = len(cpu)
    print "Total " + str(num) + "rows of data"
    x = range(1, num+1)

    print "Draw Figure..."
    displayData(x, cpu, memory_data, memory_rate_data)


if __name__ == '__main__':
    process(sys.argv)



    
