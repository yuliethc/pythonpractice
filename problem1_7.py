"""
Problem 1_7:
Write a function problem1_7() that computes the area of a trapezoid. Here is the
formula: A = (1/2)(b1+b2)h. In the formula b1 is the length of one of the 
bases, b2 the other. The height is h and the area is A. Basically, this 
takes the average of the two bases times the height. For a rectangle b1 = b2, 
so this reduces to b1*h. This means that you can do a pretty good test of the 
correctness of your function using a rectangle (that way you can compute the 
answer in your head). Use input statements to ask for the bases and the height.
Convert these input strings to real numbers using float(). Print the output
nicely EXACTLY like mine below.

Tip: Be careful that your output on the test case below is exactly as shown
so that the auto-grader judges your output correctly.  The auto-grader does
not look at your input statements, so you don't have to use my input prompts
if you don't want to. However, the auto-grader will enter the three inputs in
the order shown. See the other test run below.

problem1_7()

Enter the length of one of the bases: 3

Enter the length of the other base: 4

Enter the height: 8
The area of a trapezoid with bases 3.0 and 4.0 and height 8.0 is 28.0

"""  
#%%
def problem1_7():
    temp_b1 = input("Enter the length of one of the bases: ")
    b1 = float(temp_b1)
    temp_b2 = input("Enter the length of the other base: ")
    b2 = float(temp_b2)
    temp_h = input("Enter the height ")
    h = float(temp_h)
    A = (1/2)*(b1+b2)*h
    print("The area of a trapezoid with bases", b1, "and", b2, "and height", h, "is", A)

#%%
"""
Another test run. In grading, expect different input numbers to be used.

problem1_7()

Enter the length of one of the bases: 10

Enter the length of the other base: 11

Enter the height: 12
The area of a trapezoid with bases 10.0 and 11.0 and height 12.0 is 126.0

"""