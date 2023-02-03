
def meny():
    print("-------------------------")
    print("Velkommen til Glosemus")
    print("-------------------------\n")
    print("Meny:")
    print("1. Skriv inn gloser")
    print("2. Gloseprøve")
    print("3. Avslutt")
    valg = input("\nDitt valg: ")
    try:
        intvalg = int(valg)
    except:
        intvalg = 0
    return intvalg

def legginn():
    qna = {}
    teller = 1
    print("Legg inn spørsmål og svar. Blank avslutter.\n")
    while True:
        question = input(f"Spørsmål {teller:2d}:").strip()
        if (question == ""):
            quit = input("Vil du avslutte innlegging av gloser? (J/N)")
            if quit.lower() == 'j':
                break
            else:
                continue
        answer = input(f"Svar     {teller:2d}:").strip()
        if (answer == ""):
            quit = input("Vil du avslutte innlegging av gloser? (J/N)")
            if quit.lower() == 'j':
                break
            else:
                continue
        qna[question] = answer
        teller += 1
        print()
    return qna


def glosetest():

    return

# Hovedprogram
#------------------------------------------
while(True):
    valg = meny()
    #print(f"Du skrev {valg}")

    if(valg==1):
        qna = legginn()
        # skriv ordboken til en fil her
        print(qna)
    elif(valg==2):
        # før glosetest må man velge en glosefil
        glosetest()
    elif(valg==3):
        print("Ha det bra og god påske")
        break
    else:
        print("Ugyldig valg, prøv igjen!")





