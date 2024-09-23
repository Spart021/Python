class Car:
    def   __init__ (self, gin, maknish, guyn):
       self.gin = gin
       self.maknish = maknish
       self.guyn = guyn

    
    def __str__(self):
        return f"{self.maknish}, {self.gin}, {self.guyn}"
    def avto2(self):
        return f"{self.guyn} i {self.maknish} en xodi cher enknum vornel arjer {self.gin}"

    def avto1(self):
        return f"{self.maknish} en sksec sharjvel erb benzin lcrin"
 
xosqi = Car(gin = 60000, maknish = 'Lada', guyn = 'Spitak')

print(xosqi)
print(xosqi.avto2(),xosqi.avto1())

