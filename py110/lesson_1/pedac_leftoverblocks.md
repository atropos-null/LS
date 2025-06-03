Problem Statement:

>The building blocks are cubes.
>The structure is built in layers.
>The top layer is a single block.
>A block in an upper layer must be supported by four blocks in a lower layer.
>A block in a lower layer can support more than one block in an upper layer.ls
>You cannot leave gaps between blocks.

>Write a program that, given the number of available blocks, calculates the number of blocks 
>left over after building the tallest possible valid structure.

Step 1:
* inputs and outputs
    - input: number of available bricks. integer.
    - output: remainder of blocks available after building the tallest possible. integer. 

* explicit and implicit rules
    - Explicit rule:
        * Only one cube at the top
        * Cubes have 6 sides
        * each layer is at least 4 cubes
        * no gaps
        * a lower cube can support more than 1 higher cube

    - Implicit rule:
        * modulo by 4
        * no floats
        * think in 3D
        * pyramid shape?
        * counts down from top to bottom. Only the top layer is guaranteed.
        * Layer number correlates with blocks in a layer:
        * The number of blocks in a layer is `layer number * layer number`.


Question: 
1) Is a layer ONLY 4 cubes? Or can there be more than 4 per layer? 
2) What is the maximum any one lower cube can support?
3) Will there always be left over blocks?
4) Does the layers grow in size, or could you have a tower of just 4 blocks?

Step 2:

```python
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
```

1) no blocks equals no structure.
2) 1 block is a structure. 
3) for there to be more than 2 layers, the minimum amount of blocks for a 2 layer structure is 5 blocks.
4)  1, 2 3 4 5, 6 7 8 9 10 11 12 13 14. 1, 4, 9 . So layer to the power of 2

Layer 1 = 1
Layer 2 = 4
Layer 3 = 9
Layer 4 = 16
Layer 5 = 25
Layer 6 = 36
Layer 7 = 49
Layer 8 = 64
Layer 9 = 81
Layer 10 = 100

Step 3: Data structures

None? Just need integers and not collecting any? If so, nested lists?

Step 4: Algorithm

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





    