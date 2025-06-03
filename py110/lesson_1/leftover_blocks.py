"""
1. Start with:
     - The "number of blocks remaining" is equal to the input.
     - The "current layer number" is layer 0.

2. Calculate the "current layer number" for the next layer by
   adding 1 to the "current layer number".

3. Using the new "current layer number", calculate the "number of
   blocks required in this layer" by multiplying the "current
   layer number" by itself.

4. Determine whether the "number of blocks remaining" is greater
   than or equal to the "number of blocks required in this layer".
     - If there are enough blocks:
         - Subtract the "number of blocks required in this layer"
           from the "number of blocks remaining".
         - Go to step 2.
     - If there aren't enough blocks:
         - Return the "number of blocks remaining".
"""

def calculate_leftover_blocks(number):
    remaining_blocks = number
    current_layer = 0

    while True:
        next_layer = current_layer + 1
        blocks_used = current_layer * current_layer
        if remaining_blocks >= blocks_used:
            remaining_blocks = remaining_blocks - blocks_used
            current_layer = next_layer
        else:
            return remaining_blocks
   

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True