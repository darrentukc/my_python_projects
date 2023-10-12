from turtle import Turtle




class PlayerPaddle:
    def __init__(self, field_width, field_height):

        self.player_paddle_list = []
        self.field_width = field_width
        self.field_height = field_height


    def create(self, paddle_size):
        for index in range(0,paddle_size):
            self.paddle = Turtle(shape='square')
            self.paddle.color('white')
            self.paddle.penup()
            self.paddle.speed('fastest')
            self.paddle.goto(x=-(self.field_width / 2)+10, y=index*20)
            self.player_paddle_list.append(self.paddle)

    def up(self):
        if self.player_paddle_list[-1].ycor() < self.field_height/2:
            for index in range(len(self.player_paddle_list)):
                old_x = self.player_paddle_list[index].xcor()
                old_y = self.player_paddle_list[index].ycor()
                new_y = old_y + 20
                self.player_paddle_list[index].goto(x=old_x, y=new_y)
        else:
            pass


    def down(self):
        if self.player_paddle_list[0].ycor() > (self.field_height / -2):
            for index in range(len(self.player_paddle_list)):
                old_x = self.player_paddle_list[index].xcor()
                old_y = self.player_paddle_list[index].ycor()
                new_y = old_y - 20
                self.player_paddle_list[index].goto(x=old_x, y=new_y)


