##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#house outline
rectangle = drawpad.create_rectangle(300,300,600,500, fill = 'red')

line1 = drawpad.create_line(300,300,450,100)
line2 = drawpad.create_line(600,300,450,100)

#windows and door
rectangle2 = drawpad.create_rectangle(350,350,400,400, fill = 'white')
rectangle3 = drawpad.create_rectangle(500,350,550,400, fill = 'white')

rectangle4 = drawpad.create_rectangle(425,350,475,500, fill = 'orange')

#door handle
oval1 = drawpad.create_oval(460,425,470,450, fill = 'yellow')

line3 = drawpad.create_line(550,50,550,230)
line4 = drawpad.create_line(575,50,575,270)
line5 = drawpad.create_line(550,50,575,50)

#grass
rectangle5 = drawpad.create_rectangle(800,500,0,600, fill = 'green')
root.mainloop()
