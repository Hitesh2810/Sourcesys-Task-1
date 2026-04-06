def Hitesh(**kwargs):
    sentence = ""

    for key, value in kwargs.items():
        sentence += str(value) + " "

    #print(sentence.strip())
    return sentence.strip()