__author__ = 'Josh'
import string


def main():
    #encrypted = "HUMXZLTUFXLLFXDDVMYTMTOSEKAGLFRIWFFSBRORVHLFGVXAVNXOSWFAVUHYUXBFAWWEMMANSKWSJJFVGRAYMRNG"
    # message from http://crypto.interactive-maths.com/kasiski-analysis-breaking-the-code.html#intro
    encrypted = "CVJTNAFENMCDMKBXFSTKLHGSOJWHOFUISFYFBEXEINFIMAYSSDYYIJNPWTOKFRHWVWTZFXHLUYUMSGVDURBWBIVXFAFMYFYXPIGBHWIFHHOJBEXAUNFIYLJWDKNHGAOVBHHGVINAULZFOFUQCVFBYNFTYGMMSVGXCFZFOKQATUIFUFERQTEWZFOKMWOJYLNZBKSHOEBPNAYTFKNXLBVUAXCXUYYKYTFRHRCFUYCLUKTVGUFQBESWYSSWLBYFEFZVUWTRLLNGIZGBMSZKBTNTSLNNMDPMYMIUBVMTLOBJHHFWTJNAUFIZMBZLIVHMBSUWLBYFEUYFUFENBRVJVKOLLGTVUZUAOJNVUWTRLMBATZMFSSOJQXLFPKNAULJCIOYVDRYLUJMVMLVMUKBTNAMFPXXJPDYFIJFYUWSGVIUMBWSTUXMSSNYKYDJMCGASOUXBYSMCMEUNFJNAUFUYUMWSFJUKQWSVXXUVUFFBPWBCFYLWFDYGUKDRYLUJMFPXXEFZQXYHGFLACEBJBXQSTWIKNMORNXCJFAIBWWBKCMUKIVQTMNBCCTHLJYIGIMSYCFVMURMAYOBJUFVAUZINMATCYPBANKBXLWJJNXUJTWIKBATCIOYBPPZHLZJJZHLLVEYAIFPLLYIJIZMOUDPLLTHVEVUMBXPIBBMSNSCMCGONBHCKIVLXMGCRMXNZBKQHODESYTVGOUGTHAGRHRMHFREYIJIZGAUNFZIYZWOUYWQZPZMAYJFJIKOVFKBTNOPLFWHGUSYTLGNRHBZSOPMIYSLWIKBANYUOYAPWZXHVFUQAIATYYKYKPMCEYLIRNPCDMEIMFGWVBBMUPLHMLQJWUGSKQVUDZGSYCFBSWVCHZXFEXXXAQROLYXPIUKYHMPNAYFOFHXBSWVCHZXFEXXXAIRPXXGOVHHGGSVNHWSFJUKNZBESHOKIRFEXGUFVKOLVJNAYIVVMMCGOFZACKEVUMBATVHKIDMVXBHLIVWTJAUFFACKHCIKSFPKYQNWOLUMYVXYYKYAOYYPUKXFLMBQOFLACKPWZXHUFJYGZGSTYWZGSNBBWZIVMNZXFIYWXWBKBAYJFTIFYKIZMUIVZDINLFFUVRGSSBUGNGOPQAILIFOZBZFYUWHGIRHWCFIZMWYSUYMAUDMIYVYAWVNAYTFEYYCLPWBBMVZZHZUHMRWXCFUYYVIENFHPYSMKBTMOIZWAIXZFOLBSMCHHNOJKBMBATZXXJSSKNAULBJCLFWXDSUYKUCIOYJGFLMBWHFIWIXSFGXCZBMYMBWTRGXXSHXYKZGSDSLYDGNBXHAUJBTFDQCYTMWNPWHOFUISMIFFVXFSVFRNA"
    print(encrypted)
    matrix = grid_generator(encrypted)
    #grid_printer(matrix)
    coincidence_list = coincidence_finder(encrypted, matrix)
    tempList = coincidence_list[:10]
    tempKey = tempList.index(max(tempList)) + 1
    #print(tempKey)
    key_len = tempKey
    key = []
    for x in range(key_len):
        percent_list = percentage_maker(encrypted, key_len, x)
        combination_list = get_max_freq(percent_list) + 1
        key.append(combination_list)
    newKey = list_to_letter(key)
    print(newKey)
    message = decrypter(encrypted, newKey)
    print(message)


def decrypter(encrypted, key):
    """
    Simple decrypter for a vigenere cipher given a key.
    :param encrypted: The encrypted message.
    :param key: The key.
    :return: Returns the plaintext message.
    """
    message = ""
    currentPlace = 0
    for x in range(len(encrypted)):
        c = encrypted[x]
        k = key[currentPlace]
        currentPlace = (currentPlace + 1) % len(key)
        message += chr((ord(c) - ord(k)) % 26 + 65)
    return message


def list_to_letter(letterList):
    """
    Converts a list of numbers to uppercase letters
    :param letterList: List of numbers
    :return: Letters.
    """
    letters = ""
    for num in letterList:
        letters += chr(64 + num)
    return letters


def get_max_freq(percent_list):
    """
    Function that creates a list with all of the frequency possibilities to find the greatest overlap between
    the frequency of English and the frequency of the encrypted text
    :param percent_list: The frequency of the letters
    :return: A list with all the frequency possibilities
    """
    freq_dict = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, \
                 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, \
                 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

    ordered_freq = []
    for letter in string.ascii_uppercase:
        ordered_freq.append(freq_dict[letter])

    temp_percent = percent_list[:]
    combination_list = []
    for x in range(26):
        temp_total = 0
        for y in range(26):
            temp_total += ordered_freq[y] * temp_percent[y]
        combination_list.append(temp_total)
        temp_percent = shift(temp_percent, 1)
        #print(temp_percent)
    return combination_list.index(max(combination_list))


def shift(someList, n):
    """
    Simple shift method to emulate a circular
    :param someList:
    :param n:
    :return:
    """
    return someList[n:] + someList[:n]


def percentage_maker(encrypted, keyLength, keyShift):
    """
    Takes in the encrypted message and the key length and creates a frequency percentage
    :param encrypted: The encrypted message.
    :param keyLength: The length of the key.
    :return: A list of percents for how often a letter occurs
    """
    freq_dict = {letter: 0 for letter in string.ascii_uppercase}

    for x in range(len(encrypted)):
        if x % keyLength == keyShift:
            freq_dict[encrypted[x]] += 1

    percent_list = []
    for letter in string.ascii_uppercase:
        percent_list.append(freq_dict[letter] / len(encrypted))

    return percent_list


def coincidence_finder(encrypted, matrix):
    """
    Calculates the number of coincidences per possible string
    :param encrypted: The encrypted message
    :param matrix: The grid of shifted messages
    :return: The list of coincidences in order, used to determine the key length.
    """
    coincidence_list = []
    for offset in matrix:
        tempCount = 0
        for x in range(len(encrypted)):
            if offset[x] == encrypted[x]:
                tempCount += 1
        coincidence_list.append(tempCount)
    return coincidence_list

def grid_printer(matrix):
    """
    pretty prints the matrix grid
    :param matrix: The encrypted message grid
    :return: None
    """
    for x in matrix:
        print(x)


def grid_generator(encrypted):
    """
    Generates the 'grid' of offset encrypted text
    :param encrypted: The encrypted message
    :return: returns a matrix that is primed for the coincidences counter
    """
    matrix = []
    for x in range(1, len(encrypted)):
        tempStr = " " * x
        tempStr += encrypted[:len(encrypted) - x]
        matrix.append(tempStr)
    return matrix


if __name__ == "__main__":
    main()
