import random
from stack_implementation import Stack
# import tkinter library
import tkinter as tk
# create a tkinter window
root=tk.Tk()
root.title('Rectangle with Evenly Spaced Ovals')

# create a canvas widget to draw on
canvas=tk.Canvas(root,width=600,height=600)
canvas.pack()

# coordinates and dimensions of the rectangle
rect_x1,rect_y1=50,50  #Top-left corner
rect_x2,rect_y2=350,500 #Bottom-right corner

# Draw the rectangle
canvas.create_rectangle(rect_x1,rect_y1,rect_x2,rect_y2,outline='black',fill='white')


# calculate the position of the spring line
# spring_x1=rect_x1
# spring_x2=rect_x2
# spring_y=oval_y2+10


# # Draw the spring line
# canvas.create_line(spring_x1,spring_y,spring_x2,spring_y,fill='green',width=3)

# create the stack object
oval_stack=Stack(canvas)

#create buttons
top=tk.Button(canvas,text='Top',command=oval_stack.top)
pop=tk.Button(canvas,text='pop',command=oval_stack.pop)
push=tk.Button(canvas,text='push',command=oval_stack.push)
is_empty=tk.Button(canvas,text='is_empty',command=lambda:print(f'Is empty: {oval_stack.is_empty()}'))
size=tk.Button(canvas,text='size',command=lambda:print(f'Size:{oval_stack.size()}'))

# position the buttons on the canvas
canvas.create_window(400,200,window=top)
canvas.create_window(400,240,window=pop)
canvas.create_window(400,280,window=push)
canvas.create_window(500,200,window=is_empty)
canvas.create_window(500,240,window=size)


# start the tkinter main loop
root.mainloop()

