def intro():
 
    appetizers=['Wings','Cookies', 'Spring Rolls'] 

    entrees= ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden' ]

    desserts= ['Ice Cream', 'Cake', 'Pie']

    drinks= ['Coffee', 'Tea', 'Unicorn Tears']


    print('**************************************')
    print('**    Welcome to the Snakes Cafe!   **')
    print('**    Please see our menu below.    **')
    print('**')


    print('** To quit at any time, type "quit" **')
    print('**************************************')

    print()

 


    print('Appetizers')
    print('----------')
    for i in appetizers:
        print(i)


    print()

    print('Entrees')
    print('----------')
    for i in entrees:
        print(i)

    print()


    print('Desserts')
    print('----------')
    for i in desserts:
        print(i)

    print()

    print('Drinks')
    print('----------')
    for i in drinks:
        print(i )

    print()


    print('***********************************') 
    print('** What would you like to order? **') 
    print('***********************************') 




def choose_from_menu():
    request = ""
    meal={}
    while request!="quit":
        print()
        request= str(input('>  '))
        if request in meal:
          meal[request]+=1
        else:
            meal[request]=1
        if request not in meal:
             print(f"sorry it is not in the meanu ")    
        if request!="quit":
            print(f"** {meal[request]} order of {request} have been added to your meal")  
       



                     
   

   
        

if __name__ == '__main__':
    intro()
    choose_from_menu()
    



