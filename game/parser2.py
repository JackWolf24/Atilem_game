class ParserError(Exception):
    pass


class sentence:
    def __init__(self, sub, verb, obj):
        self.subject = sub[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]

    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_subject(word_list):
    skip(word_list, "stopword")
    next_word = peek(word_list)

    if next_word == "subject":
        return match(word_list, "subject")

    elif next_word == "verb":
        return "subject", "player"

    elif next_word == "object":
        return "error", "no sub"
    else:
        return "expected a sub next"


def parse_verb(word_list):
    skip(word_list, "stopword")

    if peek(word_list) == "verb":
        return match(word_list, "verb")

    elif peek(word_list) == "object":
        return "error", "no verb"

    else:
        return "expected a verb next"


def parse_object(word_list):
    skip(word_list, "stopword")
    next_word = peek(word_list)

    if next_word == "subject":
        return match(word_list, "noun")

    elif next_word == "object":
        return match(word_list, "object")

    elif not word_list:
        return match(word_list, "object")

    else:
        return "expected a obj next"


def parse_sentence(word_list):
    sub = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return sentence(sub, verb, obj)

