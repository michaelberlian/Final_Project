import matplotlib.pyplot as pl
import matplotlib.animation as animation
import numpy as np
import sys

class Lissajous():
# constructor
    def __init__ (self,radius_1,radius_2,speed_1,speed_2):
        self.radius_1 = radius_1
        self.radius_2 = radius_2

        self.speed_1 = speed_1
        self.speed_2 = speed_2

        self.get_maximum()

        self.constant = 600
#total of the point to be animate
        self.total = self.constant * self.maximum_circle * self.maximum_speed

        self.x_degree = []
        self.y_degree = []
        self.x_coordinate = []
        self.y_coordinate = []

# checking the biggest circle and fastest speed
    def get_maximum (self):
        if (self.radius_2 > self.radius_1):
            self.maximum_circle = self.radius_2
        else : 
            self.maximum_circle = self.radius_1

        if (self.speed_2 > self.speed_1):
            self.maximum_speed = self.speed_2
        else : 
            self.maximum_speed = self.speed_1

    def get_curve(self,repeat_count):
        for i in range (0,repeat_count):
            #find x (first circle)
            self.x_degree = np.linspace(0,(360*self.speed_1),self.total,endpoint="True")

            #find y (second circle)
            self.y_degree = np.linspace(0,(360*self.speed_2),self.total,endpoint="True")

            #find the coordinate of the degree
            for i in (self.x_degree):
                self.x_coordinate.append(self.radius_1 * np.sin(i*3.1415/180))
            for i in (self.y_degree):
                self.y_coordinate.append(self.radius_2 * np.cos(i*3.1415/180))

            # closing the end of the curve
            self.x_coordinate.append(0)
            self.y_coordinate.append(self.radius_2)

    def animate (self,repeat):
        # preparing the figure
        fig = pl.figure(facecolor="#000000")
        fig.canvas.set_window_title('Lissajous Curve')
        ax = fig.add_subplot(111,autoscale_on=False, xlim=(-self.maximum_circle,self.maximum_circle),ylim=(-self.maximum_circle,self.maximum_circle))
        #set of data
        line, = ax.plot([],[],'-',lw=1,color='#FFFFFF',zorder=1)
        ax.text(0.01,self.maximum_circle,"L I S S A J O U S   C U R V E\n", ha="center", color="#FFFFFF", fontsize=12)
        ax.text(0.01,self.maximum_circle, ' ')

        # initialize the animation
        def init():
            line.set_data([],[])
            return line
        # the animation
        def animated(i):
            if repeat.lower() == "n" :
                line.set_data(self.x_coordinate[:i],self.y_coordinate[:i])
            elif repeat.lower() == "y" :
                if i - (self.total*0.75) < 0 :
                    trail = 0
                else :
                    trail = i - int(self.total*0.75)
                line.set_data(self.x_coordinate[trail:i],self.y_coordinate[trail:i])
            
            return line
        ani = animation.FuncAnimation(fig,animated,np.arange(0,len(self.x_coordinate)),interval=1,init_func=init,repeat = False)
        # print(line)
        pl.axis("off")
        # pl.plot(x_coordinate,y_coordinate)
        pl.show()