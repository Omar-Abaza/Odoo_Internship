
print("""
      
      
    With the while loop we can execute a set of statements as long as a condition is true.


    1 - The while Loop
        first you write the while statement and the action by writing :

      ############
        while "write the statement"
            "the action will happens"
      ############
      
      ex: Print i as long as i is less than 5:
      
        i = 1
        while i < 5:
            print(i)
            i += 1
            
        ***** The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
        ***** remember to increment i, or else the loop will continue forever.
        
    ==================================================================================
      
    2 - The break Statement
        With the break statement we can stop the loop even if the while condition is true:
           
        ex: Exit the loop when i is 3:
        
        i = 1
        while i < 6:
            print(i)
            if i == 3:
                break
            i += 1 
     
    ==================================================================================
      
    3 - The continue Statement
        With the continue statement we can stop the current iteration, and continue with the next:
           
        ex: Continue to the next iteration if i is 3:

        i = 0
        while i < 6:
            i += 1
            if i == 3:
                continue
            print(i)
            
    ==================================================================================
      
    4 - The else Statement
        With the else statement we can run a block of code once when the condition no longer is true:

        ex: Print a message once the condition is false:

        i = 1
        while i < 6:
            print(i)
            i += 1
        else:
            print("i is no longer less than 6")

    ==================================================================================
    

""")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")