#!/usr/bin/python3
from glob import glob
import os

katalog = '/home/erik/Documents/program/glosemus'

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


def skrivtilfil(oppgaver, filnavn=""): 
    """Write a dictionary of strings to file 

    Args:
        oppgaver (dict): dictionary of question and answer strings
        filnavn (str): filename or empty string to ask
    """
    if filnavn == "":
        while(not filnavn.isalnum()):
            filnavn = input("Lagre glosefil med navn: ")

    filnavn += '.glo'
    filnavn = os.path.join(katalog, filnavn)
    with open(filnavn, "wt") as fh:
        for oppgave in oppgaver:
            svar = oppgaver[oppgave]
            fh.write(f"{oppgave}|{svar}\n")
    print(f"Lagret gloser i filen {filnavn}\n")
    return


def lesfrafil(filnavn):
    filnavn += '.glo'
    filnavn = os.path.join(katalog, filnavn)
    qna = {}
    with open(filnavn, "rt") as fh:
        for linje in fh:
            oppgave, svar = linje.strip().split("|")
            qna[oppgave] = svar
    return(qna)


def vurdering(prosent):
    if prosent < 25:
        return "Øvelse gjør mester!"
    elif prosent < 50:
        return "Med litt øvelse kan du nå toppen!"
    elif prosent < 75:
        return "Stå på, du nærmer deg!"
    elif prosent < 100:
        return "Strålende, stå på!"
    else:
        return "Gratulerer, perfekt score!"

def glosetest(oppgaver, glosefil):
    poeng = 0
    mulige = len(oppgaver)
    print(f"\nVelkommen til gloseprøven '{glosefil}' med {mulige} spørsmål!\n")
    for oppgave in oppgaver:
        svar = input(f"{oppgave} -> ")
        if svar == oppgaver[oppgave]:
            print("Riktig, rett og bra!")
            poeng += 1
        else:
            print(f"Nei, og fy, det skulle være: {oppgaver[oppgave]}")
    melding = vurdering(100*poeng/mulige)
    print(f"\n********************************")
    print(melding)
    print(f"Du fikk {poeng} av {mulige} mulige")
    print(f"********************************")
    return

def velgenfil():
    glosefiler = [os.path.splitext( os.path.basename(f))[0] for f in glob(os.path.join(katalog, '*.glo'))]
    N = len(glosefiler)
    filnummer = 0
    print("\nDisse glosefilene finnes i systemet\n--------------------------------------")
    for i, gf in enumerate(glosefiler):
        print(f"{i+1:2d} - {gf}")
    while filnummer < 1 or filnummer > N: 
        filnummer = input(f"Velg en glosefil fra listen : ")
        try:
            filnummer = int(filnummer)
        except:
            filnummer = 0
    filnavn = glosefiler[filnummer-1]
    return filnavn


# Hovedprogram
#------------------------------------------
while(True):
    valg = meny()
    #print(f"Du skrev {valg}")

    if(valg==1):
        qna = legginn()
        skrivtilfil(qna) # skriv ordboken til en fil her
    elif(valg==2):
        # før glosetest må man velge en glosefil
        glosefil = velgenfil()
        qna = lesfrafil(glosefil)
        # kjør gloseprøve
        glosetest(qna, glosefil)
    elif(valg==3):
        print("Ha det bra og god påske")
        break
    else:
        print("Ugyldig valg, prøv igjen!")





