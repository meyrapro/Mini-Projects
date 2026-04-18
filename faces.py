def convert(emoji):
    if emoji == ":)":
        return("😄")
    elif emoji == ":(":
        return("😔")
    else:
        return(emoji)
    

def main():
    sentence = input("Tape ta phrase : ")
    words = sentence.split()
    
    new_sentence = []

    for w in words:
        result = convert(w)
        new_sentence.append(result)

    print(" ".join(new_sentence))

main()