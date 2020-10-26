import tkinter, random
import parser2, lexicon

main = tkinter.Tk()
backpacksize = 3
startscreen = True
cheat = False
accp = False
way = None
nxt = "opening"
backpack = []
items = ["30m rope", "life jacket", "sunglasses", "key", "anti toxic potion", "flashlight", "5L of water", "3 apples",
         "raincoat", "game of cards"]


class room:
    def __init__(self, otxt, atxt, atxt2, atxt3, key, key2, key3, key4, ans, ans2, ans3, img):
        self.otxt = otxt
        self.atxt = atxt
        self.atxt2 = atxt2
        self.atxt3 = atxt3
        self.key = key
        self.key2 = key2
        self.key3 = key3
        self.key4 = key4
        self.ans = ans
        self.ans2 = ans2
        self.ans3 = ans3
        self.img = img

        main.title("ATILEM-FORGOTTEN TREASURES")
        main.geometry("{0}x{1}+-8+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))
        main.configure(bg="#000000")

        global t1, enter2, l4, enter1
        if startscreen is False:
            l2 = tkinter.Label(main, text="enter answer here:", bg="#000000", fg="#FFFFFF", font=("Courier", 15))
            l2.place(x=main.winfo_screenwidth() / 10, y=main.winfo_screenheight() / 2 + 60, anchor="w")

            t1 = tkinter.Text(main, width=50, height=10, bg="#FFFFFF", fg="#000000")
            t1.place(x=main.winfo_screenwidth() / 10, y=main.winfo_screenheight() / 1.5 + 50, anchor="w")

            enter1 = tkinter.Button(main, text="enter", command=self.enter, font=("Courier", 10),
                                    activeforeground="#FFFFFF")
            enter1.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 10, anchor="w", width=80,
                         height=78)

            enter2 = tkinter.Button(main, text="next", command=self.next, font=("Courier", 10),
                                    activeforeground="#FFFFFF")
            enter2.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 95, anchor="w", width=80,
                         height=78)

            l4 = tkinter.Label(main, text=self.otxt, bg="#000000", fg="#FFFFFF",
                               font=("Courier", 15), wraplength=650)
            l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

            img = tkinter.PhotoImage(file=self.img)
            l = tkinter.Label(main, image=img)
            l.place(x=main.winfo_screenwidth() / 2, y=1, anchor="n")
            l.image = img

            if cheat is True:
                print("enter2: ", enter2["state"], "enter1: ", enter1["state"])
                main.bind("<Control_L>", self.next)
                main.bind("<Shift_L>", self.enter)

        else:
            enter2 = tkinter.Button(main, text="start", command=self.next, font=("Courier", 10),
                                    activeforeground="#FFFFFF")
            enter2.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 95, anchor="w", width=80,
                         height=78)

            img = tkinter.PhotoImage(file=self.img)
            l = tkinter.Label(main, image=img)
            l.place(x=main.winfo_screenwidth() / 2, y=1, anchor="n")
            l.image = img

            l4 = tkinter.Label(main)
            l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

    def enter(self, _event=None):
        print("enter")
        global backpacksize, cheat, nxt
        try:
            lexicon.lexicon(t1.get("1.0", "end-1c"))
            print(lexicon.sentence)
            answer = parser2.parse_sentence(lexicon.sentence)
            global nxt, cheat, backpacksize, accp, way

            if answer.object == self.key:
                print("1", self.key)
                l4.config(text=self.atxt)
                if self.ans:
                    nxt = self.ans

            elif answer.object == self.key2:
                print("2", self.key2)
                l4.config(text=self.atxt2)
                if self.ans2:
                    nxt = self.ans2

            elif answer.object == self.key3:

                print("3", self.key3)
                l4.config(text=self.atxt3)
                if self.ans3:
                    nxt = self.ans3



            elif answer.object:
                # print(answer.object)
                if answer.object == "back":
                    print("4 back")

                    if nxt == "nofight" or nxt is "prefight":
                        nxt = "read"

                    elif accp is False:
                        print("1")
                        nxt = "opening"

                    else:
                        nxt = "victory"

                elif answer.object == "cheat":
                    cheat = True
                    backpack.extend(["sunglasses", "flashlight", "rope"])
                    print("1", "cheat:", cheat, len(backpack), backpack)
                    l4.destroy()
                    nxt = "equip"
                    equip()

                else:
                    if answer.object not in backpack and len(backpack) <= backpacksize:
                        backpack.append(answer.object)
                        print("append")
                        l4.config(text=f"great decision, you got:{backpack}")

                    elif answer.object in backpack and len(backpack) <= backpacksize:
                        l4.config(text="Its not sensible to carry the same thing around twice. choose another item.")

                    if accp == False and len(backpack) == backpacksize:
                        l4.config(text=f"your backpack is full, so lets step in. You chose:{backpack}")
                        print(len(backpack), backpack, "0: full backpack")
                        nxt = "gotlight"

            else:
                print("else")
                txtelse = """did you learn to speak in proper words???,
                     seems not like"""
                l4.config(text=txtelse)


        except TypeError:
            print("TypeError")
            print(len(backpack), nxt, cheat)
            if len(backpack) == backpacksize:
                if cheat == True and nxt is "equip":
                    l4.config(text=f"your backpack is full, so lets step in. You cheated:{backpack}")
                    print(len(backpack), backpack, "3: already full backpack")
                    nxt = "gotlight"

            else:
                txtelse = """did you learn to speak in proper words???,
                     seems not like"""
                l4.config(text=txtelse)
                print("nxt:", nxt)
                print("switch8")

    def next(self, _event=None):

        global l4
        l4.destroy()
        print("l4.destroy()")
        print("nxt:", nxt)
        var = scenes.get(nxt)
        var()


def search(ans2, ans3):
    global nxt, l4

    if ans2 is None:
        nxt = ans3
    elif ans2 in backpack:
        l4.destroy()
        print("da", nxt, ans3, ans2)
        l4 = tkinter.Label(main, text="peeeew, youre a genius. You took it with you", bg="#000000", fg="#FFFFFF",
                           font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")
        nxt = ans3

    elif ans2 not in backpack:
        l4.destroy()
        print("nix da", nxt, ans3, ans2)
        l4 = tkinter.Label(main, text="maaan, you forgot it, we have to go retry", bg="#000000", fg="#FFFFFF",
                           font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        if ans2 == "flashlight":
            backpack.clear()
            nxt = "equip"

        elif ans2 == "rope":
            l4.config(text="you got disolved")
            death()

        elif ans2 == "sunglasses":
            l4.config(text="youre set to stone")
            death()


def start():
    global nxt
    room(None, None, None, None, None, None, None, None, "opening", None, None, "0.png")
    nxt = "opening"


def opening():
    global startscreen, nxt
    startscreen = False

    if accp is True:
        victory()
    else:
        otxt = "Hey Im Gorge and Im your companion on this journey of trying to find the treasure of Atillem, an old society extincted several hundrets years ago.Today we prepare for the first atempt of finding the treasure in that scary cave over there. I heard of many brave man entering but close to non came back alive."
        room(otxt, None, None, None, None, None, None, None, "askscare", None, None, "1.png")
        nxt = "askscare"


def askscare():
    otxt = """Well didnt wanted to scare you, is all right? you look a little faint.

                yes 
                not at all
                """
    atxt = "great, I knew you were one of the brave ones, thats something i feel in ma pee"
    atxt2 = """Come on man, stop peeing your throusers. Only the one who tries is in position of having a chance to win"""
    atxt3 = "ok, lets go back"
    room(otxt, atxt, atxt2, atxt3, "yes", "not", "back", None, "askready", "askscare", "opening", "1.png")


def askready():
    otxt = "ready to rumble? \n yes \n not at all"
    atxt = "great, so lets prepare our equipment:"
    atxt2 = "what are you waiting for?, well anyways only die harten kommen in den garten so lets go"
    room(otxt, atxt, atxt2, None, "yes", "not", "back", None, "equip", "askready", "opening", "1.png")


def equip():
    otxt = "ok there are 10 Items you could take with you. But sadly our backpack is capeable of containing just 4 Items\n" + str(
        items)
    room(otxt, None, None, None, None, None, "back", None, "gotlight", None, "opening", "2.png")


def gotlight():
    otxt = "Its pretty dark in here. could you please switch on your flashlight?"
    room(otxt, None, None, None, "back", None, None, None, "equip", "flashlight", "startroom", "3.png")
    enter1.config(text="search", command=lambda: search("flashlight", "startroom"))


############################################################################################################
def startroom():
    otxt = "oh hey, the first room, 2 doors available, which one do choose? \nleft \nright"
    atxt = "ok lets take the left one"
    atxt2 = "ok lets go right"
    atxt3 = "ok, lets go back"
    room(otxt, atxt, atxt2, atxt3, "left", "right", "back", None, "l1", "gotglasses", "equip", "4.png")


############################################################################################################

def gotglasses():
    otxt = "You see that snake over there? dont look in her eyes. If you do so youll freeze to stone. sunglases might protect you, got some?"
    room(otxt, None, None, None, "back", None, None, None, "startroom", None, None, "11.png")
    enter1.config(text="search", command=lambda: search("sunglasses", "r1"))


def r1():
    otxt = "well, now we can pass safely the snake \npass"
    atxt = "ok lets pass"
    atxt2 = "ok, lets go back"
    room(otxt, atxt, atxt2, None, "pass", None, "back", None, "gotrope", None, "startroom", "11.2.png")


############################################################################################################
def gotrope():
    otxt = "new room. oh we have to cross a pond full of acid to get to the next door. got your rope?"
    room(otxt, None, None, None, "back", None, None, None, "r1", None, None, "12.1.png")
    enter1.config(text="search", command=lambda: search("rope", "rope"))


def rope():
    otxt = "ok lets spann the rope across the pond. then pass the door \npass"
    atxt = "ok lets pass"
    otxt2 = "ok, lets go back"
    room(otxt, atxt, otxt2, None, "pass", None, "back", None, "troom", None, "r1", "12.2.png")


############################################################################################################

def l1():
    global way
    way = "l"
    otxt = "oh a new room, stairs and a door, hm but where to go? \nstairs \nportal"
    atxt = "ok lets go upstairs"
    atxt2 = "ok lets enter the portal"
    atxt3 = "ok, lets go back"
    room(otxt, atxt, atxt2, atxt3, "upstairs", "door", "back", None, "upstairs", "read", "startroom", "5.png")


############################################################################################################

def upstairs():
    otxt = "oh a scroll, ill read it to you, ready? \n\tyes \n\tno "
    atxt = "ok ill start"
    atxt2 = "take ya time"
    atxt3 = "ok, lets go back"
    room(otxt, atxt, atxt2, atxt3, "yes", "no", "back", None, "upstairsread", "upstairs", "l1", "6.png")


def read():
    otxt = "new room. I think this witch over there is too strong. oh a scroll, ill read it to you, ready? \n\tyes \n\tno "
    atxt = "ok ill start"
    atxt2 = "take ya time"
    atxt3 = "ok, lets go back"
    room(otxt, atxt, atxt2, atxt3, "yes", "no", "back", None, "potions", "read", "l1", "7.png")


def upstairsread():
    global nxt
    otxt = "I suppose its a hint. Keep it in mind."
    room(otxt, None, None, None, None, "back", None, None, None, "upstairs", None, "6.1.png")
    nxt = "read"


############################################################################################################

def potions():
    otxt = "remember the hint. \nyou could take the...: \n\t'red'\n\t'green'"
    atxt = "take the red one"
    atxt2 = "take the green one"
    room(otxt, atxt, atxt2, None, "red", "green", "back", None, "prefight", "death", "l1", "7.1.png")


def prefight():
    otxt = "greaaaaaaat you got the right one, now youre superstrong, punch her on the nose so we can pass \nfight\n'nofight'"
    atxt = "ok, be aware of her left hook!!"
    atxt2 = "oh no, a pazifist, now shell kill you"
    room(otxt, atxt, atxt2, None, "fight", "nofight", None, "back", "fight", "death", "potions", "7.2.png")


def fight():
    global nxt
    otxt = "nice one, now we can pass"
    room(otxt, None, None, None, None, None, None, "back", None, None, "prefight", "7.3.png")
    nxt = "troom"


############################################################################################################

def troom():
    global way, accp, nxt
    otxt = "oh wow the treasure camber, take as much as you can. we have to bring it safely outside the cave to accomplish our mission\nback"
    accp = True
    if way == "l":
        ans2 = "potions"
    else:
        ans2 = "rope"

    room(otxt, None, None, None, None, "back", None, None, None, ans2, None, "8.png")
    print("accp:", accp)


############################################################################################################

def victory():
    quips = ["well done",
             "great job bro.",
             "thats it.",
             "mission accomplished",
             "congrats"]

    room(quips[random.randint(0, len(quips) - 1)], None, None, None, None, None, None, None, None, None, None, "9.png")
    enter1.config(text="quit", command=end)
    enter2.config(text="restart", command=res)


def death():
    room(None, None, None, None, None, None, None, None, None, None, None, "10.png")

    enter1.config(text="quit", command=end)
    enter2.config(text="restart", command=res)


def end():
    main.destroy()


def res():
    global nxt, way, accp, cheat, startscreen
    l4.destroy()
    backpack.clear()
    startscreen = True
    cheat = False
    accp = False
    way = None
    opening()


############################################################################################################

scenes = {
    "start": [None, None, None, None, None, None, None, None, "opening", None, None, "0.png"],
    "opening": opening,
    "askscare": askscare,
    "askready": askready,
    "equip": equip,
    "gotlight": gotlight,
    "startroom": startroom,
    "l1": l1,
    "gotglasses": gotglasses,
    "r1": r1,
    "gotrope": gotrope,
    "rope": rope,
    "read": read,
    "potions": potions,
    "upstairs": upstairs,
    "upstairsread": upstairsread,
    "troom": troom,
    "prefight": prefight,
    "fight": fight,
    "death": death,
    # "victory": victory(),
}
start()
main.mainloop()
