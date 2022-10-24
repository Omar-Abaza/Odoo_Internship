print("""
      
      
      In python there are three types of errors; syntax errors, logic errors and exceptions
      
         1. syntax errors : 
       
            The most common reason of an error in a Python program is when a certain statement is not in accordance with the prescribed usage.
            Such an error is called a syntax error. The Python interpreter immediately reports it, usually along with the reason.
            
        =========================================
        >>> print "hello"
        SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?
        =========================================
        
        ########################################################################################################################
        2. Logical errors 
            also called semantic errors, logical errors cause the program to behave incorrectly, but they do not usually crash the program.
            Unlike a program with syntax errors, a program with logic errors can be run, but it does not operate as intended.
       
       =========================================
        x = float(input('Enter a number: '))
        y = float(input('Enter a number: '))

        z = x+y/2
        print('The average of the two numbers you have entered is:',z)
            
        >>> 
        Enter a number: 3
        Enter a number: 4
        The average of the two numbers you have entered is: 5.0
        >>>
       =========================================
       
       ########################################################################################################################
        3. exceptions errors:
        
        Exceptions arise when the python parser knows what to do with a piece of code but is unable to perform the action.
        An example would be trying to access the internet with python without an internet connection;
        the python interpreter knows what to do with that command but is unable to perform it.
        
        =========================================
        try:
        age = int(raw_input("Enter your age: "))
        print("You must be {0} years old.".format(age))
        except ValueError:
        print("Your age must be numeric.")
        
        ####
        If the user enters a numeric value as his/her age, the output should look like this:
        ####
        
        Enter your age: 5
        Your age must be 5 years old.
        
        ####
        However, if the user enters a non-numeric value as his/her age, a ValueError is thrown when trying to execute the int() method on a non-numeric string, 
        and the code under the except clause is executed:
        ####
        
        Enter your age: five
        Your age must be numeric.
        =========================================
      
      
      """)

