## Print Arguments

`sep=''` : prints without spaces  
`end=`   : what print() prints after it prints the last argument, often for compatibility with Windows (which sometimes needs a newline of `\r\n`) 

To start a new line immediately without printing anything else, just run `print()`.

**These both are the same**:
```python
name = input("What's your name? ")
name = input("What's your name?\n")
```