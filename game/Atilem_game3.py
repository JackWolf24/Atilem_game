import tkinter, random
import parser2, lexicon

main = tkinter.Tk()
backpacksize = 3
startscreen = True
cheat = False
accp = False
way = None
path = ["start"]
backpack = []
items = ["30m rope", "life jacket", "sunglasses", "key", "anti toxic potion", "flashlight", "5L of water", "3 apples",
         "raincoat", "game of cards"]


class room:
    def __init__(self, otxt, atxt, atxt2, atxt3, key, key2, key3, key4, ans, ans2, ans3, img, dir):
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
        self.dir = dir

        main.title("ATILEM-FORGOTTEN TREASURES")
        main.geometry("{0}x{1}+-8+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))
        main.configure(bg="#000000")

        global t1, enter2, l4, enter1, startscreen, way, accp
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
                main.bind("<Control_L>",self.next)
                main.bind("<Shift_L>", self.enter)


            if self.dir is "startroom":
                enter1.config(text="search", command=lambda: search("flashlight", "startroom"))

            elif self.dir is "r1":
                enter1.config(text="search", command=lambda: search("sunglasses", "r1"))

            elif self.dir is "rope":
                enter1.config(text="search", command=lambda: search("rope", "rope"))

            elif self.dir is "victory" or self.dir is "death":
                enter1.config(text="quit", command=end)
                enter2.config(text="restart", command= res)

            elif self.dir is "troom":
                print("5")
                accp = True
                if "fight" in path:
                    self.ans2 = "potions"
                elif "rope" in path:
                    self.ans2 = "rope"

        else:
            enter2 = tkinter.Button(main, text="start", command=self.next, font=("Courier", 10),
                                    activeforeground="#FFFFFF")
            enter2.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 95, anchor="w", width=80,
                         height=78)

            enter1 = tkinter.Button(main)

            img = tkinter.PhotoImage(file=self.img)
            l = tkinter.Label(main, image=img)
            l.place(x=main.winfo_screenwidth() / 2, y=1, anchor="n")
            l.image = img

            l4 = tkinter.Label(main)
            l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

    def enter(self, _event=None):
        global backpacksize, cheat
        try:
            lexicon.lexicon(t1.get("1.0", "end-1c"))
            print(lexicon.sentence)
            answer = parser2.parse_sentence(lexicon.sentence)
            global cheat, backpacksize, accp, way

            if answer.object == self.key:
                print("1", self.key)
                l4.config(text=self.atxt)
                if self.ans:
                    self.dir = self.ans

            elif answer.object == self.key2:
                print("2", self.key2)
                l4.config(text=self.atxt2)
                if self.ans2:
                    self.dir = self.ans2

            elif answer.object == self.key3:
                print("3", self.key3)
                l4.config(text=self.atxt3)
                if self.ans3:
                    self.dir = self.ans3



            elif answer.object:
                if answer.object == "back":
                    print("4 back")
                    if self.dir == "nofight" or self.dir is "prefight":
                        self.dir = "read"

                elif answer.object == "cheat":
                    cheat = True
                    backpack.extend(["sunglasses", "flashlight", "rope"])
                    print("1", "cheat:", cheat, len(backpack), backpack)
                    l4.destroy()
                    self.dir = "equip"


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
                        self.dir = "gotlight"

            else:
                print("else")
                txtelse = """did you learn to speak in proper words???,
                     seems not like"""
                l4.config(text=txtelse)


        except TypeError:
            print("TypeError")
            print(len(backpack), cheat)
            if len(backpack) == backpacksize:
                if cheat == True and self.dir is "equip":
                    l4.config(text=f"your backpack is full, so lets step in. You cheated:{backpack}")
                    print(len(backpack), backpack, "3: already full backpack")
                    self.dir = "gotlight"

            else:
                txtelse = """did you learn to speak in proper words???,
                     seems not like"""
                l4.config(text=txtelse)



    def next(self, _event=None):
        global l4, startscreen, accp
        l4.destroy()
        try:
            if self.dir is "opening":
                print("0")
                startscreen = False
                if accp is True:
                    self.dir = "victory"

            dict = scenes.get(self.dir)
            room(dict[0], dict[1], dict[2], dict[3], dict[4], dict[5], dict[6], dict[7], dict[8], dict[9], dict[10], dict[11], dict[12])

            path.append(self.dir)
            print("path:", path)

        except:
            print("ERORRRR")
            self.dir = path[len(path)-1]
            dict = scenes.get(self.dir)
            room(dict[0], dict[1], dict[2], dict[3], dict[4], dict[5], dict[6], dict[7], dict[8], dict[9], dict[10], dict[11], dict[12])
def search(ans2, ans3):
    global l4
    if ans2 in backpack:
        l4.destroy()
        print("da", ans3, ans2)
        l4 = tkinter.Label(main, text="peeeew, youre a genius. You took it with you", bg="#000000", fg="#FFFFFF",
                           font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")
        room.dir = ans3

    elif ans2 not in backpack:
        l4.destroy()
        print("nix da", ans3, ans2)
        l4 = tkinter.Label(main, text="maaan, you forgot it, we have to go retry", bg="#000000", fg="#FFFFFF",
                           font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        if ans2 == "flashlight":
            backpack.clear()
            room.dir = "equip"

        elif ans2 == "rope":
            l4.config(text="you got disolved")
            room.dir = "death"

        elif ans2 == "sunglasses":
            l4.config(text="youre set to stone")
            room.dir = "death"


def end():
    main.destroy()


def res():
    l4.destroy()
    backpack.clear()
    path.clear()
    startscreen = True
    cheat = False
    accp = False
    room.dir = "opening"
    return startscreen, cheat, accp

scenes = {
    "start": [None, None, None, None, None, None, None, None, "opening", None, None, "0.png", "opening"],
    "opening": ["Hey Im Gorge and Im your companion on this journey of trying to find the treasure of Atillem, an old society extincted several hundrets years ago.Today we prepare for the first atempt of finding the treasure in that scary cave over there. I heard of many brave man entering but close to non came back alive.", None, None, None, None, None, None, None, "askscare", None, None, "1.png", "askscare"],
    "askscare": ["Well didnt wanted to scare you, is all right? you look a little faint.\nyes \nnot at all","great, I knew you were one of the brave ones, thats something i feel in ma pee","Come on man, stop peeing your throusers. Only the one who tries is in position of having a chance to win", "ok, lets go back", "yes", "not", "back", None, "askready", "askscare", "opening", "1.png", None],
    "askready": ["ready to rumble? \n yes \n not at all", "great, so lets prepare our equipment:","what are you waiting for?, well anyways only die harten kommen in den garten so lets go", None, "yes","not", "back", None, "equip", "askready", "opening", "1.png", None],
    "equip": ["ok there are 10 Items you could take with you. But sadly our backpack is capeable of containing just 4 Items\n" + str(items), None, None, None, None, None, "back", None, "gotlight", None, "opening", "2.png", "gotlight"],
    "gotlight": ["Its pretty dark in here. could you please switch on your flashlight?", None, None, None, "back", None, None, None, "equip", "flashlight", "startroom", "3.png", "startroom"],
    "startroom": ["oh hey, the first room, 2 doors available, which one do choose? \nleft \nright","ok lets take the left one", "ok lets go right", "ok, lets go back", "left", "right", "back", None,"l1", "gotglasses", "equip", "4.png", None],
    "l1": ["oh a new room, stairs and a door, hm but where to go? \nstairs \nportal", "ok lets go upstairs", "ok lets enter the portal", "ok, lets go back", "upstairs", "door", "back", None, "upstairs", "read", "startroom", "5.png", None],
    "gotglasses": ["You see that snake over there? dont look in her eyes. If you do so youll freeze to stone. sunglases might protect you, got some?", None, None, None, "back", None, None, None, "startroom", None, None, "11.png", "r1"],
    "r1": ["well, now we can pass safely the snake \npass", "ok lets pass", "ok, lets go back", None, "pass", None, "back", None, "gotrope", None, "startroom", "11.2.png", None],
    "gotrope": ["new room. oh we have to cross a pond full of acid to get to the next door. got your rope?", None, None, None, "back", None, None, None, "r1", None, None, "12.1.png", "rope"],
    "rope": ["ok lets spann the rope across the pond. then pass the door \npass",  "ok lets pass", "ok, lets go back", None, "pass", None, "back", None, "troom", None, "r1", "12.2.png", None],
    "read": ["new room. I think this witch over there is too strong. oh a scroll, ill read it to you, ready? \n\tyes \n\tno ",  "ok ill start", "take ya time", "ok, lets go back", "yes", "no", "back", None, "potions", "read", "l1", "7.png", None],
    "potions": ["remember the hint. \nyou could take the...: \n\t'red'\n\t'green'", "take the red one", "take the green one", None, "red", "green", "back", None, "prefight", "death", "l1", "7.1.png", None],
    "upstairs": ["oh a scroll, ill read it to you, ready? \n\tyes \n\tno ", "ok ill start", "take ya time", "ok, lets go back", "yes", "no", "back", None, "upstairsread", "upstairs", "l1", "6.png", None],
    "upstairsread": ["I suppose its a hint. Keep it in mind.", None, None, None, None, "back", None, None, None, "upstairs", None, "6.1.png", "read"],
    "troom": ["oh wow the treasure camber, take as much as you can. we have to bring it safely outside the cave to accomplish our mission\nback", None, "ok lets go back", None, None, "back", None, None, None, None, None, "8.png", None],
    "prefight": ["greaaaaaaat you got the right one, now youre superstrong, punch her on the nose so we can pass \nfight\n'nofight'", "ok, be aware of her left hook!!", "oh no, a pazifist, now shell kill you", None, "fight", "nofight", None, "back", "fight", "death", "potions", "7.2.png", None],
    "fight": ["nice one, now we can pass", None, None, None, None, None, None, "back", None, None, "prefight", "7.3.png", "troom"],
    "death": [None, None, None, None, None, None, None, None, None, None, None, "10.png", None],
    "victory": [random.randint(0, len(["well done", "great job bro.", "thats it.", "mission accomplished", "congrats"]) - 1), None, None, None, None, None, None, None, None, None, None, "9.png", None],
}
dict = scenes.get("start")
room(dict[0], dict[1], dict[2], dict[3], dict[4], dict[5], dict[6], dict[7], dict[8], dict[9], dict[10], dict[11], dict[12])
main.mainloop()
