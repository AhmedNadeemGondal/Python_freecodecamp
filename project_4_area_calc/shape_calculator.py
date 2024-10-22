class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,change):
        self.width = change

    def set_height(self,change):
        self.height = change        

    def get_area(self):
        return(self.width*self.height)

    def get_perimeter(self):
        return(2*self.width + 2*self.height)  

    def get_diagonal(self):
        return( ((self.width ** 2 + self.height ** 2) ** .5))

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return("Too big for picture.")
        shape_o = ''
        for i in range(self.height):
            for i in range(self.width):
                shape_o += '*'
            shape_o += '\n'
        return(shape_o)

    def get_amount_inside(self,shape):
        amount = self.get_area() // shape.get_area()
        return(amount)

    def __str__(self):
        shape = "Rectangle"
        print_o = f"{shape}(width={self.width}, height={self.height})"
        return(print_o)
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(self,side)
        self.side = side
        self.height = self.side
        self.width = self.side

    def set_side(self,side_len):
        self.height = side_len
        self.width = side_len

    def __str__(self):
        return(f"Square(side={self.width})")
