from turtle import Turtle,Screen

from random import randint, choice as rand_choice

colors = ["blue","green","red","black"]

class MyTurtle(Turtle):
      def random_shape(self, x ,y):
        self.color(rand_choice(colors))
       
        self.penup()
        self.setposition(randint(-200,200)), (randint(-200,200))
        self.pendown()
        self.circle(50, steps=randint(4, 12))
       
        

        
        def __init__(self):
            super().__init__()
            self.random_shape(0.0)
            self.oneclick(self.random_shape)

x = MyTurtle()
y = MyTurtle()

x.forward(50)
y.backward(50)

screen = Screen()

screen.mainloop()

