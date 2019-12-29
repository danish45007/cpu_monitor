try:
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from psutil import cpu_percent
except Exception as e:
    print("Some modules are missing {}".format(e))

cpu = cpu_percent()
#print(cpu)

y = []
frame_len = 200
def animation(i):
    y.append(cpu_percent())
    if len(y)<= frame_len:
        plt.cla()
        plt.plot(y,'r',label="Real time CPU Uses")
        
    else:
        plt.cla()
        plt.plot(y[-frame_len],"r",label="Real time CPU Uses")
        
    plt.ylim(0,100)
    plt.xlabel("Time(s)")
    plt.ylabel("CPU Uses(%)")
    plt.legend(loc="upper right")
    plt.tight_layout()
ani = FuncAnimation(plt.gcf(),animation,interval=1000)
plt.show()
