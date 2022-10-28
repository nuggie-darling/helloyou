#Importing the time module
from time import sleep 
import time 
import sys

def lprint(s):
    for c in s: 
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.01)
    print("")
    sleep(0.01)

def Start():
    lprint("???: Wake up. Hey, wake up!") #printing line
    lprint("*You’re startled awake by the strange voice*")
    lprint("You: What?")
    lprint("*Your eyes are blurry from having just woken up and you’re confused*") 
    lprint("*After adjusting your eyes to the new lighting, you finally look at the owner of the voice that woke you*")
    lprint("You: Who are you?")
    lprint("*You look around where you are. It looks like a cave of sorts*")
    lprint("*The person looks back at you and smiles*")
    lprint("???: I'm Ace.")
    lprint("*They reach their hand out for you to shake*")
    lprint("Ace: It's nice to meet you, traveler.")
    lprint("*You confusedly shake their hand*")
    lprint("You: Traveler?")
    lprint("*Ace smiles at you and nods his head*")
    lprint("You: No, you must be mistaken... I-")
    lprint("Ace: You're the chosen one.")
    lprint("You: Excuse me?")
    lprint("*Ace hands you a backpack*")
    lprint("Ace: Everything you will need is in there, traveler. I wish you great luck.")
    lprint("*Before you know it Ace has disappeared.")
    lprint("You frantically look around the cave, trying to find something.")
    lprint("You can hear water splashing on one end of the cave, but see some light from a different end. You...*")
    choice1() #Calls "def choice1"

def choice1(): #Creates a new function
    lprint('''a) *Go towards the water*
b) *Go towards the light*''') #prints two seperate lines, hense the three ' on each side

    answer = input().lower() #Ask for playerinput

    if answer == "a": #Check player input for the letter a
        lprint("*You go towards the water*")
        choice1a()
    elif answer == "b": #Check player input for the letter b
        lprint("*You go towards the light*")
        choice1b()

def choice1a():
    lprint("*The cave gets darker and darker the further you go*")
    lprint("*You decide to take a look in the backpack Ace gave you and find a torch*")
    lprint("*When you take it out you search for a lighter, but only find two rocks.")
    lprint("You: Are you serious right now??")
    lprint("*You groan out of frustration*")
    lprint("You: This has to be a dream. Wake up!")
    lprint("*You close your eyes and pinch yourself, but to no avail*")
    lprint("*When you open your eyes again you're still in the cave*")
    lprint("*You groan and get on the ground, holding the rocks and the torch*")
    lprint("*After several minutes of struggle you're finally able to Light the torch*")
    lprint("*You put the rocks back inside of your bag in case you need them in the future and hold a firm grasp on the torch, letting out a deep breath*")
    lprint("*You continue walking towards the water and find your way to a wall of rocks stacked on top of each other*")
    lprint("*You can see through the caps between the rocks that there's a waterfall behind the wall*")
    lprint("*You want to see it, but to do that you have to take this wall of rocks down. You…*")

def choice2(): 
    lprint('''a) *Decide to go back and see what's on the other side of the cave*
b) *Look through your backpack to see if you can find anything*''')

    answer = input().lower() 

    if answer == "a": 
        lprint("*Decide to go back and see what's on the other side of the cave*")
        choice2a()
    elif answer == "b": 
        lprint("*Look through your backpack to see if you can find anything*")
        choice2b()

def choice2a():
    lprint("*You decide to go back and see what's on the other side of the cave*")
    lprint("*You walk and walk, but somehow can't make your way back to where you were before*")
    lprint("*You could've sworn you walked a straight line, but the cave seemed like a maze now*")
    lprint("*The only way you could go was back to the wall*")
    lprint("*You sigh and walk back*")
    lprint("*Looking at the wall, you find a handle you can rest your torch on while you look through your backpack to find something that can help you in this situation*")
    lprint("*When you put your torch on the handle, there's a clicking noise and a loud rumble*")
    lprint("*You walk backwards, away from the wall*")
    lprint("*Small rocks tumble from the pile and the entire wall collapses, making you flinch*")
    lprint("*Once the cave is back to quiet, you look up*")
    lprint("*The torch must've triggered the wall!*")
    lprint("*You smile to yourself, happy with your accidental achievement*")
    lprint("*You climb over the rocks and go outside*")
    lprint("*The light blinds you at first, but once you've gotten used to the brightness you stand there in awe*")
    lprint("*The waterfall is beautiful*")
    lprint("*And there's animals bathing in the water!*")
    lprint("*One of the animals spots you and makes its way towards you*")
    lprint("*It's not like any animal you've ever seen before*")
    lprint("*It's… almost indescribable*")
    lprint("*It looks like a small panther, but it has beautifully colored wings*")
    lprint("*And it's tail and ears are extremely fluffy*")
    lprint("*You slowly reach your hand towards the animal, letting it sniff your hand first*")
    lprint("Ace: Ah, I see you've found the Panthesus!")
    lprint("You: The what?")
    lprint("Ace: The Panthesus! This wonderful creature right here.")
    lprint("*Ace leans over and picks the Panthesus up, stroking it's ears*")
    lprint("*He nudges you to pet it*")
    lprint("*You hesitate, but the fur looks so soft you almost HAVE to give in*")
    lprint("You: Wow...")
    lprint("Ace: I know, right? They're wonderful.")
    lprint("Ace: I'm happy to see you've made it out of the cave, traveler.")
    lprint("Ace: You've proven yourself worthy of this quest.")
    lprint("Ace: But from here on out it will only get harder.")
    lprint("Ace: Will you accept your quest?")
    lprint("You: I-")
    lprint("Ace: Perfect!")
    lprint("Ace: Your quest starts behind the waterfall. Follow me.")
    lprint("*Ace puts the Panthesus down and walks towards the water, walking into it towards the waterfall*")
    lprint("*You don't want to get your clothes wet, but you need to make your way out of this world somehow*")
    lprint("*You follow behind Ace*")
    lprint("*When you get through the waterfall, there's another cave*")
    lprint("*This one has a chest in the middle*")
    lprint("Ace: Go on, open the chest.")
    lprint("*You...*")

def choice3(): 
    lprint('''a) *Don't trust it and decide not to open it*
b) *Walk up to the chest to open it*''')

    answer = input().lower() 

    if answer == "a": 
        lprint("Don't trust it and decide not to open it.*")
        choice3a()
    elif answer == "b": 
        lprint("*Walk up to the chest to open it*")
        choice3b()

def choice3a():
    lprint("")

def choice3b():
    lprint("")

def choice2b():
    lprint("*Look through your backpack to see if you can find anything*")

def choice1b():
    lprint("**")

Start() #Call the function "Start"
