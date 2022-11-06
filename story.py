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

def Restart_Or_Quit():
    answer = ""
    lprint("Would you like to restart? (Yes / No")
    response = input().lower()
    while answer != "yes" or answer != "no":
        answer = response
        if response == "yes":
            Start()
        elif response == "no":
            quit()

def glitch():
    import random
    for i in range(10):
        original = "A̶̾̔B̷́́C̸̓̉D̵͒͊Ê̷͝F̵́̎G̴̏͂H̸̿͘I̴͆͘J̴̈͛Ḱ̶̕L̸̀̓M̸̄͌N̵͂͝Ő̵̂P̶̔̽Q̴͆͗R̵̐̀S̵̎͝Ť̴̎U̴͗̈́V̵̔̓W̵̆̾X̵̌̆Y̵͆͝Z̶̋̋"
        randomised = ''.join(random.sample(original, len(original)))

        lprint(randomised)
        Restart_Or_Quit()

def Start():
    lprint("???: Wake up. Hey, wake up!") #printing line
    lprint("*You're startled awake by the strange voice.*")
    lprint("You: What?")
    lprint("*Your eyes are blurry from having just woken up and you're confused.*") 
    lprint("*After adjusting your eyes to the new lighting, you finally look at the owner of the voice that woke you.*")
    lprint("You: Who are you?")
    lprint("*You look around where you are. It looks like a cave of sorts.*")
    lprint("*The person looks back at you and smiles.*")
    lprint("???: I'm Ace.")
    lprint("*They reach their hand out for you to shake.*")
    lprint("Ace: It's nice to meet you, traveler.")
    lprint("*You confusedly shake their hand.*")
    lprint("You: Traveler?")
    lprint("*Ace smiles at you and nods his head.*")
    lprint("You: No, you must be mistaken... I-")
    lprint("Ace: You're the chosen one.")
    lprint("You: Excuse me?")
    lprint("*Ace hands you a backpack.*")
    lprint("Ace: Everything you will need is in there, traveler. I wish you great luck.")
    lprint("*Before you know it Ace has disappeared.*")
    lprint("*You frantically look around the cave, trying to find something.*")
    lprint("*You can hear water splashing on one end of the cave, but see some light from a different end. You...*")
    choice1() #Calls "def choice1"

def choice1(): #Creates a new function
    lprint('''a) *go towards the water.*
b) *go towards the light.*''') #prints two seperate lines, hense the three ' on each side

    answer = input().lower() #Ask for playerinput

    if answer == "a": #Check player input for the letter a
        lprint("*You go towards the water.*")
        choice1a()
    elif answer == "b": #Check player input for the letter b
        lprint("*You go towards the light.*")
        choice1b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice1a():
    lprint("*The cave gets darker and darker the further you go.*")
    lprint("*You decide to take a look in the backpack Ace gave you and find a torch.*")
    lprint("*When you take it out you search for a lighter, but only find two rocks.*")
    lprint("You: Are you serious right now??")
    lprint("*You groan out of frustration.*")
    lprint("You: This has to be a dream. Wake up!")
    lprint("*You close your eyes and pinch yourself, but to no avail.*")
    lprint("*When you open your eyes again you're still in the cave.*")
    lprint("*You groan and get on the ground, holding the rocks and the torch.*")
    lprint("*After several minutes of struggle you're finally able to Light the torch.*")
    lprint("*You put the rocks back inside of your bag in case you need them in the future and hold a firm grasp on the torch, letting out a deep breath.*")
    lprint("*You continue walking towards the water and find your way to a wall of rocks stacked on top of each other.*")
    lprint("*You can see through the caps between the rocks that there's a waterfall behind the wall.*")
    lprint("*You want to see it, but to do that you have to take this wall of rocks down. You…*")
    choice2()

def choice2(): 
    lprint('''a) *decide to go back and see what's on the other side of the cave.*
b) *look through your backpack to see if you can find anything.*''')

    answer = input().lower() 

    if answer == "a": 
        lprint("*You decide to go back and see what's on the other side of the cave.*")
        choice2a()
    elif answer == "b": 
        lprint("*You look through your backpack to see if you can find anything.*")
        choice2b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice2a():
    lprint("*You walk and walk, but somehow can't make your way back to where you were before.*")
    lprint("*You could've sworn you walked a straight line, but the cave seemed like a maze now.*")
    lprint("*The only way you could go was back to the wall.*")
    lprint("*You sigh and walk back.*")
    lprint("*Looking at the wall, you find a handle you can rest your torch on while you look through your backpack to find something that can help you in this situation.*")
    lprint("*When you put your torch on the handle, there's a clicking noise and a loud rumble.*")
    lprint("*You walk backwards, away from the wall.*")
    lprint("*Small rocks tumble from the pile and the entire wall collapses, making you flinch.*")
    lprint("*Once the cave is back to quiet, you look up.*")
    lprint("*The torch must've triggered the wall!*")
    lprint("*You smile to yourself, happy with your accidental achievement.*")
    lprint("*You climb over the rocks and go outside.*")
    lprint("*The light blinds you at first, but once you've gotten used to the brightness you stand there in awe.*")
    lprint("*The waterfall is beautiful.*")
    lprint("*And there's animals bathing in the water!*")
    lprint("*One of the animals spots you and makes its way towards you.*")
    lprint("*It's not like any animal you've ever seen before.*")
    lprint("*It's… almost indescribable.*")
    lprint("*It looks like a small panther, but it has beautifully colored wings.*")
    lprint("*And it's tail and ears are extremely fluffy.*")
    lprint("*You slowly reach your hand towards the animal, letting it sniff your hand first.*")
    lprint("Ace: Ah, I see you've found the Panthesus!")
    lprint("You: The what?")
    lprint("Ace: The Panthesus! This wonderful creature right here.")
    lprint("*Ace leans over and picks the Panthesus up, stroking it's ears.*")
    lprint("*He nudges you to pet it.*")
    lprint("*You hesitate, but the fur looks so soft you almost HAVE to give in.*")
    lprint("You: Wow...")
    lprint("Ace: Aren't they just wonderful? We've got lots of creatures like this here. Also-")
    lprint("Ace: I'm happy to see you've made it out of the cave, traveler.")
    lprint("Ace: You've proven yourself worthy of this quest.")
    lprint("Ace: But from here on out it will only get harder.")
    lprint("Ace: Will you accept your quest?")
    lprint("You: I-")
    lprint("Ace: Perfect!")
    lprint("Ace: Your quest starts behind the waterfall. Follow me.")
    lprint("*Ace puts the Panthesus down and walks towards the water, walking into it towards the waterfall.*")
    lprint("*You don't want to get your clothes wet, but you need to make your way out of this world somehow.*")
    lprint("*You follow behind Ace.*")
    lprint("*When you get through the waterfall, there's another cave.*")
    lprint("*This one has a chest in the middle.*")
    lprint("Ace: Go on, open the chest.")
    lprint("*You...*")
    choice3()

def choice3(): 
    lprint('''a) *don't trust it and decide not to open it.*
b) *walk up to the chest to open it.*''')

    answer = input().lower() 

    if answer == "a": 
        lprint("*You don't trust it and decide not to open it.*")
        choice3a()
    elif answer == "b": 
        lprint("*You walk up to the chest to open it.*")
        choice3b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice3a():
    lprint("Ace: You're going to need what's inside the chest to continue your quest.")
    lprint("You: I don't even want to go on this stupid quest! I just want to go home!")
    lprint("*Ace stares at you for a second before he walks up to the chest and open sit himself.*")
    lprint("*He takes out a sword that should never have been able to fit in a chest that size.*")
    lprint("Ace: Take this, you'll need it to slay The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast.")
    lprint("You: WHY WAS KILLER IN THERE TWICE?!?")
    lprint("Ace: Believe me, its a monster worthy of its name.")
    lprint("You: YEAH, BUT WHY WAS KILLER IN THERE TWICE?? WHY IS THE NAME SO LONG AND HOW IS THAT WHAT IT'S CALLED?!?")
    lprint("Ace: It's a cold-blooded killer-")
    lprint("You: YEAH, I KNOW! YOU KNOW HOW I KNOW?? BECAUSE YOU TOLD ME TWICE! IN THE NAME!!")
    lprint("*Ace just chuckles and shoves the sword in your arms.*")
    lprint("Ace: Continue into this cave. I trust you'll find your way out like you did last time.")
    lprint("*Before you know it, Ace has disappeared again. You...*")
    choice4()

def choice4():
    lprint('''a) *make your way into the cave.*
b) *go back out from the water side and try to go somewhere from there.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You make your way into the cave.*")
        choice4a()
    elif answer == "b":
        lprint("*You decide to walk back out from where you entered.*")
        choice4b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice4a():
    lprint("*There's crystals and gorgeous colorful rocks that light up thr cave for you.*")
    lprint("*But even though it looks pretty, you're scared of the dangers of the quest ahead of you.*")
    lprint("*After a bit of walking, you end up in a round room with three paths in front of you. You...*")
    choice5()

def choice5():
    lprint('''a) *go into the left path.*
b) *go into the middle path.*
c) *go into the right path.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You go into the left path.*")
        choice5a()
    elif answer == "b":
        lprint("*You go into the middle path.*")
        choice5b()
    elif answer == "c":
        lprint("*You go into the right path.*")
        choice5c()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice5a():
    lprint("*The tunnel gets significantly darker which scares you.*")
    lprint("*You're clutching onto your sword as you walk through.*")
    lprint("*One of the stones you step on sink into the floor after you get on it.*")
    lprint("*Having seen movies and played video games, you're scared of what will happen because of this.*")
    lprint("*The cave is almost suspiciously quiet and you're not sure if you should get off the stone or not.*")
    lprint("*After several anxious minutes you decide to get off the stone.*")
    lprint("*The second you get off the stone, you...*")
    choice6()

def choice6():
    lprint('''a) *walk extremely slowly to avoid any traps that may lie ahead.*
b) *make a run for it to avoid any traps that may be right where you are.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You walk extremely slowly to avoid any traps that may lie ahead.*")
        choice6a()
    elif answer == "b":
        lprint("*You make a run for it to avoid any traps that may be right where you are.*")
        choice6b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice6a():
    lprint("*You walk extremely slowly to avoid any traps that may lie ahead. *")
    lprint("*Sadly for you, this was the wrong option!")
    lprint("*You fucking died.*") 
    Restart_Or_Quit()

def choice6b():
    lprint("*You make a run for it to avoid any traps that may be where you are.*")
    lprint("*As you're running, the walls start closing in on you.*")
    lprint("*You can see an exit ahead of you and you start sprinting.*")
    lprint("*You run and run and…*")
    lprint("*you make it!*")
    lprint("*You've made it out of the tunnel, but not yet out of the cave.*")
    lprint("*You can hear thunder rumbling from outside.*")
    lprint("*Or is it on the inside?*")
    lprint("*It's so clear that it feels like it is.*")
    lprint("*You walk further into the cave and hear a weird noise.*")
    lprint("*You look around you, but there's nothing there.*")
    lprint("*As you keep walking, you keep hearing the noise.*")
    lprint("*It's like something is chasing you.*")
    lprint("*Or someone...*")
    lprint("*After a couple of very anxious minutes, the noise just disappears.*")
    lprint("*You figure it was all just in your head and you have nothing to worry about, but you can't be sure.*")
    lprint("*fter another minute of walking, the noise returns.*")
    lprint("*This time louder than before.*")
    lprint("*You...*")
    choice7()

def choice7():
    lprint('''a) *turn around to try and find the source of the noise.*
b) *make a run for it and try to find the exit as quickly as possible.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You turn around to try and find the source of the noise.*")
        choice7a()
    elif answer == "b":
        lprint("*You turn around and try to find the exit.*")
        choice7b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice7a():
    lprint("*As you walk back into the cave, you notice all the rocks and crystals that were shining brightly before had all been dimmed to leave an ominous light.*")
    lprint("*As it's dark and scary, you wonder if you should continue on with this.*")
    lprint("*But knowing the quest ahead of you, you figure now's not the time to be scared.*")
    lprint("*You should find this monster so you can make your way out calmly.*")
    lprint("*Plus it would be good preparation for the final boss, right?*")
    choice8()

def choice8():
    lprint('''a) *You change your mind. This is too scary. You make a run for it anyway.*
b) *It'll be good preparation, you should try to find this monster!*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You change your mind. This is too scary. You make a run for it anyway.*")
        choice8a()
    elif answer == "b":
        lprint("*It'll be good preparation, you should try to find this monster!*")
        choice8b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice8a():
    lprint("*It's way too terrifying to try and find a monster.*")
    lprint("*You don't know how strong it is!*")
    lprint("*You turn back around and start sprinting down the cave, hoping to god you'll find the exit soon.*")
    lprint("*You see a light from a corner and follow it, eventually finding your way out.*")
    lprint("*Ace is standing right by the exit, waiting for you.*")
    lprint("Ace: Well, that took you long.")
    lprint("You're going to have to be faster if you want to finish this quest successfully.")
    lprint("You: Are you serious??")
    lprint("You: There's a monster in there and like a million different halls!!")
    lprint("You: It was like a maze in there!!")
    lprint("*Ace just shakes his head at you.*")
    lprint("Ace: Did you at least kill the monster?")
    lprint("You: What??")
    lprint("Ace: The monster. Did you kill it?")
    lprint("You: WAS I SUPPOSED TO??")
    lprint("Ace: Of course, you were supposed to!")
    lprint("Ace: How can the chosen one be so...")
    lprint("Ace: Cowardly?")
    lprint("Ace: Get back in there and slay the monster!")
    lprint("You: I DON'T WANT TO-")
    lprint("Ace: If you want any chance of making your way of here, you HAVE to! Go!!")
    lprint("*Ace practically pushes you back into the cave.*")
    lprint("Ace: AND WHATEVER YOU DO, DON'T USE THE SWORD!")
    lprint("You: DON'T USE THE SWORD-")
    lprint("*When you turn around to argue with Ace, he's gone.*")
    lprint("You: HE HAS GOT TO STOP DOING THAT!")
    lprint("*Seeing as you can't use the sword, you have to find a different weapon.*")
    lprint("*You reach into your backpack to try and find something that you could use.*")
    lprint("*You find a bottle with a strange liquid and a dagger.*")
    lprint("*Which one do you use?*")
    choice9()

def choice9():
    lprint('''a) *The strange liquid.*
b) *The dagger.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You use the strange liquid.*")
        choice9a()
    elif answer == "b":
        lprint("*You use the dagger.*")
        choice9b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice9a():
    lprint("*You put the dagger back inside of your backpack and hold the liquid.*")
    lprint("*It's purple and sparkly.*")
    lprint("*It's mesmerizing and you find yourself having the strong urge to smell the liquid.*")
    lprint("*You take the cork out and take a whiff.*")
    lprint("*Almost immediately after you start to get dizzy.*")
    lprint("*Your thump against the cold ground.*")
    lprint("*You blink slowly as your vision blurs.*")
    lprint("*Right before you pass out, you see something approaching you.*")
    lprint("*Is this really how you'll die?*")
    lprint("*...*")
    lprint("*...*")
    lprint("*...*")
    lprint("*You wake up several hours later with Ace sitting in front of you.*")
    lprint("Ace: Finally, you're up.")
    lprint("You: What happened..?")
    lprint("Ace: You made a rookie mistake and passed out.")
    lprint("Ace: I had to go in and save you.")
    lprint("You: Oh...")
    lprint("Ace: I expect you learned a lesson from this and you won't make a mistake like this again.")
    lprint("Ace: Now get up, you need to continue with your quest.")
    lprint("You: I don't think I can...")
    lprint("You: I'm not 'the chosen one'...")
    lprint("You: I'm just... me...")
    lprint("You: I can't slay some monster...")
    lprint("Ace: It's adorable that you think you have a choice, darling.")
    lprint("Ace: Now get up!")
    lprint("*Ace grabs you by the shoulders and stands you up, shoving the sword in your hands once again.*")
    lprint("Ace: Sadly, I do have to cut your quest short.")
    lprint("Ace: You have to slay The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast right now.")
    lprint("You: RIGHT NOW-")
    lprint("Ace: You can do it!")
    lprint("Ace: I believe in you-")
    lprint("Ace: Well, honestly, I don't, but you don't have another choice.")
    choice10()

def choice10():
    lprint('''a) *Go slay The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast.*
b) *Kill Ace.''')

    answer = input().lower()

    if answer == "a":
        lprint("*You give in and decide to go slay The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast.*")
        choice10a()
    elif answer == "b":
        lprint("*You grip the sword in your hands tightly.*")
        choice10b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice10a():
    lprint("*You make your way through a forest, holding the sword in front of you as protection.*")
    lprint("*When you get deeper into the forest, you hear a strange noise.*")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: WHO DARE DISTURB MY SLEEP?!")
    lprint("*The mysterious deep voice sends shivers down your spine. *")
    lprint("*You tremble as you continue walking.*")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: WHAT'S THIS?")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: A MERE HUMAN DARE ENTER MY FOREST?!")
    lprint("You: A-Ace sent me!")
    lprint("*You hear banging noises all around you and you stop in your tracks, circling around yourself.*")
    lprint("*You're sweating and absolutely terrified of what this monster could look like.*")
    lprint("*Not to mention what it could do to you.*")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: ACE?? AGAIN??")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: GOD, HE WILL NOT LEAVE ME ALONE!")
    lprint("You: I- I have to slay you!")
    lprint("You: Come out from where you're hiding!")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: YOU DARE CHALLENGE ME?")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: A MORTAL HAS THE GUTS TO CHALLENGE ME??")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: HAHAHAHAHHAHAHAH!")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: PERFECT, I'VE BEEN BORED FOR AGES!")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: YOU'LL FIT IN PERFECTLY WITH MY DINNER!")
    lprint("*A big shadow casts over you and loud footsteps approach you.*")
    lprint("*You're terrified out of your wits.*")
    lprint("*Once the footsteps stop, you look around.*")
    lprint("*You can'T find anything.*")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: DOWN HERE!")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: I'M RIGHT HERE!!")
    lprint("*You look down and before you stands the tiniest little hamster-like being.*")
    lprint("You: YOU'RE The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast??")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: OF COURSE, I AM!!")
    lprint("*You hold the sword firmly.*")
    lprint("*This should be a piece of cake, right?*")
    lprint("*Slaying a tiny little hamster like that?*")
    lprint("You: I have to kill you!")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: HAHAHAHHAHA!")
    lprint("The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast: I'D LIKE TO SEE YOU TRY!!")
    lprint("*You swing your sword at The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast but it avoids you.*")
    lprint("*The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast multiplies.*")
    lprint("*Then multiplies again.*")
    lprint("*And again*")
    lprint("*And again!*")
    lprint("*Over and over until there's thousands of him!*")
    lprint("You: W-what are you doing?? Stop that!!")
    lprint("*The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beast and his copies start climbing on you.*")
    lprint("*There's so many that you're drowning in them.*")
    lprint("*You reach your hand out, trying to get out from underneath them, but to no avail.*")
    lprint("*You drowned in The Cold-Blooded Iron Killer Bloodthirsty Icy Horror Crowned Killer Beasts.*")
    Restart_Or_Quit()

def choice10b():
    lprint("*You grin and hold the sword threateningly in front of Ace.*")
    lprint("You: And what's to stop me from killing you, huh??")
    lprint("You: I can just kill you right now!")
    lprint("*Ace laughs at you and holds his arms open as if he's giving you a hug.*")
    lprint("Ace: Do it then~")
    lprint("*You yell as you slam your sword into Ace's stomach.*")
    lprint("*He chuckles and blood comes out of his mouth.*")
    lprint("*He falls to his knees, chuckling.*")
    lprint("*You get an aching pain in the pit of your stomach.*")
    lprint("*When you look down you're bleeding.*")
    lprint("*You fall to the ground, gripping onto your stomach.*")
    lprint("You: What...")
    lprint("Ace: You killed yourself.")
    lprint("*You can hear the faint sound of laughter as you pass out.*")
    Restart_Or_Quit()

def choice9b():
    lprint("*You put the strange liquid back inside of your backpack and firmly grasp the dagger.*")
    lprint("*You carefully walk through the cave.*")
    lprint("*The deeper you go the darker the cave gets.*")
    lprint("*The sound you heard before gets louder and louder.*")
    lprint("*You find a tunnel in the cave.*")
    lprint("*Is that where the sound is coming from?*")
    choice30()

def choice30():
    lprint('''a) *Enter the tunnel.*
    b) *LEAVE LEAVE LEAVE-*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You take a deep breath and enter the tunnel.*")
        choice30a()
    elif answer == "b":
        lprint("*You quickly turn around and run back towards the exit, but it feels like a maze.*")
        choice30b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice30a():
    lprint("*The floor feels soft against your shoes and it sounds a little wet.*")
    lprint("*You can't see anything and end up bumping against something warm and disgustingly wet.*")
    lprint("*You take a step back, wiping your face.*")
    lprint("You: What the fuck…")
    lprint("*You hear a loud growl.*")
    lprint("*As if it's coming from inside of you.*")
    lprint("*But then you realize where it is coming from…*")
    lprint("*You quickly run back towards the exit, but it's too late.*")
    lprint("*The exit is sealed shut.*")
    lprint("*You're stuck inside the monster's mouth.*")
    lprint("*Forever.*")
    Restart_Or_Quit()

def choice30b():
    lprint("*You can't find your way back.*")
    lprint("*You don't recognize anything but at the same time all the hallways look the same to you.*")
    lprint("*You run and run but no matter what way you go, you end up in the same place.*")
    lprint("*In front of the tunnel.*")
    lprint("*There's only two choices here.*")
    choice31()

def choice31():
    lprint('''a) *Kill yourself before the monster does.*
    b) *Go into the tunnel.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You decide to take matters into your own hands.*")
        choice31a()
    elif answer == "b":
        lprint("*You walk into the tunnel.*")
        choice31b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice31a():
    lprint("*You take the dagger and slice your throat.*")
    lprint("*It starts spraying like a water fountain.*")
    lprint("*You fall down to the ground and bleed to death.*")
    Restart_Or_Quit()

def choice31b():
    lprint("*It's dark and you hear growls come from multiple parts.*")
    lprint("*You're scared to even continue walking.*")
    lprint("*Before you know it you're attacked from left and right.*")
    lprint("*What are these??*")
    lprint("*Alligators???*")
    lprint("*You're eaten alive by the alligators.*")
    Restart_Or_Quit()

def choice8b():
    lprint("*You muster up all the courage you have and look for the monster.*")
    lprint("*You look for several minutes, but it almost seemed to have disappeared.*")
    lprint("*You turn around and there's a fur wall in front of you.*")
    lprint("*But it's not a wall...*")
    lprint("*You look up and up until you finally find a face.*")
    lprint("*It's… really ugly.*")
    lprint("*It seems to not even notice you.*")
    lprint("*You...*")
    choice32()

def choice32():
    lprint('''a) *try to get its attention.*
    b) *try to walk past it unseen.*''')

    answer = input().lower()

    if answer == "a":
        lprint("You: HEY, DOWN HERE!")
        choice32a()
    elif answer == "b":
        lprint("*You attempt to walk past it unseen, but the monster is so physically massive it's impossible to pass by it without touching it. *")
        choice32b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice32a():
    lprint("*The monster looks down at you and grabs you, easily picking you up off the floor.*")
    lprint("*It growls angrily at you, leaving you drenched in its saliva.*")
    lprint("*You're so disgusted your body physically recoils and you'd rather be dead than in this stinky situation.*")
    lprint("You: I-")
    lprint("*Before you can finish your sentence the monster eats you.*")
    Restart_Or_Quit()

def choice32b():
    lprint("*You try to go between its legs, but it starts moving and you get crushed between its thighs.*")
    Restart_Or_Quit()

def choice7b():
    lprint("**")

def choice5b():
    lprint("*This tunnel is covered wall to wall in crystals, almost blinding you.*")

def choice5c():
    lprint("**")

def choice4b():
    lprint("*You don't want to go into another cave so you try to go back out from where you came in.*")
    lprint("*You reach your hand through the water, but it won't go through.*")
    lprint("*It's like a barrier is created.*")
    lprint("*You try your best to push through, but to no luck.*")
    lprint("*Your only option is to go into the cave.*")
    lprint("*Or...*")
    choice34()

def choice34():
    lprint('''a) *Look through your backpack to find something to get out through the water.*
b) *Just go into the cave.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You take off your backpack and look through it.*")
        choice34a()
    elif answer == "b":
        lprint("*You decide to just go into the cave.")
        choice34b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice34a():
    lprint("*You find a weird-looking watch.*")
    lprint("*Aside from that you don't see anything in the bag.*")
    lprint("*You put on the watch and look at it.*")
    lprint("*It has weird names on it.*")
    lprint("*You click on one and look around you.*")
    lprint("*Nothing seems to have changed.*")
    lprint("*You try another button and suddenly the cave starts to melt.*")
    lprint("*At an immensely fast pace.*")
    lprint("*Everything around you is melting.*")
    lprint("*It looks like not only the cave is melting…*")
    lprint("*EVERYTHING is melting!*")
    lprint("*Including you!*")
    lprint("*You feel your body going limp and you start to sweat.*")
    lprint("*You've turned into a puddle.*")
    Restart_Or_Quit()

def choice34b():
    lprint("*You decide to just go into the cave.*")
    choice4a()

def choice3b():
    lprint("*You hesitate a little, but your cuoriosity wins over you.*")
    lprint("*You walk up tot he chest.*")
    lprint("*You want to open it, but it's locked.*")
    lprint("*You turn to look at Ace, confused.*")
    lprint("You: It's locked.")
    lprint("Ace: Oh, my bad. Let me just-")
    lprint("*Ace searches his pockets, trying to find the key to unlock the chest with.*")
    lprint("*While he's searching his pockets, an ice pick falls from the ceiling and pierces right through Ace's skull.*")
    lprint("*He falls on the ground.*")
    lprint("You: Ace!!")
    lprint("*You run towards him and dramatically hold him in your arms.*")
    lprint("Ace: You… have to continue the quest… without me…")
    lprint("You: No!")
    lprint("You: No, just send me home!")
    lprint("You: Please just send me home!")
    lprint("*Ace puts his hand on your cheek and smiles, blood seeping out of his mouth.*")
    lprint("*He pulls you closer to his mouth and whispers.*")
    lprint("Ace: You're stuck here now.")
    choice33()

def choice33():
    lprint('''a) *Try your best to continue with the quest.*
b) *I would rather die than stay here.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You sigh and decide to go on with your quest.*")
        choice33a()
    elif answer == "b":
        lprint("*You pull the icicle out of Ace's head.*")
        choice33b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice33a():
    lprint("*What else can you do?*")
    lprint("*You continue searching Ace's pockets for him and find the key.*")
    lprint("*You go up to the chest and open it, but it's…*")
    lprint("*empty.*")
    lprint("*You look around the cave.*")
    lprint("*The entire world seems to be collapsing.*")
    lprint("*It's distorting.*")
    lprint("*Was Ace the only thing keeping this world together?*")
    lprint("*Was this world ever even real?*")
    lprint("*Are you waking up from a dream?*")
    glitch()

def choice33b():
    lprint("*You'd rather die than go on a quest that could go on forever.*")
    lprint("*Especially without a guide to help you.*")
    lprint("*You take a deep breath then stab it through your stomach.*")
    lprint("*You fall on top of Ace and you die together.*")
    Restart_Or_Quit()

def choice2b():
    lprint("*You look through your backpack to see if you can find anything.*")
    lprint("*You find a pickaxe and you sigh, putting down your torch.*")
    lprint("*You grip the pickaxe and fling it at the wall a couple of times.*")
    lprint("*After a couple of swings the wall crumbles down.*")
    lprint("*You walk through the hole you've created and end up outside.*")
    lprint("*In front of you is a waterfall, but something is slightly off about it.*")
    lprint("*The air is grim and it feels like a broken world is in front of you.*")
    lprint("*You...*")

def choice1b():
    lprint("*The tunnel gets smaller as you approach the end of it.*")
    lprint("*At the end of the tunnel you see a small door.*")
    lprint("*It's an Alive in Wonderland situation.*")
    lprint("*You look around the room and find two potions.*")
    lprint("*A green one and a red one.*")
    lprint("*You...*")
    choice11()

def choice11():
    lprint('''a) *drink the green one.*
    b) *drink the red one.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You drink the green potion.*")
        choice11a()
    elif answer == "b":
        lprint("*You drink the red potion.*")
        choice11b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice11a():
    lprint("*You feel yourself getting smaller and smaller until you're the size of the door.*")
    lprint("*You walk up to the door and open it.*")
    lprint("*Once outside you're in an ice cold place.*")
    lprint("*You shiver as you walk through the blue and white area.*")
    lprint("*You...*")
    choice12()

def choice12():
    lprint('''a) *follow the path.*
    b) *wander around.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You follow the path and end up at a cabin.*")
        choice12a()
    elif answer == "b":
        lprint("*You wander around for a bit and end up at a frozen over pond.*")
        choice12b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice12a():
    lprint("*Icicles are hanging from the roof and there's snow all around.*")
    lprint("*It seems abandoned, but you can't be too sure.*")
    lprint("*You can't reach the door handle, so you find a different way in.*")
    lprint("*You...*")
    choice13()

def choice13():
    lprint('''a) *try to find an open window.*
b) *go in from underneath the door.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You try to find an open window.*")
        choice13a()
    elif answer == "b":
        lprint("*You go in from underneath the door.*")
        choice13b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice13a():
    lprint("*As you're looking, you find a ladder that reaches the roof.*")
    lprint("*You start slowly but surely climbing the ladder, careful not to slip down due to your small size.*")
    lprint("*You make it up to the roof and climb up to the chimney.*")
    lprint("*Should you jump through it?*")
    choice28()

def choice28():
    lprint('''a) *Yes.*
b) *No.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You take the risk and jump through the chimney.*")
        choice28a()
    elif answer == "b":
        lprint("*You'll find another way in.*")
        choice28b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice28a():
    lprint("*But you didn't notice the fireplace poker until too late.*")
    lprint("*You're impaled on the edge and die almost instantly.*")
    Restart_Or_Quit()

def choice28b():
    lprint("*You want to make your way back down off the roof, but slip and fall.*")
    lprint("*You somehow end up on the one place of pavement without snow and bash your head in.*")
    lprint("*You died.*")
    Restart_Or_Quit()

def choice13b():
    lprint("*You struggle quite a bit, but succeed in the end.*")
    lprint("*Sadly, your shirt got caught on the bottom of the door and you now have a big hole on your back.*")
    lprint("*You...*")
    choice14()

def choice14():
    lprint('''a) *try to find a replacement shirt.*
    b) *don't care.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You try to find a replacement shirt.*")
        choice14a()
    elif answer == "b":
        lprint("*You don't care and just continue with your quest.*")
        choice14b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice14a():
    lprint("*You try to find a replacement shirt.*")
    lprint("*Looking around the room you see a barbie doll house in the corner of your room.*")
    lprint("*You run up to the house and enter through the door.*")
    lprint("*Inside you find yourself in a bright and nicely decorated living room.*")
    lprint("*You go up the stairs and find a barbie doll sitting on the toilet.*")
    lprint("*You sigh, but you can't find a better option.*")
    lprint("*You...*")
    choice15()

def choice15():
    lprint('''a) *strip the barbie and steal her shirt.*
    b) *just continue your quest with a ripped shirt.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You grab the barbie and steal her shirt.*")
        choice15a()
    elif answer == "b":
        lprint("*You shake your head and walk away, deciding to continue your quest with a ripped shirt.*")
        choice15b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice15a():
    lprint("*You grab the barbie and steal her shirt.*")
    lprint("*It's a bit loose on you, but it's currently the best you can do.*")
    lprint("*You get out of the dollhouse and are greeted by a very angry looking goose.*")
    lprint("*It's staring right at you, screech.*")
    lprint("*Your eyes widen in fear.*")
    lprint("*You...*")
    choice16()

def choice16():
    lprint('''a) *go back inside of the dollhouse and hide.*
    b) *run towards the dining table.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You go back inside of the dollhouse to find a hiding place.*")
        choice16a()
    elif answer == "b":
        lprint("*You run in the direction of the dining table.*")
        choice16b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice16a():
    lprint("*You get up to a bedroom and hide in the closet.*")
    lprint("*You can feel the house rumbling and shaking as the angry duck bumps against it.*")
    lprint("*The house snaps in half and you fall out of the closet.*")
    lprint("*You're now on the floor , trembling in fear as the dog growls at you.*")
    lprint("*Before you can even begin to react, the duck grabs you and eats you. *")
    Restart_Or_Quit()

def choice16b():
    lprint("*You run in the direction of the dining table.*")
    lprint("*You need to find a place to hide where the goose can't get to you.*")
    lprint("*Your eyes move to the kitchen.*")
    lprint("*You could hide underneath the fridge.*")
    lprint("*OR you could fight the goose!*")
    lprint("*You...*")
    choice17()

def choice17():
    lprint('''a) *sprint to the kitchen and slide underneath the fridge.*
    b) *try to find something to fight the goose with.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You sprint to the kitchen and slide underneath the fridge.*")
        choice17a()
    elif answer == "b":
        lprint("*You try to find something to fight the goose with.*")
        choice17b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice17a():
    lprint("*It's dusty which makes you sneeze a couple of times.*")
    lprint("*You can see the duck approaching the kitchen, but it doesn't seem to know where you went.*")
    lprint("*After a minute it waddles away.*")
    lprint("*You slowly crawl back out from underneath the fridge, but you have to be cautious.*")
    lprint("*The duck could come back at any moment.*")
    lprint("*You...*")
    choice18()

def choice18():
    lprint('''a) *look around in the kitchen.*
    b) *look around in the dining room.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You look around in the kitchen.*")
        choice18a()
    elif answer == "b":
        lprint("*You look around in the dining room.*")
        choice18b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice18a():
    lprint("*You struggle to open one of the cabinets.*")
    lprint("*Once it's opened you make your way inside.*")
    lprint("*It's filled with different potions and pots.*")
    lprint("*You find a potion you recognize.*")
    lprint("*It's the red potion you had earlier!*")
    lprint("*Or an exact replica.*")
    lprint("*You...*")
    choice19()

def choice19():
    lprint('''a) *grab the potion and drink it.*
    b) *don't risk it.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You grab the potion and drag it out of the cabinet.*")
        choice19a()
    elif answer == "b":
        lprint("*You decide not to risk it and continue looking through the cabinet.*")
        choice19b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice19a():
    lprint("*You're somehow able to get the cork out of the bottle and tip it over, taking a sip.*")
    lprint("*You watch as the kitchen gets smaller and smaller until it's normal-sized.*")
    lprint("*You've grown back to your regular size.*")
    lprint("*You...*")
    choice20()

def choice20():
    lprint('''a) *go find the goose and fucking kick it.*
    b) *leave the cabin.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You go into the living room to find the goose.*")
        choice20a()
    elif answer == "b":
        lprint("*You decide not to be petty and just leave the cabin.*")
        choice20b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice20a():
    lprint("*Once you find it, you and the goose make intense eye contact with each other.*")
    lprint("*You grin at the goose and run towards it at full speed, kicking the everliving shit out of it.*")
    lprint("*Afterwards you leave the cabin.*")
    lprint("*Once outside you're met with a gothy-looking person.*")
    lprint("*They look you up and down and you do the same to them.*")
    choice21()

def choice21():
    lprint('''a) *greet them awkwardly.*
    b) *walk away.*''')

    answer = input().lower()

    if answer == "a":
        lprint("You: Uhm... hi?")
        choice21a()
    elif answer == "b":
        lprint("*You ignore the gothy-looking person and try to walk away from them.*")
        choice21b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice21a():
    lprint("???: Who are you? What are you doing here?")
    lprint("*The gothy-looking person holds a potion in their hand threateningly.*")
    lprint("You: I'm nobody! Nobody at all.")
    lprint("You: I just… need to make my way to-")
    lprint("Ace: He's with me.")
    lprint("*You look behind you and there stands Ace. He smiles at you then wraps his arm around your shoulder.*")
    lprint("Ace: Come on, buddy.")
    lprint("Ace: We've got a quest to continue.")
    lprint("*Without saying another word to the gothy-looking person, Ace pulls you away from them.*")
    lprint("*You look behind you at them as you walk off.*")
    lprint("*The gothy-looking person is looking at you with almost murderous intent.*")
    lprint("You: Ace-")
    lprint("Ace: Don't look back.")
    lprint("Ace: Look in front of you.")
    lprint("Ace: How did you get here?")
    lprint("You: I just followed the path...")
    lprint("*Ace takes you way away from the cabin before saying another word to you.*")
    lprint("Ace: I need you to listen to me carefully, okay?")
    lprint("*He grabs your shoulders, staring into your soul. You nod at him.*")
    lprint("Ace: The person you just met was Luna.")
    lprint("Ace: She owns this place.")
    lprint("Ace: You can't just wander around in her area, you understand?")
    lprint("Ace: But speaking of her, you're going to have to-")
    lprint("You: You want me to kill her??")
    lprint("Ace: No! I need you to kill the one she cares most about.")
    lprint("You: And who's that?")
    lprint("Ace: It's... her duck.")
    lprint("You: Her duck..?")
    lprint("You: I've... already killed her duck-")
    lprint("Luca: YOU KILLED HER!")
    lprint("*The air gets grim and Luna angrily stands behind you.*")
    lprint("*Before you know it everything turns black.*")
    lprint("*You're dead.*")
    Restart_Or_Quit()

def choice21b():
    lprint("*You ignore the gothy-looking person and try to walk away from them.*")
    lprint("*Sadly, you're not lucky enough to have them just ignore you.*")
    lprint("*They grab the collar of your shirt and pull you back.*")
    lprint("???: Don't make me repeat myself, mortal.")
    lprint("*You gulp and don't say a word.*")
    lprint("*You blink and can no longer open your eyes.*")
    lprint("*You died.*")
    Restart_Or_Quit()

def choice20b():
    lprint("*You decide not to be petty and just leave the cabin.*")
    lprint("*Once outside you're met with an angry-looking goth.*")
    lprint("???: Why were you in my house?")
    lprint("You: S-sorry, I'm lost…")
    lprint("???: Who sent you, huh??")
    lprint("*They back you up and you take steps back inside of the cabin.*")
    lprint("You: I- I'm just looking for Ace-")
    lprint("???: Ace, huh?")
    lprint("???: That asshole never learns to mind his own business.")
    lprint("???: Listen to me carefully. I'm going to give you two options.")
    lprint("???: Either turn against Ace and help me get rid of him or die.")
    lprint("???: Your pick.")
    choice23()

def choice23():
    lprint('''a) *turn against Ace.*
    b) *Let the goth kill you.*''')

    answer = input().lower()

    if answer == "a":
        lprint("You: I'll help you get rid of Ace.")
        choice23a()
    elif answer == "b":
        lprint("You: Kill me...")
        choice23b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice23a():
    lprint("Ace: Oh you will, huh?")
    lprint("*Your breath hitches.*")
    lprint("*Ace is standing right behind you.*")
    lprint("*You: I- I just said that-*")
    lprint("*Before you can finish your sentence your sight turns dark.*")
    lprint("*Ace has killed you.*")
    Restart_Or_Quit()

def choice23b():
    lprint("Luna: As you wish~")
    lprint("*Luna slams her hand into your chest, creating a cavity.*")
    lprint("*She pulls her hand out and is holding your still thumping heart.*")
    lprint("*You fall to your knees.*")
    lprint("*Luna gets on her knees in front of you and whispers in your ear four words.*")
    lprint("*'You wished for this.' Are the last words you hear before she gives you a light push.*")
    lprint("*You fall on the snow, looking up at the sky as the life drains out of you.*")
    Restart_Or_Quit()

def choice19b():
    lprint("*You bump into one of the potions and it explodes.*")
    lprint("*You died.*")
    Restart_Or_Quit()

def choice18b():
    lprint("*You find a large ring sitting next to one of the table legs.*")
    lprint("*Or maybe it's a regular size ring.*")
    lprint("*There's an engraving inside of the ring.*")
    lprint("*It reads 'Luna Bushida; warrior for life'.*")
    lprint("*You wonder if this Luna is the owner of this house.*")
    lprint("*As the ring is too heavy to drag around with you, you decide to leave it and keep looking.*")
    choice25()

def choice25():
    lprint('''a) *Go to the living room.*
    b) *Go upstairs.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*Uh oh!*")
        choice25a()
    elif answer == "b":
        lprint("*You find the staircase and start to climb it.*")
        choice25b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice25a():
    lprint("*Have you forgotten where the goose was?*")
    lprint("*The goose grabs you by the leg with its mouth, flinging you around until your leg is chomped off.*")
    lprint("*You're crying in pain, desperately trying to get away from this murderous goose.*")
    lprint("*But you're too slow.*")
    lprint("*The goose finds you again and eats you whole.*")
    Restart_Or_Quit()

def choice25b():
    lprint("*It's more of a ladder than a staircase, so it's awfully steep.*")
    lprint("*Your hands get sweaty the further up you are.*")
    lprint("*You end up slipping and sliding down the ladder.*")
    lprint("*The goose hears the thump and before you can react you're eaten.*")
    Restart_Or_Quit()

def choice17b():
    lprint("*You try to find something to fight the goose with.*")
    lprint("*You find a toothpick on the ground and hold it in front of the goose.*")
    lprint("You: ENGARDE!!")
    lprint("*The goose frowns at you then screeches.*")
    lprint("*It comes at you, wanting to eat you.*")
    lprint("*You attack the goose with the toothpick and hit it in the eye.*")
    lprint("*It screeches again and takes two steps away from you.*")
    lprint("*You...*")
    choice22()

def choice22():
    lprint('''a) *stab the goose again.*
    b) *throw the toothpick at the goose and run away.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You wait for the goose to approach you again then stab it in its other eye.*")
        choice22a()
    elif answer == "b":
        lprint("*You throw the toothpick at the goose and sprint as fast as you can in the opposite direction.*")
        choice22b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice22a():
    lprint("*You wait for the goose to approach you again then stab it in its other eye.*")
    lprint("*After that the goose runs away from you.*")
    lprint("*You let out a relieved sigh and continue looking around the house.*")
    lprint("*Your eye catches something shiny on top of the coffee table.*")
    lprint("*As you approach it you notice it's a ring.*")
    lprint("*You reach into your backpack and take out a catapult.*")
    lprint("*You can either use the catapult or try to climb on the table.*")
    lprint("*What do you do?*")
    choice24()

def choice24():
    lprint('''a) *Use the catapult.*
    b) *Climb the table.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You set up the catapult to use it.*")
        choice24a()
    elif answer == "b":
        lprint("*You put the catapult back inside your bag for future use and decide to climb the table.*")
        choice24b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice24a():
    lprint("*You get ready and stand against the elastic, pulling it back as far as you can.*")
    lprint("*When you finally let go, you realize you didn't angle the catapult correctly.*")
    lprint("*You're shot straight forward and splatter against one of the table's legs.*")
    lprint("*You died.*")
    Restart_Or_Quit()

def choice24b():
    lprint("*You try your best to keep balance.*")
    lprint("*Sadly, you slip and fall to your death.*")
    Restart_Or_Quit()

def choice22b():
    lprint("*Luckily, the goose doesn't follow you.*")
    lprint("*But as you're running, you're picked up and are floating in the air.*")
    lprint("???: Ugh, I hate bugs.")
    lprint("*You're thrown outside of the window and fall on the snow.*")
    lprint("*You can't see over the snow, so you can't see the foot about to step on you until it's much too late.*")
    lprint("*You're crushed to death.*")
    Restart_Or_Quit()

def choice15b():
    lprint("*You can't steal a barbie's shirt.*")
    lprint("*You'll just have to deal with your ripped shirt.*")
    lprint("*You exit the barbie house and are met with a very angry looking goose.*")
    lprint("*Before you know it, it starts attacking you.*")
    lprint("*You...*")
    choice29()

def choice29(): 
    lprint('''a) *run left.*
b) *run right.*''') 

    answer = input().lower() 

    if answer == "a": 
        lprint("*You attempt to run left, but the goose is much faster and much bigger than you.*")
        choice29a()
    elif answer == "b": 
        lprint("*You try to run left, but the goose steps on you.*")
        choice29b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice29a():
    lprint("*It's beak covers your body whole and he swallows you at once.*")
    lprint("*You suffocate inside of the goose's stomach.*")
    Restart_Or_Quit()

def choice29b():
    lprint("*Your head is crushed between the goose's foot and the floor.*")
    lprint("*You died.*")
    Restart_Or_Quit()

def choice14b():
    lprint("*But, what is your quest exactly?*")
    lprint("*Right as you confusedly look around, Ace pops up.*")
    lprint("Ace: How's it going? Why are you so small?")
    lprint("*He picks you up and sits you on the palm of his hand.*")
    lprint("You: I drank a potion.")
    lprint("Ace: Ohh, I can help with that.")
    lprint("*Ace walks into the kitchen and puts you down on the counter.*")
    lprint("*He looks around some cabinets and pulls out a red potion.*")
    lprint("Ace: This should do the trick.")
    lprint("*He opens the bottle and hands it to you.*")
    lprint("*You look at him suspiciously but agree to drink it.*")
    lprint("*Right after drinking it you start to grow and grow.*")
    lprint("*You grow almost endlessly.*")
    lprint("*And fast!*")
    lprint("*You keep growing until your head hits the roof and it becomes hard to stay compact.*")
    lprint("*You accidentally burst a pipe that was in the ceiling.*")
    lprint("*You don't even notice Ace leaving the kitchen.*")
    lprint("You: Where are you going?? Help me!")
    lprint("Ace: So I can die with you? No thanks~")
    lprint("*He takes a lighter out of his pocket and throws it behind his back as he's leaving.*")
    lprint("*You burn along with the house and die a slow and painful death.*")
    Restart_Or_Quit()

def choice12b():
    lprint("*There's blue and white frogs hopping over it, slipping every once in a while and sliding around which you find funny.*")
    lprint("*You approach the pond and put a foot on it, scared to add your second foot.*")
    lprint("*But it seems secure enough.*")
    choice26()

def choice26():
    lprint('''a) *Get on the pond.*
b) *Don't risk it and continue wandering.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You get on the pond and slide around for a while.*")
        choice26a()
    elif answer == "b":
        lprint("*You decide not to risk it and continue wandering the land.*")
        choice26b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice26a():
    lprint("*It's going surprisingly well…*")
    lprint("*Almost suspiciously well.*")
    lprint("*Until a frog jumps on your chest and you slip and fall backwards.*")
    lprint("*The ice begins to crack and you can't move.*")
    choice27()

def choice27():
    lprint('''a) *Try to get on land.*
b) *Stay in place.*''')

    answer = input().lower()

    if answer == "a":
        lprint("*You try your best to get on land, but to no luck.*")
        choice27a()
    elif answer == "b":
        lprint("*You stay in place, trying your best not to make a move.*")
        choice27b()

    else: 
        lprint("You can't do that.")
        lprint("Please try again.")

def choice27a():
    lprint("*The ice cracks more and you fall through.*")
    lprint("*You can swim, but it feels like something has grabbed you and dragged you down into the water.*")
    lprint("*You're not even able to catch a last breath before you sink into the pond.*")
    lprint("*You drown to death.*")
    Restart_Or_Quit()

def choice27b():
    lprint("*But an asshole frog jumps on top of you, causing another crack in the ice.*")
    lprint("*Suddenly a bunch more frogs jump on you.*")
    lprint("*It's like they're doing it on purpose to try and kill you!*")
    lprint("*The ice fully breaks and you fall into the pond, sinking deeper and deeper no matter how much you try to swim upwards.*")
    lprint("*You look down and the frogs somehow have gotten a hold of your clothing and are dragging you down into the pond.*")
    lprint("*The frogs drowned you to death.*")
    Restart_Or_Quit()

def choice26b():
    lprint("*You hear some rumbling from what feels like far away.*")
    lprint("*When you look up you notice a huge tree shaking.*")
    lprint("*Is it falling?*")
    lprint("*Before you know it, the tree is falling towards you.*")
    lprint("*You're unsure of what to do.*")
    lprint("*Do you run?*")
    lprint("*It's probably too far away to hit you anyway, right?*")
    lprint("*You spent too much time thinking about what to do.*")
    lprint("*The tree has fallen on top of you and killed you.*")
    Restart_Or_Quit()

def choice11b():
    lprint("*You start getting bigger and bigger, your clothes luckily growing along with you.*")
    lprint("*You bump your head against the top of the cave and the cave starts rumbling.*")
    lprint("*You're getting too big for the cave.*")
    lprint("*So big that the wall starts breaking.*")
    lprint("*You keep on growing until you practically reach the land of the giants.*")
    lprint("*You find yourself unable to breathe.*")
    lprint("*Your limp body flails down on the land and you break the matrix.*")
    lprint("*But you can't explore it because you died.*")
    Restart_Or_Quit()

Start() #Call the function "Start"
