class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    #def __add__(self, other):
        #sec = self.sec + other.sec
        #minute = self.min + other.min
        #hour = self.hr + other.hr

       # minute += sec // 60
        #sec = sec % 60

        #hour += minute // 60
       # minute = minute % 60

        #return Time(hour, minute, sec
    def __add__(self, other):
        tsec=0
        tmin=0
        thr=0
        tsec=(self.Sec+other.sec)%60
        rem=(self.Sec+other.Sec)//60
        tmin=((self.Min+other.Min)%60)+rem
        tmin=(self.Min+other.Min)//60
        thr=self.hr
       
    


    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"


t1 = Time(1, 2, 33)
t2 = Time(3, 5, 33)

#print(t1)
#print(t2)
print(t1 + t2)



    
            