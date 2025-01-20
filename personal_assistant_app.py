#Documentation for this code : https://drive.google.com/file/d/1F8MxbhGuaB2ahk09-9yKdROrrR2J4NUQ/view?usp=sharing
import requests
from bs4 import BeautifulSoup
import random
class User:
    def __init__(self):
        self.users_list = []
        self.store_tasks = []
        self.expenses_tracker = []

    def get(self):
        print(f'Welcome to the Personal Assistant Application! \n1. Log In \n2. Sign Up \n3. Exit')

    def select_options(self):
        self.get()
        try:
            i = int(input('Enter your choice: '))
        except ValueError:
            print('Value Error: Choice must be an number.')
        if (i == 1):
            print(f'Your Choice is: {i} \nThis is Login.')
            username = input('Username: ')
            password = input('Password: ')
            for eachUser in self.users_list:
                if (eachUser[0] == username and eachUser[1] == password):
                    print("Successful Login")
            url = "https://commonslibrary.org/marshall-ganz-quotes-and-wisdom/?gad_source=1&gclid=Cj0KCQiAuou6BhDhARIsAIfgrn5Iexl7qSzY1DzQA9eJvBHqvQIjl0slxOYhzvaaHwCboTVK9wmxnwgaApeHEALw_wcB"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all('p')
            quotes = [quote.text.strip() for quote in paragraphs]
            if (len(quotes) != 0):
                print(f'\nQuote of the Day: {random.choice(quotes)}\n')
            else:
                print('No Quotes Found')
            user.select_options_to_assist()
            
        elif (i == 2):
            print(f'Your Choice is: {i} \nThis is Submit.')
            username = input('Username: ')
            password = input('Password: ')
            self.users_list.append([username, password])
            print("Account created successfully!")
            print("Current Users:", self.users_list)
            user.select_options_to_assist()

        else:
            print(f'Your Choice is: {i} \nThis is Exit.')
    
    def select_options_to_assist(self):
        while True:
            print('Main Menu: \n1. Task Management \n2. Expense Tracker \n3. View Weather \n4. Log Out')
            try:
                choice = int(input('Enter your choice: '))
                if choice == 1:
                    self.task_manager()
                elif choice == 2:
                    self.expense_tracker()
                elif choice == 3:
                    self.view_weather()
                elif choice == 4:
                    print("Logging out...")
                    print("Thanks for using!!")
                    break
                else:
                    print("Feature not implemented yet.")
                    
            except ValueError:
                print('Value Error: Choice must be an number.')


    def task_manager(self):
        a = True
        while a:
            try:
                task_option = input('Enter your choice (add - for adding tasks/ remove - for removing/ view - to view tasks): ')
            except ValueError:
                print('Task Option must be a string.')
            if task_option.lower() == 'add':
                print('Add a task: ')
                task_name = input('Task Name: ')
                task_priority = input('Priority (High/Medium/Low): ')
                task_status = input('Status (Pending/Completed): ')
                self.store_tasks.append({
                    "task_name": task_name,
                    "task_priority": task_priority,
                    "task_status": task_status
                })
                print('Task added successfully!')
                
            elif task_option.lower() == 'remove':
                inp = input('Enter the task name to remove the task: ')
                for task in self.store_tasks:
                    if(task["task_name"] == inp):
                        self.store_tasks.remove(task)
                print('Task is Removed Successfully!!')

            elif task_option.lower() == 'view':
                print("Tasks:", self.store_tasks)
            elif task_option.lower() == 'back':
                break
            else:
                print("Invalid option. Try again.")
                a = False

    def expense_tracker(self):
        a = True
        total = 0
        while a:
            print('Expense Summary (To exit enter Chore as exit and Cost as 0): ')
            item = input('Chore: ')
            cost = int(input('Cost: '))
            total = total + cost
            if (item != 'exit' and cost != 0):
                print(f'-{item}: ${cost}')
                self.expenses_tracker.append({"item" : item, "cost": {cost}})
                print(f'-Total: ${total}')
            else:
                break
        a = False
    
    def view_weather(self):
        print("Weather Report: ")
        BASE_URL = 'http://api.weatherapi.com/v1/current.json'
        API_KEY = 'ce98504065214d1992a82723242411'
        name = input('Enter the City: ')
        url=f"{BASE_URL}?key={API_KEY}&q={name}"
        response=requests.get(url)
        if response.status_code==200:
            weather_data=response.json()
            weather_info = weather_data
            print(f"City: {weather_info['location']['name']}")
            print(f"Condition: {weather_info['current']['temp_c']} °C")
            print(f"Temperature: {weather_info['current']['condition']['text']}")
        else:
            print(f"Failed to Fetch the data of {name}")


user = User()
user.select_options()