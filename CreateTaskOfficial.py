while True:
    print('''
    Hello! Welcome to the Music Recommendation Generator.
    There will be 5 questions.
    Each question will provide 5 artists, and will ask you to choose your favorite of the five.''')
    print("")
    Readyresponse = input("Are you ready? Type yes or no: ")

    if Readyresponse == "yes" or Readyresponse == "Yes" or Readyresponse == "YES":
        print("Great! Lets get started.")
    else:
        break

    directions = "Of these artists, who is your favorite? In your answer, please type the letter answer of your choice"
    cont = "Great. Let's continue."

    #question 1
    print("")
    print(directions)
    print("A: Kendrick Lamar")
    print("B: Led Zeppelin")
    print("C: Justin Bieber")
    print("D: The Weeknd")
    print("E: Jack Johnson")

    Q1response = input("Your answer (A, B, C, D or E): ")

    if Q1response == "A" or Q1response == "a":
        print(cont)
    elif Q1response == "B" or Q1response == "b":
        print(cont)
    elif Q1response == "C" or Q1response == "c":
        print(cont)
    elif Q1response == "D" or Q1response == "d":
        print(cont)
    elif Q1response == "E" or Q1response == "e":
        print(cont)


    #question 2
    print("")
    print(directions)
    print("A: A$AP Rocky")
    print("B: Fleetwood Mac")
    print("C: Ariana Grande")
    print("D: ZAYN")
    print("E: Vance Joy")
    
    Q2response = input("Your answer (A, B, C, D or E): ")

    if Q2response == "A" or Q2response == "a":
        print(cont)
    elif Q2response == "B" or Q2response == "b":
        print(cont)
    elif Q2response == "C" or Q2response == "c":
        print(cont)
    elif Q2response == "D" or  Q2response == "d":
        print(cont)
    elif Q2response == "E" or  Q2response == "e":
        print(cont)
        

    #question 3
    print("")
    print(directions)
    print("A: Kanye")
    print("B: The Rolling Stones")
    print("C: Selena Gomez")
    print("D: Justin Timberlake")
    print("E: Bob Dylan")

    Q3response = input("Your answer (A, B, C, D or E): ")

    if Q3response == "A" or Q3response == "a":
        print(cont)
    elif Q3response == "B" or Q3response == "b":
        print(cont)
    elif Q3response  == "C" or Q3response == "c":
        print(cont)
    elif Q3response == "D" or Q3response == "d":
        print(cont)
    elif Q3response == "E" or Q3response == "e":
        print(cont)

   

    #question 4
    print("")
    print(directions)
    print("A: Chance the Rapper")
    print("B: The Velvet Underground")
    print("C: Ed Sheeran")
    print("D: Khalid")
    print("E: The Head and the Heart")

    Q4response = input("Your answer (A, B, C, D or E): ")

    if Q4response == "A" or Q4response == "a":
        print(cont)
    elif Q4response == "B" or Q4response == "b":
        print(cont)
    elif Q4response == "C" or Q4response == "c":
        print(cont)
    elif Q4response == "D" or Q4response == "d":
        print(cont)
    elif Q4response == "E" or Q4response == "e":
        print(cont)


    #question 5
    print("")
    print(directions)
    print("A: Migos")
    print("B: The Beatles")
    print("C: Liam Payne")
    print("D: Bryson Tiller")
    print("E: Mac Demarco")

    Q5response = input("Your answer (A, B, C, D or E): ")
    woohoo = "Great!"
    space = ""

    if Q5response == "A" or Q5response == "a":
        print(space)
    elif Q5response == "B" or Q5response == "b":
        print(space)
    elif Q5response == "C" or Q5response == "c":
        print(space)
    elif Q5response == "D" or Q5response == "d":
        print(space)
    elif Q5response == "E" or Q5response == "e":
        print(space)

    print(space)
    print(space)
    FinalAnswer = input("Which letter did you choose the most? A, B, C, D or E): ")
    print(space)
    print(space)
    recommendation = "You should listen to these artists:"

    if FinalAnswer == "A" or FinalAnswer == "a":
        print(recommendation)
        print("Earl Sweatshirt")
        print("Amine")
        print("Jay Critch")
        print("Mac Miller")
        print("Tyler, The Creator")
        print("A$AP Ferg")
        print("Future")
        print("Travis $scott")
        print("Logic")
        print("Rae Sremmurd")
        print("BROCKHAMPTON")
        print("J. Cole")
        print("Big Sean")
    if FinalAnswer == "B" or FinalAnswer == "b":
        print(recommendation)
        print("The Cure")
        print("Greta Van Fleet")
        print("Harry Styles")
        print("Arctic Monkeys")
        print("Pink Floyd")
        print("Suzi Quatro")
        print("Todd Rundgren")
        print("David Bowie")
        print("Heart")
        print("Eagles")
        print("The Allman Brothers Band")
        print("James Bay")
        print("Joni Mitchell")
    if FinalAnswer == "C" or FinalAnswer == "c":
        print(recommendation)
        print("Maroon 5")
        print("Rita Ora")
        print("Daya")
        print("Dua Lipa")
        print("Shawn Mendes")
        print("Jack & Jack")
        print("Liam Payne")
        print("Halsey")
        print("Bleachers")
        print("DNCE")
        print("Charlie Puth")
        print("PRETTYMUCH")
        print("Meghan Trainor")       
    if FinalAnswer == "D" or FinalAnswer == "d":
        print(recommendation)
        print("Daniel Caesar")
        print("Jhene Aiko")
        print("XXXTENTACION")
        print("Frank Ocean")
        print("Rihanna")
        print("LANY")
        print("Russ")
        print("Kehlani")
        print("Michl")
        print("Mac Miller")
        print("Lil Xan")
        print("Childish Gambino")
        print("H.E.R.")
    if FinalAnswer == "E" or FinalAnswer == "e":
        print(recommendation)
        print("Mazzy Star")
        print("The Band")
        print("Joseph")
        print("Simon & Garfunkel")
        print("Bob Dylan")
        print("Corey Harper")
        print("Niall Horan")
        print("Ziggy Alberts")
        print("Big Star")
        print("James Taylor")
        print("Iron & Wine")
        print("Rex Orange County")
        print("Faces")
        print("Crosby, Stills and Nash")
        print("Soccer Mommy")

    print("______________________________________________________________________________________________________________________")
    print("")
    user_input = input("Would you like to play again? Y/N: ")
    if user_input == "Y" or user_input == "y":
              continue
    else:
        break
        
    
    
