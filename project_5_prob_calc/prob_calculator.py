import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        if len(kwargs) == 0:
            raise TypeError("At least one keyword argument is required")
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self,draw_count):
        removed = []
        if draw_count >= len(self.contents):
            removed = self.contents
            self.contents = []
            return(removed)
        else:
            for value in range(draw_count):
                r_num = random.randint(0,len(self.contents)-1)
                # print(value,r_num, len(self.contents)-1)
                removed.append(self.contents.pop(r_num))
                # print(removed,len(self.contents))
            return(removed)            

    def __str__(self):
        return(str(self.contents))

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
      
        expected_balls_lst = []
        lst = list(expected_balls.items())
        for key, value in lst:
            for i in range(value):
                expected_balls_lst.append(key)
        M = 0
        # removed = 0
        for i in range(0,num_experiments):
            hat1 = copy.deepcopy(hat)
            # print(type(hat1))
            removed = hat1.draw(num_balls_drawn)
#             print(f'Experiment Iter: {i}')
#             print(f'''Expected Balls: {expected_balls_lst}
# Balls Drawn: {removed}
# Length of class:{len(hat1.contents)}''')
            condition = True
            for item in expected_balls_lst:
                main_count = removed.count(item)
                if main_count  < expected_balls_lst.count(item):
                    # print(expected_balls_lst.count(item),main_count)
                    # print(f"{item} is not present enough times in list2\n")
                    condition = False
                    break
                # else:
                #     print(expected_balls_lst.count(item),main_count)
                #     print('Ok\n')
            if condition:
                M += 1
        #     print(f'M = {M}')
        # print(f'Probablity: {M/num_experiments}')
        return(M/num_experiments)



if __name__ == "__main__":
    # hat1 = Hat(blue=4, red=2, green=3)
    # random.seed(95)
    # # hat1.draw(3)
    # experiment(hat=hat1, expected_balls={"blue": 2,"red": 1},num_balls_drawn=4, num_experiments=5)
    random.seed(95)
    hat = Hat(blue=4, red=2, green=6)
    probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
    print("Probability:", probability)
