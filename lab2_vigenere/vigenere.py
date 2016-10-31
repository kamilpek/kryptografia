import sys
import string
import random

ciphertext = ""
plaintext = ""
words_list = ["the", "name", "open", "ten", "of", "very", "seem", "simple", "to", "through", "together", "several", "and", "just", "next", "vowel", "a", "form", "white", "toward", "in", "much", "children", "war", "is", "great", "begin", "lay", "it", "think", "got", "against", "you", "say", "walk", "pattern", "that", "help", "example", "slow", "he", "low", "ease", "center", "was", "line", "paper", "love", "for", "before", "often", "person", "on", "turn", "always", "money", "are", "cause", "music", "serve", "with", "same", "those", "appear", "as", "mean", "both", "road", "I", "differ", "mark", "map", "his", "move", "book", "science", "they", "right", "letter", "rule", "be", "boy", "until", "govern", "at", "old", "mile", "pull", "one", "too", "river", "cold", "have", "does", "car", "notice", "this", "tell", "feet", "voice", "from", "sentence", "care", "fall", "or", "set", "second", "power", "had", "three", "group", "town", "by", "want", "carry", "fine", "hot", "air", "took", "certain", "but", "well", "rain", "fly", "some", "also", "eat", "unit", "what", "play", "room", "lead", "there", "small", "friend", "cry", "we", "end", "began", "dark", "can", "put", "idea", "machine", "out", "home", "fish", "note", "other", "read", "mountain", "wait", "were", "hand", "north", "plan", "all", "port", "once", "figure", "your", "large", "base", "star", "when", "spell", "hear", "box", "up", "add", "horse", "noun", "use", "even", "cut", "field", "word", "land", "sure", "rest", "how", "here", "watch", "correct", "said", "must", "color", "able", "an", "big", "face", "pound", "each", "high", "wood", "done", "she", "such", "main", "beauty", "which", "follow", "enough", "drive", "do", "act", "plain", "stood", "their", "why", "girl", "contain", "time", "ask", "usual", "front", "if", "men", "young", "teach", "will", "change", "ready", "week", "way", "went", "above", "final", "about", "light", "ever", "gave", "many", "kind", "red", "green", "then", "off", "list", "oh", "them", "need", "though", "quick", "would", "house", "feel", "develop", "write", "picture", "talk", "sleep", "like", "try", "bird", "warm", "so", "us", "soon", "free", "these", "again", "body", "minute", "her", "animal", "dog", "strong", "long", "point", "family", "special", "make", "mother", "direct", "mind", "thing", "world", "pose", "behind", "see", "near", "leave", "clear", "him", "build", "song", "tail", "two", "self", "measure", "produce", "has", "earth", "state", "fact", "look", "father", "product", "street", "more", "head", "black", "inch", "day", "stand", "short", "lot", "could", "own", "numeral", "nothing", "go", "page", "class", "course", "come", "should", "wind", "stay", "did", "country", "question", "wheel", "my", "found", "happen", "full", "sound", "answer", "complete", "force", "no", "school", "ship", "blue", "most", "grow", "area", "object", "number", "study", "half", "decide", "who", "still", "rock", "surface", "over", "learn", "order", "deep", "know", "plant", "fire", "moon", "water", "cover", "south", "island", "than", "food", "problem", "foot", "call", "sun", "piece", "yet", "first", "four", "told", "busy", "people", "thought", "knew", "test", "may", "let", "pass", "record", "down", "keep", "farm", "boat", "side", "eye", "top", "common", "been", "never", "whole", "gold", "now", "last", "king", "possible", "find", "door", "size", "plane", "any", "between", "heard", "age", "new", "city", "best", "dry", "work", "tree", "hour", "wonder", "part", "cross", "better", "laugh", "take", "since", "true", "thousand", "get", "hard", "during", "ago", "place", "start", "hundred", "ran", "made", "might", "am", "check", "live", "story", "remember", "game", "where", "saw", "step", "shape", "after", "far", "early", "yes", "back", "sea", "hold", "hot", "little", "draw", "west", "miss", "only", "left", "ground", "brought", "round", "late", "interest", "heat", "man", "run", "reach", "snow", "year", "don’t", "fast", "bed", "came", "while", "five", "bring", "show", "press", "sing", "sit", "every", "close", "listen", "perhaps", "good", "night", "six", "fill", "me", "real", "table", "east", "give", "life", "travel", "weight", "our", "few", "less", "language", "under", "stop", "morning", "among", "time", "be", "good", "person", "have", "new", "year", "do", "first", "way", "say", "last", "day", "get", "long", "thing", "make", "great", "man", "go", "little", "world", "know", "own", "life", "take", "other", "hand", "see", "old", "part", "come", "right", "child", "think", "big", "eye", "look", "high", "woman", "want", "different", "place", "give", "small", "work", "use", "large", "week", "find", "next", "case", "tell", "early", "point", "ask", "young", "government", "work", "important", "company", "seem", "few", "number", "feel", "public", "group", "try", "bad", "problem", "leave", "same", "fact", "call", "able"]
letters_frequencies = { "a": 81, "b": 14, "c": 27, "d": 42, "e": 127, "f": 22, "g": 20, "h": 60, "i": 69, "j": 1, "k": 7, "l": 40, "m": 24, "n": 67, "o": 75, "p": 19, "q": 0, "r": 59, "s": 63, "t": 90, "u": 27, "v": 9, "w": 23, "x": 1, "y": 19, "z": 0 }

# key = [6,1,8,0,3,3,9,8,8,7,4]

def crypto(plain, key):
    if(plain == None or key == None):
        return None
    else:
        result = ord(plain) + key
        if(result <= ord('z')):
            return chr(result)
        else:
            return chr(result - 26)

def decrypto(cipher, key):
    if(cipher == None or key == None):
        return None
    else:
        result = ord(cipher) - key
        if(result >= ord('a')):
            return chr(result)
        else:
            return chr(result + 26)

def crypt(key, msg):
    cipher = []
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            pos_c = ord(c) - ord('a')
            pos_k = ord(key[i]) - ord('a')
            cipher.append(chr((pos_c + pos_k) % 26 + ord('a')))
            i = (i + 1) % len(key)
        else:
            cipher.append(c)
    return ''.join(cipher)

def decrypt_ca(key, msg):
    cipher = []
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            pos_c = ord(c) - ord('a')
            pos_k = ord(key[i]) - ord('a')
            cipher.append(chr((pos_c - pos_k) % 26 + ord('a')))
            i = (i + 1) % len(key)
        else:
            cipher.append(c)
    return ''.join(cipher)

def prepare():
    orig = open("orig.txt", "r")
    plain = open("plain.txt", "w")
    for line in orig:
        text = line.lower()
        text = text.replace(" ", "")
        text = text.replace(".", "")
        text = text.replace(",", "")
        text = text.replace(";", "")
        text = text.replace(":", "")
        text = text.replace("!", "")
        text = text.replace("?", "")
        text = text.replace("/", "")
        text = text.replace("\\", "")
        text = text.replace("(", "")
        text = text.replace(")", "")
        text = text.replace("*", "")
        text = text.replace("=", "")
        text = text.replace("-", "")
        text = text.replace("+", "")
        text = text.replace("$", "")
        text = text.replace("%", "")
        text = text.replace("&", "")
        text = text.replace("#", "")
        text = text.replace("@", "")
        text = text.replace("~", "")
        text = text.replace("\"", "")
        text = text.replace("''", "")
        text = text.replace("<", "")
        text = text.replace(">", "")
        text = text.replace("|", "")
        plain.write(text)

class VigenereIndividual:
    def __init__(self, cipher, key, index, letter):
        self._key = key[:]
        self._key[index] = letter
        self._cipher = cipher
        self._fitness = 0
        self.compute_fitness()

    @property
    def new_key(self):
        return self._key

    @property
    def fitness(self):
        return self._fitness

    def compute_fitness(self):
        plain = decrypt_ca("".join(self._key), self._cipher)
        for w in words_list:
            self._fitness += plain.count(w)


def generate_individuals(cipher, key):
    individuals = list()
    for index in range(len(key)):
        for letter in string.ascii_lowercase:
            individuals.append(VigenereIndividual(cipher, key, index, letter))
    return individuals


def get_solution_from_individuals(individuals):
    individuals = sorted(individuals, key=lambda x: x.fitness, reverse=True)
    return individuals[0]


def analyze(data, key_size):
    key = [random.choice(string.ascii_lowercase) for _ in range(key_size)]
    while True:
        individuals = generate_individuals(data, key)
        solution = get_solution_from_individuals(individuals)
        if "".join(key) == "".join(solution.new_key):
            break
        key = solution.new_key
        print('Key=%s\t\tFitness=%d' % ("".join(key), solution.fitness))

    print("")
    print("Key=%s" % "".join(key))
    print(decrypt_ca("".join(key), data))


def getkey():
    key = []
    i = 0
    ach = 0
    gkey = open("key.txt", "r")
    for line in gkey:
        for ch in line:
            ach = ord(ch)
            ach = ach-97
            key.append(ach)
    key.remove(-87)
    # print(key)
    return key

def main():

    if sys.argv[1] == "-e":
        i = 0
        plain = open("plain.txt", "r")
        cryptow = open("crypto.txt", "w")
        ekey = getkey()
        for line in plain:
            for c in line:
                i = i%len(ekey)
                # tcr = prettifyString(map(crypto, line, ekey), plaintext)
                tcr = crypto(c, ekey[i])
                # print(ekey[i])
                i += 1
                cryptow.write(tcr)
        plain.close()
        cryptow.close()
    elif sys.argv[1] == "-d":
        i = 0
        cryptor = open("crypto.txt", "r+")
        decrypt = open("decrypt.txt", "w")
        dkey = getkey()
        for line in cryptor:
            for c in line:
                i = i%len(dkey)
                # tdc = prettifyString(map(decrypto, line, dkey), ciphertext)
                tdc = decrypto(c, dkey[i])
                i += 1
                decrypt.write(tdc)
        cryptor.close()
        decrypt.close()
    elif sys.argv[1] == "-p":
        prepare()
    elif sys.argv[1] == "-k":
        kkey = getkey()
        skey = len(kkey)
        cryptor = open("crypto.txt", "r+")
        for line in cryptor:
            analyze(line, skey)
        cryptor.close()
    else:
        print("wybierz poprawna opcje")

main()
