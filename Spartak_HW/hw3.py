# l1 = [2,3,5,6,7]
# l2 = [2,8,5,4,9]

# for i in l1:
#     if i in l2:
#         print('Krknvogh tiv',i, end = ' ')

# class Shun:
#     def __init__(self,anun, tariq, guyn):
#         self.anun = anun
#         self.tariq = tariq
#         self.guyn = guyn

#     def bark(self):
#         return f"{self.guyn} guyni shuny {self.anun} anunov sksec hachal" 
    
#     def mardkain_tariq(self):
#         return self.mardkain_tariq * 7
    
# im_shun = Shun('Reqs',34,'Sev')

# print(im_shun.bark())
# print(f"{im_shun.anun}i martkain tariqy {im_shun.mardkain_tariq()}e")


class Avto:
    def __init__(self, maknish, guyn, aragutyun):
        self.maknish = maknish
        self.guyn = guyn
        self.aragutyun = aragutyun

    def tras(self):
        return f"{self.guyn} guyn i  {self.maknish} en sksec sharjvel {self.aragutyun} aragutyamb"
    
lav_avto = Avto('BMW','Sev',40)

print(lav_avto.tras())