class Gun:
    def __init__(self, kind):
        self.kind = kind

    def bang(self):
        print('bang bang!')

class Police:
    def __init__(self):
        self.gun = None           #1

    def acquire_gun(self, gun):   #2
        self.gun = gun

    def release_gun(self):        #3
        gun = self.gun
        self.gun = None
        return gun
        
    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print("Unable to shoot")

if __name__ == "__main__":
    p1 = Police()                #4
    print('p1 shoots')
    p1.shoot()
    print('')

    #p1은 아직 총을 소유하지 않음. 
    revolver = Gun('Revolver')
    #p1이 revolver를 획득
    p1.acquire_gun(revolver)    #5
    #이제 p1이 총을 소유하므로
    #revolver는 None
    revolver = None
    
    print('p1 shoots again')
    p1.shoot()
    print('')

    #p1이 총을 반납했으므로
    #더 이상 총을 소유하지 않는다
    revolver = p1.release_gun() #6
    print('p1 shoots again')
    p1.shoot()

    
