import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
    
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(word,":",meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Lamentablemente no se el significado de esa palabra...")
    print("pero te puedo compartir otra que te será util:")
    new = random.choice( meme_dict.keys() )
    print( new,":",meme_dict[new] )
