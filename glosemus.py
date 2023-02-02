
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
    
    return


def glosetest():

    return

# Hovedprogram
#------------------------------------------
while(True):
    valg = meny()
    #print(f"Du skrev {valg}")

    if(valg==1):
        legginn()
    elif(valg==2):
        glosetest()
    elif(valg==3):
        print("Ha det bra og god påske")
        break
    else:
        print("Ugyldig valg, prøv igjen!")





