import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Sudoku")
root.geometry("400x400")


# A Quadrant
a1_textbox = tk.Entry(root, width=2, justify='center')
a1_textbox.place(x=100, y=100)
a1_textbox.configure(font=('Courier New',10))

a2_textbox = tk.Entry(root, width=2, justify='center')
a2_textbox.place(x=122, y=100)
a2_textbox.configure(font=('Courier New',10))

a3_textbox = tk.Entry(root, width=2, justify='center')
a3_textbox.place(x=144, y=100)
a3_textbox.configure(font=('Courier New',10))

a4_textbox = tk.Entry(root, width=2, justify='center')
a4_textbox.place(x=100, y=122)
a4_textbox.configure(font=('Courier New',10))

a5_textbox = tk.Entry(root, width=2, justify='center')
a5_textbox.place(x=122, y=122)
a5_textbox.configure(font=('Courier New',10))

a6_textbox = tk.Entry(root, width=2, justify='center')
a6_textbox.place(x=144, y=122)
a6_textbox.configure(font=('Courier New',10))

a7_textbox = tk.Entry(root, width=2, justify='center')
a7_textbox.place(x=100, y=144)
a7_textbox.configure(font=('Courier New',10))

a8_textbox = tk.Entry(root, width=2, justify='center')
a8_textbox.place(x=122, y=144)
a8_textbox.configure(font=('Courier New',10))

a9_textbox = tk.Entry(root, width=2, justify='center')
a9_textbox.place(x=144, y=144)
a9_textbox.configure(font=('Courier New',10))

# A Quadrant end

# B Quadrant
b1_textbox = tk.Entry(root, width=2, justify='center')
b1_textbox.place(x=166, y=100)
b1_textbox.configure(font=('Courier New',10))

b2_textbox = tk.Entry(root, width=2, justify='center')
b2_textbox.place(x=188, y=100)
b2_textbox.configure(font=('Courier New',10))

b3_textbox = tk.Entry(root, width=2, justify='center')
b3_textbox.place(x=210, y=100)
b3_textbox.configure(font=('Courier New',10))

b4_textbox = tk.Entry(root, width=2, justify='center')
b4_textbox.place(x=166, y=122)
b4_textbox.configure(font=('Courier New',10))

b5_textbox = tk.Entry(root, width=2, justify='center')
b5_textbox.place(x=188, y=122)
b5_textbox.configure(font=('Courier New',10))

b6_textbox = tk.Entry(root, width=2, justify='center')
b6_textbox.place(x=210, y=122)
b6_textbox.configure(font=('Courier New',10))

b7_textbox = tk.Entry(root, width=2, justify='center')
b7_textbox.place(x=166, y=144)
b7_textbox.configure(font=('Courier New',10))

b8_textbox = tk.Entry(root, width=2, justify='center')
b8_textbox.place(x=188, y=144)
b8_textbox.configure(font=('Courier New',10))

b9_textbox = tk.Entry(root, width=2, justify='center')
b9_textbox.place(x=210, y=144)
b9_textbox.configure(font=('Courier New',10))

# B Quadrant end

# C Quadrant
c1_textbox = tk.Entry(root, width=2, justify='center')
c1_textbox.place(x=232, y=100)
c1_textbox.configure(font=('Courier New',10))

c2_textbox = tk.Entry(root, width=2, justify='center')
c2_textbox.place(x=254, y=100)
c2_textbox.configure(font=('Courier New',10))

c3_textbox = tk.Entry(root, width=2, justify='center')
c3_textbox.place(x=276, y=100)
c3_textbox.configure(font=('Courier New',10))

c4_textbox = tk.Entry(root, width=2, justify='center')
c4_textbox.place(x=232, y=122)
c4_textbox.configure(font=('Courier New',10))

c5_textbox = tk.Entry(root, width=2, justify='center')
c5_textbox.place(x=254, y=122)
c5_textbox.configure(font=('Courier New',10))

c6_textbox = tk.Entry(root, width=2, justify='center')
c6_textbox.place(x=276, y=122)
c6_textbox.configure(font=('Courier New',10))

c7_textbox = tk.Entry(root, width=2, justify='center')
c7_textbox.place(x=232, y=144)
c7_textbox.configure(font=('Courier New',10))

c8_textbox = tk.Entry(root, width=2, justify='center')
c8_textbox.place(x=254, y=144)
c8_textbox.configure(font=('Courier New',10))

c9_textbox = tk.Entry(root, width=2, justify='center')
c9_textbox.place(x=276, y=144)
c9_textbox.configure(font=('Courier New',10))

# C Quadrant end

# D Quadrant
d1_textbox = tk.Entry(root, width=2, justify='center')
d1_textbox.place(x=100, y=166)
d1_textbox.configure(font=('Courier New',10))

d2_textbox = tk.Entry(root, width=2, justify='center')
d2_textbox.place(x=122, y=166)
d2_textbox.configure(font=('Courier New',10))

d3_textbox = tk.Entry(root, width=2, justify='center')
d3_textbox.place(x=144, y=166)
d3_textbox.configure(font=('Courier New',10))

d4_textbox = tk.Entry(root, width=2, justify='center')
d4_textbox.place(x=100, y=188)
d4_textbox.configure(font=('Courier New',10))

d5_textbox = tk.Entry(root, width=2, justify='center')
d5_textbox.place(x=122, y=188)
d5_textbox.configure(font=('Courier New',10))

d6_textbox = tk.Entry(root, width=2, justify='center')
d6_textbox.place(x=144, y=188)
d6_textbox.configure(font=('Courier New',10))

d7_textbox = tk.Entry(root, width=2, justify='center')
d7_textbox.place(x=100, y=210)
d7_textbox.configure(font=('Courier New',10))

d8_textbox = tk.Entry(root, width=2, justify='center')
d8_textbox.place(x=122, y=210)
d8_textbox.configure(font=('Courier New',10))

d9_textbox = tk.Entry(root, width=2, justify='center')
d9_textbox.place(x=144, y=210)
d9_textbox.configure(font=('Courier New',10))


# D Quadrant end

# E Quadrant
e1_textbox = tk.Entry(root, width=2, justify='center')
e1_textbox.place(x=166, y=166)
e1_textbox.configure(font=('Courier New',10))

e2_textbox = tk.Entry(root, width=2, justify='center')
e2_textbox.place(x=188, y=166)
e2_textbox.configure(font=('Courier New',10))

e3_textbox = tk.Entry(root, width=2, justify='center')
e3_textbox.place(x=210, y=166)
e3_textbox.configure(font=('Courier New',10))

e4_textbox = tk.Entry(root, width=2, justify='center')
e4_textbox.place(x=166, y=188)
e4_textbox.configure(font=('Courier New',10))

e5_textbox = tk.Entry(root, width=2, justify='center')
e5_textbox.place(x=188, y=188)
e5_textbox.configure(font=('Courier New',10))

e6_textbox = tk.Entry(root, width=2, justify='center')
e6_textbox.place(x=210, y=188)
e6_textbox.configure(font=('Courier New',10))

e7_textbox = tk.Entry(root, width=2, justify='center')
e7_textbox.place(x=166, y=210)
e7_textbox.configure(font=('Courier New',10))

e8_textbox = tk.Entry(root, width=2, justify='center')
e8_textbox.place(x=188, y=210)
e8_textbox.configure(font=('Courier New',10))

e9_textbox = tk.Entry(root, width=2, justify='center')
e9_textbox.place(x=210, y=210)
e9_textbox.configure(font=('Courier New',10))

# E Quadrant end

# F Quadrant
f1_textbox = tk.Entry(root, width=2, justify='center')
f1_textbox.place(x=232, y=166)
f1_textbox.configure(font=('Courier New',10))

f2_textbox = tk.Entry(root, width=2, justify='center')
f2_textbox.place(x=254, y=166)
f2_textbox.configure(font=('Courier New',10))

f3_textbox = tk.Entry(root, width=2, justify='center')
f3_textbox.place(x=276, y=166)
f3_textbox.configure(font=('Courier New',10))

f4_textbox = tk.Entry(root, width=2, justify='center')
f4_textbox.place(x=232, y=188)
f4_textbox.configure(font=('Courier New',10))

f5_textbox = tk.Entry(root, width=2, justify='center')
f5_textbox.place(x=254, y=188)
f5_textbox.configure(font=('Courier New',10))

f6_textbox = tk.Entry(root, width=2, justify='center')
f6_textbox.place(x=276, y=188)
f6_textbox.configure(font=('Courier New',10))

f7_textbox = tk.Entry(root, width=2, justify='center')
f7_textbox.place(x=232, y=210)
f7_textbox.configure(font=('Courier New',10))

f8_textbox = tk.Entry(root, width=2, justify='center')
f8_textbox.place(x=254, y=210)
f8_textbox.configure(font=('Courier New',10))

f9_textbox = tk.Entry(root, width=2, justify='center')
f9_textbox.place(x=276, y=210)
f9_textbox.configure(font=('Courier New',10))

# F Quadrant end

# G Quadrant
g1_textbox = tk.Entry(root, width=2, justify='center')
g1_textbox.place(x=100, y=232)
g1_textbox.configure(font=('Courier New',10))

g2_textbox = tk.Entry(root, width=2, justify='center')
g2_textbox.place(x=122, y=232)
g2_textbox.configure(font=('Courier New',10))

g3_textbox = tk.Entry(root, width=2, justify='center')
g3_textbox.place(x=144, y=232)
g3_textbox.configure(font=('Courier New',10))

g4_textbox = tk.Entry(root, width=2, justify='center')
g4_textbox.place(x=100, y=254)
g4_textbox.configure(font=('Courier New',10))

g5_textbox = tk.Entry(root, width=2, justify='center')
g5_textbox.place(x=122, y=254)
g5_textbox.configure(font=('Courier New',10))

g6_textbox = tk.Entry(root, width=2, justify='center')
g6_textbox.place(x=144, y=254)
g6_textbox.configure(font=('Courier New',10))

g7_textbox = tk.Entry(root, width=2, justify='center')
g7_textbox.place(x=100, y=276)
g7_textbox.configure(font=('Courier New',10))

g8_textbox = tk.Entry(root, width=2, justify='center')
g8_textbox.place(x=122, y=276)
g8_textbox.configure(font=('Courier New',10))

g9_textbox = tk.Entry(root, width=2, justify='center')
g9_textbox.place(x=144, y=276)
g9_textbox.configure(font=('Courier New',10))

# G Quadrant end

# H Quadrant
h1_textbox = tk.Entry(root, width=2, justify='center')
h1_textbox.place(x=166, y=232)
h1_textbox.configure(font=('Courier New',10))

h2_textbox = tk.Entry(root, width=2, justify='center')
h2_textbox.place(x=188, y=232)
h2_textbox.configure(font=('Courier New',10))

h3_textbox = tk.Entry(root, width=2, justify='center')
h3_textbox.place(x=210, y=232)
h3_textbox.configure(font=('Courier New',10))

h4_textbox = tk.Entry(root, width=2, justify='center')
h4_textbox.place(x=166, y=254)
h4_textbox.configure(font=('Courier New',10))

h5_textbox = tk.Entry(root, width=2, justify='center')
h5_textbox.place(x=188, y=254)
h5_textbox.configure(font=('Courier New',10))

h6_textbox = tk.Entry(root, width=2, justify='center')
h6_textbox.place(x=210, y=254)
h6_textbox.configure(font=('Courier New',10))

h7_textbox = tk.Entry(root, width=2, justify='center')
h7_textbox.place(x=166, y=276)
h7_textbox.configure(font=('Courier New',10))

h8_textbox = tk.Entry(root, width=2, justify='center')
h8_textbox.place(x=188, y=276)
h8_textbox.configure(font=('Courier New',10))

h9_textbox = tk.Entry(root, width=2, justify='center')
h9_textbox.place(x=210, y=276)
h9_textbox.configure(font=('Courier New',10))

# H Quadrant end

# I Quadrant
i1_textbox = tk.Entry(root, width=2, justify='center')
i1_textbox.place(x=232, y=232)
i1_textbox.configure(font=('Courier New',10))

i2_textbox = tk.Entry(root, width=2, justify='center')
i2_textbox.place(x=254, y=232)
i2_textbox.configure(font=('Courier New',10))

i3_textbox = tk.Entry(root, width=2, justify='center')
i3_textbox.place(x=276, y=232)
i3_textbox.configure(font=('Courier New',10))

i4_textbox = tk.Entry(root, width=2, justify='center')
i4_textbox.place(x=232, y=254)
i4_textbox.configure(font=('Courier New',10))

i5_textbox = tk.Entry(root, width=2, justify='center')
i5_textbox.place(x=254, y=254)
i5_textbox.configure(font=('Courier New',10))

i6_textbox = tk.Entry(root, width=2, justify='center')
i6_textbox.place(x=276, y=254)
i6_textbox.configure(font=('Courier New',10))

i7_textbox = tk.Entry(root, width=2, justify='center')
i7_textbox.place(x=232, y=276)
i7_textbox.configure(font=('Courier New',10))

i8_textbox = tk.Entry(root, width=2, justify='center')
i8_textbox.place(x=254, y=276)
i8_textbox.configure(font=('Courier New',10))

i9_textbox = tk.Entry(root, width=2, justify='center')
i9_textbox.place(x=276, y=276)
i9_textbox.configure(font=('Courier New',10))

def generate_r1_num():
    global a1_int,a2_int,a3_int,b1_int,b2_int,b3_int,c1_int,c2_int,c3_int
    clear_r1()
    r1_numbers = random.sample(range(1,10),9)
    a1_int,a2_int,a3_int,b1_int,b2_int,b3_int,c1_int,c2_int,c3_int = r1_numbers
    a1_textbox.insert(0, f"{a1_int}")
    a2_textbox.insert(0, f"{a2_int}")
    a3_textbox.insert(0, f"{a3_int}")
    b1_textbox.insert(0, f"{b1_int}")
    b2_textbox.insert(0, f"{b2_int}")
    b3_textbox.insert(0, f"{b3_int}")
    c1_textbox.insert(0, f"{c1_int}")
    c2_textbox.insert(0, f"{c2_int}")
    c3_textbox.insert(0, f"{c3_int}")



global b1_int, b2_int, b3_int, b4_int, b5_int, b6_int, b7_int, b8_int, b9_int
global c1_int, c2_int, c3_int, c4_int, c5_int, c6_int, c7_int, c8_int, c9_int
global d1_int, d2_int, d3_int, d4_int, d5_int, d6_int, d7_int, d8_int, d9_int
global e1_int, e2_int, e3_int, e4_int, e5_int, e6_int, e7_int, e8_int, e9_int
global f1_int, f2_int, f3_int, f4_int, f5_int, f6_int, f7_int, f8_int, f9_int
global g1_int, g2_int, g3_int, g4_int, g5_int, g6_int, g7_int, g8_int, g9_int
global h1_int, h2_int, h3_int, h4_int, h5_int, h6_int, h7_int, h8_int, h9_int

# I Quadrant end
def generate_values():
    global b1_int, b2_int, b3_int, b4_int, b5_int, b6_int, b7_int, b8_int, b9_int
    global c1_int, c2_int, c3_int, c4_int, c5_int, c6_int, c7_int, c8_int, c9_int
    global d1_int, d2_int, d3_int, d4_int, d5_int, d6_int, d7_int, d8_int, d9_int
    global e1_int, e2_int, e3_int, e4_int, e5_int, e6_int, e7_int, e8_int, e9_int
    global f1_int, f2_int, f3_int, f4_int, f5_int, f6_int, f7_int, f8_int, f9_int
    global g1_int, g2_int, g3_int, g4_int, g5_int, g6_int, g7_int, g8_int, g9_int
    global h1_int, h2_int, h3_int, h4_int, h5_int, h6_int, h7_int, h8_int, h9_int
    global i1_int,i2_int,i3_int,i4_int,i5_int,i6_int,i7_int,i8_int,i9_int
    
    c1_int = 0
    c2_int = 0
    c3_int = 0
    c4_int = 0
    c5_int = 0
    c6_int = 0
    c7_int = 0
    c8_int = 0
    c9_int = 0
    
    b1_int = 0
    b2_int = 0
    b3_int = 0
    b4_int = 0
    b5_int = 0
    b6_int = 0
    b7_int = 0
    b8_int = 0
    b9_int = 0
    
    d1_int = 0
    d2_int = 0
    d3_int = 0
    d4_int = 0
    d5_int = 0
    d6_int = 0
    d7_int = 0
    d8_int = 0
    d9_int = 0
    
    e1_int = 0
    e2_int = 0
    e3_int = 0
    e4_int = 0
    e5_int = 0
    e6_int = 0
    e7_int = 0
    e8_int = 0
    e9_int = 0
    
    f1_int = 0
    f2_int = 0
    f3_int = 0
    f4_int = 0
    f5_int = 0
    f6_int = 0
    f7_int = 0
    f8_int = 0
    f9_int = 0
    
    g1_int = 0
    g2_int = 0
    g3_int = 0
    g4_int = 0
    g5_int = 0
    g6_int = 0
    g7_int = 0
    g8_int = 0
    g9_int = 0
    
    h1_int = 0
    h2_int = 0
    h3_int = 0
    h4_int = 0
    h5_int = 0
    h6_int = 0
    h7_int = 0
    h8_int = 0
    h9_int = 0

    i1_int = 0
    i2_int = 0
    i3_int = 0
    i4_int = 0
    i5_int = 0
    i6_int = 0
    i7_int = 0
    i8_int = 0
    i9_int = 0

def gen_r2():
    global a1_int,a2_int,a3_int,b1_int,b2_int,b3_int,c1_int,c2_int,c3_int
    global a4_int,a5_int,a6_int,b4_int,b5_int,b6_int,c4_int,c5_int,c6_int
    clear_r2()
    c = [b1_int,b2_int,b3_int,c1_int,c2_int,c3_int]
    a4_int = random.choice(c)
    a4_textbox.insert(0, f"{a4_int}")
    c.remove(a4_int)
    a5_int = random.choice(c)
    a5_textbox.insert(0, f"{a5_int}")
    c.remove(a5_int)
    a6_int = random.choice(c)
    a6_textbox.insert(0, f"{a6_int}")

    c = [a1_int,a2_int,a3_int,c1_int,c2_int,c3_int]
    if a4_int in c:
        c.remove(a4_int)
    if a5_int in c:
        c.remove(a5_int)
    if a6_int in c:
        c.remove(a6_int)
    b4_int = random.choice(c)
    b4_textbox.insert(0, f"{b4_int}")
    c.remove(b4_int)
    b5_int = random.choice(c)
    b5_textbox.insert(0, f"{b5_int}")
    c.remove(b5_int)
    b6_int = random.choice(c)
    b6_textbox.insert(0, f"{b6_int}")

    c = [a1_int,a2_int,a3_int,b1_int,b2_int,b3_int]
    if a4_int in c:
        c.remove(a4_int)
    if a5_int in c:
        c.remove(a5_int)
    if a6_int in c:
        c.remove(a6_int)
    if b4_int in c:
        c.remove(b4_int)
    if b5_int in c:
        c.remove(b5_int)
    if b6_int in c:
        c.remove(b6_int)
    if len(c) == 0:
        return gen_r2()
    c4_int = random.choice(c)
    if len(c) == 0:
        return gen_r2()
    c6_int = random.choice(c)
    c4_textbox.insert(0, f"{c4_int}")
    c.remove(c4_int)
    if len(c) == 0:
        return gen_r2()
    c6_int = random.choice(c)
    c5_int = random.choice(c)
    c5_textbox.insert(0, f"{c5_int}")
    c.remove(c5_int)
    if len(c) == 0:
        return gen_r2()
    c6_int = random.choice(c)
    c6_textbox.insert(0, f"{c6_int}")

    
def gen_r3():
    global a1_int,a2_int,a3_int,a4_int,a5_int,a6_int,a7_int,a8_int,a9_int
    global b1_int,b2_int,b3_int,b4_int,b5_int,b6_int,b7_int,b8_int,b9_int
    global c1_int,c2_int,c3_int,c4_int,c5_int,c6_int,c7_int,c8_int,c9_int
    clear_r3()
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a1_int)
    c.remove(a2_int)
    c.remove(a3_int)
    c.remove(a4_int)
    c.remove(a5_int)
    c.remove(a6_int)
    a7_int = random.choice(c)
    a7_textbox.insert(0, f"{a7_int}")
    c.remove(a7_int)
    a8_int = random.choice(c)
    a8_textbox.insert(0, f"{a8_int}")
    c.remove(a8_int)
    a9_int = random.choice(c)
    a9_textbox.insert(0, f"{a9_int}")
    c.remove(a9_int)


    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b1_int)
    c.remove(b2_int)
    c.remove(b3_int)
    c.remove(b4_int)
    c.remove(b5_int)
    c.remove(b6_int)
    b7_int = random.choice(c)
    b7_textbox.insert(0, f"{b7_int}")
    c.remove(b7_int)
    b8_int = random.choice(c)
    b8_textbox.insert(0, f"{b8_int}")
    c.remove(b8_int)
    b9_int = random.choice(c)
    b9_textbox.insert(0, f"{b9_int}")
    c.remove(b9_int)

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c1_int)
    c.remove(c2_int)
    c.remove(c3_int)
    c.remove(c4_int)
    c.remove(c5_int)
    c.remove(c6_int)
    c7_int = random.choice(c)
    c7_textbox.insert(0, f"{c7_int}")
    c.remove(c7_int)
    c8_int = random.choice(c)
    c8_textbox.insert(0, f"{c8_int}")
    c.remove(c8_int)
    c9_int = random.choice(c)
    c9_textbox.insert(0, f"{c9_int}")
    c.remove(c9_int)
    
            
def gen_r4():
    global a1_int,a2_int,a3_int,a4_int,a5_int,a6_int,a7_int,a8_int,a9_int
    global b1_int,b2_int,b3_int,b4_int,b5_int,b6_int,b7_int,b8_int,b9_int
    global c1_int,c2_int,c3_int,c4_int,c5_int,c6_int,c7_int,c8_int,c9_int
    global d1_int,d2_int,d3_int,e1_int,e2_int,e3_int,f1_int,f2_int,f3_int
    clear_r4()
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a1_int)
    c.remove(a4_int)
    c.remove(a7_int)
    d1_int = random.choice(c)
    d1_textbox.insert(0, f"{d1_int}")
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a2_int)
    c.remove(a5_int)
    c.remove(a8_int)
    if d1_int in c:
        c.remove(d1_int)
    d2_int = random.choice(c)
    d2_textbox.insert(0, f"{d2_int}")
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a3_int)
    c.remove(a6_int)
    c.remove(a9_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    d3_int = random.choice(c)
    d3_textbox.insert(0, f"{d3_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b1_int)
    c.remove(b4_int)
    c.remove(b7_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    e1_int = random.choice(c)
    e1_textbox.insert(0, f"{e1_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b2_int)
    c.remove(b5_int)
    c.remove(b8_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if e1_int in c:
        c.remove(e1_int)
    e2_int = random.choice(c)
    e2_textbox.insert(0, f"{e2_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b3_int)
    c.remove(b6_int)
    c.remove(b9_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    e3_int = random.choice(c)
    e3_textbox.insert(0, f"{e3_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c1_int)
    c.remove(c4_int)
    c.remove(c7_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if len(c) == 0:
        return gen_r4()
    f1_int = random.choice(c)
    f1_textbox.insert(0, f"{f1_int}")
    
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c2_int)
    c.remove(c5_int)
    c.remove(c8_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if f1_int in c:
        c.remove(f1_int)
    if len(c) == 0:
        return gen_r4()
    f2_int = random.choice(c)
    f2_textbox.insert(0, f"{f2_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c3_int)
    c.remove(c6_int)
    c.remove(c9_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if f1_int in c:
        c.remove(f1_int)
    if f2_int in c:
        c.remove(f2_int)
    if len(c) == 0:
        return gen_r4()
    f3_int = random.choice(c)
    f3_textbox.insert(0, f"{f3_int}")
    
    

def gen_r5():
    global a1_int,a2_int,a3_int,a4_int,a5_int,a6_int,a7_int,a8_int,a9_int
    global b1_int,b2_int,b3_int,b4_int,b5_int,b6_int,b7_int,b8_int,b9_int
    global c1_int,c2_int,c3_int,c4_int,c5_int,c6_int,c7_int,c8_int,c9_int
    global d1_int,d2_int,d3_int,e1_int,e2_int,e3_int,f1_int,f2_int,f3_int
    global d4_int,d5_int,d6_int,e4_int,e5_int,e6_int,f4_int,f5_int,f6_int
    clear_r5()
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a1_int)
    c.remove(a4_int)
    c.remove(a7_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    d4_int = random.choice(c)
    d4_textbox.insert(0, f"{d4_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a2_int)
    c.remove(a5_int)
    c.remove(a8_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if d4_int in c:
        c.remove(d4_int)
    d5_int = random.choice(c)
    d5_textbox.insert(0, f"{d5_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a3_int)
    c.remove(a6_int)
    c.remove(a9_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    d6_int = random.choice(c)
    d6_textbox.insert(0, f"{d6_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b1_int)
    c.remove(b4_int)
    c.remove(b7_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if len(c) == 0:
        return gen_r5()
    e4_int = random.choice(c)
    e4_textbox.insert(0, f"{e4_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b2_int)
    c.remove(b5_int)
    c.remove(b8_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if e4_int in c:
        c.remove(e4_int)
    if len(c) == 0:
        return gen_r5()
    e5_int = random.choice(c)
    e5_textbox.insert(0, f"{e5_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b3_int)
    c.remove(b6_int)
    c.remove(b9_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if e4_int in c:
        c.remove(e4_int)
    if e5_int in c:
        c.remove(e5_int)
    if len(c) == 0:
        return gen_r5()
    e6_int = random.choice(c)
    e6_textbox.insert(0, f"{e6_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c1_int)
    c.remove(c4_int)
    c.remove(c7_int)
    if f1_int in c:
        c.remove(f1_int)
    if f2_int in c:
        c.remove(f2_int)
    if f3_int in c:
        c.remove(f3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if e4_int in c:
        c.remove(e4_int)
    if e5_int in c:
        c.remove(e5_int)
    if e6_int in c:
        c.remove(e6_int)
    if len(c) == 0:
        return gen_r5()
    f4_int = random.choice(c)
    f4_textbox.insert(0, f"{f4_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c2_int)
    c.remove(c5_int)
    c.remove(c8_int)
    if f1_int in c:
        c.remove(f1_int)
    if f2_int in c:
        c.remove(f2_int)
    if f3_int in c:
        c.remove(f3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if e4_int in c:
        c.remove(e4_int)
    if e5_int in c:
        c.remove(e5_int)
    if e6_int in c:
        c.remove(e6_int)
    if f4_int in c:
        c.remove(f4_int)
    if len(c) == 0:
        return gen_r5()
    f5_int = random.choice(c)
    f5_textbox.insert(0, f"{f5_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c3_int)
    c.remove(c6_int)
    c.remove(c9_int)
    if f1_int in c:
        c.remove(f1_int)
    if f2_int in c:
        c.remove(f2_int)
    if f3_int in c:
        c.remove(f3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if e4_int in c:
        c.remove(e4_int)
    if e5_int in c:
        c.remove(e5_int)
    if e6_int in c:
        c.remove(e6_int)
    if f4_int in c:
        c.remove(f4_int)
    if f5_int in c:
        c.remove(f5_int)
    if len(c) == 0:
        return gen_r5()
    f6_int = random.choice(c)
    f6_textbox.insert(0, f"{f6_int}")

def gen_r6():
    global a1_int,a2_int,a3_int,a4_int,a5_int,a6_int,a7_int,a8_int,a9_int
    global b1_int,b2_int,b3_int,b4_int,b5_int,b6_int,b7_int,b8_int,b9_int
    global c1_int,c2_int,c3_int,c4_int,c5_int,c6_int,c7_int,c8_int,c9_int
    global d1_int,d2_int,d3_int,e1_int,e2_int,e3_int,f1_int,f2_int,f3_int
    global d4_int,d5_int,d6_int,e4_int,e5_int,e6_int,f4_int,f5_int,f6_int
    global d7_int,d8_int,d9_int,e7_int,e8_int,e9_int,f7_int,f8_int,f9_int
    clear_r6()
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a1_int)
    c.remove(a4_int)
    c.remove(a7_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if len(c) == 0:
        return gen_numbers()
    d7_int = random.choice(c)
    d7_textbox.insert(0, f"{d7_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a2_int)
    c.remove(a5_int)
    c.remove(a8_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if d7_int in c:
        c.remove(d7_int)
    if len(c) == 0:
        return gen_numbers()
    d8_int = random.choice(c)
    d8_textbox.insert(0, f"{d8_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a3_int)
    c.remove(a6_int)
    c.remove(a9_int)
    if d1_int in c:
        c.remove(d1_int)
    if d2_int in c:
        c.remove(d2_int)
    if d3_int in c:
        c.remove(d3_int)
    if d4_int in c:
        c.remove(d4_int)
    if d5_int in c:
        c.remove(d5_int)
    if d6_int in c:
        c.remove(d6_int)
    if d7_int in c:
        c.remove(d7_int)
    if d8_int in c:
        c.remove(d8_int)
    if len(c) == 0:
        return gen_numbers()
    d9_int = random.choice(c)
    d9_textbox.insert(0, f"{d9_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b1_int)
    c.remove(b4_int)
    c.remove(b7_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if e4_int in c:
        c.remove(e4_int)
    if e5_int in c:
        c.remove(e5_int)
    if e6_int in c:
        c.remove(e6_int)
    if d7_int in c:
        c.remove(d7_int)
    if d8_int in c:
        c.remove(d8_int)
    if d9_int in c:
        c.remove(d9_int)
    if len(c) == 0:
        return gen_numbers()
    e7_int = random.choice(c)
    e7_textbox.insert(0, f"{e7_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b2_int)
    c.remove(b5_int)
    c.remove(b8_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if e4_int in c:
        c.remove(e4_int)
    if e5_int in c:
        c.remove(e5_int)
    if e6_int in c:
        c.remove(e6_int)
    if d7_int in c:
        c.remove(d7_int)
    if d8_int in c:
        c.remove(d8_int)
    if d9_int in c:
        c.remove(d9_int)
    if e7_int in c:
        c.remove(e7_int)
    if len(c) == 0:
        return gen_numbers()
    e8_int = random.choice(c)
    e8_textbox.insert(0, f"{e8_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b3_int)
    c.remove(b6_int)
    c.remove(b9_int)
    if e1_int in c:
        c.remove(e1_int)
    if e2_int in c:
        c.remove(e2_int)
    if e3_int in c:
        c.remove(e3_int)
    if e4_int in c:
        c.remove(e4_int)
    if e5_int in c:
        c.remove(e5_int)
    if e6_int in c:
        c.remove(e6_int)
    if d7_int in c:
        c.remove(d7_int)
    if d8_int in c:
        c.remove(d8_int)
    if d9_int in c:
        c.remove(d9_int)
    if e7_int in c:
        c.remove(e7_int)
    if e8_int in c:
        c.remove(e8_int)
    if len(c) == 0:
        return gen_numbers()
    e9_int = random.choice(c)
    e9_textbox.insert(0, f"{e9_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c1_int)
    c.remove(c4_int)
    c.remove(c7_int)
    if f1_int in c:
        c.remove(f1_int)
    if f2_int in c:
        c.remove(f2_int)
    if f3_int in c:
        c.remove(f3_int)
    if f4_int in c:
        c.remove(f4_int)
    if f5_int in c:
        c.remove(f5_int)
    if f6_int in c:
        c.remove(f6_int)
    if d7_int in c:
        c.remove(d7_int)
    if d8_int in c:
        c.remove(d8_int)
    if d9_int in c:
        c.remove(d9_int)
    if e7_int in c:
        c.remove(e7_int)
    if e8_int in c:
        c.remove(e8_int)
    if e9_int in c:
        c.remove(e9_int)
    if len(c) == 0:
        return gen_numbers()
    f7_int = random.choice(c)
    f7_textbox.insert(0, f"{f7_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c2_int)
    c.remove(c5_int)
    c.remove(c8_int)
    if f1_int in c:
        c.remove(f1_int)
    if f2_int in c:
        c.remove(f2_int)
    if f3_int in c:
        c.remove(f3_int)
    if f4_int in c:
        c.remove(f4_int)
    if f5_int in c:
        c.remove(f5_int)
    if f6_int in c:
        c.remove(f6_int)
    if d7_int in c:
        c.remove(d7_int)
    if d8_int in c:
        c.remove(d8_int)
    if d9_int in c:
        c.remove(d9_int)
    if e7_int in c:
        c.remove(e7_int)
    if e8_int in c:
        c.remove(e8_int)
    if e9_int in c:
        c.remove(e9_int)
    if f7_int in c:
        c.remove(f7_int)
    if len(c) == 0:
        return gen_numbers()
    f8_int = random.choice(c)
    f8_textbox.insert(0, f"{f8_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c3_int)
    c.remove(c6_int)
    c.remove(c9_int)
    if f1_int in c:
        c.remove(f1_int)
    if f2_int in c:
        c.remove(f2_int)
    if f3_int in c:
        c.remove(f3_int)
    if f4_int in c:
        c.remove(f4_int)
    if f5_int in c:
        c.remove(f5_int)
    if f6_int in c:
        c.remove(f6_int)
    if d7_int in c:
        c.remove(d7_int)
    if d8_int in c:
        c.remove(d8_int)
    if d9_int in c:
        c.remove(d9_int)
    if e7_int in c:
        c.remove(e7_int)
    if e8_int in c:
        c.remove(e8_int)
    if e9_int in c:
        c.remove(e9_int)
    if f7_int in c:
        c.remove(f7_int)
    if f8_int in c:
        c.remove(f8_int)
    if len(c) == 0:
        return gen_numbers()
    f9_int = random.choice(c)
    f9_textbox.insert(0, f"{f9_int}")
    
def gen_r7():
    global a1_int,a2_int,a3_int,a4_int,a5_int,a6_int,a7_int,a8_int,a9_int
    global b1_int,b2_int,b3_int,b4_int,b5_int,b6_int,b7_int,b8_int,b9_int
    global c1_int,c2_int,c3_int,c4_int,c5_int,c6_int,c7_int,c8_int,c9_int
    global d1_int,d2_int,d3_int,e1_int,e2_int,e3_int,f1_int,f2_int,f3_int
    global d4_int,d5_int,d6_int,e4_int,e5_int,e6_int,f4_int,f5_int,f6_int
    global d7_int,d8_int,d9_int,e7_int,e8_int,e9_int,f7_int,f8_int,f9_int
    global g1_int,g2_int,g3_int,h1_int,h2_int,h3_int,i1_int,i2_int,i3_int
    clear_r7()
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a1_int)
    c.remove(a4_int)
    c.remove(a7_int)
    c.remove(d1_int)
    c.remove(d4_int)
    c.remove(d7_int)
    if len(c) == 0:
        return gen_r7()
    g1_int = random.choice(c)
    g1_textbox.insert(0, f"{g1_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a2_int)
    c.remove(a5_int)
    c.remove(a8_int)
    c.remove(d2_int)
    c.remove(d5_int)
    c.remove(d8_int)
    if g1_int in c:
        c.remove(g1_int)
    if len(c) == 0:
        return gen_numbers()
    g2_int = random.choice(c)
    g2_textbox.insert(0, f"{g2_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a3_int)
    c.remove(a6_int)
    c.remove(a9_int)
    c.remove(d3_int)
    c.remove(d6_int)
    c.remove(d9_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if len(c) == 0:
        return gen_r7()
    g3_int = random.choice(c)
    g3_textbox.insert(0, f"{g3_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b1_int)
    c.remove(b4_int)
    c.remove(b7_int)
    c.remove(e1_int)
    c.remove(e4_int)
    c.remove(e7_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if len(c) == 0:
        return gen_r7()
    h1_int = random.choice(c)
    h1_textbox.insert(0, f"{h1_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b2_int)
    c.remove(b5_int)
    c.remove(b8_int)
    c.remove(e2_int)
    c.remove(e5_int)
    c.remove(e8_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if h1_int in c:
        c.remove(h1_int)
    if len(c) == 0:
        return gen_r7()
    h2_int = random.choice(c)
    h2_textbox.insert(0, f"{h2_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b3_int)
    c.remove(b6_int)
    c.remove(b9_int)
    c.remove(e3_int)
    c.remove(e6_int)
    c.remove(e9_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if h1_int in c:
        c.remove(h1_int)
    if h2_int in c:
        c.remove(h2_int)
    if len(c) == 0:
        return gen_r7()
    h3_int = random.choice(c)
    h3_textbox.insert(0, f"{h3_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c1_int)
    c.remove(c4_int)
    c.remove(c7_int)
    c.remove(f1_int)
    c.remove(f4_int)
    c.remove(f7_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if h1_int in c:
        c.remove(h1_int)
    if h2_int in c:
        c.remove(h2_int)
    if h3_int in c:
        c.remove(h3_int)
    if len(c) == 0:
        return gen_r7()
    i1_int = random.choice(c)
    i1_textbox.insert(0, f"{i1_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c2_int)
    c.remove(c5_int)
    c.remove(c8_int)
    c.remove(f2_int)
    c.remove(f5_int)
    c.remove(f8_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if h1_int in c:
        c.remove(h1_int)
    if h2_int in c:
        c.remove(h2_int)
    if h3_int in c:
        c.remove(h3_int)
    if i1_int in c:
        c.remove(i1_int)
    if len(c) == 0:
        return gen_r7()
    i2_int = random.choice(c)
    i2_textbox.insert(0, f"{i2_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c3_int)
    c.remove(c6_int)
    c.remove(c9_int)
    if f3_int in c:
        c.remove(f3_int)
    c.remove(f6_int)
    c.remove(f9_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if h1_int in c:
        c.remove(h1_int)
    if h2_int in c:
        c.remove(h2_int)
    if h3_int in c:
        c.remove(h3_int)
    if i1_int in c:
        c.remove(i1_int)
    if i2_int in c:
        c.remove(i2_int)
    if len(c) == 0:
        return gen_r7()
    i3_int = random.choice(c)
    i3_textbox.insert(0, f"{i3_int}")
    
cc8 = 0
mc8 = 10
def gen_r8():
    global cc8
    global mc8
    global a1_int,a2_int,a3_int,a4_int,a5_int,a6_int,a7_int,a8_int,a9_int
    global b1_int,b2_int,b3_int,b4_int,b5_int,b6_int,b7_int,b8_int,b9_int
    global c1_int,c2_int,c3_int,c4_int,c5_int,c6_int,c7_int,c8_int,c9_int
    global d1_int,d2_int,d3_int,e1_int,e2_int,e3_int,f1_int,f2_int,f3_int
    global d4_int,d5_int,d6_int,e4_int,e5_int,e6_int,f4_int,f5_int,f6_int
    global d7_int,d8_int,d9_int,e7_int,e8_int,e9_int,f7_int,f8_int,f9_int
    global g1_int,g2_int,g3_int,h1_int,h2_int,h3_int,i1_int,i2_int,i3_int
    global g4_int,g5_int,g6_int,h4_int,h5_int,h6_int,i4_int,i5_int,i6_int
    clear_r8()
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a1_int)
    c.remove(a4_int)
    c.remove(a7_int)
    c.remove(d1_int)
    c.remove(d4_int)
    c.remove(d7_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if len(c) == 0:
        return gen_r8()
    g4_int = random.choice(c)
    g4_textbox.insert(0, f"{g4_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a2_int)
    c.remove(a5_int)
    c.remove(a8_int)
    c.remove(d2_int)
    c.remove(d5_int)
    c.remove(d8_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if g4_int in c:
        c.remove(g4_int)
    if len(c) == 0:
        return gen_r8()
    g5_int = random.choice(c)
    g5_textbox.insert(0, f"{g5_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a3_int)
    c.remove(a6_int)
    c.remove(a9_int)
    c.remove(d3_int)
    c.remove(d6_int)
    c.remove(d9_int)
    if g1_int in c:
        c.remove(g1_int)
    if g2_int in c:
        c.remove(g2_int)
    if g3_int in c:
        c.remove(g3_int)
    if g4_int in c:
        c.remove(g4_int)
    if g5_int in c:
        c.remove(g5_int)
    if len(c) == 0:
        return gen_r8()
    g6_int = random.choice(c)
    g6_textbox.insert(0, f"{g6_int}")


    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b1_int)
    c.remove(b4_int)
    c.remove(b7_int)
    c.remove(e1_int)
    c.remove(e4_int)
    c.remove(e7_int)
    if h1_int in c:
        c.remove(h1_int)
    if h2_int in c:
        c.remove(h2_int)
    if h3_int in c:
        c.remove(h3_int)
    if g4_int in c:
        c.remove(g4_int)
    if g5_int in c:
        c.remove(g5_int)
    if g6_int in c:
        c.remove(g6_int)
    if len(c) == 0:
        return gen_r8()
    h4_int = random.choice(c)
    h4_textbox.insert(0, f"{h4_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b2_int)
    c.remove(b5_int)
    c.remove(b8_int)
    c.remove(e2_int)
    c.remove(e5_int)
    c.remove(e8_int)
    if h1_int in c:
        c.remove(h1_int)
    if h2_int in c:
        c.remove(h2_int)
    if h3_int in c:
        c.remove(h3_int)
    if g4_int in c:
        c.remove(g4_int)
    if g5_int in c:
        c.remove(g5_int)
    if g6_int in c:
        c.remove(g6_int)
    if h4_int in c:
        c.remove(h4_int)
    if len(c) == 0:
        return gen_r8()
    h5_int = random.choice(c)
    h5_textbox.insert(0, f"{h5_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b3_int)
    c.remove(b6_int)
    c.remove(b9_int)
    c.remove(e3_int)
    c.remove(e6_int)
    c.remove(e9_int)
    if h1_int in c:
        c.remove(h1_int)
    if h2_int in c:
        c.remove(h2_int)
    if h3_int in c:
        c.remove(h3_int)
    if g4_int in c:
        c.remove(g4_int)
    if g5_int in c:
        c.remove(g5_int)
    if g6_int in c:
        c.remove(g6_int)
    if h4_int in c:
        c.remove(h4_int)
    if h5_int in c:
        c.remove(h5_int)
    if len(c) == 0:
        return gen_r8()
    h6_int = random.choice(c)
    h6_textbox.insert(0, f"{h6_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c1_int)
    c.remove(c4_int)
    c.remove(c7_int)
    c.remove(f1_int)
    c.remove(f4_int)
    c.remove(f7_int)
    if i1_int in c:
        c.remove(i1_int)
    if i2_int in c:
        c.remove(i2_int)
    if i3_int in c:
        c.remove(i3_int)
    if g4_int in c:
        c.remove(g4_int)
    if g5_int in c:
        c.remove(g5_int)
    if g6_int in c:
        c.remove(g6_int)
    if h4_int in c:
        c.remove(h4_int)
    if h5_int in c:
        c.remove(h5_int)
    if h6_int in c:
        c.remove(h6_int)
    if len(c) == 0:
        return gen_r8()
    i4_int = random.choice(c)
    i4_textbox.insert(0, f"{i4_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c2_int)
    c.remove(c5_int)
    c.remove(c8_int)
    c.remove(f2_int)
    c.remove(f5_int)
    c.remove(f8_int)
    if i1_int in c:
        c.remove(i1_int)
    if i2_int in c:
        c.remove(i2_int)
    if i3_int in c:
        c.remove(i3_int)
    if g4_int in c:
        c.remove(g4_int)
    if g5_int in c:
        c.remove(g5_int)
    if g6_int in c:
        c.remove(g6_int)
    if h4_int in c:
        c.remove(h4_int)
    if h5_int in c:
        c.remove(h5_int)
    if h6_int in c:
        c.remove(h6_int)
    if i4_int in c:
        c.remove(i4_int)
    if len(c) == 0:
        if cc8 == mc8:
            mc8 = mc8 + 10
            return gen_numbers()
        else:
            cc8 += 1
            return gen_r8()
    i5_int = random.choice(c)
    i5_textbox.insert(0, f"{i5_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c3_int)
    c.remove(c6_int)
    c.remove(c9_int)
    if f3_int in c:
        c.remove(f3_int)
    c.remove(f6_int)
    c.remove(f9_int)
    if i1_int in c:
        c.remove(i1_int)
    if i2_int in c:
        c.remove(i2_int)
    if i3_int in c:
        c.remove(i3_int)
    if g4_int in c:
        c.remove(g4_int)
    if g5_int in c:
        c.remove(g5_int)
    if g6_int in c:
        c.remove(g6_int)
    if h4_int in c:
        c.remove(h4_int)
    if h5_int in c:
        c.remove(h5_int)
    if h6_int in c:
        c.remove(h6_int)
    if i4_int in c:
        c.remove(i4_int)
    if i5_int in c:
        c.remove(i5_int)
    if len(c) == 0:
        if cc8 == mc8:
            mc8 = mc8 + 10
            return gen_numbers()
        else:
            cc8 += 1
            return gen_r8()
    i6_int = random.choice(c)
    i6_textbox.insert(0, f"{i6_int}")



    

def gen_r9():
    global a1_int,a2_int,a3_int,a4_int,a5_int,a6_int,a7_int,a8_int,a9_int
    global b1_int,b2_int,b3_int,b4_int,b5_int,b6_int,b7_int,b8_int,b9_int
    global c1_int,c2_int,c3_int,c4_int,c5_int,c6_int,c7_int,c8_int,c9_int
    global d1_int,d2_int,d3_int,e1_int,e2_int,e3_int,f1_int,f2_int,f3_int
    global d4_int,d5_int,d6_int,e4_int,e5_int,e6_int,f4_int,f5_int,f6_int
    global d7_int,d8_int,d9_int,e7_int,e8_int,e9_int,f7_int,f8_int,f9_int
    global g1_int,g2_int,g3_int,h1_int,h2_int,h3_int,i1_int,i2_int,i3_int
    global g4_int,g5_int,g6_int,h4_int,h5_int,h6_int,i4_int,i5_int,i6_int
    global g7_int,g8_int,g9_int,h7_int,h8_int,h9_int,i7_int,i8_int,i9_int
    clear_r9()
    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a1_int)
    c.remove(a4_int)
    c.remove(a7_int)
    c.remove(d1_int)
    c.remove(d4_int)
    c.remove(d7_int)
    c.remove(g1_int)
    c.remove(g4_int)
    g7_int = random.choice(c)
    g7_textbox.insert(0, f"{g7_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a2_int)
    c.remove(a5_int)
    c.remove(a8_int)
    c.remove(d2_int)
    c.remove(d5_int)
    c.remove(d8_int)
    c.remove(g2_int)
    c.remove(g5_int)
    g8_int = random.choice(c)
    g8_textbox.insert(0, f"{g8_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(a3_int)
    c.remove(a6_int)
    c.remove(a9_int)
    c.remove(d3_int)
    c.remove(d6_int)
    c.remove(d9_int)
    c.remove(g3_int)
    c.remove(g6_int)
    g9_int = random.choice(c)
    g9_textbox.insert(0, f"{g9_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b1_int)
    c.remove(b4_int)
    c.remove(b7_int)
    c.remove(e1_int)
    c.remove(e4_int)
    c.remove(e7_int)
    c.remove(h1_int)
    c.remove(h4_int)
    h7_int = random.choice(c)
    h7_textbox.insert(0, f"{h7_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b2_int)
    c.remove(b5_int)
    c.remove(b8_int)
    c.remove(e2_int)
    c.remove(e5_int)
    c.remove(e8_int)
    c.remove(h2_int)
    c.remove(h5_int)
    h8_int = random.choice(c)
    h8_textbox.insert(0, f"{h8_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(b3_int)
    c.remove(b6_int)
    c.remove(b9_int)
    c.remove(e3_int)
    c.remove(e6_int)
    c.remove(e9_int)
    c.remove(h3_int)
    c.remove(h6_int)
    h9_int = random.choice(c)
    h9_textbox.insert(0, f"{h9_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c1_int)
    c.remove(c4_int)
    c.remove(c7_int)
    c.remove(f1_int)
    c.remove(f4_int)
    c.remove(f7_int)
    c.remove(i1_int)
    c.remove(i4_int)
    i7_int = random.choice(c)
    i7_textbox.insert(0, f"{i7_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c2_int)
    c.remove(c5_int)
    c.remove(c8_int)
    c.remove(f2_int)
    c.remove(f5_int)
    c.remove(f8_int)
    c.remove(i2_int)
    c.remove(i5_int)
    i8_int = random.choice(c)
    i8_textbox.insert(0, f"{i8_int}")

    c = [1,2,3,4,5,6,7,8,9]
    c.remove(c3_int)
    c.remove(c6_int)
    c.remove(c9_int)
    if f3_int in c:
        c.remove(f3_int)
    c.remove(f6_int)
    c.remove(f9_int)
    if i3_int in c:
       c.remove(i3_int)
    if i6_int in c:
       c.remove(i6_int)
    i9_int = random.choice(c)
    i9_textbox.insert(0, f"{i9_int}")
    
def gen_numbers():
    generate_r1_num()
    gen_r2()
    gen_r3()
    gen_r4()
    gen_r5()
    gen_r6()
    gen_r7()
    gen_r8()
    gen_r9()
           
def clear_textboxes():
    textboxes = [
        a1_textbox, a2_textbox, a3_textbox, a4_textbox, a5_textbox, a6_textbox, a7_textbox, a8_textbox, a9_textbox,
        b1_textbox, b2_textbox, b3_textbox, b4_textbox, b5_textbox, b6_textbox, b7_textbox, b8_textbox, b9_textbox,
        c1_textbox, c2_textbox, c3_textbox, c4_textbox, c5_textbox, c6_textbox, c7_textbox, c8_textbox, c9_textbox,
        d1_textbox, d2_textbox, d3_textbox, d4_textbox, d5_textbox, d6_textbox, d7_textbox, d8_textbox, d9_textbox,
        e1_textbox, e2_textbox, e3_textbox, e4_textbox, e5_textbox, e6_textbox, e7_textbox, e8_textbox, e9_textbox,
        f1_textbox, f2_textbox, f3_textbox, f4_textbox, f5_textbox, f6_textbox, f7_textbox, f8_textbox, f9_textbox,
        g1_textbox, g2_textbox, g3_textbox, g4_textbox, g5_textbox, g6_textbox, g7_textbox, g8_textbox, g9_textbox,
        h1_textbox, h2_textbox, h3_textbox, h4_textbox, h5_textbox, h6_textbox, h7_textbox, h8_textbox, h9_textbox,
        i1_textbox, i2_textbox, i3_textbox, i4_textbox, i5_textbox, i6_textbox, i7_textbox, i8_textbox, i9_textbox
    ]
    
    for textbox in textboxes:
        textbox.delete(0, 'end')
    

def clear_r1():
    textboxes = [
        a1_textbox,a2_textbox,a3_textbox,
        c1_textbox,c2_textbox,c3_textbox,
        b1_textbox,b2_textbox,b3_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')

def clear_r2():
    textboxes = [
        a4_textbox,a5_textbox,a6_textbox,
        c4_textbox,c5_textbox,c6_textbox,
        b4_textbox,b5_textbox,b6_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')

def clear_r3():
    textboxes = [
        a7_textbox,a8_textbox,a9_textbox,
        c7_textbox,c8_textbox,c9_textbox,
        b7_textbox,b8_textbox,b9_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')

def clear_r4():
    textboxes = [
        d1_textbox,d2_textbox,d3_textbox,
        e1_textbox,e2_textbox,e3_textbox,
        f1_textbox,f2_textbox,f3_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')

def clear_r5():
    textboxes = [
        d4_textbox,d5_textbox,d6_textbox,
        e4_textbox,e5_textbox,e6_textbox,
        f4_textbox,f5_textbox,f6_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')

def clear_r6():
    textboxes = [
        d7_textbox,d8_textbox,d9_textbox,
        e7_textbox,e8_textbox,e9_textbox,
        f7_textbox,f8_textbox,f9_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')

def clear_r7():
    textboxes = [
        g1_textbox,g2_textbox,g3_textbox,
        h1_textbox,h2_textbox,h3_textbox,
        i1_textbox,i2_textbox,i3_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')

def clear_r8():
    textboxes = [
        g4_textbox,g5_textbox,g6_textbox,
        h4_textbox,h5_textbox,h6_textbox,
        i4_textbox,i5_textbox,i6_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')

def clear_r9():
    textboxes = [
        g7_textbox,g8_textbox,g9_textbox,
        h7_textbox,h8_textbox,h9_textbox,
        i7_textbox,i8_textbox,i9_textbox,
        ]  
    for textbox in textboxes:
        textbox.delete(0, 'end')


refresh_enabled = True
def refresh_board():
    clear_textboxes()
    generate_values()
    gen_numbers()
    
def reset_refresh():
    global refresh_enabled
    refresh_enabled = True
    refresh_button.config(state = "normal")
        

def refresh_click():
    global refresh_enabled
    if refresh_enabled:
        refresh_board()
        refresh_button.config(state = "disabled")
        refresh_enabled = False
        refresh_button.after(100,reset_refresh)
        return
    else:
        return
    
refresh_button = tk.Button(root, text="Refresh", command=refresh_click)
refresh_button.place(x=100, y=300)

refresh_click()

root.mainloop()
