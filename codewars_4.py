def anagrams(word,p_words):
    print([answer for answer in p_words if sorted(list(answer)) == sorted(list(word))])

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'raceref', 'racer'])
