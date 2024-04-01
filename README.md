# DSA-Laboratory-Activity

In the PDF file named "SCREEN SHOTS OF GRAPHS.pdf" 
      -The content of this file consists of screenshots showing the graph outputs. First is the overall graph showing the answers for all the given functions, followed by individual outputs for each function given.

In the "problems.txt" file, I wrote down 10 problems. They are:

      x²+7x+2, 
      3x+2, 
      x², 
      x³, 
      x⁵, 
      x³+2x²+x+10, 
      x⁴-3x³+2x²-x+11, 
      Sin(x), 
      Cos(x), 
      x⁵+4x⁴+x³-2x²+100, 
      

In the second file, named 'Solution.py', is the Python file that contains my program.
      -The first thing I did was create a program that reads a text file with problems and saves each problem separately in a list named "problems." Then, I define the function called solve_polynomial. This function needs two things: coefficients, which is a list of numbers showing the coefficients of a polynomial, and x, which is the value where the polynomial should be calculated. Then I made a code that can Solve each problem for x from 1 to 50. This process takes a list of problems, each representing a polynomial equation. It then processes each problem, ensuring it's properly formatted by adding a coefficient of 1 to any term starting with 'x'. After that, it splits the problem into its individual terms and extracts the coefficients. And then it wil solves each polynomial equation for values of x ranging from 1 to 50 and stores the solutions in a list. Furthermore, the next step code i did is to Plot the solutions of all given problems in the graph called "plot_all_problems" that plots solutions for a set of given problems. It iterates through the solutions list and plots each solution against the range from 1 to 50. The x-axis represents the range and the y-axis represents the solution, with each problem labeled accordingly before displaying the plot. Then I made a code that will Plot the solution of a specific problem chosen by the user. In this code it defines a function called plot_specific_problem that takes a problem number as input. If the chosen problem number is within the range of available solutions, it plots the solution of that problem using Matplotlib. The x-axis represents numbers from 1 to 50, and the y-axis shows the corresponding solution values. If the chosen problem number is invalid, it displays a message prompting the user to select a number within the valid range. And then I add a Function to display all given problems with numbers. This function called display_problems, which shows a numbered list of all the given problems. It first prints "List of Available Problems:", then iterates through each problem in the 'problems' list, and prints each problem along with its corresponding number. It ensures that problems are neatly displayed and easily identifiable for users. Lastly, I added a code that will ask the user what action they want to perform. It presents three options: plotting all problems, plotting a specific problem, or exiting. If the user selects option 1, it plots all the given problems. If they choose option 2, it displays all available problems and then plots the one the user selects. If the user selects option 3, the program exits. If the user enters an invalid choice, it prompts them to enter 1, 2, or 3 again.





