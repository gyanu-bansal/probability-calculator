import random
class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.box=[]
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
            self.box.extend([color] * count)
    def draw(self, num_balls):
        self.drawn_balls = []
        if num_balls >= len(self.contents):
            #print(self.contents)
            drawn_balls = self.contents
            self.contents = []
            return drawn_balls
        else:
            for _ in range(num_balls):
                self.index = random.randint(0, len(self.contents) - 1)
                ball = self.contents[self.index]
                self.drawn_balls.append(ball)
                self.contents.remove(ball)
            return self.drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M=0
    for execute in range(num_experiments):
        obj_dictionary = hat.__dict__
        #print(obj_dictionary)
        obj_list = obj_dictionary['box']
        d = dict()
        for i in obj_list:
            d[i] = d.get(i, 0) + 1
        hat_c = Hat(**d)
        drawn_ball_dict=dict()
        drawn_ball=hat_c.draw(num_balls_drawn)

        for i in drawn_ball:
            drawn_ball_dict[i]=drawn_ball_dict.get(i,0)+1
        expected_ball=expected_balls
        drawn_ball_dict=drawn_ball_dict
        # start matching whether drawn ball meets expectation or not!
        counter = 0
        for k, v in expected_ball.items():
            for key, value in drawn_ball_dict.items():
                if k==key and value>=v:
                    counter+=1

        if counter==len(expected_ball):
            status='matched'
            M=M+1
    return M/num_experiments
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,expected_balls={"red":2,"green":1},num_balls_drawn=5,num_experiments=2000)
print("prob: ",probability)
