#!/usr/bin/env python
# coding: utf-8

# In[21]:


import ipywidgets as widgets
from IPython.display import display
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Cannot be divided by 0"
    return x/y

operator=None
first_number=None
current_number=""

output = widgets.Textarea(value='', placeholder='', description='', disabled=True, layout=widgets.Layout(width='300px', height='100px'))
     
def on_button_click(btn):
    global current_number,first_number,operator
    global current_number, first_number, operator
    label = btn.description  # Corrected this
    if label.isdigit() or label == '.':  # Corrected this
        current_number += label
    elif label in ['+','-','*','%']:
        first_number=float(current_number)
        operator=label
        current_number=""
    elif label == '=':
        if operator=='+':
            current_number=str(add(first_number,float(current_number)))
        elif operator=='-':
            current_number=str(sub(first_number,float(current_number)))
        elif operator=='*':
            current_number=str(mul(first_number,float(current_number)))
        elif operator=='%':
            current_number=str(div(first_number,float(current_number)))
    elif label =='C':
        first_number=None
        operator=None
        current_number=""
    output.value=current_number
buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '%', '='],
    ['C']
]
for row in buttons:
    btns=[widgets.Button(description=btn,layout=widgets.Layout(width='70px',height='70px')) for btn in row]
    for btn in btns:
        btn.on_click(on_button_click)
    display(widgets.HBox(btns))
display(output)


# In[ ]:




