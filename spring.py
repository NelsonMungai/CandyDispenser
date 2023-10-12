import random
import tkinter as tk

class Stack:
    def __init__(self, canvas):
        self.canvas = canvas
        self.oval_stack = []
        self.colors = []  # Store colors for each oval
        self.spring_height =450  # Initial height of the sliding rectangle
        self.spring_width = 300  # Width of the sliding rectangle
        # create a rectangle
        rect_x1 = 50
        rect_x2 = 350
        rect_y1 = 50
        rect_y2 = 500
        self.canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline='black', fill='white')
        # create the spring rect
        self.spring_x1 = rect_x1
        self.spring_x2 = rect_x2
        self.spring_y1 = rect_y1
        self.spring_y2 = rect_y1 + self.spring_height
        self.spring = self.canvas.create_rectangle(self.spring_x1, self.spring_y1, self.spring_x2, self.spring_y2, outline='black', fill='cyan')

    def push(self):
        if len(self.oval_stack) >= 7:  # Limit the number of ovals
            return
        oval_x1 = 100
        oval_x2 = 300

        # Calculate the Y-coordinates for the new oval
        if self.oval_stack:
            # Calculate Y-coordinates for the new oval
            oval_y2 = self.oval_stack[0][3]
            oval_y1 = oval_y2 - 50
        else:
            oval_y2 = 100  # Initial Y-coordinate of the bottom oval
            oval_y1 = 50

        # Push the existing ovals downwards
        for i in range(len(self.oval_stack)):
            self.canvas.move(self.oval_stack[i][4], 0, 50)

        # Move the sliding rectangle downwards
        self.spring_height -=50
        self.spring_y1 = self.spring_y2 - self.spring_height
        self.canvas.coords(self.spring, self.spring_x1, self.spring_y1, self.spring_x2, self.spring_y2)

        # Add oval to the canvas with different random colors
        random_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.colors.insert(0, random_color)

        # Draw the new oval
        oval = self.canvas.create_oval(oval_x1, oval_y1, oval_x2, oval_y2, outline='black', fill=random_color, tags='oval')

        # Insert oval at the beginning of the stack
        self.oval_stack.insert(0, (oval_x1, oval_y1, oval_x2, oval_y2, oval))

    def pop(self):
        if not self.oval_stack:
            return
        oval_coords = self.oval_stack.pop(0)
        self.canvas.delete(oval_coords[4])  # Delete the oval

        # Move the sliding rectangle upwards
        self.spring_height+= 50
        self.spring_y1 = self.spring_y2-self.spring_height
        self.canvas.coords(self.spring, self.spring_x1, self.spring_y1, self.spring_x2, self.spring_y2)

        for i in range(len(self.oval_stack)):
            self.canvas.move(self.oval_stack[i][4], 0, -50)

    def is_empty(self):
        return len(self.oval_stack) == 0

    def size(self):
        return len(self.oval_stack)

    def top(self):
        if self.oval_stack:
            print(self.oval_stack[-1])

# Create a tkinter window
root = tk.Tk()
root.title('Rectangle with Evenly Spaced Ovals')

# Create a canvas widget to draw on
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Create a stack object
oval_stack = Stack(canvas)

# Create buttons
top_button=tk.Button(canvas,text='top',command=oval_stack.top)
push_button = tk.Button(canvas, text='Push', command=oval_stack.push)
pop_button = tk.Button(canvas, text='Pop', command=oval_stack.pop)
is_empty_button = tk.Button(canvas, text='Is Empty', command=lambda: print(f'Is Empty: {oval_stack.is_empty()}'))
size_button = tk.Button(canvas, text='Size', command=lambda: print(f'Size: {oval_stack.size()}'))

# Position the buttons on the canvascan
canvas.create_window(450,360,window=top_button)
canvas.create_window(400, 280, window=push_button)
canvas.create_window(400, 320, window=pop_button)
canvas.create_window(500, 280, window=is_empty_button)
canvas.create_window(500, 320, window=size_button)

# Start the tkinter main loop
root.mainloop()
