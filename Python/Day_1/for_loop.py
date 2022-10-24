
print("""
      
      
    A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).



    1 - The for Loop
        With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

      ############
        for x in "sequence"
            "the action will happens"
      ############
      
      ex: Print each name in a names list:
     
        names = ["ahmed", "ali", "omar"]
        for x in names:
            print(x)
        
    >>> output :
            ahmed
            ali
            omar
        
    ==================================================================================
      
    2 - The break Statement
        With the break statement we can stop the loop before it has looped through all the items:
           
        ex: Exit the loop when x is "ali":
        
        names = ["ahmed", "ali", "omar"]
        for x in names:
            print(x)
            if x == "ali":
                break
                
    >>> output :
            ahmed
            ali
                 
    ==================================================================================
      
    3 - The continue Statement
        With the continue statement we can stop the current iteration of the loop, and continue with the next:
           
        ex: Continue to the next iteration if x is "ali":

        names = ["ahmed", "ali", "omar"]
        for x in names:
            if x == "ali":
                continue
            print(x)
                
    >>> output :
            ahmed
            omar

    ==================================================================================
      
    4 - The else Statement
        The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

        ex: Break the loop when x is "ali", and see what happens with the else block:

        names = ["ahmed", "ali", "omar"]
        for x in names:
            if x == "ali": break
            print(x)
        else:
            print("Finally finished!")
            
        >>> output :
            ahmed
            
        * The else block will NOT be executed if the loop is stopped by a break statement.

    ==================================================================================
    

""")

names = ["ahmed", "ali", "omar"]
for x in names:
    if x == "khaled": break
    print(x)
else:
    print("Finally finished!")