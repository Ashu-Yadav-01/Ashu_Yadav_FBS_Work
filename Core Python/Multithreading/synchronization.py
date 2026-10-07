from threading import Thread,Lock
from time import sleep
class withdrw:
    bal=100
    lock=Lock()
    def run(self):
        #withdrw.lock.acquire()
        if withdrw.bal>0:
            print(self.name,"Check Balance")
            withdrw.bal=withdrw.bal-50
            print(self.name,"Balance get Withraw")
            sleep(1)
        else:
            print("Insuficent fund")
        print(f"Remaining amount={withdrw.bal}")
        withdrw.lock.release()
    def deposite(self):
        print(f"get Credeted")

    #def run(self):
     #   self.deposite()        
b1=withdrw()
#t1=withdrw()
#t2=withdrw()            
 
t1=Thread(target=b1.withdraw)
t2=Thread(target=b1.deposite) 
t1.start()
t2.start()                     

            

    