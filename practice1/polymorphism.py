#Animal Sounds
class Dog:
    def sound(self):
        print("barks")     
class Cat(Dog):
    def sound(self):
        print("meow")
class Cow(Dog):
    def sound(self):
        print("cow")
obj=[Dog(),Cat(),Cow()]
for objects in obj:
    objects.sound()
    
#2
class Notification:
    def send(self):
        print("Sending notification")
class EmailNotification(Notification):
    def send(self):
        print("Email notification sent")
class SMSNotification(Notification):
    def send(self):
        print("SMS notification sent")
class PushNotification(Notification):
    def send(self):
        print("Push notification sent")
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]
for notification in notifications:
    notification.send()