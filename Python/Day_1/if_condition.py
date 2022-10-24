
print("""
      
      
    The if statement executes a statement if a specified condition is truthy.
    If the condition is falsy, another statement in the optional else clause will be executed.


    At first you write the if statement and the action by writing :
      
      ############
        if "write the statement"
            "the action will happens"
      ############
      
    then you write the else if statement and the action if you the if statement didn't work by writing:  
           
      ############
        elif "write the statement"
            "the action will happens"
      ############   
        
    then you write the last else if statement and the action if non of the statement work by writing:  
        
      ############
        else "write the statement"
            "the action will happens"
      ############


        if a >= 0 and a < 50:
            print("you failed")
        elif  a >= 50 and a <= 100 :
            print("you passed")
        else:
            print("you entered a wrong answer ")
  
  
        Here is an example ::
        Enter a number between 0-100
        from (0-49) you failed
        from (50-100) you passed
        another will print the else statement

""")


a = int(input ("enter your degree : "))
if a >= 0 and a < 50:
    print("you failed")
elif  a >= 50 and a <= 100 :
  print("you passed")
else:
  print("you entered a wrong answer ")