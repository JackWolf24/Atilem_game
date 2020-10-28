#items = ["30m rope", "life jacket", "sunglasses", "key", "anti toxic potion", "flashlight", "5L of water", "3 apples",
#         "raincoat", "game of cards"]

#Synonyme
rope = ["rope", "30m rope",  "30m", "Rope"]
glasses = ["sunglasses", "Sunglasses", "glasses", "Glasses"]
potion = ["antidote", "potion", "bottle", "glass", "vessel", "antitoxic",  "antidote"]
light = ["flashlight", "light", "lamp", "Light", "Lamp", "Flashlight", "On", "on"]
water = ["water","5L of water", "5L", "5l",  "blue wet"]
apple = ["apples", "3 apples", "3 Apples", "Apples", "apple", "Apple"]
cards = ["cardgame", "game of cards", "cards", "game"]
stairs = ["upstairs", "up", "stairs" ]
yes = ["yes", "ys", "si", "jo", "jop"]
no = ["no", "not", "nope", "noo"]
fight = ["fight", "hit", "punsh"]
nofight = ["nofight", "nonvioleze"]
door = ["door", "portal", "gate"]

#satzbausteine
ljacket = ["jacket", "lifejacket", "life jacket"]
object = ["north", "south", "east", "west", "down", "up", "left", "right", "back", "upstairs", "stairs",
          "yes", "ys", "si", "jo", "jop", "no", "not", "nope", "noo",
          "first", "second", "third", "1st", "2nd", "3rd",
          "door", "gate", "portal",
          "potion", "bottle", "glass", "vessel", "anti toxic potion", "antidote",
          "red", "blue", "green", "Red", "Blue", "Green",
          "rope", "30m rope", "30m", "Rope"
          "jacket", "life jacket",
          "glasses", "sunglasses", "Sunglasses", "Glasses",
          "key",
          "light", "lamp", "flashlight", "Light", "Lamp", "Flashlight", "on", "On",
          "water", "5L water", "5L", "blue wet", "Water",
          "3 apples", "3 Apples", "apples", "Apples", "apple", "Apple"
          "raincoat",
          "game", "cards", "game of cards", "cardgame",
          "fight", "hit", "punsh", "nofight",
          "pass",
          "cheat", "loose"]

verbs = ["say", "shout", "mean", "tell",
         "go", "run", "hit", "rush", "hustle",
         "take", "grab",
         "drink", "consume", "sip"
         "switch"]

stopwords = ["the", "in", "of", "from", "at", "it", "to", "all"]
subject = ["player", "me", "I", "lets"]
sentence = []

#abfrage ob x in satzbausteine und oder synonyme
def lexicon(x):
    words = x.split()
    for x in words:
        try:
            if x in object:
                if x in rope:
                    sentence.append(("object", rope[0]))
                elif x in glasses:
                    sentence.append(("object", glasses[0]))
                elif x in potion:
                    sentence.append(("object", potion[0]))
                elif x in light:
                    sentence.append(("object", light[0]))
                elif x in water:
                    sentence.append(("object", water[0]))
                elif x in apple:
                    sentence.append(("object", apple[0]))
                elif x in cards:
                    sentence.append(("object", cards[0]))
                elif x in stairs:
                    sentence.append(("object", stairs[0]))
                elif x in nofight:
                    sentence.append(("object", nofight[0]))
                elif x in door:
                    sentence.append(("object", door[0]))
                else:
                    sentence.append(("object", x))

            elif x in verbs:
                sentence.append(("verb", x))

            elif x in stopwords:
                sentence.append(("stopword", x))

            elif x in subject:
                sentence.append(("subject", x))

        except ValueError:
            print("thats not a string")

    #print(sentence)


