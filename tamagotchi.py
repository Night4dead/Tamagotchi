from tkinter import *
from time import *
from random import *

file = open(file="config.txt",mode ="r")
config = file.readlines()
file.close()


global health_ga,health_max, hunger_ga,hunger_max, bore_ga,bore_max, dirtiness,turns
health_ga = float(config[0])
health_max = float(config[1])
hunger_ga = float(config[2])
hunger_max = float(config[3])
bore_ga = float(config[4])
bore_max = float(config[5])
dirtiness = float(config[6])
turns = float(config[7])

def startGame():
    global dirtiness
    if dirtiness > 0:
        clean.place(x=205,y=450)
        shower.place(x=265, y=450)
        disp_tama.place_forget()
        disp_tama.configure(image=tamagotchi_dirty)
        disp_tama.place(x=185, y=185)
    elif dirtiness == 0:
        disp_tama.place_forget()
        disp_tama.configure(image=tamagotchi)
        disp_tama.place(x=185, y=185)
    health_lbl.place(x=25, y=25)
    hunger_lbl.place(x=25, y=75)
    boredom_lbl.place(x=25, y=125)
    mood_lbl.place(x=225, y=125)
    mood_color_lbl.place(x=300, y=100)
    rules.place(x=225, y=25)
    rules.insert(INSERT, "Les règles sont simples ! Vous devez garder la santé de l'animal au maximum, et sa faim et son ennui au minimum !")
    btn_start.place_forget()
    btn_new.place(x= 425, y= 450)
    feed.place(x=25, y=450)
    sleep.place(x=85, y=450)
    play.place(x=145, y=450)
    save.place(x=355, y=450)
    

def saveGame():
    file = open(file="config.txt", mode="w")
    config[0]=float(health_ga)
    config[1]=float(health_max)
    config[2]=float(hunger_ga)
    config[3]=float(hunger_max)
    config[4]=float(bore_ga)
    config[5]=float(bore_max)
    config[6]=float(dirtiness)
    config[7]=float(turns)
    config[0]=str(config[0]) + "\n"
    config[1]=str(config[1]) + "\n"
    config[2]=str(config[2]) + "\n"
    config[3]=str(config[3]) + "\n"
    config[4]=str(config[4]) + "\n"
    config[5]=str(config[5]) + "\n"
    config[6]=str(config[6]) + "\n"
    config[7]=str(config[7]) + "\n"
    for i in range(0,8):
        file.write(str(config[i]))
    file.close()

def newGame():
    file = open(file="config.txt", mode="w")
    config[0]=10.0
    config[1]=10.0
    config[2]=5.0
    config[3]=10.0
    config[4]=5.0
    config[5]=10.0
    config[6]=0.0
    config[7]=0.0
    config[0]=str(config[0]) + "\n"
    config[1]=str(config[1]) + "\n"
    config[2]=str(config[2]) + "\n"
    config[3]=str(config[3]) + "\n"
    config[4]=str(config[4]) + "\n"
    config[5]=str(config[5]) + "\n"
    config[6]=str(config[6]) + "\n"
    config[7]=str(config[7]) + "\n"
    for i in range(0,8):
        file.write(str(config[i]))
    file.close()
    window.destroy()
    
def homeScreen():
    global dirtiness
    
    feed_soda.place_forget()
    feed_fries.place_forget()
    feed_sandwich.place_forget()
    feed_salad.place_forget()
    feed_question.place_forget()
    cancel_btn.place_forget()
    play_question.place_forget()
    play_caress.place_forget()
    play_ball.place_forget()
    feed.place(x=25, y=450)
    sleep.place(x=85, y=450)
    play.place(x=145, y=450)
    if dirtiness > 0:
        clean.place(x=205,y=450)
        shower.place(x=265, y=450)
        disp_tama.place_forget()
        disp_tama.configure(image=tamagotchi_dirty)
        disp_tama.place(x=185, y=185)
    elif dirtiness == 0:
        disp_tama.place_forget()
        disp_tama.configure(image=tamagotchi)
        disp_tama.place(x=185, y=185)
    death()

def feed():
    sleep.place_forget()
    play.place_forget()
    feed.place_forget()
    clean.place_forget()
    shower.place_forget()
    disp_tama.place_forget()
    disp_tama.configure(image=tamagotchi_eating)
    disp_tama.place(x=185, y=185)
    feed_question.place(x=25, y=385)
    feed_soda.place(x=25,y=450)
    feed_fries.place(x=85,y=450)
    feed_salad.place(x=145,y=450)
    feed_sandwich.place(x=205,y=450)
    cancel_btn.place(x=300,y=450)
    
def feedSoda():
    global hunger_ga,health_ga,turns
    if dirtiness >0 :
        hunger_ga = hunger_ga -0.5
        if hunger_ga < 0:
            hunger_ga = 0.0
            health_ga += 1.0
            if health_ga > health_max:
                health_ga =health_max
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
    else:
        hunger_ga = hunger_ga -1
        if hunger_ga < 0:
            hunger_ga = 0.0
            health_ga += 1.5
            if health_ga > health_max:
                health_ga =health_max
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
    hunger_lbl.place_forget()
    hunger_lbl.configure(text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
    hunger_lbl.place(x=25, y=75)
    moodColor()
    turns +=1
    homeScreen()
def feedFries():
    global hunger_ga,health_ga,turns
    if dirtiness >0:
        hunger_ga = hunger_ga -1.5
        if hunger_ga < 0:
            hunger_ga = 0.0
            health_ga += 1.0
            if health_ga > health_max:
                health_ga =health_max
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)

    else:
        hunger_ga = hunger_ga -2
        if hunger_ga < 0:
            hunger_ga = 0.0
            health_ga += 1.5
            if health_ga > health_max:
                health_ga =health_max
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
    hunger_lbl.place_forget()
    hunger_lbl.configure(text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
    hunger_lbl.place(x=25, y=75)
    moodColor()
    turns +=1
    homeScreen()
def feedSalad():
    global hunger_ga,health_ga,turns
    if dirtiness > 0:
        hunger_ga = hunger_ga -2.5
        if hunger_ga < 0:
            hunger_ga = 0.0
            health_ga += 1.0
            if health_ga > health_max:
                health_ga =health_max
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)

    else:
        hunger_ga = hunger_ga -3
        if hunger_ga < 0:
            hunger_ga = 0.0
            health_ga += 1.5
            if health_ga > health_max:
                health_ga =health_max
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
    hunger_lbl.place_forget()
    hunger_lbl.configure(text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
    hunger_lbl.place(x=25, y=75)
    moodColor()
    turns +=1
    homeScreen()
def feedSandwich():
    global hunger_ga,health_ga,turns
    if dirtiness >0:
        hunger_ga = hunger_ga -3.5
        if hunger_ga < 0:
            hunger_ga = 0.0
            health_ga += 1.0
            if health_ga > health_max:
                health_ga =health_max
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
    else:
        hunger_ga = hunger_ga -4
        if hunger_ga < 0:
            hunger_ga = 0.0
            health_ga += 1.5
            if health_ga > health_max:
                health_ga =health_max
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
    hunger_lbl.place_forget()
    hunger_lbl.configure(text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
    hunger_lbl.place(x=25, y=75)
    moodColor()
    turns +=1
    homeScreen()

def toilet():
    global hunger_ga, dirtiness
    
    if (hunger_ga/hunger_max)*10 < 2.5 and (turns % 3) == 0:
        if dirtiness == 0:
            a = randint(0,184)
            b = randint(185,300)
            poop.place(x=a, y=b)
            dirtiness += 1
        else :
            dirtiness += 1



def sleep():
    global hunger_ga, health_ga, bore_ga, bore_max,turns
    hunger_ga += 2
    if dirtiness > 0:
        if hunger_ga > hunger_max:
            health_ga = health_ga - (hunger_ga-hunger_max)
            hunger_ga = hunger_max
        health_ga += 1.5
        if health_ga > health_max:
            health_ga = health_max
            bore_ga = bore_ga -0.25
            if bore_ga < 0:
                bore_ga = 0.0
        bore_ga += 1.5
        if bore_ga > bore_max:
            
            health_ga = health_ga - (bore_ga-bore_max)
            bore_ga = bore_max
    else:
        if hunger_ga > hunger_max:
            health_ga = health_ga - (hunger_ga-hunger_max)
            hunger_ga = hunger_max
        health_ga += 2.0
        if health_ga > health_max:
            health_ga = health_max
            bore_ga = bore_ga -0.5
            if bore_ga < 0:
                bore_ga = 0.0
        bore_ga += 1.0
        if bore_ga > bore_max:
            
            health_ga = health_ga - (bore_ga-bore_max)
            bore_ga = bore_max
    hunger_lbl.place_forget()
    health_lbl.place_forget()
    boredom_lbl.place_forget()
    health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
    hunger_lbl.configure(text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
    boredom_lbl.configure(text="Ennui : " + str(bore_ga) + "/" + str(bore_max))
    health_lbl.place(x=25, y=25)
    hunger_lbl.place(x=25, y=75)
    boredom_lbl.place(x=25, y=125)
    moodColor()
    turns +=1
    homeScreen()


def play():
    sleep.place_forget()
    play.place_forget()
    feed.place_forget()
    clean.place_forget()
    shower.place_forget()
    disp_tama.place_forget()
    disp_tama.configure(image=tamagotchi_playing)
    disp_tama.place(x=185, y=185)
    play_question.place(x=25, y=375)
    play_caress.place(x=25,y=450)
    play_ball.place(x=125, y=450)
    
    cancel_btn.place(x=300,y=450)

def playCaress():
    global hunger_ga, hunger_max, bore_ga, health_ga,turns
    bore_ga = bore_ga - 1.0
    if dirtiness > 0:
        if bore_ga < 0:
            bore_ga = 0.0
        hunger_ga += 1.5
        if hunger_ga > hunger_max:
            
            health_ga = health_ga - (hunger_ga-hunger_max)
            hunger_ga = hunger_max
    else:
        if bore_ga < 0:
            bore_ga = 0.0
        hunger_ga += 0.5
        if hunger_ga > hunger_max:
            
            health_ga = health_ga - (hunger_ga-hunger_max)
            hunger_ga = hunger_max
    hunger_lbl.place_forget()
    health_lbl.place_forget()
    boredom_lbl.place_forget()
    health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
    hunger_lbl.configure(text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
    boredom_lbl.configure(text="Ennui : " + str(bore_ga) + "/" + str(bore_max))
    health_lbl.place(x=25, y=25)
    hunger_lbl.place(x=25, y=75)
    boredom_lbl.place(x=25, y=125)
    moodColor()
    turns +=1
    homeScreen()
        
        

def playBall():
    global hunger_ga, hunger_max, bore_ga, health_ga,turns,dirtiness
    bore_ga = bore_ga - 3.5
    if dirtiness > 0:
        if bore_ga < 0:
            bore_ga = 0.0
        hunger_ga += 3
        if hunger_ga > hunger_max:
        
            health_ga = health_ga - (hunger_ga-hunger_max)
            hunger_ga = hunger_max
    else:
        if bore_ga < 0:
            bore_ga = 0.0
        hunger_ga += 2
        if hunger_ga > hunger_max:
            
            health_ga = health_ga - (hunger_ga-hunger_max)
            hunger_ga = hunger_max
    hunger_lbl.place_forget()
    health_lbl.place_forget()
    boredom_lbl.place_forget()
    health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
    hunger_lbl.configure(text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
    boredom_lbl.configure(text="Ennui : " + str(bore_ga) + "/" + str(bore_max))
    health_lbl.place(x=25, y=25)
    hunger_lbl.place(x=25, y=75)
    boredom_lbl.place(x=25, y=125)
    moodColor()
    turns +=1
    homeScreen()

def clean():
    global turns,dirtiness
    if dirtiness > 1:
        dirtiness = dirtiness -1
    elif dirtiness == 1:
        poop.place_forget()
        dirtiness = dirtiness -1
    turns+=1
def shower():
    global dirtiness,turns
    disp_tama.place_forget()
    disp_tama.configure(image=tamagotchi)
    disp_tama.place(x=185, y=185)
    dirtiness =0
    turns +=1
def moodColor():
    global health_ga, hunger_ga, bore_ga, health_max, hunger_max, bore_max
    toilet()
    if health_ga == health_max and hunger_ga == 0.0 and bore_ga == 0.0:
        health_max += 1.5
        hunger_max += 1.5
        bore_max += 1.5
        health_ga = health_ga - 3.5
        hunger_ga += 3.5
        bore_ga += 3.5
        hunger_lbl.place_forget()
        health_lbl.place_forget()
        boredom_lbl.place_forget()
        health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
        hunger_lbl.configure(text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
        boredom_lbl.configure(text="Ennui : " + str(bore_ga) + "/" + str(bore_max))
        health_lbl.place(x=25, y=25)
        hunger_lbl.place(x=25, y=75)
        boredom_lbl.place(x=25, y=125)
        
    if (health_ga/health_max)*10 > 7.5:
        if hunger_ga < 2.5 and (bore_ga/bore_max)*10 < 4.5:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "green")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >=2.5 and (hunger_ga/hunger_max)*10 < 5.0 and (bore_ga/bore_max)*10 >= 4.5 and (bore_ga/bore_max)*10 < 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "yellow")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >=5.0 and (hunger_ga/hunger_max)*10 < 7.5 and (bore_ga/bore_max)*10 <= 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "yellow")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >= 7.5 and (bore_ga/bore_max)*10 > 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "red")
            mood_color_lbl.place(x=300, y=100)
            
    elif (health_ga/health_max)*10 <= 7.5 and (health_ga/health_max)*10 > 5.0 :
        if (hunger_ga/hunger_max)*10 >=2.5 and (hunger_ga/hunger_max)*10 < 5.0 and (bore_ga/bore_max)*10 >= 4.5 and (bore_ga/bore_max)*10 < 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "yellow")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 < 2.5 and bore_ga < 4.5:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "green")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >=5.0 and (hunger_ga/hunger_max)*10 < 7.5 and (bore_ga/bore_max)*10 <= 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "yellow")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >= 7.5 and (bore_ga/bore_max)*10 > 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "red")
            mood_color_lbl.place(x=300, y=100)
            
    elif (health_ga/health_max)*10 <= 5.0 and (health_ga/health_max)*10 > 2.5 :
        if (hunger_ga/hunger_max)*10 >=2.5 and (hunger_ga/hunger_max)*10 < 5.0 and (bore_ga/bore_max)*10 >= 4.5 and (bore_ga/bore_max)*10 < 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "red")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 < 2.5 and (bore_ga/bore_max)*10 < 4.5:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "yellow")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >=5.0 and (hunger_ga/hunger_max)*10 < 7.5 and (bore_ga/bore_max)*10 <= 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "red")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >= 7.5 and (bore_ga/bore_max)*10 > 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "black")
            mood_color_lbl.place(x=300, y=100)
            health_ga = health_ga - 0.5
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
            
    elif (health_ga/health_max)*10 <2.5:
        if (hunger_ga/hunger_max)*10 >=2.5 and (hunger_ga/hunger_max)*10 < 5.0 and (bore_ga/bore_max)*10 >= 4.5 and (bore_ga/bore_max)*10 < 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "black")
            mood_color_lbl.place(x=300, y=100)
            health_ga = health_ga - 0.5
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
            
        elif (hunger_ga/hunger_max)*10 < 2.5 and (bore_ga/bore_max)*10 < 4.5:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "red")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >=5.0 and (hunger_ga/hunger_max)*10 < 7.5 and (bore_ga/bore_max)*10 <= 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "red")
            mood_color_lbl.place(x=300, y=100)
            
        elif (hunger_ga/hunger_max)*10 >= 7.5 and (bore_ga/bore_max)*10 > 6.0:
            mood_color_lbl.place_forget()
            mood_color_lbl.configure(bg = "black")
            mood_color_lbl.place(x=300, y=100)
            health_ga = health_ga - 0.5
            health_lbl.place_forget()
            health_lbl.configure(text="Santé : " + str(health_ga) + "/" + str(health_max))
            health_lbl.place(x=25, y=25)
            

def death():
    global health_ga, hunger_ga, bore_ga, health_max, hunger_max, bore_max
    if health_ga == 0.0:
        disp_tama.place_forget()
        disp_tama.configure(image=dead)
        disp_tama.place(x=185, y=185)
    elif (health_ga/health_max)*10 <= 3.0 and hunger_ga == hunger_max and (bore_ga/bore_max)*10 > 4.0:
        disp_tama.place_forget()
        disp_tama.configure(image=dead)
        disp_tama.place(x=185, y=185)
        
        sleep.place_forget()
        play.place_forget()
        feed.place_forget()
        clean.place_forget()
        shower.place_forget()
        save.place_forget()
        
        rules.insert(INSERT,"\n" + "Votre animal est mort de faim et d'ennui vous ne vous en etes pas assez bien occupé !")
        rules.see("end")
   






window = Tk()
window.geometry("600x525")
window.title("PYmagocchi")
window.configure(background = "white")

shit = PhotoImage(file="images/dirt.gif")
sandwich = PhotoImage(file="images/Sandwich.gif")
shower_gif = PhotoImage(file="images/Shower_symbol.gif")
ball = PhotoImage(file="images/ball.gif")
broom = PhotoImage(file="images/balai.gif")
hand = PhotoImage(file="images/hand.gif")
sleeping = PhotoImage(file="images/sleep.gif")
save_disk = PhotoImage(file="images/floppy.gif")
game = PhotoImage(file="images/game.gif")
food = PhotoImage(file="images/food.gif")
fries=PhotoImage(file="images/fries.gif")
salad=PhotoImage(file="images/salad.gif")
soda=PhotoImage(file="images/soda.gif")
dead = PhotoImage(file="images/death.gif")



tamagotchi = PhotoImage(file="images/Kuchipatchi.gif")
tamagotchi_playing = PhotoImage(file="images/Kuchipatchi_anime.gif")
tamagotchi_eating = PhotoImage(file="images/Kuchipatchi_eating.gif")
tamagotchi_dirty = PhotoImage(file="images/Kuchipatchi_dirty.gif")
disp_tama = Label(window, image=tamagotchi)

health_lbl = Label(window,relief=RAISED, text="Santé : " + str(health_ga) + "/" + str(health_max))
hunger_lbl = Label(window,relief=RAISED, text="Faim : " + str(hunger_ga) + "/" + str(hunger_max))
boredom_lbl = Label(window,relief=RAISED, text="Ennui : " + str(bore_ga) + "/" + str(bore_max))
mood_lbl = Label(window,relief=RAISED, text="Humeur : ")
mood_color_lbl = Label(window,text= "   "+"\n"+"   "+"\n"+"    "+"\n"+"    ", bg = "green", width = 10)

btn_start = Button(window, text="Start", command = startGame)
btn_start.place(x=25, y=450)
btn_new = Button(window,relief=RAISED, text="Effacer save et quitter", command = newGame)
                 
feed = Button(window, text="Nourrir",image=food, command = feed)
sleep = Button(window, text="Dormir",image=sleeping, command = sleep)
play = Button(window, text="Jouer",image=game, command = play)
clean = Button(window, text="Nettoyer",image=broom, command = clean)
shower = Button(window, text="Laver",image=shower_gif, command = shower)
poop = Label(window, image=shit)
rules = Text(window, width = "45", height = "3")
save = Button(window, text="Save game",image = save_disk, command = saveGame)



feed_question = Label(window,relief=RAISED, text = "Avec quel aliment voulez vous nourrir votre animal ?")
feed_soda = Button(window, text="Soda",image=soda, command = feedSoda )
feed_fries = Button(window, text="French Fries",image=fries, command = feedFries )
feed_salad = Button(window, text="Salad",image=salad, command = feedSalad )
feed_sandwich = Button(window, text="Sandwich",image = sandwich, command = feedSandwich)
cancel_btn = Button(window, text="Cancel", command = homeScreen)


play_question = Label(window,relief=RAISED, text ="A quoi voulez vous jouer ?")
play_caress = Button(window, text="Caresser",image = hand, command = playCaress)
play_ball = Button(window, text="Balle",image = ball, command= playBall)





window.mainloop()

