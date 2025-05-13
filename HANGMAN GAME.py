import random
import sys
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="naman2005")
mc=mydb.cursor()
mc.execute("create database if not exists hangman;")
mc.execute("use hangman;")
mc.execute("create table if not exists List(word char(20));")
mc.execute("create table if not exists Player(Name char(20),Points int,Words int);")        


List=[]
mysql=("select * from List;")
mc.execute(mysql)
x=mc.fetchall()
for i in x:
    for r in i:
        List.append(r)

w={}

mysql=("select * from player;")
mc.execute(mysql)
x=mc.fetchall()
for i in x:
    w[i[0]]=(i[1],i[2])

while True:
    print("▾"*100,"\n")
    print("""
⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀ 1.To Display Word List                ⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀⚀

⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁ 2.To Enter Word In List               ⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁⚁

⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂ 3.To Delete Word From List            ⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂⚂

⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃ 4.To Play Hangman                     ⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃⚃

⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄ 5.To Display Players Score            ⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄⚄

⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅ 6.To Delete Player Details            ⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅⚅

❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖  7.EXIT                                ❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖❖""")

    
    c=int(input("\nEnter Choice:"))

    if c==1:
        List=[]
        mysql=("select * from List;")
        mc.execute(mysql)
        x=mc.fetchall()
        for i in x:
            for r in i:
                List.append(r)
        p=input("\nEnter Password:")
        if List==[]:
            print("\nOOPS! List Is empty please Create List")
        elif p=="naman":
            mysql=("select * from List;")
            mc.execute(mysql)
            x=mc.fetchall()
            for i in x:
                for r in i:
                    print("{0:15}{1:20}{2:40}".format("✭"*11,r.upper(),"✭"*11))
        else:
            print("\nYou Are Not Authorized ")

    elif c==2:
        p=input("Enter Password:")
        if p=="naman":
            r=int(input("\nEnter Total Words To Insert In List:"))
            for i in range(r):
                word=input("\nEnter Word To Insert:")
                if word in List:
                    print("\nOOPS! Word Is already Inserted ◕‿◕")
                else:
                    mysql="insert into List values(%s);"
                    val=(word,)
                    mc.execute(mysql,val)
                    mydb.commit()
                    List.append(word)
        else:
            print("\nYou Are Not Authorized !>_<!")
    elif c==3:
        p=input("\nEnter Password:")
        if List==[]:
            print("\nOOPS! List is already Empty ◕‿◕")
        elif p=="naman":
            word=input("\nEnter Word To Delete:")
            if word in List:
                mysql="delete from list where word=%s;"
                val=(word,)
                mc.execute(mysql,val)
                mydb.commit()
                print(word,"Word has been deleted")
            else:
                print(word,"\nIs Not In The List ☠")
        else:
            print("\nYou Are Not Authorized ☺")
            
        

    elif c==4:
        global wo
        pt=0
        wo=0
        if List==[]:
            print("\nPlease Create List ☺")
        else:
            guess_word = []
            secretWord = random.choice(List) 
            list
            length_word = len(secretWord)
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            letter_storage = []



            def beginning():
                while True:
                    name = input("\nPlease enter Your name:").upper()
                    if name == '':
                        print("\nYou can't do that! No blank lines")
                    else:
                        print("\nHello",name,"☺")
                        break
                return name

            def change():
                for character in secretWord:
                    guess_word.append('_')
                print("\nOk, so the word You need to guess has", length_word, "characters")
                print("\nBe aware that You can enter only 1 letter from a-z\n\n")
                print("{0:}{1:}{2:}".format("-~"*10,guess_word,"~-"*10))

            def guessing(name):
                global wo
                chance=0
                global guess_taken
                guess_taken = 1
                while guess_taken < 6:
                    guess = input("\nPick a letter:").lower()
                    if not guess in alphabet: 
                        print("\nEnter a letter from a-z alphabet")
                    elif guess in letter_storage:
                        print("\nYou have already guessed that letter!")
                    else:
                        letter_storage.append(guess)
                        if guess in secretWord:
                            print("\nYou guessed correctly!")
                            for x in range(0, length_word):
                                if secretWord[x] == guess:
                                    guess_word[x] = guess
                            print("{0:}{1:}{2:}".format("-~"*10,guess_word,"~-"*10))

                            if '_' not in guess_word:
                                print("\nYou Guessed The word Correctly !")
                                print("\nThe Word Was:",secretWord)
                                wo=wo+1
                                break

                        else:
                            chance+=1
                            print("\nThe letter is not in the word. Try Again !+_+!")
                            if chance == 1:
                                print("   _____ \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "__|__\n")
                                print("\nBE CAREFUL.")
                                
                            elif chance==2:
                                print("   _____ \n"
                                      "  |     | \n"
                                      "  |     |\n"
                                      "  |      \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "__|__\n")
                                print("\nWATCH OUT |^_^|")

                            elif chance==3:
                               print("   _____ \n"
                                     "  |     | \n"
                                     "  |     |\n"
                                     "  |     | \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "__|__\n")
                               print("\nYOU ARE GOING TO HANG BE CAREFUL !!")

                            elif chance==4:                           
                                print("   _____ \n"
                                      "  |     | \n"
                                      "  |     |\n"
                                      "  |     | \n"
                                      "  |     O \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "__|__\n")
                                print("\nYOU ARE ABOUT TO HANG !!")
                                print("\nLast chance remaining :)")
                                
                            elif chance==5:
                                print("   _____ \n"
                                      "  |     | \n"
                                      "  |     |\n"
                                      "  |     | \n"
                                      "  |     O \n"
                                      "  |    /|\ \n"
                                      "  |    / \ \n"
                                      "__|__\n")
                                print("\nOH NO YOU ARE HANGED |*_*| ☠")
                            if chance!=5:                        
                                print("\nTill now you have guessed",chance,"letters wrong")
                                print("\nRemaining Chances:",5-chance)
                            guess_taken+=1
                        if guess_taken == 6:
                            print("\n",name.upper(),"The secret word was",secretWord,"!^-^!")
                            break
                    print("-"*80)
            guess_taken = 1
            name=beginning()
            while guess_taken<6:
                guess_word = []
                secretWord = random.choice(List) 
                list
                length_word = len(secretWord)
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                letter_storage = []
                if wo==0:
                    print("\nNow You Need To Guess The First Word:")
                else:
                    print("\nCongratulations!! You Gussed The Previous Word Correctly Now You Need To Guess The Another Word:")

                change()                    
                guessing(name)
                if guess_taken==1:
                    pt=pt+50
                elif guess_taken==2:
                    pt=pt+40
                elif guess_taken==3:
                    pt=pt+30
                elif guess_taken==4:
                    pt=pt+20
                elif guess_taken==5:
                    pt=pt+10
                else:
                    pt=pt+0
                

            print("\nYou Guessed",wo,"words correctly")
            print("\nYour Score Is:",pt)
                
            if name in w:
                mysql=("update player set points=%s and words=wo where name=%s;")
                val=(pt,wo,name)
                mc.execute(mysql,val)
                mydb.commit()
                w[name]=(pt,wo)
            else:
                mysql=("""insert into player(Name,Points,Words) values(%s,%s,%s);""")
                val=(name,pt,wo)
                mc.execute(mysql,val)
                mydb.commit()
                w[name]=(pt,wo)
    elif c==5:
        w={}
        mysql=("select * from player;")
        mc.execute(mysql)
        x=mc.fetchall()
        for i in x:
            w[i[0]]=(i[1],i[2])
        if w=={}:
            print("\nOOPS! NO player Played It YET  ◕‿◕")
        else:
            if len(x)==1:
                print("\nTill Now",len(x),"player has played this game (+_+)")
            else:
                print("\nTill Now",len(x),"players has played this game (+_+)")
            mysql=("select * from player;")
            mc.execute(mysql)
            x=mc.fetchall()
            for i in x:
                print("<>"*60,"\n")
                print("\t"*3,"-"*15,"PLAYER:",i[0],"-"*15,"\n\t\t\t\t\tGuessed",i[2],"Words Correctly\n\t\t\t\t\tScore:",i[1],"Points")
                    


    elif c==6:
        mysql=("select * from player;")
        mc.execute(mysql)
        x=mc.fetchall()
        if w=={}:
            print("\nOOPS! NO player Played It YET ◕‿◕")
        else:
            print("\nNumber of Data:",len(x))
            p=input("\nEnter Player Name To Delete:").upper()
            if p in w:
                mysql="""delete from player where name='"""+p+"'"
                mc.execute(mysql)
                mydb.commit()
                w.pop(p)
                print(p,"Data Has Been Removed")
            else:
                print("\n!*-*! NO PLAYER WITH THIS NAME HAS PLAYED IT YET ◕‿◕")

    else:
        print("\nTHANKS FOR USING MY CODE ツ")
        break
