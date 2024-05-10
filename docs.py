####### Uppgift 5 - Docs #######

## Language Reference

#Avgränsing av BNF
if_stmt ::= "if" assignment_expression ":" suite
("elif" assignment_expression ":" suite)*
["else" ":" suite]

#Exempel där man ber användaren ange sin ålder
#if-sats:
age = int(input("Hur gammal är du? "))

# Kontrollerar om personen är myndig eller inte
if age > 18:  # Åldern är större än 18 år
    print("Du är myndig.")
    print("Välkommen till vuxenvärlden!")
elif age >= 13 and age <= 17:  # Åldern är mellan 13 och 17 år
    print("Du är tonåring.")
    print("Upplev tonårens äventyr!")
else:  # Åldern är mindre än 13 år
    print("Du är inte tonåring än.")
    print("Njut av barndomen!")

# > större än
# >= större än eller lika med
# <= mindre än eller lika med
# < mindre än
# == lika med
# != inte lika med

#"if" och "else" delar av "suites". Beroende på värdet av variabeln "age", kommer antingen den första eller andra delen av koden att köras.
#Dessa exempel visar hur "assignment_expression" och "suite" kan användas i olika sammanhang

#Exempel på användning av "assignment_expression" och "suite"
#assignment_expression är "Du är mydndig" "Du är tonåring" osv. så skall då suite skrivas ut baserat på vilken ålders siffra



#2.While-loopar:

while_stmt ::= "while" assignment_expression ":" suite
["else" ":" suite]

#Exempel på en while-loop:

while True:
    try:
        d = int(input("Vad är d? "))
        if d < 0:
            print("Vänligen ange ett positivt heltal eller noll.")
        else:
            break
    except ValueError:
        print("Vänligen ange en giltig siffra.")



#om värdet är mer än 0, då blir det break ut från while-loopen.

#Assignment expression är det uttryck som ska vara sant i detta fallet för att
#Inom en while-loop är "suiten" det kodblock som upprepas så länge villkoret är sant och det är det som utför inom while-satsen.

#Detta upprepar testet flera gånger och om villkoret är uppfyllt, utförs den första delen av koden. Om villkoret är falskt, vilket kan 
#vara fallet vid första testet, körs den efterföljande delen, som är else-satsen. Om inmatningen är giltig fortsätter koden att utföras, 
#annars bryter den loopen med "break" för att undvika oändlig körning.

#En while-loop används för att göra samma sak om och om igen tills något speciellt händer. Istället för att hoppa mellan olika delar av 
#koden upprepas en viss del av koden tills ett värdet är uppnått. När värdet är uppnått fortsätter programmet att köra från där while-loopen 
#slutade.



3. For-loopar:

for_stmt ::= "for" target_list "in" starred_list ":" suite
["else" ":" suite]

#Exempel på for-loop:

for number in [0, 1, 2, 3, 4]:
print(number)

#I detta scenario representerar Target_list de variabler som for-loopen ska gå igenom. Iteration innebär att loopen körs upprepade gånger
#tills alla variabler har behandlats.

#Starred_list är den lista av nummer från 0 till 4 som är angiven inom hakparenteser, vilket skapar listan.

#Suite definierar vad som ska göras inuti loopen, i detta fall att skriva ut siffrorna 0 till 4. Suite är alltså det script som ska köras 
#inuti loopen.

#Denna for-loop betyder helt enkelt att för varje nummer eller objekt i listan ska numret skrivas ut, och detta upprepas fem gånger tills 
#loopen är klar. Således kommer siffrorna 0, 1, 2, 3, och 4 att skrivas ut.




## Standard Library

4.Strängmetoder:

str.casefold() - 
#Det är en metod i Python som används för att konvertera alla bokstäver i en sträng till små bokstäver, 
#vilket ger en fallfällningsversion av strängen. Detta är användbart för att göra strängjämförelser fallskänsliga och 
#för att hantera olika teckenkodningar.
T.ex "Python Programming"
lowercased_text = text.casefold()
print(lowercased_text)
"python programming" - Både konvertera bokstäver i en sträng till små bokstäver som här både bokstäverna "P" blev "p"



str.capitalize() - 
#Är en metod i Python som används för att konvertera den första bokstaven i en sträng till en versal och resten av bokstäverna till små.
T.ex "jag heter David!"
storbokstav är samma betydelse som - text.capitalize()
print(storbokstav)
"Jag heter David!" - Första bokstaven J har ändrats till en större bokstav



str.replace() - 
#Det är en metod som används för att ersätta alla förekomster av en viss delsträng med en annan delsträng
#inom en större sträng.
#Exempel:
text = "Jag älskar att äta äpplen."
ny_text = text.replace("älskar", "gillar")
print(ny_text)
Exempel ersätt alla förekomster av ordet "älskar" med ordet "gillar" i strängen. Resultatet blir:
"Jag gillar att äta äpplen."


str.islower(): 
#Denna kollar ifall alla bokstäver i strängen är skrivna med små bokstäver (versaler), till exmpel: david eller adam. 
#Detta kommer då ge ett värde som är sant eller falskt.
#Exempel:
print(("david").islower()) = Sant
print(("DavID").islower()) = Falskt

5.Sekvenstyper och deras operationer:

Svar:

# Jag skapar en lista nedan:
lista = [3, 6, 9, 19, 21, 33, 39]

# Nu adderar jag numret 69 till lista över
lista.append(69)

# Nu får jag numrena att går från 3-69 till 69-3
lista.reverse()

# detta gör så att listan rensas:
lista.clear()



6.Ordböcker:

Svar:

# För att skapa en dictionary använder du en variabel och specificerar sedan värdena inom krullparenteser {}. 
# Den första delen du specificerar, till exempel "david", kallas för nyckel och värdet, till exempel 3, blir då värdet till nyckeln. 
# En dictionary är föränderlig (mutable), vilket innebär att den kan ändras efter att den har skapats.

namn = {}

# Det finns 3 David, 1 Adam och 5st Alex.

namn = {"David": 3, "Adam": 1, "Alex": 5}

# För att lägga till Namn i min lista och antalet Namn som finns så skriver man som nedan

namn["Kent"] = 9
namn["Erik"] = 3

# Man kan ändra värde genom att skriva:

namn["David"] = 19

# Hämta värde för en nyckel

print(namn["Kent"]) # Skriver ut 9st Kent

#Loopa igenom nycklar och värden i en namn-dictionary genom att använda en for-loop.

for namn, antal in namn.items():
print(namn, antal)



7.Inbyggda funktioner:


Len() #returnerar längden på antal objekt (number of items). Argumentet kan vara en sträng, bytes, lista, tuple eller range.

Exempel:
lista = [3, 6, 9, 19, 33, 39]
objekt = len(lista)
print("Antal objekt i listan:", objekt)

Print() - #Är en inbyggd funktion som används för att skriva ut text eller andra objekt till konsolen eller terminalen.
#När du anropar print() med ett argument, skrivs värdet av det argumentet ut till standardutgången. Till exempel:
#print("Kent hade rätt!")


Range()
#range() en inbyggd funktion som används för att generera en följd av heltal. Den kan användas på flera sätt,
#men vanligtvis används den i iterationer, såsom i en for-loop, för att generera en sekvens av siffror. 

Exempel:
for i in range(5):
    print(i)

0
1
2
3
4


input()
#input() är en inbyggd funktion som används för att läsa in användarinmatning från tangentbordet under körning av ett program.
#När input() anropas, väntar programmet på att användaren ska ange något från tangentbordet och trycka på Enter. 
#Det inmatade värdet behandlas som en sträng och returneras av input().

Exempel:

name = input("Skriv ditt namn: ")
print("Hej, " + name + "!")

#Det här programmet skulle be användaren att ange sitt namn och sedan skriva ut en hälsning med det inmatade namnet