# Progression-Outcome

A python program to predict progression outcomes based on the given criteria:
![image](https://github.com/trikto/Progression-Outcome/assets/77225260/e6108c4b-4e54-43e8-9f26-a0bdef6fb547)

The program should allow students to predict their progression outcome at the end of each academic year. The program should prompt for the number of credits at pass, defer and fail and then display the appropriate progression outcome for an individual student (i.e., progress, trailing, module retriever or exclude). 


## Implementing User Validation

+ The program should display **‘Integer required’** if a credit input is the wrong data type. 
+ The program should display **‘Out of range’** if credits entered are not in the range 0, 20, 40, 60, 80, 100 and 120. 
+ The program should display **‘Total incorrect’** if the total of the pass, defer and fail credits is not 120. 
+ An example of the program running with user input (shown in bold):

> Please enter your credits at pass: **p**
> Integer required
> Please enter your credits at pass: **140**
> Out of range.
> Please enter your credits at pass: **100**
> Please enter your credit at defer: **40**
> Please enter your credit at fail: **20**
> Total incorrect.
> Please enter your credits at pass: 100
> Please enter your credit at defer: 20
> Please enter your credit at fail: 0
> Progress (module trailer)


## Multiple Outcomes

+ The program loops to allow a staff member to predict progression outcomes for multiple students.
+ The program should prompt for credits at pass, defer and fail and display the appropriate progression for each individual student until the staff member enters **‘q’ to quit**. Optionally use an input of **‘y’ to continue**.


# Histogram Feature

+ When ‘q’ is entered, the program should use the **“graphics.py”** module to produce a ‘histogram’ representing the number of students who achieved a progress outcome in each category range: progress, trailing, module retriever and exclude. **The histogram should relate to the data input entered during the program run and work for any number of outcomes, it must use the graphics.py module.** 
+ Display the number of students for each progression category and the total number of students. 
+ Example of a program run and input (in bold). Note: program should exit on ‘q’ to quit and produce the histogram.

Example Output:
> Enter your total PASS credits: 120
> Enter your total DEFER credits: 0
> Enter your total FAIL credits: 0
> Progress
>
> Would you like to enter another set of data?
> Enter 'y' for yes or 'q' to quit and view results: y
> Enter your total PASS credits: 100
> Enter your total DEFER credits: 0
> Enter your total FAIL credits: 20
> Progress (module trailer)
>
> Would you like to enter another set of data?
> Enter 'y' for yes or 'q' to quit and view results: y
> Enter your total PASS credits: 80
> Enter your total DEFER credits: 20
> Enter your total FAIL credits: 20
> Module
>
> Would you like to enter another set of data?
> Enter 'y' for yes or 'q' to quit and view results: y
> Enter your total PASS credits: 60
> Enter your total DEFER credits: 0
> Enter your total FAIL credits: 60
> Module retriever
>
> Would you like to enter another set of data?
> Enter 'y' for yes or 'q' to quit and view results: y
> Enter your total PASS credits: 40
> Enter your total DEFER credits: 0
> Enter your total FAIL credits: 80
> Exclude
>
> Would you like to enter another set of data?
> Enter 'y' for yes or 'q' to quit and view results: 

**The program should now display a histogram of results using the graphics.py module. Example Window Below**

![image](https://github.com/trikto/Progression-Outcome/assets/77225260/2a5992c4-0203-4ce3-96a0-1896c76e32ed)


## List (extension)
In the above version, most of the solutions would use variables to store the input data. For Part 2, the solution is extended so that the program saves the input progression data to a list or nested list. Then access the stored data from the list and print the data in the following format below.
Example Output: The following should display after the histogram:

> Part 2:
> Progress - 120, 0, 0
> Progress (module trailer) - 100, 0, 20
> Module retriever - 80, 20, 20
> Module retriever - 60, 0, 60
> Exclude – 40, 0, 80


## Text File (extension)
Use python to save any input progression data to a text file. Later in the program, access the stored data and print out as shown below. Test plan not required. Example output (with data from text file):

> Part 3:
> Progress - 120, 0, 0
> Progress (module trailer) - 100, 0, 20
> Module retriever - 80, 20, 20
> Module retriever - 60, 0, 60
> Exclude – 40, 0, 80
