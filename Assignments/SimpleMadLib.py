#once apon a time a(n) [adjective] [noun] was livng in a [noun].
#one day, the [1st adjective and noun] went to the store hoping to get a(n) [adjective] [noun].
#but, when he got there the [previous adjectiv and noun] was gone!
#so instead, the [first asjective and noun] went to the [location].
#after he got there a(n) [noun] had stole his [noun]!
#so, after all that the [first adjective and noun] just went home

#intro
print("Welcome to the my mad lib. Complete it by filling in the blanks.")
#character adjective and noun
char_adj = input("adjective\n>")
char_noun = input("noun\n>")
#ask for location
loc_noun = input("noun\n>")
#ask for object adjective and noun
thing_adj = input("adjective\n>")
thing_noun = input("noun\n>")
#ask for location
location = input("location\n>")
#ask for theif's noun
bad_noun = input("noun\n>")
#ask for stolen object
keys_noun = input("noun\n>")

#print summary
print("Once apon a time, a(n) ",char_adj," ",char_noun,"was living in a(n) ",loc_noun,".\n","one day, the ",char_adj," ", char_noun," went to the store hoping to get a(n)",thing_adj," ",thing_noun,".\n>","But, when he got there the",thing_adj," ",thing_noun," was gone!\n","so, instead, the ",char_adj," ",char_noun," went to the ",location,".\n","after he got there a(n) ",bad_noun," had stole his ",keys_noun,"!\n","So, after all that, the ", char_adj," ",char_noun," just went home.")
