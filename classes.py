class Point():
    #this method will be automatically called anytime we create a new point (an instance of this class)
    #self represents the object in question because two different points will have two different 
    # x and y values, so we would want to store that in the object itself.
    #self is the point itself, but point also has x and y values to store those values we have to save it in the self
    def __init__(self , input1 , input2):
        #self.x equals to whatever input x might be 
        self.x = input1
        #self.y equals to whateber input y might be
        self.y = input2
    
p = Point(2,5)
print(p.x)
print(p.y)