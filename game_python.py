from random import randint 

def level2():
  print("hello")
 
def level1():
      heal_up_num = 4 
      health = 30 
      monster_health = 50 
      monster_a = 10 
      player_a = 50
      control1 = 0
      while control1 == 0: 
        monster_a = 10
        print("health: ", health) 

        print("monster health:", monster_health) 

        move1 = input(""" a = attack(5hp), d = defend(10% less damage), h = heals up 5 points(every 3 moves) 

        ROOKIE MONSTER 

        """) 

        if  move1 == "h": 

          if heal_up_num >= 3: 
            health += 25 
            heal_up_num = 3
            print("you healed up")
          
          elif heal_up_num < 3:
            print("you need to wait", heal_up_num, "turns") 
            monster_a = 0

        elif  move1 == "a":
          monster_health -= player_a
          print("you attacked") 
          heal_up_num += 1

        elif  move1 == "d": 
          monster_a = 1 
          print("you defended")
          heal_up_num += 1

        else:
          print("error")

        health -= monster_a  

        if monster_health < 1: 
          print("health: ", health) 
          print("monster health:", monster_health) 
          print("""you won!
          
          
          
          
          
          """) 
          control1 += 1
          level2()

        if health <= 0: 
          print("you lost...") 
          exit()

        print("""
        
        
        
        
        
        
        """) 
if __name__ == "__main__": 
  level1()  