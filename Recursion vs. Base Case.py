# taking an example of a countdown timer.

# recursive case:
def count_down(i):
    print(i)
    count_down(i-1)

# Base case :
def count_down2(i):
    print(i)
    if i <= 0:
        return
    else:
        count_down2(i-1)

# other recursive example:
def step_counter(steps):
    print(steps)
    if steps >= 20:
        return
    step_counter(steps+1)

i = 1
print(step_counter(i))
