def get_grades():
    """
    Asks the user to input grades one by one and returns a list of those grades.
    """
    # TODO: Initialize an empty list to store the grades
    grades = []

    print("Enter grades (type 'done' or '-1' to finish):")

    while True:
        
        # TODO: Take input from the user
        print("Enter grades (type 'done' or '-1' to finish):")
        Grades=input("Enter your grade, please ")
        
        # TODO: Check if the user wants to stop
        if Grades== "done" or Grades=="-1":
            break
        
        # Check if the input is 'done' or '-1'. If so, break the loop.
        
        
        # TODO: Convert the input to a number (integer or float)
        if Grades == ("-1") :
            Grades=float(Grades)
        
# TODO: Add the number to your grades list
        grades.append(Grades)
        


    # TODO: Return the populated list of grades
    return grades
    # This is crucial so the other function can use this data.


def analyze_grades(sl):
    """
    Analyzes a list of scores to find the average,
    number of passing grades, and number of failing grades.
    """
    # TODO: Check if the list is empty before proceeding
    if len(sl)==0 :
        return []
    # (To avoid dividing by zero later!)
    
    
    # TODO: Initialize variables (sum, pass_count, fail_count)
    Sum= 0
    pass_count= 0
    fail_count= 0    
    # TODO: Loop through sl and calculate stats
    for score in sl:
        sum = sum + score

    # TODO: Calculate Average and Print results
    Avg=sum/len(sl)

# --- Main Execution ---

# TODO: Call the get_grades function and store the result in a variable

# TODO: Call the analyze_grades function passing the list you just created
