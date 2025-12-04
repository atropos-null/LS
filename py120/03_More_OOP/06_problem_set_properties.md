1. Create a `Person` class with a "private" attribute _name. Use properties to create a getter and setter for the `_name` attribute. The `_name` attribute must be a string. Be sure to test your code.

```python

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        self._name = name

linda = Person('Linda')
print(linda.name)                   # Linda

linda.name = 'Lin'
print(linda.name)                   # Lin

linda.name = ['Linda']

``` 

2. Update your answer from problem 1 to disallow empty strings. You should raise a ValueError. Be sure to test your code.

```python

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        
        if name == "":
            raise ValueError("Name must not be empty.")
        self._name = name

linda = Person('Linda')
print(linda.name)                   # Linda

linda.name = 'Lin'
print(linda.name)                   # Lin

#linda.name = ['Linda']

linda.name = '' 

```

3. Create a Rectangle class with attributes _width and _height. Add properties to get the width and height but to disallow modification after the object is created (i.e., no setters).

```python

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    
rectangle = Rectangle(3, 7)
print(rectangle.width, rectangle.height)      # 3 7

rectangle.width = 8
```

4. Consider the following code from the previous assignment:

```python
class SmartLamp:
    def __init__(self, color):
        self.color = color

    def glow(self):
        return (f'The lamp glows {self.color}.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color
```

Your task for this problem is to add a brightness property to this class. Your code should work as shown in the following test code:
```python
lamp = SmartLamp('blue', 70)
print(lamp.color)      # blue
print(lamp.brightness) # 70
print(lamp.glow())     # The lamp glows blue with brightness 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)      # red
print(lamp.brightness) # 90
print(lamp.glow())     # The lamp glows red with brightness 90%.

lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.
```

Answer:

```python
class SmartLamp:
    def __init__(self, color, brightness):
        self.color = color
        self.brightness = brightness

    def glow(self):
        return (f'The lamp glows {self.color} with brightness {self.brightness}%.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color
    
    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, brightness):
        if isinstance(brightness, int):
            if 0 <= brightness <= 100:
                self._brightness = brightness
                return

        raise ValueError('Brightness must be between 0 and 100.')
        
        

lamp = SmartLamp('blue', 70)
print(lamp.color)      # blue
print(lamp.brightness) # 70
print(lamp.glow())     # The lamp glows blue with brightness 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)      # red
print(lamp.brightness) # 90
print(lamp.glow())     # The lamp glows red with brightness 90%.

lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.
```
