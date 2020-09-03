from tkinter import *
 
root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.pack()
 
ball = c.create_oval(0, 100, 60, 140, fill='green')
bog= c.create_oval (50 , 200, 200, 50, fill='yellow' ) 

def motion():
    print (str(c.coords(ball)[1]))
    if c.coords(ball)[2] == 60 and c.coords(ball)[1] == 100:
      while c.coords(ball)[2] != 150 and c.coords(ball)[1] !=10:
        c.move(ball, 1, -1)
        #print (str(c.coords(ball)[2] )+'\nHELL'+ (str((c.coords(ball)[1]))))
        root.after(100, motion) 
    if c.coords(ball)[2] == 150 and c.coords(ball)[1] == 10:
      while c.coords(ball)[2] != 240 and c.coords(ball)[1] !=100:
        c.move(ball, 1, 1)
        #print (str(c.coords(ball)[2] )+'\nHELL_1  '+ (str((c.coords(ball)[1]))))
        root.after(100, motion)  
    if c.coords(ball)[2] == 240 and c.coords(ball)[1] == 100:
      while c.coords(ball)[2] != 150 and c.coords(ball)[1] !=190:
        c.move(ball, -1, 1)
        #print (str(c.coords(ball)[2] )+'\nHELL_2  '+ (str((c.coords(ball)[1]))))
        root.after(100, motion)  
    if c.coords(ball)[2] == 150 and c.coords(ball)[1] == 190:
      while c.coords(ball)[2] != 60 and c.coords(ball)[1] !=100:
        c.move(ball, -1, -1)
        #print (str(c.coords(ball)[2] )+'\nHELL_3  '+ (str((c.coords(ball)[1]))))
        root.after(100, motion) 

motion()
 
root.mainloop()
