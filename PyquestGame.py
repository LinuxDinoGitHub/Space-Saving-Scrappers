import random
from colorama import Fore, Back, Style
import time
#Welcome to the source code of SPACE SAVING SCRAPPERS! There will be comments (Syntax: #commenttext) to guide you how the code works.
optionC1 = Fore.BLACK
optionC2 = Fore.BLACK
optionC3 = Fore.BLACK
optionStatus = []

#Color scheme
colorReset = Fore.RESET + Back.RESET
galactic1 = Fore.WHITE + Back.BLACK
galactic2 = Fore.MAGENTA + Back.BLACK
galactic3 = Fore.RED + Back.BLACK
galactic4 = Fore.GREEN + Back.BLACK
mealcolor = Fore.YELLOW + Back.BLACK


art1 = """
     _______..______      ___       ______  _______ 
    /       ||   _  \    /   \     /      ||   ____|
   |   (----`|  |_)  |  /  ^  \   |  ,----'|  |__   
    \   \    |   ___/  /  /_\  \  |  |     |   __|  
.----)   |   |  |     /  _____  \ |  `----.|  |____ 
|_______/    | _|    /__/     \__\ \______||_______|
                                          """
art2 = """
                                                                                            ^
     _______.     ___   ____    ____  __  .__   __.   _______                        __    / \__
    /       |    /   \  \   \  /   / |  | |  \ |  |  /  _____|       _______________/__\__/_____\_______
   |   (----`   /  ^  \  \   \/   /  |  | |   \|  | |  |  ___       /                                   > > >
    \   \      /  /_\  \  \      /   |  | |  . `  | |  | |_  |  ---<    O    O   Created by: Linus Choi  > > >
.----)   |    /  _____  \  \    /    |  | |  |\   | |  |__|  |      \___________________________________>  >
|_______/    /__/     \__\  \__/     |__| |__| \__|  \_______|                      \__/


"""

art3 = """
     _______.  ______ .______          ___      .______   .______    _______ .______          _______.
    /       | /      ||   _  \        /   \     |   _  \  |   _  \  |   ____||   _  \        /       |
   |   (----`|  ,----'|  |_)  |      /  ^  \    |  |_)  | |  |_)  | |  |__   |  |_)  |      |   (----`
    \   \    |  |     |      /      /  /_\  \   |   ___/  |   ___/  |   __|  |      /        \   \    
.----)   |   |  `----.|  |\  \----./  _____  \  |  |      |  |      |  |____ |  |\  \----.----)   |   
|_______/     \______|| _| `._____/__/     \__\ | _|      | _|      |_______|| _| `._____|_______/
"""

gameoverart = """
                                                                                                   _|  
   _|_|_|    _|_|    _|      _|  _|_|_|_|        _|_|    _|      _|  _|_|_|_|  _|_|_|            _|    
 _|        _|    _|  _|_|  _|_|  _|            _|    _|  _|      _|  _|        _|    _|      _|  _|    
 _|  _|_|  _|_|_|_|  _|  _|  _|  _|_|_|        _|    _|  _|      _|  _|_|_|    _|_|_|            _|    
 _|    _|  _|    _|  _|      _|  _|            _|    _|    _|  _|    _|        _|    _|          _|    
   _|_|_|  _|    _|  _|      _|  _|_|_|_|        _|_|        _|      _|_|_|_|  _|    _|      _|  _|    
                                                                                                   _| 
"""

canteenart = """                                                                   
                                                                                                            
                                                                   @@@                      
                                                              @@@@@@@@@@@@@                 
                                                          @@@@@@@        @@@@@@@@           
                                                    @@@@@@@@@                @@@@@@@@@      
                                                     @@@@@@@@@@@@@@                 @@@@@@@ 
                                                     @@@       @@@@@@@@                @@@@@
                                      @@@@@@@@@@@    @@@            @@@@@@@@       @@@@@@@@@
   @@@@@@@@@@@@@                 @@@@@@@@    @@@@@@@@@@@                  @@@@@@@@@@@@   @@@
   @@ @@  @@@@@@             @@@@@@@                @@@@@@@@@@@@@@           @@@@@     @@@@@
   @@ @@  @@@@@@            @@@@@                             @@@@@@@@@@@      @@@  @@@@@   
   @@@@@@@@@@@@@            @@@@@@@@@@@@@                             @@@@@    @@@  @@@@@@@@
   @@@@@@@@@@@@             @@@       @@@@@@@@@@@                 @@@@@@@@@         @@@   @@
    @@@@    @@              @@           @@@ @@@@@@@@@@@@      @@@@@@    @@  @@@@@  @@@     
 @@@@@@@@@@@@@@@@@        @@@@@@@@@                   @@@@@@@@@@@        @@@@@@@@@@@@@@     
@@@@@@@@@@@@   @@@        @@@@@@@@@@@@@@@@@               @@@           @@@@@@     @@@@@@@@ 
@@@            @@@        @@@    @@@@@@@@@@@@@@@@@@@      @@@      @@@@@@@@             @@@@
@@@            @@@        @@@             @@@@@@@@@@@@@   @@@     @@@@@@@@@                 
@@@            @@@                                @@@@@   @@@     @@@   @@@@@@@@            
@@@            @@@                                  @@@   @@@     @@@        @@@@           
@@@            @@@                                  @@     @      @@           @@@@@@       
@@@            @@@                @@@@@  @@@   @@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@   
 @@@@@@@@@@@@@@@@@               @@   @   @@@   @@@ @ @@ @ @@ @@ @@@ @@ @@@ @@@ @@    @@@@@@
   @@@@@@ @@@@@@                 @@      @@@@@  @@@@@    @    @@@@   @@@@   @@@@@@        @@
   @@@                            @@ @@@@@   @@ @@ @@   @@@   @@@@@@ @@@@@@ @@ @@@          
                                                                                            
                                                                                            
                                                                                            """

recycleintroart = """                                                                                                                 
                                                                                                                 
                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                              
                                   @@@@@@@@@@@@@@@@                             @@@@                             
                                   @@@@                 @@@@@@                   @@@                             
                                    @@@                @@@@@@@@@                 @@@@                            
                                    @@@               @@@@  @@@@                 @@@@                            
                                    @@@              @@@@    @@                   @@@                            
                                    @@@            @@@@@      @@@@@@              @@@                            
                                    @@@       @@  @@@@        @@@@@@@@@           @@@                            
                                    @@@     @@@@@@@@@         @@@@@@@@@@          @@@@                           
                                    @@@    @@@@ @@@@@@@      @@@@@@@@@             @@@                           
                                    @@@    @@@@@@@@@@@             @@@@            @@@                           
                                    @@@       @@                    @@@@           @@@                           
                                    @@@      @@@                     @@@@@         @@@                           
                                    @@@     @@@              @@@@@     @@@@        @@@@                          
                                    @@@    @@@@@@@          @@@@@@@ @@@@@@@@       @@@@                          
                                    @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@                          
                                    @@@            @@@@@@@@@@@@@@@                 @@@@                          
                                    @@@                     @@@@@                  @@@@                          
   @@@@@@@@@@@@@@@@                 @@@                                            @@@@                          
   @@@@@@@@@@@@@@@@                 @@@@@@@@@@@                                    @@@@                          
   @@@@@@@  @@@@@@@                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@                          
   @@@@@@@   @@@@@@                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
   @@@@@@@@@@@@@@@@                                                             @@@@@@                           
   @@@@@@@@@@@@@@@@                                              @@@@@@@@@@@@@@@@                                
      @@@     @@@@                                         @@@@@@@@@@@@@@@@@@@@@@@@                              
     @@@@   @@@@@@@@@                                     @@@@@      @@@@@      @@@@                             
 @@@@@@@@@@@@@@@@@@@@@                                   @@@@      @@@@@@@@      @@@@                            
@@@@@@@@@@@@@      @@@                                 @@@@       @@@@@@@@@@      @@@                            
@@@@               @@@                                @@@@        @@@    @@@       @@@                           
 @@@               @@@                               @@@@         @@@   @@@@        @@@                          
 @@@               @@@                              @@@@          @@@@@@@@@         @@@@                         
 @@@               @@@                             @@@@             @@@@@@           @@@                         
 @@@               @@@                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
 @@@               @@@                            @@@@                               @@@                         
 @@@               @@@                             @@@                               @@@                         
 @@@@@@@@@@@@@@@@@@@@@                             @@@                               @@@                         
 @@@@@@@@@@@@@@@@@@@@@                             @@@                               @@@                         
   @@@@@@@@  @@@@@@@                               @@@                               @@@                         
    @@@                                            @@@@                              @@@                         
                                                   @@@@                              @@@                         
                                                   @@@@                              @@@                         
                                                   @@@                               @@@                         
                                                   @@@                               @@@                         """

rubbishart = """                                                                                                               
                                                                                                               
                                                                                                               
           ============          ===========             ===========           ===========                            
          /            \        /           \           /           \         /           \                   
         /    1.PET     \      /   2.HDPE    \         /    3.PVC    \       /    4.LDPE   \                  
        /                \    /               \       /               \     /               \                
        ==================    =================       =================     =================                 
       *- =: *  *  + .- :-   +* -: -. -: :: =. *     :*: * := .= :: :: -.  :*- =..-. -. + .= =.                
       *- =: *  *  + .- :-   +* -: -. -: :: =. *     :*: * := .= :: :: -.  :*- =..-. -. +  + =.                
       *- =: =  :  - .- :-   +* -: :. .. .: =. *     :*: * :- .: :: :: -.  :*- =..-  :. =  + =.                
       *- =:         .- :-   +* -:          =. *     :*: *          :: -.  :*- =.          + =.                
       *- +.         .= :-   +* =           -: *     :*:.+          :: -.  :*-.-.          + =.                
       *- +. *  -  + .= :-   +* =  -. .. :: -: *     :*:.+ :- .. :- :: -.  :*-.-..-  .  =. + =.                
       *- +. *  *  + .= :-   +* =  -. -: :: -: *     :*:.+ -- .= :- :: -.  :*-.-..-  -. =. + =.                
       *- +. *  *  +  = :-   +* =  -. -: :: :- *     :*:.+ -- .= :- :: -.  :*-.-..-  -. =. + =.                
         ...............       ...............         ...............        ...............
                                                                                                   
                       ============          ===========             ===========           ===========                            
                      /            \        /           \           /           \         /           \                   
                     /     5.PP     \      /     6.PS    \         /   7.Other   \       /   8.Normal  \                  
                    /                \    /               \       /               \     /     waste     \                
                    ==================    =================       =================     =================                 
                   *- =: *  *  + .- :-   +* -: -. -: :: =. *     :*: * := .= :: :: -.  :*- =..-. -. + .= =.                
                   *- =: *  *  + .- :-   +* -: -. -: :: =. *     :*: * := .= :: :: -.  :*- =..-. -. +  + =.                
                   *- =: =  :  - .- :-   +* -: :. .. .: =. *     :*: * :- .: :: :: -.  :*- =..-  :. =  + =.                
                   *- =:         .- :-   +* -:          =. *     :*: *          :: -.  :*- =.          + =.                
                   *- +.         .= :-   +* =           -: *     :*:.+          :: -.  :*-.-.          + =.                
                   *- +. *  -  + .= :-   +* =  -. .. :: -: *     :*:.+ :- .. :- :: -.  :*-.-..-  .  =. + =.                
                   *- +. *  *  + .= :-   +* =  -. -: :: -: *     :*:.+ -- .= :- :: -.  :*-.-..-  -. =. + =.                
                   *- +. *  *  +  = :-   +* =  -. -: :: :- *     :*:.+ -- .= :- :: -.  :*-.-..-  -. =. + =.                
                     ...............       ...............         ...............        ...............       
                                                                                                         """

bossart = """           ___
          |_|_|
          |_|_|              _____
          |_|_|     ____    |*_*_*|
 _______   _\__\___/ __ \____|_|_   _______
/ ____  |=|      \  <_+>  /      |=|  ____ \
~|    |\|=|======\\______//======|=|/|    |~
 |_   |    \      |      |      /    |    |
  \==-|     \     | BOSS |     /     |----|~~/
  |   |      |    |      |    |      |____/~/
  |   |       \____\____/____/      /    / /
  |   |         {----------}       /____/ /
  |___|        /~~~~~~~~~~~~\     |_/~|_|/
   \_/        |/~~~~~||~~~~~\|     /__|\
   | |         |    ||||    |     (/|| \)
   | |        /     |  |     \       \\
   |_|        |     |  |     |
              |_____|  |_____|
              (_____)  (_____)
              |     |  |     |
              |     |  |     |
              |/~~~\|  |/~~~\|
              /|___|\  /|___|\
             <_______><_______>"""

#handy functions
def skiplines(lines = 1):
    print(lines*"\n")
    
def border(lines=40, color = Fore.BLACK):
    print(color+(lines*"-")+Fore.RESET)
    
def focus(msg, lines=1):
    skiplines(lines)
    print(msg)
    skiplines(lines)

def invalid(direct,para=None,msg = ""):#directory
    print(Fore.RED+"Invalid input, try again.")
    print(msg)
    input(Fore.RESET+">>> Press enter to continue ")
    if para != None:
        direct(para)
    else:
        direct()
        
def typeani(msg):
    for char in msg:
        time.sleep(0.06)
        print(char,end = "", flush = True)
    print("\n")


def preProcedure(): #Total Reset of the game
    global optionC1, optionC2, optionC3, optionStatus, meal1, meal2, meal3, repurposedItems
    optionC1 = Fore.BLACK
    optionC2 = Fore.BLACK
    optionC3 = Fore.BLACK
    optionStatus = [False, False, False]
    #Constructing object/class (later mentioned) into 3 instances
    meal1 = Meal("Fruit salad on plate","Ceasar salad in plastic box","Styrofoam cup noodles")
    meal2 = Meal("Lettuce cheese tomato sandwich", "Paper wrapped chicken leg","A very large bowl of spicy noodles")
    meal3 = Meal("Cup of tea", "Oil container", "Water in plastic bottle")
    repurposedItems = 0 #For repurposing part
    titleScreen1()
    
def titleScreen1(): #If dead from events not restart
    global called, inv, warning, bosshappy
    warning = 0
    inv = ["Empty","Empty","Empty","Empty","Empty"]
    called = []
    bosshappy = False
    #Options done status
    print(galactic1+Style.BRIGHT, end = "")
    typeani("Welcome to...")
    time.sleep(1)
    print(Fore.RED+art1)
    time.sleep(1)
    print(Fore.GREEN + art2)
    time.sleep(1)
    print(Fore.RED+ art3)
    input(colorReset+"Press Enter to continue...")
    skiplines(5)
    border()
    robotHome()
    
    #Branch
    
def robotHome():
    if (winchecker() == False):
        print(galactic1+"You are a robot standing in the lobby of the spaceship."+colorReset)
        print("There are 5 paths ahead of you.")
        print("Explore freely around the spaceship!")
        border()
        print("Workspaces: ")
        print(optionC1+"1. Space canteen"+colorReset)
        print(optionC2+"2. Recycling station"+colorReset)
        print(optionC3+"3. Repurposing station"+colorReset)
        print("\nTools:")
        print(Fore.MAGENTA+"4. Galactic bulletin")
        print("5. Edit inventory")
        border()
        userinput = input(colorReset+">>> Choose where to go(1/2/3/4/5): ")
        #Logical options
        #Anything that starts with r means it is the robot's function
        if userinput == "1":
            rCanteen1()
        elif userinput == "2":
            rRecycling()
        elif userinput == "3":
            rRepurpose()
        elif userinput == "4":
            bulletin()
        elif userinput == "5":
            editInv()
        else:
            invalid(robotHome)
    else:
        win()
        

#COMPLEX 1.CANTEEN CODE starts
    
    
class Meal: #Creates class for every meal
    def __init__(self, m1, m2, m3):
        self.rand = random.randint(1,3)
        if self.rand == 1:
            self.ml1 = m1
            self.ml2 = m2
            self.ml3 = m3
        elif self.rand == 2:
            self.ml1 = m2
            self.ml2 = m1
            self.ml3 = m3
        else:
            self.ml1 = m3
            self.ml2 = m2
            self.ml3 = m1
        self.true = m1
    def printMeals(self):
        x = mealcolor+f"1.{self.ml1}"+Back.RESET+"\n"+mealcolor+f"2.{self.ml2}"+Back.RESET+"\n"+mealcolor+f"3.{self.ml3}"+Back.RESET+Fore.RESET
        return x
    def checkVal(self, val):
        if val == "1":
            return self.ml1
        elif val == "2":
            return self.ml2
        elif val == "3":
            return self.ml3
        else:
            return False
        
def meals(meal):
    border()
    print(meal.printMeals())
    border()
    userinput = input(">>> Enter 1,2 or 3 to select your choice: ")
    userinput = meal.checkVal(userinput)
    if meal.true == userinput:
        print(Fore.GREEN+Back.BLACK+"Wise decision. You move on."+Fore.RESET+Back.RESET)
        skiplines(3)
        return 0
    elif userinput == False:
        invalid(meals, meal)
    else:
        print(Fore.RED+Back.BLACK+f"Unfortuantely, you picked the wrong choice because a {userinput} is a bad material for the environment."+Fore.RESET+Back.RESET)
        print("Your robot boss sees this and decides to fire you because you didnt follow regulations and laws.")
        gameover()
        

def rCanteen1():
    global optionStatus
    global optionC1
    if optionStatus[0] == True:
        CanteenRedirect()
    else:
        print(canteenart)
        time.sleep(1)
        skiplines(3)
        print("You go into the canteen and line up for food.")
        #First set
        border()
        print("You walk to the first set choices, these are the options: ")
        meals(meal1)
        #Second  set
        border()
        print("You walk to the second set choices, these are the options: ")
        meals(meal2)
        #Thrid set
        border()
        print("You walk to the final set choices, these are the options: ")
        meals(meal3)
        print("You peacefully eat the meal.\n(You successfully passed because the other options goes to waste)")
        input("Lunch is finished. Press enter to return to start and do other tasks.")
        skiplines(3)
        optionStatus[0] = True
        optionC1 = Fore.GREEN
        robotHome()
        
def CanteenRedirect():
    border()
    print("You have already eaten lunch and lunch hour has passed.")
    input(">>> Press enter to go back ")
    border()
    skiplines(3)
    robotHome()
    
#1.Canteen code ends

#2.Recycling code starts

recycleObj = {
    1: "PET space plastic water bottle", #PET
    2: "Space Milk (From Space Cows) Jug", #HDPE
    3: "PVC pipe", #PVC
    4: "Soft squishy plastic wrap",#LDPE
    5: "Tupperware/plastic container",#PP
    6: "Styrofoam box",#PS
    7: "CD that plays rocket man", #Other plastic and SPECIAL CASE WHERE IT PLAYS THE ACTUAL MUSIC
    8: "Pizza cardboard box" #Rubbish
    }
#Explainations
p1 = """PET is one of the most   
commonly used plastics.  
It’s lightweight, strong,
typically transparent and
is often used in food    
packaging and water      
bottles.
"""
p2 = """HDPE is a versatile &
durable plastic used for
bottles, containers, &
pipes. Resistant to
chemicals & impact.
"""
p3 = """Polyvinyl Chloride (PVC)
is a durable, low-cost
plastic. Used in pipes, vinyl
flooring, and electrical
insulation. But it is quite
toxic.
"""
p4 = """LDPE is a flexible &
lightweight plastic used for
plastic bags, wraps, &
squeezable bottles.
LDPE offers excellent
clarity, moisture barrier,
and ease of processing.
"""
p5 = """Polypropylene (PP) is a
versatile plastic known for
its heat and chemical
resistance. Used in food
containers, auto parts, and
packaging.
"""
p6 = """Polystyrene (PS) is a
lightweight plastic used in
packaging and disposable
products like foam cups
and food containers. You
may know polystyrene boxes
which is also called styrofoam.
"""
p7 = """Ah yes, the final plastic type.
Other plastics. They are what
does not fit into the other 6
categories and is recycled here.
For example, DVDs, swimming
goggles, etc.
"""

#Explaination of why their choice was right/wrong
recycleMsg = {
    1: p1,
    2: p2,
    3: p3,
    4: p4,
    5: p5,
    6: p6,
    7: p7,
    8: "A pizza box is made out of cardboard, so it cannot be recycled as plastic. Also, oil contaminated things usually cannot be recycled and has to be thrown away..."
    }
def rRecycling():
    skiplines(5)
    print(recycleintroart)
    border()
    print("You head to the recycling station and your working shift is up.")
    print("Your job is to sort the plastics/rubbish into different bins, by typing a number from 1 - 8.\n1-7 means the 7 plastic recycling types and 8 means rubbish in general.")
    focus(Fore.BLUE+"Tip: Go back to the start and read the bulletin for more info about plastic types."+Fore.RESET,1)
    print(galactic1+f"You have {8-len(called)} (plastic) objects left to recycle for your shift."+colorReset)
    userinput = input(">>> Start recycling (1)? Or go back to start (2)?")
    if userinput == "1":
        recycleChoice()
    elif userinput == "2":
        robotHome()
    else:
        invalid(rRecycling)
        
        

def recycleChoice():
    global called
    number = 0
    newNumber = False
    if optionStatus[1] == False:
        while newNumber == False:
            number = random.randint(1,8)
            if number in called:
                continue
            else:
                called.append(number)
                newNumber = True
        border()
        item = recycleObj.get(number)
        recycleGame(item)
    else:
        print("You already recycled all the platics... Your shift has ended...")
        input(">>> Press enter to go back to home")
        border()
        skiplines()
        robotHome()
    
    

recyclelist = """1. PET
2. HDPE
3. PVC
4. LDPE
5. PP
6. PS
7. Other plastics
8. Rubbish
9. Keep in inventory
0. Skip
"""
def recycleGame(item):
    skiplines(100)
    border()
    print(rubbishart)
    print("Where does the "+Fore.GREEN+item+Fore.RESET+" belong?")
    border()
    print(galactic1+recyclelist+colorReset)
    userinput = input(">>> Enter your choice: ")
    if userinput in [str(i) for i in range(1,9)]:
        recycleItem(userinput)
    elif userinput == "9":
        recycleKeep(item)
    elif userinput == "0":
        recycleSkip(item)
    else:
        invalid(recycleGame,item)

def recycleItem(choice):
    global warning, optionStatus, optionC2
    answerIndex = called[-1] #Latest index
    if choice == str(answerIndex):
        print(galactic4+"You put the plastic into the bin and the system says it is correct!"+colorReset)
        skiplines()
        print(galactic1+recycleMsg.get(answerIndex)+colorReset)
        skiplines(2)
        if len(called) == 8:
            optionStatus[1] = True
            optionC2 = Fore.GREEN
        userinput = input(">>> Continue recycling (1)? Or go back to starting point (2)?")
        if userinput == "1":
            recycleChoice()
        else:
            robotHome()
    else:
        warning += 1
        if warning < 3:
            print(galactic3+"OH NO! The system detects an error because you put it in the wrong bin!"+colorReset)
            print(f"The system notifies your boss and he gives you {warning} warning(s)... (After the third, you are fired.)")
            userinput = int(input(">>> Continue recycling (1)? Or go back to starting point (2)?"))
            if int(userinput) == 1:
                recycleChoice()
            else:
                robotHome()
        else:
            print(galactic3+"The speaker immediately broadcasts: ")
            time.sleep(0.5)
            typeani("Robot #3750239, you have been fired for recycling wrongly a lot of times...")
            gameover()
            
        
    
    #Case when user keeps
def recycleKeep(item):
    global inv, optionStatus, optionC2
    print(f"You decide to keep {item} in your inventory.")
    if "Empty" in inv:
        i = inv.index("Empty") #Built in python function to find FIRST occurance - index of array specified value
        inv.pop(i)
        inv.insert(i, item)
        print("Successfully kept. Here is your new inventory.")
        focus(inv)
        if len(called) == 8:
            optionStatus[1] = True
            optionC2 = Fore.GREEN
    else:
        print(Fore.RED+"Inventory FULL."+Fore.RESET+" Unable to store...") 
        input(">>> Press enter to choose again...")
        recycleGame(item)
    userinput = input(">>> Continue recycling (1)? Or go back to starting point (2)?")
    if userinput == "1":
        recycleChoice()
    else:
        robotHome()


def recycleSkip(item):
    global called
    print("You skip the item (Will come back later.)")
    called.pop(-1)
    input(">>> Press enter to continue recycling (to exit your job shift, either recycle at least 1 object   OR   store in inventory)...")
    recycleChoice()
    
#2.Recycle code ends
    
#3.Repurpose code starts
    
def rRepurpose():
    print("Welcome to the repurposing section, where robots turn human trash into something useful!")
    print("It is a beneficial practice to turn "+Fore.RED+"useless things "+Fore.RESET+"into "+Fore.GREEN+"useful things"+Fore.RESET+".")
    print("This is also known as:")
    focus("The circular economy. (Learn more about it in 4. Gallactic bulletin)")
    userinput = input(">>> Start repuposing (1)? Or go back (2)?")
    if userinput == "1":
        RepurposeIntro()
    elif userinput == "2":
        robotHome()
    else:
        invalid(rRepurpose)

recipes = {
    "1. Vase": ["plastic bottle", "string"],
    "2. Pencil holder": ["aluminum can", "fabric scraps", "paper clips"],
    "3. Photo frame": ["string", "cardboard","paper clips"]
}

recipeIndex = list(recipes.keys())

repurposeObjects = ["plastic bottle", "cardboard", "string", "aluminum can", "fabric scraps", "paper clips", "broken electronics","styrofoam"]



def RepurposeIntro():
    border()
    #print art
    typeani("In front of you, there are a plethora of waste materials scattered on the ground which could be repurposed into something more useful rather than waste.")
    typeani("Instructions:\nYour job is to find materials, then try and create something new with it.")
    border()
    print("You will store the items in your inventory, which will have 5 slots.")
    print("If your invetory is full, you have to go back to the spaceship lobby, then 5.Edit invetory, or take the shortcut (in the crafter station) and throw away items.")
    time.sleep(1)
    print("While doing that, you have to try to avoid picking up "+Fore.RED+"risky items."+colorReset)
    border()
    time.sleep(1)
    print("After collecting materials, you have to go to the CRAFTER STATION and attempt to create an item WITH recipes in the crafter station.")
    time.sleep(1)
    print("You need AT LEAST 3 item (can be the same) to present to your boss after you can find in the CRAFTER STATON.")
    print("Good luck!")
    border()
    skiplines(2)
    input(">>> Press enter to start ")
    skiplines(3)
    RepurposeOptions()
    
def RepurposeOptions():
    print("You can either find waste materials (1), go to the crafter for recipes (2), or go back to start (3)?")
    userinput = input(">>> Choose where to go: ")
    if userinput == "1":
        collection()
    elif userinput == "2":
        crafter()
    elif userinput == "3":
        robotHome()
    else:
        invalid(RepurposeOptions)
        
#Collects the trash in 3 different ways
lastcalledcase = [0]
def collection():
    global lastcalledcase, inv
    if "Empty" not in inv: #Checking if inventory is full or not
        print(Fore.RED+"UNABLE TO COLLECT... INVENTORY FULL..."+colorReset)
        print("Luckily there is a secret one way tunnel in the collection zone that leads to the editing inventory area.")
        input(">>> Press enter to go to in the secret tunnel (you have to manually come back later)")
        editInv()
    #Double case in a row preventing code
    casenum = lastcalledcase[-1]
    while lastcalledcase[-1] == casenum: # So the player does not get a duplicate dialogue case 2 times in a row
        casenum = random.randint(1,3)
    itemnum = random.randint(1,len(repurposeObjects))
    item = repurposeObjects[itemnum-1]
    displayitem = galactic1+item+colorReset
    lastcalledcase.append(casenum)
    border()
    #3 cases/scenarios to make it more interestingz
    match casenum: #New python syntax from python 3.10, matches the parameter to specific cases
        case 1:
            typeani("Your robot friend calls you in the field of waste.")
            print("He found a potentially useful "+displayitem+". But he has no use of it, you can keep it for him.")
        case 2:
            typeani("You find Jerry the Human outside preparing to put more waste materials for you.")
            typeani("You ask him in a robot voice if you could please have a fresh piece of material for creating your item.")
            print("He reaches into his bag and grabs a "+displayitem+" for you.")
        case 3:
            typeani("Carson the rat scours through the rubbish patch.")
            typeani("He lends you an item because you are such a good friend!")
            print("He gives you a "+displayitem+" to you.")
    border()   
    userinput = input(f">>> Keep {item} in your inventory (1)? Or ignore it (2)?")
    if userinput == "1": #Not risky items
        if item not in ["broken electronics","styrofoam"]:
            i = inv.index("Empty") #Built in python function to find FIRST occurance - index of array specified value
            inv.pop(i)
            inv.insert(i, item)
            print("Successfully kept. Here is your new inventory.")
            focus(inv)
        else:
            print("Ouch, the material you chose was a RISKY item! And it contained a lot of hazards!")
            if item == "styrofoam": #Choosing error message
                print("Styrofoam can absorb a lot of toxic waste and carcinogens due to its material properties,  your boss saw this as a hazard and fired you for unsafe handling of materials, potentially risking other robots being harmed.")
            else:
                print("Broken electronics can be very dangerous to deal with, your boss saw this as a hazard and fired you for unsafe handling of materials, potentially risking other robots being harmed.")
            gameover()    
    userinput = input(">>> Continue scavenging for trash(1)? Or go back to crafter(2)? * Or GO TO BOSS * (3)? Or go back to instructions(4)?")
    skiplines(3)
    border()
    if userinput == "1":
        collection()
    elif userinput == "2":
        crafter()
    elif userinput == "3":
        boss()
    elif userinput == "4":
        RepurposeOptions()
    else:
        invalid(collection)
        
 
def crafter():
    global inv, recipes, repurposedItems
    skiplines(3)
    border()
    print("Welcome to the Crafter Station!")
    print("Here, you can attempt to create new items using the waste materials you have collected.")
    print("Here are some recipes you can try:")
    border()
    
    for key, value in recipes.items():
        print(key + ":")
        print("- Ingredients: " + ", ".join(value)) #Python method for joining array strings 
        print()
    print(f"Current inventory: {inv}")
    userinput = input(">>> Choose a recipe to attempt(1/2/3): ")
    try: #Error handling
        userinput = int(userinput)
    except:
        invalid(crafter)
    if userinput in [1,2,3]:
        recipename = recipeIndex[userinput-1]
        recipeItems = list(recipes.get(recipename))
        material = 0
        for i in range(len(recipeItems)): # Check if recipe items in inventory
            if recipeItems[i] in inv:
                material += 1
        
        if material == len(recipeItems): #If all recipe itmes are present
            skiplines(2)
            print("Congratulations! You have successfully created", recipename)
            for i in range(len(recipeItems)): # Remove Item from inventory
                inv.remove(recipeItems[i])
                inv.append("Empty")
            i = inv.index("Empty")
            inv.pop(i)
            inv.insert(i, recipename)
            repurposedItems += 1
            print(f"Your new inv: {inv}")
            skiplines()
            userinput = input(">>> Continue scavenging for trash(1)? Or continue crafting(2)? Or go to boss (3)? Or go back to instructions(4)?")
            skiplines(3)
            border()
            if userinput == "1":
                collection()
            elif userinput == "2":
                crafter()
            elif userinput == "3":
                boss()
            elif userinput == "4":
                RepurposeOptions()
            else:
                invalid(collection)
        else:
            print("You don't have all the required materials to create", recipename)
            input(">>> Try again later... Press enter to go back.")
            RepurposeOptions()
    else:
        print("Invalid recipe selection.")
        invalid(crafter)
    
def boss():
    global inv, optionStatus, optionC3, bosshappy
    print(bossart)
    typeani("The robot boss approaches you, ready to assess your work.")
    time.sleep(1)
    typeani("He searches your inventory...")
    
    if repurposedItems == 3:
        for i in range(len(inv)):
            if inv[i] in recipeIndex:
                time.sleep(1)
                print("...")
                time.sleep(1)
                print(f"He finds your finished {inv[i]}")
                print("He is impressed by the quality of the work!")
        if "CD that plays rocket man" in inv:
            border()
            typeani("Oh?")
            time.sleep(1)
            typeani("He finds the CD of Rocket Man in your inventory!")
            print("Turns out it it one of the boss's favourite CDs he owns and he thanks you for keeping it!")
            bosshappy = True
        border()
        time.sleep(1)
        print("Well done, you have successfully finished repurposing!")
        optionStatus[2] = True
        optionC3 = Fore.GREEN
        input("Press enter to return to spaceship lobby ")
        robotHome()
    else:
        for i in range(len(inv)):
            if inv[i] in recipeIndex:
                time.sleep(1)
                print("...")
                time.sleep(1)
                print(f"He finds your finished {inv[i]}")
                print("He is impressed by the quality of the work!")
        typeani("However...")
        time.sleep(1)
        print("He is not impressed with your time management...")
        time.sleep(1)
        typeani("He thinks that you are inefficient and fires you from the spaceship :( \nHint: Repurpose AT LEAST 3 objects to get the boss' approval...")
        time.sleep(1)
        gameover()
    

intro = """The spaceship now operates in a circular economy, which is
 economy is a system used to describe the CYCLE between
 product consumption and production from the consumed products
 - the waste goes back to the prodcers for reusing it."""

def bulletin():
    print("Welcome to the bulletin, where intergalactic news would be broadcasted and updated (every 500 light years).")
    input(">>> Press enter to proceed")
    print(f"""
{intro}

You must recycle accordingly to its plastic types or else it is illegal and space police will come after you!
The 7 plastic types:
 1.{p1} 2.{p2}
 3.{p3} 4.{p4}
 5.{p5} 6.{p6}
 7.{p7}

The circular economy isn't just about recycling, it is also about keeping materials in a cycle, not wasting it.
So if you have any old robot compartments, you could donate them to the charities and potentially help other robots!
Robot sitting in front of the screen, the circular economy is not only in this spaceship, it should be
YOUR WORLD's dream and vision. Materials should be conserved with maximum efforts, and every small
effort helps! Let's go!
""")
    input(">>> Press enter to go back... ")
    robotHome()
    
def editInv():
    global inv
    border()
    skiplines(3)
    print("Welcome to the rubbish center, where you can throw away your inventory items into the vast emptiness of space.")
    focus(Fore.BLUE+f"Your inventory: {inv}"+Fore.BLACK)
    userinput = input(">>> Do you want to remove anything from your inventory?(yes/no) ")
    
    if userinput == "yes": #Confirmation to start editing inv
        userinput = input(">>> Enter which item do you want to remove according to order (1/2/3/4/5)?") #Item to remove in inv
        try: #Error handling to see if input is integer
            userinput = int(userinput)
        except:
            invalid(editInv)
        
        confirmation = input(f">>> Confirm to remove {inv[userinput-1]}? (yes/no)") #Final confirmation
        
        if confirmation == "yes":
            if userinput in [1,2,3,4,5]: # If item in range of 1 - 5
                inv.pop(userinput-1) #Takes out specified index (-1 because input is 1-5 [base 10 normal human counting] not 0-4 [index])
                inv.append("Empty") #Adds Empty to end like a pulling out item in a STACK and adding on top of STACK
                typeani("Your rubbish has been ejected into space.")
                focus(Fore.BLUE+f"Your new inventory: {inv}"+Fore.BLACK)
                input(">>> Press enter to return.")
                robotHome()
            else:
                invalid(editInv)
        else:
            input("Ok then. Press enter to go back to starting point.")
            robotHome()
    else:
        input("Ok then. Press enter to go back to starting point.")
        robotHome()
        
def winchecker():
    if optionStatus[0] == True:
        if optionStatus[1] == True:
            if optionStatus[2] == True:
                return True
    return False

    
def win():
    global bosshappy
    print(galactic4+"Congratulations! You have successfully completed all the recycling and repurposing rewarding.\n")
    typeani("You have contributed to the circular economy and helped reduce waste in the galaxy spaceship.")
    if bosshappy == True:
        typeani("Best Ending:\nYour efforts have been recognized BY YOUR BOSS, and the intergalactic community applauds your dedication to the circular economy,\nand your boss promotes you to be the CEO!!!")
    else:
        typeani("Good Ending:\nYour efforts have been recognized, and the intergalactic community applauds your dedication to sustainability.")
        typeani("But there is a better ending! Try to get it playing again. Hint: The boss likes music a lot...")
    skiplines()
    time.sleep(1)
    typeani("Credits: ")
    typeani("Authored by Linus Choi")
    typeani("Coded by Linus Choi")
    typeani("Directed by Linus Choi")
    typeani("Libraries/Packages used: time, colorama, random")
    print(colorReset)
    skiplines(3)
    border()
    print("Thank you for playing!")
    userinput = input(">>> Play again??? (y/n)")
    if userinput == "y":
        skiplines(50)
        preProcedure()
    else:
        print("We hope to see you again! Stay tuned for future updates.")
        exit()
    

def gameover():
    print(Fore.GREEN+Back.BLACK+f"{gameoverart} ")
    userinput = input(Fore.RESET+Back.RESET+">>> Restart? (y/n)")
    if userinput == "y":
        skiplines(50)
        preProcedure()
    else:
        print("Thanks for playing...")
        exit()


#Main loop / program
preProcedure()