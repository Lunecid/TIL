class Football_Player :
    def __init__(self,name,age,height,weight,league,club,nationality,position,foot,race):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.league = league
        self.club = club
        self.nationality = nationality
        self.position = position
        self.foot = foot
        self.race = race

    def shot(self):

        import random
        foot = ['왼발','오른발']
        foot_result = random.choice(foot)
        shotting_position = ['near','middle','far']
        shotting_height = ['low','center','high']
        shotting_p_result= random.choice(shotting_position) 
        shotting_h_result = random.choice(shotting_height)
        print(f'{self.name}이/가 {foot_result}로 {shotting_p_result}포스트 {shotting_h_result}로 찼습니다.')


f1 = Football_Player('손흥민',30,180,78,'EPL','토트넘','한국','공격수','양발','인종')
print(Football_Player.shot(f1))

class Goal_Keeper(Football_Player):
    def __init__(self,name,age,height,weight,league,club,nationality,position,foot,race,hand):
        
        super().__init__(self,name,age,height,weight,league,club,nationality,position,foot,race)

        self.hand = hand

    def block(self):

        import random
        foot = ['왼발','오른발']
        hand = ['왼손', '오른손']
        body_choice = [foot,hand]
        block_choice = random.choice(random.choice(body_choice))
        blocking_position = ['near','middle','far']
        blocking_height = ['low','center','high']
        blocking_way = ['close','not close']
        blocking_p_result= random.choice(blocking_position) 
        blocking_h_result = random.choice(blocking_height)
        blocking_w_result = random.choice(blocking_way)
        print(f'{self.name}이/가 {block_choice}로{blocking_w_result}하여 {blocking_p_result}의{blocking_h_result}를 막는 것을 선택 했습니다.')

f2 = Goal_Keeper('데헤아',32,190,90,'EPL','맨유','스페인','골키퍼','오른발','인종','양손')
print(Goal_Keeper.block(f2))
