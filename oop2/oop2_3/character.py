from abc import *

#추상 클래스로 만듭니다.
class Character(metaclass = ABCMeta):
    def __init__(self, name, hp, power):
        self.name = name
        self.HP = hp
        self.power = power
        
    #추상 메서드
    #파생 클래스는 반드시 attack과 get_damage 메서드를
    #오버라이딩 해야 합니다.
    @abstractmethod
    def attack(self, other, attack_kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return '{} : {}'.format(self.name, self.HP)

class Player(Character):
    def __init__(self, name = 'player', hp = 100, power = 10, *attack_kinds):
        super().__init__(name, hp, power)
        
        #추가된 인스턴스 멤버 
        self.skills = []
        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)

    #재정의된 attack() 메서드
    #반드시 재정의 되어야 한다
    def attack(self, other, attack_kind):
        if attack_kind in self.skills:
            other.get_damage(self.power, attack_kind)

    #재정의된 get_damage() 메서드
    #반드시 재정의 되어야 한다
    def get_damage(self, power, attack_kind):
        '''
        만약 공격 종류가
        플레이어의 기술 중 하나라면
        데미지가 절반으로 감소합니다.  
        '''
        if attack_kind in self.skills:
            self.HP -= (power//2)
        else:    
            self.HP -= power

#불과 얼음 몬스터는 모두 Character 클래스에서 추가된
#attack_kind 멤버를 가지고 있고
#attack 메서드와 get_damage 메서드는 동일한 행동을 한다
#공통된 부분이 많으므로 Monster라는 부모 클래스를 만들어
#공통적인 코드를 위치시킨다
class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attack_kind = 'None'

    def attack(self, other, attack_kind):
        if self.attack_kind == attack_kind:
            other.get_damage(self.power, attack_kind)

    #만약 플레이어가  불 공격을 할 때
    #공격받는 객체가 얼음 몬스터라면
    #체력이 깎이겠지만
    #공격받는 객체가 불 몬스터라면
    #오히려 체력이 증가한다
    def get_damage(self, power, attack_kind):
        '''
        몬스터는 자신과 타입이 같은 공격을 당하면
        오히려 체력이 늘어납니다.
        조심해서 공격하세요.
        '''
        if self.attack_kind == attack_kind:
            self.HP += power
        else:
            self.HP -= power

    def get_attack_kind(self):
        return self.attack_kind

class IceMonster(Monster):
    def __init__(self, name = 'Ice monster', hp = 50, power = 10):
        super().__init__(name, hp, power)
        self.attack_kind = 'ICE'

class FireMonster(Monster):
    def __init__(self, name = 'Fire monster', hp = 50, power = 20):
        super().__init__(name, hp, power)
        self.attack_kind = 'FIRE'
        
    #메서드 추가
    #FireMonster만의 행동
    def fireball(self):
        print('fireball')

if __name__ == "__main__":
    player = Player('sword master',100, 30, 'ICE')
    monsters = []
    monsters.append(IceMonster())
    monsters.append(FireMonster())
    
    for monster in monsters:
        print(monster)

    for monster in monsters:
        #공격을 받는 monster 객체가
        #어떤 몬스터인지에 따라 호출되는 메서드가 달라지고
        #그에 따라 결과도 달라진다
        player.attack(monster, 'ICE')

    print('after the player attacked')

    for monster in monsters:
        print(monster)
    print('')
    
    print(player)
    
    for monster in monsters:
        #플레이어가 'ICE' 공격만 가지고 있으므로
        #아이스 몬스터가 공격할 때는 공격력(10)의 반만 깎이고
        #파이어 몬스터가 공격할 때는 공격력(20)이 그대로 깎인다.
        #모든 공격이 끝난 후 플레이어의 체력은
        #100 - ((10//2) + 20) = 75 
        monster.attack(player, monster.get_attack_kind())
    print('after monsters attacked')
    
    print(player)        
        
