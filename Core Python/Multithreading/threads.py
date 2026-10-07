from threading import Thread
from time import sleep
class Demo1(Thread):
    def run(self):
        for i in range(5):
            print("Pizza🍕🍕🍕")
            sleep(1)
            

class Demo2(Thread):
    def run(self):
        for i in range(5):
            print("Burger🍔🍔🍔")
            sleep(1)

t1=Demo1()
t2=Demo2()   
t1.start()
t2.start()  
print("Sub ")



#print(t1.getName())
#print(t2.getName())                            