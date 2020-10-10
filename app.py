from tkinter import*

cal = Tk()
cal.title("calculator")
operator = ""
text_Input =StringVar ()

txtDisplay = Entry(cal,font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify = "right").grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="7").grid(row=1, column=0)
btn8=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="8").grid(row=1, column=1)
btn9=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="9").grid(row=1, column=2)
addition=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="+").grid(row=1, column=3)
#========================================================================================================
btn4=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="4").grid(row=2, column=0)
btn5=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="5").grid(row=2, column=1)
btn6=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="6").grid(row=2, column=2)
subtraction=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="-").grid(row=1, column=3)
#============================================================================================================
btn0=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="0").grid(row=3, column=0)
btnClear=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="C").grid(row=3, column=1)
btnEquals=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="=").grid(row=3, column=2)
divison=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="/").grid(row=3, column=3)
btnEquals=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="*").grid(row=3, column=2)
divison=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="+").grid(row=3, column=3)
#============================================================================================================
btn1=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="4").grid(row=4, column=0)
btn2=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="5").grid(row=4, column=1)
btn3=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="6").grid(row=4, column=2)
multiply=Button(cal,padx=16,bd=8,fg="black", font=('arial', 20, 'bold'), text="-").grid(row=1, column=3)

cal.mainloop()
