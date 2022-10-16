from socket import timeout
import time
from turtle import title
from pip import main
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water!!",
            message = '''Health experts commonly recommend eight 8-ounce glasses, which equals about 2 liters, or half a gallon a day. This is called the 8x8 rule and is very easy to remember.''',
            app_icon = ("C:\\Users\\jaymin\\Desktop\\Python Projects\\Water notification system\\icon.ico"),   
            timeout = 10
        )
        time.sleep(60*60)