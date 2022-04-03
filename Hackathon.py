#Program that keeps stock of your pantry, and automatically adds items to the grocery list.

menu='''\nWelcome to your Digital Shopping List! Select an option:
1 - Modify the list of your pantry's contents
2 - See your current stores of food
3 - Check which items are running low
4 - See your automatically generated shopping list
5 - Exit
Selection:\n'''

#Any item <=2 is considered 'low'

option=0
typo=0
item=''
value=0
change=0
modify=0
current={'Bread':3,'Baked Beans':4,'Chicken Broth':1,'Cookies':0}
low=[]
shopping=[]

while option==0:
    option=int(input(menu))

    if option==1:
        item=str(input('Which item is being added/used? '))

        if item not in current.keys():
            typo=int(input("This appears to be a new item in your pantry. Would you like to add it to your pantry?\t1 - Yes\t2 - No\n"))

            if typo==1:
                value=int(input("Please input how many of this new item you have bought: "))
                current[item]=value
                print('Item successfully added to database.')
            else:
                print('Contents are unchanged.')
        elif item in current.keys():
            modify=int(input('Are you taking or adding this item?\t1 - Adding\t 2 - Taking\n'))
            if modify==1:
                change=int(input('How many of this item have you added? '))
                current[item]=current.get(item)+change
                print('Contents updated.')

            elif modify==2:
                change=int(input('How many of this item have you taken? '))
                current[item]=current.get(item)-change
                print('Contents updated.')
        
        option=0

    elif option==2:
        print('Here is the current contents of your pantry:')
        print(current)
        option=0

    elif option==3:
        for key in current:
            if current.get(key)<=2:
                if key not in low:
                    low.append(key)
            elif current.get(key)>2:
                if key in low:
                    low.remove(key)

        if low:
            print(low, 'are running low!')
        elif not low:
            print('Nothing is running low.')

        option=0

    elif option==4:
        for key in current:
            if current.get(key)<=0:
                if key not in shopping:
                    shopping.append(key)
            elif current.get(key)>0:
                if key in shopping:
                    shopping.remove(key)

        if shopping:
            print('Here is your shopping list:')
            print(shopping)
        if not shopping:
            print("Your shopping list is empty.")
            
        option=0

    elif option==5:
        print("Exiting...")

    else:
        print("Please choose one of the available options.")
        option=0
