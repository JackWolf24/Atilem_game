import time as t
import vlc
import parser2
import lexicon

global i

items = ["30m rope", "life jacket", "sunglasses", "key", "anti toxic potion", "flashlight", "5L of water", "3 apples",
         "raincoat", "game of cards"]
backpack = []
backgoundp = vlc.MediaPlayer(r"C:\Users\maurice.jarck\Documents\tutorials\lpthw\Resistance - AShamaluevMusic.mp3")
backgoundp2 = vlc.MediaPlayer(r"C:\Users\maurice.jarck\Documents\tutorials\lpthw\Epicness - AShamaluevMusic.mp3")
witchp = vlc.MediaPlayer(r"C:\Users\maurice.jarck\Documents\tutorials\lpthw\witch.m4a")
gameoverp = vlc.MediaPlayer(r"C:\Users\maurice.jarck\Documents\tutorials\lpthw\game over.mp3")
hintp = vlc.MediaPlayer(r"C:\Users\maurice.jarck\Documents\tutorials\lpthw\hint.m4a")
walkp = vlc.MediaPlayer(r"C:\Users\maurice.jarck\Documents\Projects\Atilem\walking.mp3")  # 6s
doorp = vlc.MediaPlayer(r"C:\Users\maurice.jarck\Documents\tutorials\lpthw\door open..mp3")  # 4s
winp = vlc.MediaPlayer(r"C:\Users\maurice.jarck\Documents\tutorials\lpthw\positive-notification-sound-winning-melody.mp3")  # 3s
backgoundp.audio_set_volume(40)

def opening():

    walkp.play()

    t.sleep(4)

    print("Hey Im Gorge and Im your companion on this journey of trying to find the")

    walkp.stop()

    backgoundp2.play()

    print("""
    \t\t treasure of Atillem 
    
    an old society extincted several hundrets years ago.""")
    t.sleep(3)
    print(
        "Today we prepare for the first atempt of finding the treasure in that scary cave over there. \nI heard of many brave man entering but close to non came back alive.")
    t.sleep(6)

    askscare()


def askscare():
    print("Well didnt wanted to scare you, is all right? you look a little faint. \n yes \n not at all")

    while True:

        in1 = input("> ")
        lexicon.lexicon(in1)
        answer1 = parser2.parse_sentence(lexicon.sentence)

        if answer1.object == "yes":
            print("great, I knew you were one of the brave ones, thats something i feel in ma pee")
            askready()
        elif answer1.object == "not":
            print("Come on man, stop peeing your throusers. Only the one who tries is in possition of having a chance to win")
            askscare()
        else:
            print("did you learn to speak in proper words???, seems not like")


def askready():
    print("ready to rumble? \n yes \n not at all")
    while True:

        in2 = input("> ")
        lexicon.lexicon(in2)
        answer2 = parser2.parse_sentence(lexicon.sentence)

        if answer2.object == "yes":
            print("great, so lets prepare our equipment:")
            t.sleep(2)
            equip()
            break
        elif answer2.object == "not":
            print("what are you waiting for?, well anyways only die harten kommen in den garten so lets go")
            equip()
            break
        else:
            print("did you learn to speak in proper words???, seems not like")


def equip():
    print(
        "ok there are 10 Items you could take with you. But sadly our backpack is capeable of containing just 4 Items")
    t.sleep(3)

    for r in range(0, len(items)):
        t.sleep(2)
        print("\t", items[r])
    print("choose wisely")
    i = 0

    while i < 4:
        in3 = input("> ")
        lexicon.lexicon(in3)
        answer3 = parser2.parse_sentence(lexicon.sentence)

        if answer3.object in items:
            print("great decision")
            print("you got", 4 - (i + 1), "items left")
            backpack.append(answer3)
            i += 1

        elif answer3.object not in items:
            print("bro, lifes not a wunschkonzert")

    print("ok, you chose:")
    for n in range(0, len(backpack)):
        t.sleep(2)
        print("\t", backpack[n])

    startroom()


def startroom():
    print("OK great, lets enter the cave")
    backgoundp2.pause()
    backgoundp.audio_set_volume(40)
    backgoundp.play()
    t.sleep(6)
    print("Its pretty dark in here. could you please switch on your flashlight?")
    print("#searching")
    t.sleep(5)
    if "flashlight" in backpack:
        print("\ngreat. \n#light switches on")
        t.sleep(5)

    else:
        print("\nmaaan, you forgott it, we have to go back and pick one up")
        t.sleep(10)
        equip()

    t.sleep(2)

    print("oh hey, the first room, 2 doors available, which one do choose? \nleft \nright\nback")
    while True:

        in4 = input("> ")
        lexicon.lexicon(in4)
        answer4 = parser2.parse_sentence(lexicon.sentence)

        if answer4.object == "left":
            print("ok lets take the left one")
            t.sleep(2)
            print("#opens door")
            backgoundp.pause()
            doorp.play()
            t.sleep(4)
            backgoundp.play()
            l1()
            break
        elif answer4.object == "right":
            print("ok lets go right")
            t.sleep(2)
            print("#opens door")
            backgoundp.pause()
            doorp.play()
            t.sleep(4)
            backgoundp.play()
            r1()
            break

        elif answer4.object == "back":
            print("ok lets go back")
            t.sleep(2)
            print("#opens door")
            backgoundp.pause()
            doorp.play()
            t.sleep(4)
            backgoundp.play()
            startroom()
            break
        else:
            print("did you learn to speak in proper words???, seems not like")


def l1():
    print("oh a new room, stairs and a door, hm but where to go? \nleft(stairs) \nright(door) \nback")
    while True:

        in5 = input("> ")
        lexicon.lexicon(in5)
        answer5 = parser2.parse_sentence(lexicon.sentence)

        if answer5.object == "door":
            print("ok lets try to open the door, oh shit, its locked. Do we have a key? wait ill check the backpack")
            t.sleep(2.0)

            if "key" in backpack:
                print("\npeeew lucky ones. \n#door opens")
                backgoundp.pause()
                doorp.play()
                t.sleep(4)
                backgoundp.play()
                print("#loud metallic sound \nOh no the key broke, we cant use it another time. Ill throw it away.")
                backpack.remove("key")
                t.sleep(3)
                l2()
                break
            else:
                print("\nmaaan, you forgott it, we have to go retry")
                l1()
                break
        elif answer5.object == "stairs":
            print("ok lets go upstairs")
            up()
            break
        elif answer5.object == "back":
            startroom()
        else:
            print("did you learn to speak in proper words???, seems not like")


def l2():
    print("new room. oh a sign, ill read it to you, ready? \n\tyes \n\tno ")
    while True:

        in11 = input("> ")
        lexicon.lexicon(in11)
        answer11 = parser2.parse_sentence(lexicon.sentence)

        if answer11.object == "yes":
            print("great, so ill start")
            backgoundp.pause()
            backgoundp.audio_set_volume(60)
            witchp.play()
            t.sleep(31)
            backgoundp.audio_set_volume(40)
            backgoundp.play()
            break
        elif answer11.object == "no":
            print("take ya time")

        else:
            print("did you learn to speak in proper words???, seems not like")

    print("you could take the...: \n\t'red' one \n\t'green' one\n\t'blue' one \nor go 'back'' ")
    while True:

        in6 = input("> ")
        lexicon.lexicon(in6)
        answer6 = parser2.parse_sentence(lexicon.sentence)

        if answer6.object == "blue":
            print("#drinks")
            t.sleep(2.0)
            print("shit you look kinda green. Wheres the antioxic potion???")
            print("#searching")
            if "anti toxic potion" in backpack:
                print("\npeeew. come one hurry up drink it all up")
                t.sleep(2)
                print("you look way better")
                backpack.remove("anti toxic potion")
                l2()
                break
            else:
                print("\nmaaan, you forgott it, youre going to die")
                print("#dies low and painful")
                print("GAMEOVER")
                backgoundp.pause()
                gameoverp.play()
                t.sleep(5)
                exit(0)
        elif answer6.object == "red" or "green":
            print("hm theres no recation I think we got the right one")
            goal()
            break
        elif answer6.object == "back":
            l1()
        else:
            print("did you learn to speak in proper words???, seems not like")


def up():
    print("oh yea a piece of paper with advices, Ill read it for you, ready? \n\tyes \n\tno ")
    while True:

        in12 = input("> ")
        lexicon.lexicon(in12)
        answer12 = parser2.parse_sentence(lexicon.sentence)

        if answer12.object == "yes":
            print("great, so ill start")
            backgoundp.pause()
            backgoundp.audio_set_volume(60)
            hintp.play()
            t.sleep(31)
            backgoundp.audio_set_volume(40)
            backgoundp.play()
            break
        elif answer12.object == "no":
            print("take ya time")

        else:
            print("did you learn to speak in proper words???, seems not like")

    print("good to know")
    print("our options are:, \ndownstairs next room \nback")
    while True:

        in7 = input("> ")
        lexicon.lexicon(in7)
        answer7 = parser2.parse_sentence(lexicon.sentence)

        if answer7.object == "downstairs next room":
            print("ok lets go")
            l2()
            break
        elif answer7.object == "back":
            print("ok lets go back")
            l1()
            break
        else:
            print("did you learn to speak in proper words???, seems not like")


def r1():
    t.sleep(2)
    print("You see that snake infront of that door? dont look in her eyes. If you do so youll freeze to stone")
    t.sleep(3)
    print("sunglases might protect you, got some?")
    t.sleep(2)
    if "sunglasses" in backpack:
        print("\nok, you got some. thatll be an easy one put her by the side in order to unravel the door")
        backgoundp.pause()
        doorp.play()
        t.sleep(4)
        backgoundp.play()
        print("oh the door isnt locked at all lets step right in")

        backpack.remove("sunglasses")
        r2()

    else:
        print("\nmaaan, you forgott it, youre going to die")
        print("#dies low and painful because of becoming stone")
        print("GAMEOVER")
        backgoundp.pause()
        gameoverp.play()
        t.sleep(4)
        exit(0)


def r2():
    print("noe were entering a labyrinth seems like there are alway only two options \n\tleft \n\tright \n\tback")
    while True:

        in8 = input("> ")
        lexicon.lexicon(in8)
        answer8 = parser2.parse_sentence(lexicon.sentence)

        if answer8.object == "left":
            print("ok lets take the left one")
            t.sleep(2)
            print("#opens door")
            backgoundp.pause()
            doorp.play()
            t.sleep(4)
            backgoundp.play()
            print("once again the same, \n\tleft \n\tright \n\tback")
            while True:

                in9 = input("> ")
                lexicon.lexicon(in9)
                answer9 = parser2.parse_sentence(lexicon.sentence)

                if answer9.object == "left":
                    print("ok lets take the left one")
                    t.sleep(2)
                    print("#opens door")
                    backgoundp.pause()
                    doorp.play()
                    t.sleep(4)
                    backgoundp.play()
                    goal()
                    break

                elif answer9.object == "right":
                    print("ok lets go right")
                    t.sleep(2)
                    print("#opens door")
                    backgoundp.pause()
                    doorp.play()
                    t.sleep(4)
                    backgoundp.play()
                    print("dead end, we have to go back")
                    r2()
                    break

                elif answer9.object == "back":

                    print("ok lets go back")
                    backgoundp.pause()
                    doorp.play()
                    t.sleep(4)
                    backgoundp.play()
                    r2()
                else:
                    print("did you learn to speak in proper words???, seems not like")
            break
        elif answer8.object == "right":
            print("ok lets go right")
            t.sleep(2)
            print("#opens door")
            backgoundp.pause()
            doorp.play()
            t.sleep(4)
            backgoundp.play()
            print("once again the same, \n\tleft \n\tright \n\tback")
            while True:

                in10 = input("> ")
                lexicon.lexicon(in10)
                answer10 = parser2.parse_sentence(lexicon.sentence)

                if answer10.object == "left":
                    print("ok lets take the left one")
                    t.sleep(2)
                    print("#opens door")
                    backgoundp.pause()
                    doorp.play()
                    t.sleep(4)
                    backgoundp.play()
                    print("dead end, we have to go back")
                    r2()
                    break

                elif answer10.object == "right":
                    print("ok lets go right")
                    t.sleep(2)
                    print("#opens door")
                    backgoundp.pause()
                    doorp.play()
                    t.sleep(4)
                    backgoundp.play()
                    print("dead end, we have to go back")
                    r2()
                    break

                elif answer10.object == "back":

                    print("ok lets go back")
                    backgoundp.pause()
                    doorp.play()
                    t.sleep(4)
                    backgoundp.play()
                    r2()
                else:
                    print("did you learn to speak in proper words???, seems not like")

            break
        elif answer8.object == "back":

            print("ok lets go back")
            backgoundp.pause()
            doorp.play()
            t.sleep(4)
            backgoundp.play()
            r1()
        else:
            print("did you learn to speak in proper words???, seems not like")


def goal():
    print("jeeeeeeeeeeeeeeeea there it is we found the treasure!!!, lets try get back to daylight")
    backgoundp.pause()
    winp.play()
    t.sleep(4)
    exit(0)


opening()
