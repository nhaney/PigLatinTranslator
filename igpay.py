#CptS 481 - igpay.py, returns translation of string into pig latin

def igpay(string):
    vowels = set(['a','e','i','o','u','A','E','I','O','U'])
    returnString = ""
    #if it starts with a vowel
    if string[0] in vowels:
        #check if length is 1 because it is kind of weird to translate
        #I -> IWAY or A -> AWAY
        if(string.isupper() and len(string) != 1):
            return string + "WAY"
        else:
            return string + "way"
    
    #if it has a vowel in it, go to it, and then return the correct word
    for i, c in enumerate(string):
        if c in vowels:
            if(string.isupper()):
                returnString = (string[i:] + string[:i] + "ay").upper()
            elif(string[0].isupper()):
                returnString = string[i].upper() + string[i+1:] + string[:i].lower() + "ay"
            else:
                returnString = string[i:] + string[:i] + "ay"
            return returnString
    #function reaches here if there is no vowel in the word and returns it    
    return string

if __name__ == '__main__':
    print("Testing functionality of igpay:")
    print("igpay(\"yes\"):", igpay("yes"))
    print("igpay(\"parrot\"):", igpay("parrot"))
    print("igpay(\"office\"):",igpay("office"))
    print("igpay(\"why\"):",igpay("why"))
    print("igpay(\"The\"):", igpay("The"))
    print("igpay(\"STUFF\"):", igpay("STUFF"))


    

    

    

    
    

