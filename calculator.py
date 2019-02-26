from tkinter import *
def button_congiq(a):
    global operator
    operator=operator + str(a)
    text_input.set(operator)

def clear_func():
    global operator
    operator=""
    text_input.set(operator)
    text_output.set(operator)


def equal_func():
    global operator
    sum1 = str(eval(operator))
    text_output.set(sum1)
    operator=""

#------
window1=Tk()
text_input = StringVar()
text_output = StringVar()
window1.title("Calculator")
window1.geometry("230x380")
operator=""
textbox1= Entry(window1,font=("aerial",20,"bold"),bd=5,textvariable=text_input,bg="powder blue",justify="right",width=15).pack()
textbox2= Entry(window1,font=("aerial",20,"bold"),bd=5,textvariable=text_output,bg="powder blue",justify="right",width=15).pack()
button7=Button(window1,command=lambda:button_congiq(7),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="7").place(x=0,y=90)
button8=Button(window1,command=lambda:button_congiq(8),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="8").place(x=60,y=90)
button9=Button(window1,command=lambda:button_congiq(9),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="9").place(x=120,y=90)
button_mul=Button(window1,command=lambda:button_congiq("*"),padx=10,pady=10,bg="powder blue",font=("courier",20,"bold"),text="X").place(x=180,y=90)

#------

button4=Button(window1,command=lambda:button_congiq(4),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="4").place(x=0,y=165)
button5=Button(window1,command=lambda:button_congiq(5),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="5").place(x=60,y=165)
button6=Button(window1,command=lambda:button_congiq(6),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="6").place(x=120,y=165)
button_sub=Button(window1,command=lambda:button_congiq("-"),padx=10,pady=10,bg="powder blue",font=("courier",20,"bold"),text="-").place(x=180,y=165)

#------

button1=Button(window1,command=lambda:button_congiq(1),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="1").place(x=0,y=240)
button2=Button(window1,command=lambda:button_congiq(2),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="2").place(x=60,y=240)
button3=Button(window1,command=lambda:button_congiq(3),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="3").place(x=120,y=240)
button_add=Button(window1,command=lambda:button_congiq("+"),padx=10,pady=10,bg="powder blue",font=("courier",20,"bold"),text="+").place(x=180,y=240)

#------

button_clear=Button(window1,command=lambda:clear_func(),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="C").place(x=0,y=315)
button0=Button(window1,command=lambda:button_congiq(0),padx=10,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="0").place(x=60,y=315)
button_div=Button(window1,command=lambda:button_congiq("/"),padx=11,pady=10,bg="powder blue",font=("aerial",20,"bold"),text="/ ").place(x=120,y=315)
button_equal=Button(window1,command=lambda:equal_func(),padx=10,pady=10,bg="powder blue",font=("courier",20,"bold"),text="=").place(x=180,y=315)
window1.mainloop()
