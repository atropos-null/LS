""" 
Problem: Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values 
and its values become keys.

    - input: dictionary
    - output: dictionary
    - swap values with keys

Example: {"fruit": "apple"} => {"apple": "fruit"}

Data Structure: Lists, but as a conversion, not as an initialization

Algorithm:
   - convert dict.keys and dict.values and zip, switching positions
   - convert back to a dictionary

"""

def invert_dict(dictionary):
    return dict(zip(dictionary.values(), dictionary.keys()))

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True


"""
Further Optimization:

def invert_dict(my_dict):
    return {value: key for key, value in my_dict.items()}
"""