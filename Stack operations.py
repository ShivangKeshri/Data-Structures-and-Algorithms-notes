stack = []

# append(push) an element into a stack
stack.append("a")
stack.append("b")
stack.append("c")
print("stack: ",stack)

# pop
element = stack.pop()
print('pop', element) # pops the last element of the stack automatically
print(stack)

# peek
element = stack[-1]
print('peek value: ', element)

# size of stack
element = len(stack)
print("the size of stack is :", element)

# is_empty:
isEmpty = not bool(stack) # if stack is empty then output is 0, then is_empty is 
print("isEmpty: ", isEmpty)

