project = open("Day_1\Project 1\documentation.txt", "x")

project.write("""
      
    1 - What you have learned today?

    I have learned how to write a readable documentation, how to make it clear and useful for the reader, 
    how to describe the details amd make shore to add an examples that makes the reader comfortable that 
    everything is clear and he can understands it by practicing the examples.
    
    also the comments and documentations makes my code more clear and readable for me at least it makes 
    me thinks of the code and describe it in myself so I can know if the code is stable and readable or 
    it's difficult to keep up with it.
        
    ==================================================================================
      
    2 - What new skills you need?

    I need to practice more in writing comments and documentations.
    I need to make my code stable and readable.

    ==================================================================================
      
    3 - What is your expectations?
    
    I expect to write a clean code at the end.   

    ==================================================================================
      
    4 - How was the day for you?

    It's been great. Starting the day by playing some IQ questions was a good practice for the brain and 
    made me get along with the group quickly.
    Practicing the right strategies in writing the code by adding comments and documentations and sharing it
    with the group made me focus on a new roles that I should practice more end involve it my code in the future.

    ==================================================================================
    

""")
project.close()

project = open("Day_1\Project 1\documentation.txt", "r")
print(project.read())
