def intro():
    introduction = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ***********************************
    ** What would you like to order? **
    ***********************************
    """

    print(introduction)


def choose_from_menu():
    request = ""
    meal={}
    while request!="quit":
        request= str(input('  >  '))
        if request in meal:
          meal[request]+=1
        else:
            meal[request]=1
        if request!="quit":
            print(f"  ** {meal[request]} order of {request} have been added to your meal")           
   

   
        

if __name__ == '__main__':
    intro()
    choose_from_menu()
    



