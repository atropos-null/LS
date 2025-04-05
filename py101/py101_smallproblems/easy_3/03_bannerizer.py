def print_in_box(string):
   
    dashes = ''
    spaces = ''
    for _ in range(len(string)):
        dashes += '-'
        spaces += ' '
    
    print('+-' + dashes + '-+')
    print('| ' + spaces + ' |')
    print('| ' + string + ' |')
    print('| ' + spaces + ' |')
    print('+-' + dashes + '-+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')

