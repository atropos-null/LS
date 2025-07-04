""" 
Problem: Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values 
and its values become keys.

    - input: dictionary
    - output: dictionary
    - swap values with keys

Example: {"fruit": "apple"} => {"apple": "fruit"}

Data Structure: Lists, but as a conversion, not as an initialization

Algorithm:
   - convert dict.keys and dict.values to a list to preserve order
   - zip the two lists
   - convert back to a dictionary

"""

def invert_dict(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    zipped = zip(values, keys)
    result = dict(zipped)
    return result 


print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True