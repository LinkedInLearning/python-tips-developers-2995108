text1 = "abcd"
text2 = "bacd"
text3 = "bAcd"
def is_anagram(t1,t2,cs=True):
    if cs:
        print("Case-sensitiver Test")
        return sorted(t1) == sorted(t2)
    else:
        print("Kein case-sensitiver Test")
        return sorted(t1.lower()) == sorted(t2.lower())
print("{} und {} sind Anagramme: {}\n".format(text1,text2,is_anagram(text1,text2,False)))
print("{} und {} sind Anagramme: {}\n".format(text1,text3,is_anagram(text1,text3,False)))
print("{} und {} sind Anagramme: {}\n".format(text1,text3,is_anagram(text1,text3,True)))