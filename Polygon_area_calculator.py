#!/usr/bin/env python
# coding: utf-8

# In[1]:


def __str__(self):
    return(("Rectangle(width={0}, height={1})").format(self.width, self.height))

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#setting function width
def set_width(self, width):
    self.width = width

#setting height function
def set_height(self, height):
    self.height = height

#Getting area of the shape
def get_area(self):
    return self.width * self.height

#Getting the perimeter of the shape
def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

#Getting the diagonal
def get_diagonal(self):
    return((self.width**2 + self.height**2)**.5)

#getting (*) picture
def get_picture(self):
    if self.height > 50 or self.width > 50:
        return "Too big for picture"
    else:
        return ((("*" * self.width) + "\n")* self.height)

#get no of shape(square | rectangle) can occupy in the given shape
def get_amount_inside(self, obj):
    return (self.width // obj.width) * (self.height // obj.height)

class Square(Rectangle):
    def __init__(self,side):
        self.height = side
        self.width = side

#setting function (width)
def set_width(self, side):
    self.width = side

#setting function (height)
def set_height(self, side):
    self.height = side

#string represerntation of object
def __str__(self):
    return f"Square(side={self.width})"

