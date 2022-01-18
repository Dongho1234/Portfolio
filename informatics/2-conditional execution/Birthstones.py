'''
INPUT

The name of a birthstone.
'''

'''
OUTPUT
The name of the month (or months) that corresponds to the given birthstone, 
described using the following template: "<stone> is a birthstone of the month <month>". 
The fragments in between less than and greater then characters must be filled up with the name of the given birthstone and the name of the corresponding month.
'''

a = input()

if a == "lapis lazuli":
    print(a, "is a birthstone of the month September or December")

elif a == "garnet":
    print(a, "is a birthstone of the month January")

elif a == "amethyst":
    print(a, "is a birthstone of the month February")
    
elif a == "bloodstone" or a == "aquamarine":
    print(a, "is a birthstone of the month March")
    
elif a == "diamond" or a == "rock crystal":
    print(a, "is a birthstone of the month April")
    
elif a == "emerald" or a == "chrysoprase":
    print(a, "is a birthstone of the month May")

elif a == "pearl" or a == "moonstone" or a == "alexandrite":
    print(a, "is a birthstone of the month June")

elif a == "ruby" or a == "carnelian":
    print(a, "is a birthstone of the month July")
    
elif a == "sardonyx" or a == "peridot" or a == "spinel":
    print(a, "is a birthstone of the month August")
    
elif a == "sapphire" or a == "lapis lazuli":
    print(a, "is a birthstone of the month September")
    
elif a == "opal" or a == "tourmaline":
    print(a, "is a birthstone of the month October")

elif a == "topaz" or a == "citrine":
    print(a, "is a birthstone of the month November")
    
elif a == "turquoise" or a == "lapis lazuli" or a == "zircon" or a == "tanzanite":
    print(a, "is a birthstone of the month December")
  
'''
sapphire
stdout
sapphire is a birthstone of the month September
'''
