# ouvrir le fichier exo.txt et de pouvoir le lire seuelement grace a l'option r
file = open('exo.txt', 'r')

# obtenir une liste a partir de chaque ligne du fichier
text = file.readlines()

# fermer le fichier grace a la methode close()
file.close()


# declarer deux variable pour stocker la base de faits et le but
bf=None
but=None

# declarer un dictionnaire au nom de regles pour stocker nos regles
regles={}

# la methode enumerate sert a obtenir l'index d'un element d'une liste
for i,t in enumerate(text):
    # suprimer les \n
    t = t.replace('\n', '')

    # apres avoir suprimer le \n (saut a la ligne) on peu se retrouver avec un element vide
    # par example ['ceci est un example\n', '\n'] ici le deuxieme element contient just
    # \n donc apres sa supression on aura un element vide
    if len(t) > 0:
        # avec la methode split on va pouvoir couper notre chaines de caractere avec
        # le caractere qu'on a mit dans le split
        # example 'ceci#est#un#example'.split('#') = ['ceci', 'est', 'un', 'example']
        t = t.split('#')
        if i == 0:
            # on va obtenir notre BF et not but si on est dans la premiere ligne du text
            bf = [f for f in t[0].split(',')]
            but = t[1]
        else:
            # ici on va prendre chaque regles et l'enregistrer comme ceci
            # par example i = 1 et t[0] = ['B,C'] et t[1] = F
            # alors { 'R1': (['B', 'C'], F) }
            regles[f'R{i}'] = ([f for f in t[0].split(',')], t[1])

# on creer un loop qui ne s'arrete sauf si on a atteint le but ou il n'y a pas de resultat
stopLoop = False
while not stopLoop:
    stopLoop = True

    # on va mtn commencer a travailler avec les regles obtenu
    for r in regles:
        # on va extraire nos informations a partir de chaque regles
        # on sait que chaque regle contient un tuble de forme ([], element('H par example'))
        # donc on va nomé notre liste avec si et notre element avec alors tout comme dans le text de l'exo
        si, alors = regles[r]

        # on doir verifier si l'element da la condition n'existe pas dans notre bf
        # pour pouvoir utiliser les regles correctement
        if alors not in bf:

            # cette instruction va nous permettre de savoir si la liste dans la regle
            # est contenu dans la base de faits
            isContained = all(s in bf for s in si)

            # si oui alors on va ajouter le resultat de la regle dans notre BF
            if isContained:

                # si le but est dans la bf alors on arrete la loop (boucle) 'for'
                if but in bf:
                    # imprimer qu'on est arriver au but
                    print('\n')
                    print('#'*30, '\n')
                    print(f'le but {but} a etait atteint et ceci est notre nouvelle base de faits :\n{bf}', '\n')
                    print('#'*30, '\n')
                    break
                else:
                    # sinon on ajoute l'element dans notre BF et change la variable 
                    # stopLoop a False pour refaire la loop while et arreter la loop for 
                    bf.append(alors)

                    # on va imprimer le resultat de notre BF apres avoir obtenu un resultat avec une regle
                    print(f'depuis la regle {r} on obtient une nouvelle base de faits :\n{bf}\n', '#'*30)
                    stopLoop = False
                    # si le but est dans la bf alors on arrete la loop (boucle) 'for'
                    if but in bf:
                        # imprimer qu'on est arriver au but
                        print('\n')
                        print('#'*30, '\n')
                        print(f'le but {but} a etait atteint et ceci est notre nouvelle base de faits :\n{bf}', '\n')
                        print('#'*30, '\n')
                    break
