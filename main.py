import datetime
import birthday

today = datetime.date.today()
my_next_bday = datetime.date(2023, 4, 5)
days_away = my_next_bday - today

if my_next_bday == today: 
    print(birthday.random_message)
else: 
    print(f'my next birthday is {days_away.days} days away!')
