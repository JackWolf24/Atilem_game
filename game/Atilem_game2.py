import tkinter, random, playsound
import lexicon, parser2

main = tkinter.Tk()

backpacksize = 3
openvar = True
startscreen = True
cheat = False
accp = False
way = None

items = ["30m rope", "life jacket", "sunglasses", "key", "anti toxic potion", "flashlight", "5L of water", "3 apples",
         "raincoat", "game of cards"]
backpack = []


class template:
    def __init__(self, atxt1, atxt2, atxt3, atxt4, key, key2, key3, key4, ans, ans2, ans3):

        self.txt2 = atxt1
        self.txt3 = atxt2
        self.txt4 = atxt3
        self.txt5 = atxt4
        self.key = key
        self.key2 = key2
        self.key3 = key3
        self.key4 = key4
        self.ans = ans
        self.ans2 = ans2
        self.ans3 = ans3

        global l, l2, t1, enter1, enter2, cheat

        main.title("ATILEM-FORGOTTEN TREASURES")
        main.geometry("{0}x{1}+-8+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))
        main.configure(bg="#000000")

        if startscreen is False:
            l2 = tkinter.Label(main, text="enter answer here:", bg="#000000", fg="#FFFFFF", font=("Courier", 15))
            l2.place(x=main.winfo_screenwidth() / 10, y=main.winfo_screenheight() / 2 + 60, anchor="w")

            t1 = tkinter.Text(main, width=50, height=10, bg="#FFFFFF", fg="#000000")
            t1.place(x=main.winfo_screenwidth() / 10, y=main.winfo_screenheight() / 1.5 + 50, anchor="w")

            enter1 = tkinter.Button(main, text="enter", command=self.enter, font=("Courier", 10),
                                    activeforeground="#FFFFFF")
            enter1.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 10, anchor="w", width=80,
                         height=78)
            enter2.config(text="next")

            l = tkinter.Label(main)
            l.place(x=main.winfo_screenwidth() / 2, y=1, anchor="n")

            if not openvar and cheat is False:
                switchButtonState1(enter2)
                print("switch0")

            elif cheat is True:
                print("enter2: ", enter2["state"], "enter1: ", enter1["state"])
                main.bind("<Control_L>", self.next)
                main.bind("<Shift_L>", self.enter)

        else:
            enter2 = tkinter.Button(main, text="start", command=self.next, font=("Courier", 10),
                                    activeforeground="#FFFFFF")
            enter2.place(x=main.winfo_screenwidth() / 2.4, y=main.winfo_screenheight() / 1.5 + 95, anchor="w", width=80,
                         height=78)
            l = tkinter.Label(main)
            l.place(x=main.winfo_screenwidth() / 2, y=1, anchor="n")

    def enter(self, _event=None):
        print("enter")
        global backpacksize, cheat, nxt
        try:
            lexicon.lexicon(t1.get("1.0", "end-1c"))
            print(lexicon.sentence)
            answer = parser2.parse_sentence(lexicon.sentence)
            global nxt, cheat, backpacksize, accp, way

            if not cheat:
                print("switch1")
                switchButtonState1(enter2)

            if answer.object == self.key:
                print("1", self.key)
                l4.config(text=self.txt2)
                if way == "R":
                    print("switch3")
                    switchButtonState1(enter2)
                if nxt == "upstaitsread":
                    print("switch 2.5")
                    switchButtonState1(enter2)
                if self.ans:
                    nxt = self.ans

            elif answer.object == self.key2:
                print("2", self.key2)
                l4.config(text=self.txt3)
                if self.ans2:
                    nxt = self.ans2

            elif answer.object == self.key3:

                print("3", self.key3)
                l4.config(text=self.txt4)
                if self.ans3:
                    nxt = self.ans3



            elif answer.object:
                # print(answer.object)
                if answer.object == "back":
                    print("4 back")

                    if nxt == "nofight" or nxt is "prefight":
                        print("switch: nofight")
                        switchButtonState1(enter2)
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

                else:
                    if answer.object not in backpack:
                        backpack.append(answer.object)
                        l4.config(text=f"great decision, you got:{backpack}")

                    else:
                        l4.config(text="Its not sensible to carry the same thing around twice. choose another item.")
                        print("switch4")
                        if enter2["state"] == "disabled":
                            switchButtonState1(enter2)
            else:
                print("else")
                txtelse = """did you learn to speak in proper words???,
                     seems not like"""
                l4.config(text=txtelse)
                print("switch5")
                switchButtonState1(enter2)

            if len(backpack) == backpacksize:
                print("Backpack full")
                if cheat == True and nxt is "equip":
                    l4.config(text=f"your backpack is full, so lets step in. You chose:{backpack}")
                    print(len(backpack), backpack, "3: already full backpack")
                    nxt = "gotlight"

                elif cheat is False and nxt is "equip":
                    nxt = "gotlight"

                if nxt is not "equip":
                    print("pass 1")
                    pass

                elif accp is False:
                    if cheat:
                        pass
                    else:
                        if enter2["state"] == "disabled":
                            print("switch7")
                            switchButtonState1(enter2)

                            l4.config(text=f"your backpack is full, so lets step in. You chose:{backpack}")
                            print(len(backpack), backpack, "1: already full backpack")
                            nxt = "gotlight"

                else:
                    l4.config(text="your backpack is already full")
                    print(len(backpack), backpack, "2: allready full backpack")
                    nxt = "opening"

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
                switchButtonState1(enter2)

    def next(self, _event=None):
        try:
            l4.destroy()
        except:
            pass
        print("nxt:", nxt)
        b_map = Map(nxt)
        b_game = engine(b_map)
        b_game.play()

    def search(self, ans2, ans3):

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
            backpack.clear()
            nxt = "equip"


class switchButtonState1:
    def __init__(self, buttonname):
        self.buttoname = buttonname

        if (buttonname['state'] == "normal"):
            buttonname['state'] = "disable"
        else:
            buttonname['state'] = "normal"


class engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        if current_scene == last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class victory:
    def enter(self):
        quips = ["well done",
                 "great job bro.",
                 "thats it.",
                 "mission accomplished",
                 "congrats"]

        img = tkinter.PhotoImage(file="9.png")
        l.configure(image=img)
        l.image = img
        l4 = tkinter.Label(main, text=quips[random.randint(0, len(quips) - 1)], bg="#000000", fg="#FFFFFF",
                           font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        print("switch9")
        switchButtonState1(enter2)

        enter1.config(text="quit", command=self.end)
        enter2.config(text="restart", command=self.res)

    def end(self):
        main.destroy()

    def res(self):
        global nxt, accp
        nxt = "opening"
        accp = False
        print("switch res")
        switchButtonState1(enter2)
        l4.destroy()
        backpack.clear()
        b_map = Map(nxt)
        b_game = engine(b_map)
        b_game.play()


class death:
    def enter(self):
        quips = ["you died",
                 "great job bro.",
                 "thats it.",
                 "game over"]

        img = tkinter.PhotoImage(file="10.png")
        l.configure(image=img)
        l.image = img
        l4 = tkinter.Label(main, text=quips[random.randint(0, len(quips) - 1)], bg="#000000", fg="#FFFFFF",
                           font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        enter1.config(text="quit", command=self.end)
        enter2.config(text="restart", command=self.res)

    def end(self):
        main.destroy()

    def res(self):
        global nxt
        nxt = "opening"

        l4.destroy()
        backpack.clear()
        b_map = Map(nxt)
        b_game = engine(b_map)
        b_game.play()


class start:

    def enter(self):
        global l, nxt
        playsound.playsound(r"C:\Users\maurice.jarck\Documents\Projects\Atilem\tests\Resistance - AShamaluevMusic.mp3",
                            False)

        img = tkinter.PhotoImage(file="0.png")
        l.config(image=img)
        l.image = img
        template(None, None, None, None, None, None, None, None, None, None, None)

        nxt = "opening"


class opening:

    def enter(self):
        global nxt, l4, startscreen
        startscreen = False
        print("startscreen:", startscreen)
        try:
            if accp == True:
                nxt = "victory"

            else:
                otxt = "Hey Im Gorge and Im your companion on this journey of trying to find the treasure of Atillem, an old society extincted several hundrets years ago.Today we prepare for the first atempt of finding the treasure in that scary cave over there. I heard of many brave man entering but close to non came back alive."

                img = tkinter.PhotoImage(file="1.png")
                l.config(image=img)
                l.image = img

                l4 = tkinter.Label(main, text=otxt, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
                l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

                template(otxt, None, None, None, None, None, None, None, None, None, None)
                nxt = "askscare"
                if not way:
                    print("switch10")
                    switchButtonState1(enter1)
        except NameError:

            otxt = "Hey Im Gorge and Im your companion on this journey of trying to find the treasure of Atillem, an old society extincted several hundrets years ago.Today we prepare for the first atempt of finding the treasure in that scary cave over there. I heard of many brave man entering but close to non came back alive."

            img = tkinter.PhotoImage(file="1.png")
            l.config(image=img)
            l.image = img

            l4 = tkinter.Label(main, text=otxt, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
            l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

            template(otxt, None, None, None, None, None, None, None, None, None, None)
            nxt = "askscare"

            print("switch11")
            switchButtonState1(enter1)


class askscare:

    def enter(self):
        global nxt, l, l4, openvar, cheat, startscreen
        print("startscreen", startscreen)
        if cheat == False:
            openvar = False

        txt11 = """Well didnt wanted to scare you, is all right? you look a little faint.
    
            yes 
            not at all
            """
        txt12 = "great, I knew you were one of the brave ones, thats something i feel in ma pee"
        txt13 = """Come on man, stop peeing your throusers. Only the one who tries is in position of having a chance to win"""
        key11 = "yes"
        key12 = "not"
        key13 = "back"
        ans3 = "opening"

        img = tkinter.PhotoImage(file="1.png")
        l.config(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt11, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")
        print("switch12")
        switchButtonState1(enter1)

        template(txt12, txt13, None, None, key11, key12, key13, None, None, None, ans3)
        nxt = "askready"


class askready:

    def enter(self):
        global nxt, l4

        txt21 = "ready to rumble? \n yes \n not at all"
        txt22 = "great, so lets prepare our equipment:"
        txt23 = "what are you waiting for?, well anyways only die harten kommen in den garten so lets go"
        key21 = "yes"
        key22 = "not"
        key23 = "back"
        ans = "askscare"

        img = tkinter.PhotoImage(file="1.png")
        l.configure(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt21, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt22, txt23, None, None, key21, key22, key23, None, None, None, ans)
        nxt = "equip"


class equip():

    def enter(self):
        global openvar, l4, cheat, nxt

        if cheat == True:
            openvar = False
            # print("switch13")
            # switchButtonState1(enter2)

        txt31 = "ok there are 10 Items you could take with you. But sadly our backpack is capeable of containing just 4 Items\n" + str(
            items)
        txt32 = items
        key34 = items
        ans = "opening"

        img = tkinter.PhotoImage(file="2.png")
        l.configure(image=img)
        l.image = img

        global l4
        l4 = tkinter.Label(main, text=txt31, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt31, txt32, None, None, None, None, None, key34, ans, None, None)


class gotlight(template):

    def __init__(self):
        template.__init__(self, None, None, None, None, None, None, None, None, None, None, None)

    def enter(self):
        global l4, openvar, cheat, nxt
        if cheat == False:
            openvar = True
        else:
            nxt = "startroom"

        txt41 = "Its pretty dark in here. could you please switch on your flashlight?"
        ans2 = "flashlight"
        ans3 = "startroom"
        ans = "equip"
        key = "back"
        template(None, None, None, None, key, None, None, None, ans, ans2, ans3)
        img = tkinter.PhotoImage(file="3.png")
        l.configure(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt41, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        enter1.config(text="search", command=lambda: template.search(self, ans2, ans3))


class startroom:

    def enter(self):
        global l4, openvar, cheat
        if cheat == False:
            openvar = False

        enter1.config(text="enter", command=template.enter)

        txt42 = "oh hey, the first room, 2 doors available, which one do choose? \nleft \nright"
        txt43 = "ok lets take the left one"
        txt44 = "ok lets go right"
        txt45 = "ok, lets go back"
        key41 = "left"
        key42 = "right"
        key43 = "back"
        ans = "l1"
        ans2 = "gotglasses"
        ans3 = "equip"

        img = tkinter.PhotoImage(file="4.png")
        l.configure(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt42, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt43, txt44, txt45, None, key41, key42, key43, None, ans, ans2, ans3)


class gotglasses(template):

    def __init__(self):
        template.__init__(self, None, None, None, None, None, None, None, None, None, None, None)

    def enter(self):
        global openvar, l4, cheat, nxt
        if cheat == False:
            openvar = True
        else:
            nxt = "r1"
        txt41 = "You see that snake over there? dont look in her eyes. If you do so youll freeze to stone. sunglases might protect you, got some?"
        ans2 = "sunglasses"
        ans3 = "r1"
        ans = "startroom"
        key = "back"
        template(None, None, None, None, key, None, None, None, ans, None, None)
        img = tkinter.PhotoImage(file="11.png")
        l.configure(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt41, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        enter1.config(text="search", command=lambda: template.search(self, ans2, ans3))


class r1:

    def enter(self):
        global l4, way, openvar, cheat
        if cheat == False:
            openvar = False

        way = "r"

        enter1.config(text="enter", command=template.enter)

        txt42 = "well, now we can pass safely the snake \npass"
        txt43 = "ok lets pass"
        txt45 = "ok, lets go back"
        key41 = "pass"
        key43 = "back"
        ans = "gotrope"
        ans3 = "startroom"

        img = tkinter.PhotoImage(file="11.2.png")
        l.configure(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt42, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt43, None, txt45, None, key41, None, key43, None, ans, None, ans3)


class gotrope(template):

    def __init__(self):
        template.__init__(self, None, None, None, None, None, None, None, None, None, None, None)

    def enter(self):
        global l4, openvar, cheat, nxt
        if cheat == False:
            openvar = True
        else:
            nxt = "rope"

        txt41 = "new room. oh we have to cross a pond full of acid to get to the next door. got your rope?"
        ans = "r1"
        ans2 = "rope"
        ans3 = "rope"
        key = "back"
        template(None, None, None, None, key, None, None, None, ans, None, None)
        img = tkinter.PhotoImage(file="12.1.png")
        l.configure(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt41, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        enter1.config(text="search", command=lambda: template.search(self, ans2, ans3))


class rope:

    def enter(self):
        global l4, openvar, cheat
        if cheat == False:
            openvar = False

        enter1.config(text="enter", command=template.enter)

        txt42 = "ok lets spann the rope across the pond. then pass the door \npass"
        txt43 = "ok lets pass"
        txt45 = "ok, lets go back"
        key41 = "pass"
        key43 = "back"
        ans = "troom"
        ans3 = "r1"

        img = tkinter.PhotoImage(file="12.2.png")
        l.configure(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt42, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt43, None, txt45, None, key41, None, key43, None, ans, None, ans3)


class l1:
    def enter(self):
        global l4, way
        way = "l"
        txt52 = "oh a new room, stairs and a door, hm but where to go? \nstairs \nportal"
        txt53 = "ok lets go upstairs"
        txt54 = "ok lets enter the portal"
        txt55 = "ok, lets go back"
        key51 = "upstairs"
        key52 = "door"
        key53 = "back"
        ans = "upstairs"
        ans2 = "read"
        ans3 = "startroom"

        img = tkinter.PhotoImage(file="5.png")
        l.configure(image=img)
        l.image = img

        l4 = tkinter.Label(main, text=txt52, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt53, txt54, txt55, None, key51, key52, key53, None, ans, ans2, ans3)


class read:
    def enter(self):
        txt52 = "new room. I think this witch over there is too strong. oh a scroll, ill read it to you, ready? \n\tyes \n\tno "
        txt53 = "ok ill start"
        txt54 = "take ya time"
        txt55 = "ok, lets go back"
        key51 = "yes"
        key52 = "no"
        key53 = "back"
        ans = "potions"
        ans2 = "read"
        ans3 = "l1"

        img = tkinter.PhotoImage(file="7.png")
        l.configure(image=img)
        l.image = img

        global l4
        l4 = tkinter.Label(main, text=txt52, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt53, txt54, txt55, None, key51, key52, key53, None, ans, ans2, ans3)


class potions:
    def enter(self):
        txt52 = "remember the hint. \nyou could take the...: \n\t'red'\n\t'green'"
        txt53 = "take the red one"
        txt54 = "take the green one"
        key51 = "red"
        key52 = "green"
        key54 = "back"
        ans = "prefight"
        ans2 = "death"
        ans3 = "l1"

        img = tkinter.PhotoImage(file="7.1.png")
        l.configure(image=img)
        l.image = img

        global l4
        l4 = tkinter.Label(main, text=txt52, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt53, txt54, None, None, key51, key52, key54, None, ans, ans2, ans3)


class prefight:
    def enter(self):
        txt52 = "greaaaaaaat you got the right one, now youre superstrong, punch her on the nose so we can pass \nfight\n'nofight'"
        txt53 = "ok, be aware of her left hook!!"
        txt54 = "oh no, a pazifist, now shell kill you"
        key51 = "fight"
        key52 = "nofight"
        key54 = "back"
        ans = "fight"
        ans2 = "death"
        ans3 = "potions"

        img = tkinter.PhotoImage(file="7.2.png")
        l.configure(image=img)
        l.image = img

        global l4
        l4 = tkinter.Label(main, text=txt52, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt53, txt54, None, None, key51, key52, None, key54, ans, ans2, ans3)


class fight:
    def enter(self):
        txt52 = "nice one, now we can pass"
        key54 = "back"
        ans3 = "prefight"

        img = tkinter.PhotoImage(file="7.4.png")
        l.configure(image=img)
        l.image = img

        global l4, nxt
        nxt = "troom"
        l4 = tkinter.Label(main, text=txt52, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(None, None, None, None, None, None, None, key54, None, None, ans3)


class upstairs:
    def enter(self):
        txt52 = "oh a scroll, ill read it to you, ready? \n\tyes \n\tno "
        txt53 = "ok ill start"
        txt54 = "take ya time"
        txt55 = "ok, lets go back"
        key51 = "yes"
        key52 = "no"
        key53 = "back"
        ans = "upstairsread"
        ans2 = "upstairs"
        ans3 = "l1"

        img = tkinter.PhotoImage(file="6.png")
        l.configure(image=img)
        l.image = img

        global l4
        l4 = tkinter.Label(main, text=txt52, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(txt53, txt54, txt55, None, key51, key52, key53, None, ans, ans2, ans3)


class upstairsread:
    def enter(self):
        txt52 = "I suppose its a hint. Keep it in mind."
        key54 = "back"
        ans2 = "upstairs"

        img = tkinter.PhotoImage(file="6.1.png")
        l.configure(image=img)
        l.image = img

        global l4, nxt
        l4 = tkinter.Label(main, text=txt52, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")

        template(None, None, None, None, None, key54, None, None, None, ans2, None)
        nxt = "read"


class troom:

    def enter(self):
        txt52 = "oh wow the treasure camber, take as much as you can. we have to bring it safely outside the cave to accomplish our mission\nback"
        key54 = "back"

        if way == "l":
            ans2 = "potions"
        else:
            ans2 = "rope"

        img = tkinter.PhotoImage(file="8.png")
        l.configure(image=img)
        l.image = img

        global l4, nxt, accp
        nxt = "read"
        accp = True

        l4 = tkinter.Label(main, text=txt52, bg="#000000", fg="#FFFFFF", font=("Courier", 15), wraplength=650)
        l4.place(x=main.winfo_screenwidth() / 2, y=main.winfo_screenheight() / 1.5 + 30, anchor="w")
        template(None, None, None, None, None, key54, None, None, None, ans2, None)
        print("accp:", accp)


class Map():
    scenes = {
        "start": start(),
        "askready": askready(),
        "askscare": askscare(),
        "opening": opening(),
        "equip": equip(),
        "gotlight": gotlight(),
        "startroom": startroom(),
        "l1": l1(),
        "gotglasses": gotglasses(),
        "r1": r1(),
        "gotrope": gotrope(),
        "rope": rope(),
        "read": read(),
        "potions": potions(),
        "upstairs": upstairs(),
        "upstairsread": upstairsread(),
        "troom": troom(),
        "prefight": prefight(),
        "fight": fight(),
        "death": death(),
        "victory": victory(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        var = Map.scenes.get(scene_name)

        return var

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("start")
a_game = engine(a_map)
a_game.play()
main.mainloop()
