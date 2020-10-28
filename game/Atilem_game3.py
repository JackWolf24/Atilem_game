import tkinter, random
import parser2, lexicon

main = tkinter.Tk()
path = ["start"]
backpack = []
items = ["rope", "life jacket", "sunglasses", "key", "antidote", "flashlight", "water", "apples",
         "raincoat", "cardgame"]
quips = ["well done", "great job bro.", "thats it.", "mission accomplished", "congrats"]


class room:
    def __init__(self, otxt, atxt, atxt2, atxt3, key, key2, key3, key4, ans, ans2, ans3, img, dir, startscreen, cheat):
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
        self.startscreen = startscreen
        self.cheat = cheat
        self.backpacksize = 3
        main.title("ATILEM-FORGOTTEN TREASURES")
        main.geometry("{0}x{1}+-8+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))
        main.configure(bg="#000000")


        if self.startscreen is False:
            self.l2 = tkinter.Label(main, text="enter answer here:", bg="#000000", fg="#FFFFFF", font=("Courier", 15))
            self.l2.place(x=main.winfo_screenwidth() / 10, y=main.winfo_screenheight() / 2 + 60, anchor="w")

            self.t1 = tkinter.Text(main, width=50, height=10, bg="#FFFFFF", fg="#000000")
            self.t1.place(x=main.winfo_screenwidth() / 10, y=main.winfo_screenheight() / 1.5 + 50, anchor="w")

            self.enter1 = tkinter.Button(main, text="enter", command=self.enter, font=("Courier", 10), activeforeground="#FFFFFF")
            self.enter1.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 10, anchor="w", width=80, height=78)

            self.enter2 = tkinter.Button(main, text="next", command=self.next, font=("Courier", 10), activeforeground="#FFFFFF")
            self.enter2.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 95, anchor="w", width=80, height=78)

            self.l4 = tkinter.Label(main, text=self.otxt, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
            self.l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

            img = tkinter.PhotoImage(file=self.img)
            self.l = tkinter.Label(main, image=img)
            self.l.place(x=main.winfo_screenwidth() / 2, y=1, anchor="n")
            self.l.image = img
            print("dir", self.dir)
            if "cheat" in scenes.get(path[len(path)-1]):
                main.bind("<Control_L>", self.next)
                main.bind("<Shift_L>", self.enter)

            if self.dir is "startroom":
                self.enter1.config(text="search", command=lambda: self.search("flashlight", "startroom"))

            elif self.dir is "r1":
                self.enter1.config(text="search", command=lambda: self.search("sunglasses", "r1"))

            elif self.dir is "rope":
                self.enter1.config(text="search", command=lambda: self.search("rope", "rope"))

            elif path[len(path)-1] == "victory" and "troom" in path or path[len(path)-1] == "death": #if you were in the treasure room and get back to first stage victory screen appear
                self.enter1.config(text="quit", command=self.end)
                self.enter2.config(text="restart", command= self.res)
        else:
            self.enter2 = tkinter.Button(main, text="start", command=lambda: self.next(self.backpacksize), font=("Courier", 10),
                                    activeforeground="#FFFFFF")
            self.enter2.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 95, anchor="w", width=80,
                         height=78)

            self.enter1 = tkinter.Button(main)

            img = tkinter.PhotoImage(file=self.img)
            self.l = tkinter.Label(main, image=img)
            self.l.place(x=main.winfo_screenwidth() / 2, y=1, anchor="n")
            self.l.image = img

            self.l4 = tkinter.Label(main)

    def enter(self, _event=None):
        try:
            lexicon.lexicon(self.t1.get("1.0", "end-1c"))
            print(lexicon.sentence)
            answer = parser2.parse_sentence(lexicon.sentence)

            if answer.object == self.key:
                self.l4.config(text=self.atxt)
                if self.ans:
                    self.dir = self.ans

            elif answer.object == self.key2:
                self.l4.config(text=self.atxt2)
                if path[len(path) - 1] is "troom":
                    if "fight" in path: self.dir = "potions"
                    elif "rope" in path: self.dir = "rope"

                elif self.ans2:
                    self.dir = self.ans2

            elif answer.object == self.key3:
                self.l4.config(text=self.atxt3)
                if self.ans3:
                    self.dir = self.ans3

            elif answer.object:
                if answer.object == "back":
                    if self.dir == "nofight" or self.dir is "prefight":
                        self.dir = "read"

                elif answer.object == "cheat" or answer.object == "loose":
                    for k in scenes.keys():
                        scenes.get(k)[len(scenes.get(k))-1] = "cheat"

                    self.cheat = True
                    if answer.object == "cheat":
                        backpack.extend(["sunglasses", "flashlight", "rope"])
                    else:
                        backpack.extend(["water", "flashlight", "apples"])

                    print("1", "cheat:", self.cheat,"backpack:", len(backpack), backpack)
                    self.l4.config(text=f"You cheated:{backpack}")
                    self.dir = "equip"


                else:
                    if answer.object not in backpack and len(backpack) <= self.backpacksize and answer.object in items:
                        backpack.append(answer.object)
                        print("append")
                        self.l4.config(text=f"great decision, you got:{backpack}")

                    elif answer.object in backpack and len(backpack) <= self.backpacksize:
                        self.l4.config(text="Its not sensible to carry the same thing around twice. choose another item.")

                    if "troom" not in path and len(backpack) == self.backpacksize:
                        self.l4.config(text=f"your backpack is full, so lets step in. You chose:{backpack}")
                        print(len(backpack), backpack, "0: full backpack")
                        self.dir = "gotlight"


        except TypeError:
            print("TypeError")
            txtelse = """did you learn to speak in proper words???,
                 seems not like"""
            self.l4.config(text=txtelse)


    def next(self, _event=None):
        print(self.dir)
        try:
            if len(backpack) != self.backpacksize and self.dir == "gotlight":  #sends you back to equip if your bckpack is not yet full
                self.dir = "equip"

            if self.dir == "death":
                pass
            else:
                self.l4.destroy()

            if self.dir is "opening" and "troom" in path: #if you was in the treasure room and get back to first stage victory screen appear
                self.dir = "victory"

            dict = scenes.get(self.dir)
            path.append(self.dir)
            print("path:", path)

        except:
            print("ERORRRR")    #if you type nothing the last scene loads
            dict = scenes.get(path[len(path)-1])

        room(dict[0], dict[1], dict[2], dict[3], dict[4], dict[5], dict[6], dict[7], dict[8], dict[9], dict[10], dict[11], dict[12], dict[13], dict[14])


    def search(self, ans2, ans3): #looks up your backpack for the desired item
        self.l4.destroy()
        self.l4 = tkinter.Label(main, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        self.l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")
        if ans2 in backpack:
            print("there", ans3, ans2)
            self.l4.config(text="peeeew, youre a genius. You took it with you")
            self.dir = ans3

        elif ans2 not in backpack:
            print("not there", ans3, ans2)
            if ans2 == "flashlight":
                backpack.clear()
                self.l4.config(text="maaan, you forgot it, we have to go retry")
                self.dir = "equip"

            elif ans2 == "rope":
                self.l4.config(text="you try to cross the pond without any help. you stagger, you fall, you get disolved")
                self.dir = "death"

            elif ans2 == "sunglasses":
                self.l4.config(text="youve forgott your sund glasses. Now youre set to stone")
                self.dir = "death"


    def end(self):
        main.destroy()


    def res(self):
        for k in scenes.keys(): scenes.get(k)[len(scenes.get(k)) - 1] = "honest"
        self.l4.destroy()
        backpack.clear()
        self.dir = "opening"
        self.next(3)
scenes = {
    "start": [None, None, None, None, None, None, None, None, "opening", None, None, "0.png", "opening", True, "honest"],
    "opening": ["Hey Im Gorge and Im your companion on this journey of trying to find the treasure of Atillem, an old society extincted several hundrets years ago.Today we prepare for the first atempt of finding the treasure in that scary cave over there. I heard of many brave man entering but close to non came back alive.", None, None, None, None, None, None, None, "askscare", None, None, "1.png", "askscare", False, "honest"],
    "askscare": ["Well didnt wanted to scare you, is all right? you look a little faint.\nyes \nnot at all","great, I knew you were one of the brave ones, thats something i feel in ma pee","Come on man, stop peeing your throusers. Only the one who tries is in position of having a chance to win", "ok, lets go back", "yes", "not", "back", None, "askready", "askscare", "opening", "1.png", None, False, "honest"],
    "askready": ["ready to rumble? \n yes \n not at all", "great, so lets prepare our equipment:","what are you waiting for?, well anyways only die harten kommen in den garten so lets go", None, "yes","not", "back", None, "equip", "askready", "opening", "1.png", None, False, "honest"],
    "equip": ["ok there are 10 Items you could take with you. But sadly our backpack is capeable of containing just 4 Items\n" + str(items), None, None, None, None, None, "back", None, "gotlight", None, "opening", "2.png", "gotlight", False, "honest"],
    "gotlight": ["Its pretty dark in here. could you please switch on your flashlight?", None, None, None, "back", None, None, None, "equip", "flashlight", "startroom", "3.png", "startroom", False, "honest"],
    "startroom": ["oh hey, the first room, 2 doors available, which one do choose? \nleft \nright","ok lets take the left one", "ok lets go right", "ok, lets go back", "left", "right", "back", None,"l1", "gotglasses", "equip", "4.png", None, False, "honest"],
    "l1": ["oh a new room, stairs and a door, hm but where to go? \nstairs \nportal", "ok lets go upstairs", "ok lets enter the portal", "ok, lets go back", "upstairs", "door", "back", None, "upstairs", "read", "startroom", "5.png", None, False, "honest"],
    "gotglasses": ["You see that snake over there? dont look in her eyes. If you do so youll freeze to stone. sunglases might protect you, got some?", None, None, None, "back", None, None, None, "startroom", None, None, "11.png", "r1", False, "honest"],
    "r1": ["well, now we can pass safely the snake \npass", "ok lets pass", "ok, lets go back", None, "pass", None, "back", None, "gotrope", None, "startroom", "11.2.png", None, False, "honest"],
    "gotrope": ["new room. oh we have to cross a pond full of acid to get to the next door. got your rope?", None, None, None, "back", None, None, None, "r1", None, None, "12.1.png", "rope", False, "honest"],
    "rope": ["ok lets spann the rope across the pond. then pass the door \npass",  "ok lets pass", "ok, lets go back", None, "pass", None, "back", None, "troom", None, "r1", "12.2.png", None, False, "honest"],
    "read": ["new room. I think this witch over there is too strong. oh a scroll, ill read it to you, ready? \n\tyes \n\tno ",  "ok ill start", "take ya time", "ok, lets go back", "yes", "no", "back", None, "potions", "read", "l1", "7.png", None, False, "honest"],
    "potions": ["remember the hint. \nyou could take the...: \n\t'red'\n\t'green'", "take the red one", "take the green one", None, "red", "green", "back", None, "prefight", "death", "l1", "7.1.png", None, False, "honest"],
    "upstairs": ["oh a scroll, ill read it to you, ready? \n\tyes \n\tno ", "ok ill start", "take ya time", "ok, lets go back", "yes", "no", "back", None, "upstairsread", "upstairs", "l1", "6.png", None, False, "honest"],
    "upstairsread": ["I suppose its a hint. Keep it in mind.", None, None, None, None, "back", None, None, None, "upstairs", None, "6.1.png", "read", False, "honest"],
    "troom": ["oh wow the treasure camber, take as much as you can. we have to bring it safely outside the cave to accomplish our mission\nback", None, "ok lets go back", None, None, "back", None, None, None, None, None, "8.png", None, False, "honest"],
    "prefight": ["greaaaaaaat you got the right one, now youre superstrong, punch her on the nose so we can pass \nfight\n'nofight'", "ok, be aware of her left hook!!", "oh no, a pazifist, now shell kill you", None, "fight", "nofight", None, "back", "fight", "death", "potions", "7.2.png", None, False, "honest"],
    "fight": ["nice one, now we can pass", None, None, None, None, None, None, "back", None, None, "prefight", "7.3.png", "troom", False, "honest"],
    "death": [None, None, None, None, None, None, None, None, None, None, None, "10.png", None, False, "honest"],
    "victory": [quips[random.randint(0, len(quips) - 1)], None, None, None, None, None, None, None, None, None, None, "9.png", None, False, "honest"],
}
dict = scenes.get("start")
room(dict[0], dict[1], dict[2], dict[3], dict[4], dict[5], dict[6], dict[7], dict[8], dict[9], dict[10], dict[11], dict[12], dict[13], dict[14])
main.mainloop()
