# Jagd auf den Wumpus {#hunt-the-wumpus}

Heute werden wir ein Text-Abenteuer-Computerspiel [Jagd auf den Wumpus](https://en.wikipedia.org/wiki/Hunt_the_Wumpus) programmieren: "Im Spiel bewegt sich der Spieler durch eine Reihe von miteinander verbundenen Höhlen, die in einem Dodekaeder angeordnet sind, während sie ein Monster namens Wumpus jagen. Das rundenbasierte Spiel hat den Spieler versucht, tödliche bodenlose Gruben und "super Fledermäuse" zu vermeiden, die sie durch das Höhlensystem bewegen; das Ziel ist es, einen ihrer "krummen Pfeile" durch die Höhlen zu schießen, um den Wumpus zu töten..."

Wie zuvor werden wir mit einem sehr einfachen Programm beginnen und es Schritt für Schritt zur endgültigen Version ausbauen. Der Zweck dieses Kapitels ist es, die Fähigkeiten, die du bereits hast, zu festigen, indem du sie in einem komplexeren Spiel mit mehreren Funktionen, Spielobjekten usw. anwendest. Vergiss nicht, die gesamte Datei zu kommentieren (oberer mehrzeiliger Kommentar, um zu erklären, worum es hier geht), strukturiere deinen Code, kommentiere einzelne Abschnitte und verwende sinnvolle Variablen- und Funktionsnamen. Deine Codekomplexität wird ziemlich hoch sein, daher wirst du den guten Stil benötigen, um dir dabei zu helfen.


Hol dir das [Übungsnotebook](notebooks/Hunt the Wumpus.ipynb), bevor wir starten.

## Kapitel Konzepte
* Verwenden von [sets](#sets).

## Ein Höhlensystem
In unserem Spiel wird der Spieler durch ein System von Höhlen wandern, wobei jede Höhle mit drei anderen Höhlen verbunden ist. Das Layout der Höhle wird eine _KONSTANTE_ sein, daher definieren wir es zu Beginn des Programms wie folgt.

```python
CONNECTED_CAVES = [[1, 4, 5], [2, 0, 7], [3, 1, 9], [4, 2, 11], 
                   [0, 3, 13], [6, 14, 0], [7, 5, 15], [8, 6, 1], 
                   [9, 7, 16], [10, 8, 2], [11, 9, 17], [12, 10, 3], 
                   [13, 11, 18], [14, 12, 4], [5, 13, 19], [16, 19, 6], 
                   [17, 15, 8], [18, 16, 10], [19, 17, 12], [15, 18, 14]]
```

Lassen uns das entschlüsseln. Du hast eine Liste von zwanzig Elementen (Höhlen). Innerhalb jeden Elements ist eine Liste von verbundenen Höhlen (Höhlen, zu denen du reisen kannst). Das bedeutet, dass du, wenn du in Höhle Nr. 1 (Index `0`) bist, verbunden bist mit `CONNECTED_CAVES[0]` → `[1, 4, 5]` (beachte, dass auch diese Zahlen im Inneren nullbasierte Indizes sind!). Um also zu sehen, welchen Index die zweite mit der ersten verbundene Höhle hat, würdest du `CONNECTED_CAVES[0][1]` schreiben (du erhältst das erste Element der Liste und dann das zweite Element der Liste aus dem Inneren).

Um dem Spieler das Herumwandern zu ermöglichen, müssen wir zunächst wissen, wo er sich befindet. Lass uns eine neue Variable namens `player_location` definieren und einen zufälligen vordefinierten Index zuweisen. Denke über den niedrigsten gültigen Index nach, den du in Python haben kannst (diesen musst du fest verdrahten). Um den höchstmöglichen gültigen Index zu berechnen, musst du die Gesamtzahl der Höhlen kennen, d.h., die Länge - [len()](https://docs.python.org/3/library/functions.html#len) - der Liste. Denke daran, dass die Indizes in Python nullbasiert sind, also überlege, wie du den höchsten gültigen Index aus der Länge berechnest! Nutze diese beiden Indizes und setze den Spieler in eine zufällige Höhle. Hierfür kannst du die Funktion [randint](https://docs.python.org/3/library/random.html#random.randint) verwenden. Schau in den vorherigen Kapiteln nach, falls du vergessen hast, wie man sie benutzt.

Unser Spieler muss wissen, wohin er gehen kann, also müssen wir in jeder Runde die Informationen darüber ausgeben, in welcher Höhle sich der Spieler befindet und über die verbindende Höhle (verwende [String-Formatierung](#string-formatting), um dies schön aussehen zu lassen). Lass uns das unser erster Code-Ausschnitt für das Spiel sein. Der Code sollte so aussehen

```python
# Import randint

# Definiere CONNECTED_CAVES (einfach die Definition kopieren und einfügen)

# Erstelle Variable `player_location` und weise ihr einen zufälligen gültigen Index zu 
# Spieler in eine zufällige Höhle setzen

# Ausgabe des aktuellen Höhlenindexes und der Indizes der verbundenen Höhlen. Verwende String-Formatierung.
```

::: {.program}
Füge deinen Code in _code01.py_ ein.
:::

## Herumwandern
Jetzt, da der Spieler "sehen" kann, wo er sich befindet, lass ihn herumwandern! Verwende die Funktion `input()`, um den Index der Höhle abzufragen, in die der Spieler gehen möchte, und "bewege" den Spieler in diese Höhle (welche Variable musst du ändern?). Denke daran, dass `input()` einen String zurückgibt, daher musst du ihn explizit in eine Ganzzahl umwandeln (siehe das [Zahlenraten](#guess-the-number-single-round) Spiel, wenn du vergessen hast, wie man das macht). Gib vorerst nur gültige Zahlen ein, da wir später Überprüfungen hinzufügen werden. Um das Herumwandern kontinuierlich zu gestalten, setze es in eine [While-Schleife](#while-loop), sodass der Spieler herumwandert, bis er zur Höhle Nr. 5 (Index `4`!) gelangt. Wir werden später sinnvollere Spiel-Ende-Bedingungen haben, aber dies ermöglicht es dir, das Spiel zu beenden, ohne es von außen zu unterbrechen. Der Code sollte wie folgt aussehen (achte auf deine Einrückungen!).


```python
# import randint function

# define CONNECTED_CAVES (simply copy-paste the definition)

# create `player_location` variable and set it to a random valid cave index

# solange der Spieler nicht in der Höhle Nr. 5 ist (Index 4):
    # Ausgabe des aktuellen Standorts und Liste der verbundenen Höhlen. Verwende String-Formatierung.
    # Eingabeaufforderung, in welche Höhle der Spieler gehen möchte und "verschiebung" des Spielers
    
# Ausgabe einer schönen Game-Over-Nachricht
```

::: {.program}
Füge deinen Code in _code02.py_ ein.
:::

## Prüfen, ob ein Wert _in_ der Liste ist[#in-collection]
Momentan vertrauen wir dem Spieler (naja, dir), den korrekten Index für die Höhle einzugeben. Daher wird das Programm den Spieler zu einer neuen Höhle versetzen, selbst wenn du einen Index einer Höhle eingibst, die nicht mit der aktuellen verbunden ist. Noch schlimmer ist, dass es versuchen wird, den Spieler zu einer undefinierten Höhle zu versetzen, wenn du einen Index größer als 19 eingibst. Um zu prüfen, ob ein eingegebener Index mit einer der verbundenen Höhlen übereinstimmt, musst du die bedingte Anweisung [<value> in <list>](https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions) verwenden. Die Idee ist einfach, wenn der Wert in der Liste ist, ist die Aussage `True`, wenn nicht, ist sie `False`.


```python
x = [1, 2, 3]
print(1 in x)
#> True
print(4 in x)
#> False
```

Beachte, dass du jeweils _einen_ Wert/Objekt prüfen kannst. Da eine Liste auch ein einzelnes Objekt ist, prüfst du, ob sie ein Element der anderen Liste ist, und nicht, ob alle oder einige ihrer Elemente darin enthalten sind.


```python
x = [1, 2, [3, 4]]
# Das ist Falsch, weil x kein Element [1, 2] hat, sondern nur 1 und 2 (getrennt voneinander).
print([1, 2] in x)
#> False

# Das ist wahr, weil x das Element [3, 4] hat.
print([3, 4] in x)
#> True
```

::: {.practice}
Mache Übung #1.
:::

## Gültigen Höhlenindex prüfen
Jetzt, da du weißt, wie man prüft, ob ein Wert in der Liste ist, lass uns das verwenden, um den Höhlenindex zu validieren. Bevor du den Spieler bewegst, musst du jetzt prüfen, ob der eingegebene Index in der Liste der verbundenen Höhlen enthalten ist. Wenn dies `True` ist, bewegst du den Spieler wie zuvor. Andernfalls gib eine Fehlermeldung aus, z. B. "Falscher Höhlenindex!" ohne den Spieler zu bewegen. Die Schleife stellt sicher, dass der Spieler erneut zur Eingabe aufgefordert wird, sodass wir uns darüber im Moment keine Sorgen machen müssen. Hier musst du eine temporäre Variable erstellen, um die Eingabe des Spielers zu speichern, da du ihre Gültigkeit prüfen musst _bevor_ du entscheidest, ob du den Spieler bewegst. Du machst das Letztere nur, wenn der Wert in dieser temporären Variable ein Index einer der verbundenen Höhlen ist! 

Ändere deinen Code, um die Überprüfung der Eingabegültigkeit einzuschließen.

::: {.program}
Füge deinen Code in _code03.py_ ein.
:::

## Überprüfung, ob eine Zeichenfolge in eine ganze Zahl umgewandelt werden kann {#isdigit}
Es gibt eine weitere Gefahr bei unserer Eingabe: Der Spieler ist nicht garantiert eine gültige Ganzzahl einzugeben! Bisher haben wir uns darauf verlassen, dass du dich benimmst, aber im wirklichen Leben werden die Leute, selbst wenn sie nicht absichtlich versuchen, dein Programm zu stören, gelegentlich die falsche Taste drücken. Daher müssen wir überprüfen, ob die _Zeichenfolge_, die sie eingegeben haben, in eine _Ganzzahl_ umgewandelt werden kann.

Die Python-Zeichenkette ist ein Objekt (mehr dazu in ein paar Kapiteln) mit verschiedenen Methoden, die es ermöglichen, verschiedene Operationen an ihnen durchzuführen. Eine Teilmenge von Methoden ermöglicht es dir, eine grobe Überprüfung ihres Inhalts durchzuführen. Die Methode, die uns interessiert, ist [str.isdigit()](https://docs.python.org/3/library/stdtypes.html#str.isdigit), die überprüft, ob alle Symbole Ziffern sind und dass die Zeichenfolge nicht leer ist (sie hat mindestens ein Symbol). Du kannst dem obigen Link folgen, um andere Alternativen wie `str.islower()`, `str.isalpha()`, usw. zu überprüfen.

::: {.practice}
Mache Übung #2.
:::

## Überprüfung der gültigen Ganzzahleneingabe
Ändere den Code, der die Eingabe vom Benutzer erhält. Speichere zuerst die rohe Zeichenkette (nicht in eine Ganzzahl umgewandelt!) in einer Zwischenvariable. Wenn diese Zeichenkette dann nur aus Ziffern besteht, konvertiere sie in eine Ganzzahl und überprüfe dann, ob es sich um einen gültigen verbundenen Höhlenindex handelt (Verschieben des Spielers oder Ausgeben einer Fehlermeldung). Wenn die Eingabezeichenkette jedoch nicht nur aus Ziffern besteht, gib nur die Fehlermeldung aus ("Ungültiger Höhlenindex!"). Dies bedeutet, dass du eine if-Anweisung in der if-Anweisung haben musst!

::: {.program}
Füge deinen Code in _code04.py_ ein.
:::

## Den Code in einer Funktion kapseln
Dein Code ist bereits in seiner Komplexität gewachsen, mit zwei Überprüfungen auf einer Eingabefunktion, daher macht es Sinn, diese Komplexität zu verbergen, indem man ihn in einer Funktion kapselt. Nennen wir es `input_cave`, da es nur eine Eingabe für einen gültigen Index einer verbundenen Höhle sein wird. Du hast bereits den gesamten Code, den du brauchst, aber denke darüber nach, welchen Parameter (oder welche Parameter?) es benötigt: Du kannst nicht direkt auf die globale Konstante `CONNECTED_CAVES` oder die globale Variable `player_location` zugreifen!

Lege die Funktion in eine separate `utils.py` Datei, dokumentiere sowohl die Datei als auch die Funktion! Importiere und verwende sie im Hauptskript. Dein Programm sollte _genau_ wie zuvor laufen!

::: {.program}
Lege `input_cave` in _utils.py_ ab.
<br/>
Aktualisiere deinen Code in _code05.py_.
:::

## Mengen {#sets}

Bisher hatten wir nur den Spieler im Auge und wir haben das getan, indem wir seinen Standort in der Variable `player_location` gespeichert haben. Da wir jedoch mehr Spielobjekte hinzufügen werden (bodenlose Gruben, Fledermäuse, den Wumpus), müssen wir den Überblick behalten, wer-wo-ist, damit wir sie nicht in einer bereits besetzten Höhle platzieren. Wir werden dies als Gelegenheit nutzen, um etwas über [sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) zu lernen: eine _ungeordnete_ Sammlung von _einzigartigen_ Elementen. Diese sind eine Implementierung von [mathematischen Mengen](https://de.wikipedia.org/wiki/Menge_(Mathematik)) und haben Eigenschaften, die für unsere notwendige Buchhaltung nützlich sind. Du erstellst eine Menge über die Funktion [set()](https://docs.python.org/3/library/stdtypes.html#set) und es kann entweder eine leere Menge sein (zu der du `.add()` hinzufügen kannst) oder es kann eine Liste (oder ein Tupel) in eine Menge umwandeln, aber es wird alle Duplikate entfernen.


```python
# Beginnen mit einer leeren Menge
a_set = set()
a_set.add(1)
print(a_set)
#> {1}
a_set.intersection()
#> {1}

# Umwandlung einer Liste in eine Menge
print(set([1, 2, 2, 3]))
#> {1, 2, 3}
```

Wenn du zwei Mengen hast, kannst du verschiedene Operationen durchführen, um die [Vereinigung](https://docs.python.org/3/library/stdtypes.html#frozenset.union), [Schnittmenge](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection)oder [Differenz](https://docs.python.org/3/library/stdtypes.html#frozenset.difference) zwischen zwei Mengen zu finden (siehe _Grundlegende Operationen_ in der [Wikipedia](https://de.wikipedia.org/wiki/Menge_(Mathematik)).

::: {.practice}
Mache Übung #3.
:::

Beachte bitte, dass die Menge _nicht geordnet_ ist, so dass du nicht auf ihre einzelnen Elemente zugreifen kannst. Allerdings kannst du genauso wie bei Listen überprüfen, ob ein Wert in der Menge ist.

```python
a_set = set([1, 2, 3, 3])
3 in a_set
#> True
```


## Die Belegung von Höhlen im Auge behalten
Jetzt, da du Mengen kennst, wird es leicht sein, den Überblick über die belegten Höhlen zu behalten. Im globalen Skript benötigen wir eine Variable, die die Indizes aller belegten Höhlen in einer [Menge](#sets) enthält (du startest mit einer leeren Menge, da alle Höhlen anfangs leer sind). Außerdem benötigen wir eine Funktion, die einen gültigen Index für eine freie Höhle generiert. Dies basiert auf 1) dem Bereich der gültigen Indizes (denke darüber nach, wie du diese Informationen am wirtschaftlichsten an die Funktion weitergeben kannst, du kommst mit nur einer Ganzzahl aus) und 2) den Indizes der bereits belegten Höhlen (wir haben das in der globalen Variable, die du definierst, aber du kannst auf diese Variable _nicht_ direkt zugreifen, also _musst_ du diese Information als Parameter übergeben!).

Wir werden diese Funktion zweimal schreiben. Zunächst verwenden wir eine Brute-Force-Methode, um eine freie Höhle zu finden: Erzeuge einfach in einer Schleife einen gültigen zufälligen Index, bis er _nicht_ in der Menge der belegten Höhlen ist. Da er es nicht ist, handelt es sich um eine gültige freie Höhle, also solltest du die Schleife verlassen und diesen Wert zurückgeben. Nenne diese Funktion `find_vacant_cave_bruteforce`, implementiere und dokumentiere sie in `utils.py`, teste sie, indem du sie in ein Jupiter-Notebook kopierst und mehrmals mit verschiedenen fest codierten Mengen von belegten Höhlen ausführst. Überprüfen, dass die gültige Höhle nie in der Menge der belegten Höhlen ist.

::: {.program}
Lege `find_vacant_cave_bruteforce` in _utils.py_ ab.
<br/>
Teste es in Übung 4.
:::

Die Funktion, die du geschrieben hast, funktioniert, ist aber sehr ineffizient und kann ziemlich problematisch sein, wenn unsere Menge an belegten Höhlen lang ist, da du viele Versuche benötigst, bevor du zufällig eine freie findest. Wir können das besser machen, indem wir Mengenoperationen verwenden: Wir können [range](https://docs.python.org/3/library/functions.html#func-range) generieren, es in eine Menge umwandeln, belegte Höhlen davon [subtrahieren](https://docs.python.org/3/tutorial/datastructures.html#sets) (das ergibt eine Menge von unbesetzten Höhlen) und dann einen Wert [auswählen](https://docs.python.org/3/library/random.html#random.choice) (beachte aber, dass du dafür eine Menge in eine [Liste](https://docs.python.org/3/library/stdtypes.html#list) umwandeln musst!). Im letzten Schritt wählen wir zufällig, aber _nur_ aus freien Höhlen, so dass wir keine Schleifen und mehrere Versuche benötigen, um es richtig zu machen.

Implementiere die Funktion `find_vacant_cave` und teste sie mit dem gleichen Code wie zuvor. Du solltest immer nur einen gültigen Index für eine freie Höhle erhalten.

::: {.program}
Lege `find_vacant_cave` in _utils.py_ ab.
<br/>
Teste es in Übung 5.
:::

## Platzieren von bodenlosen Gruben
Jetzt, da wir das Gerüst haben, fügen wir bodenlose Gruben hinzu. Die Idee ist einfach, wir platzieren zwei davon in zufälligen _freien_ Höhlen. Wenn der Spieler in eine Höhle mit einer bodenlosen Grube stolpert, fällt er hinein und stirbt (Spielende). Wir werden den Spieler jedoch warnen, dass seine gegenwärtige Höhle neben einer bodenlosen Grube ist, ohne ihm zu sagen, in welcher Höhle sie genau ist.

Zuerst fügen wir sie hinzu. Dazu erstellen wir eine neue Konstante `NUMBER_OF_BOTTOMLESS_PITS` (ich schlage vor, dass wir sie auf `2` setzen, aber du kannst mehr oder weniger davon haben) und eine neue Variable (`bottomless_pits`), die eine Menge von Indizes von Höhlen mit bodenlosen Gruben in ihnen enthält. Füge bodenlose Gruben mit einer for-Schleife hinzu: Bei jeder Iteration erhalte einen Index einer leeren Höhle (über die Funktion `find_empty_cave`, denke über ihre Parameter nach), füge diesen Index sowohl zu 1) `bottomless_pits` als auch zu 2) `occupied_caves` hinzu, so dass du 1) weißt, wo die bodenlosen Gruben sind und 2) weißt, welche Höhlen belegt sind. Hier ist der Code-Umriss für den Initialisierungsteil (kopiere die Hauptschleife noch nicht). Überprüfe, ob die Zahlen sinnvoll sind (die Anzahl der Höhlen entspricht deinen Erwartungen, der Wert liegt im erwarteten Bereich, es gibt keine Duplikate, usw.)

```python
# Erstelle die Variable `occupied_caves` und initialisiere sie als leere Menge
# Erstelle die Variable `bottomless_pits` und initialisiere sie als leere Menge
# Benutze eine for-Schleife und die range-Funktion, um die for-Schleife NUMBER_OF_BOTTOMLESS_PITS-mal zu wiederholen
#     Generiere einen neuen Standort für die bodenlose Grube über die Funktion find_empty_cave() und füge ihn zu beiden Mengen hinzu
```

::: {.program}
Teste den Code zum Erstellen von bodenlosen Gruben <br/> in Übung 6.
:::

## In eine bodenlose Grube fallen
Jetzt fügen wir eine der Möglichkeiten hinzu, das Spiel zu beenden: Der Spieler fällt in eine bodenlose Grube. Dafür müssen wir nur überprüfen, ob sich der Spieler in jeder Runde gerade in einer Höhle befindet, in der eine bodenlose Grube ist. Wenn das der Fall ist, ist die Höhle des Spielers tatsächlich in der Liste der bodenlosen Gruben, drucke eine traurige Spiel-Ende-Nachricht und `breche` aus der Schleife aus. Darüber hinaus verändern wir die Bedingung der `while` Schleife zu `while True:`, so dass die einzige Möglichkeit, das Spiel zu beenden, darin besteht, in die Grube zu fallen (nicht ganz fair für den Spieler, aber das werden wir später korrigieren).

Füge den Code für das Platzieren von bodenlosen Gruben und das Hineinfallen in sie in das Hauptskript ein. Drucke die Höhlen mit bodenlosen Gruben zu Beginn des Programs aus und wandere in sie hinein, um sicherzustellen, dass dies das Spiel korrekt beendet.

::: {.program}
Aktualisiere deinen Code in _code06.py_.
:::

## Warnung vor einer bodenlosen Grube
Wir müssen dem Spieler die Chance geben, das Schicksal zu vermeiden, in eine bodenlose Grube zu fallen, indem wir ihn warnen, dass eine (oder zwei oder mehr) in der Nähe sind. Zu diesem Zweck müssen wir zusätzliche Informationen _vor_ ihrer Entscheidung, ihren Zug zu machen, ausdrucken. Deine Aufgabe ist es, zu überprüfen, ob eine Höhle sowohl im Set `bottomless_pits` als auch in der aktuellen Liste der verbundenen Höhlen ist. Du kannst eine [for-Schleife](#for-loop) verwenden, aber die Verwendung von Mengenoperationen ist viel einfacher, du musst nur überprüfen, ob eine [Schnittmenge](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection) dieser beiden Mengen leer ist (sie hat null [Länge](https://docs.python.org/3/library/functions.html#len)). Wenn mindestens eine der verbundenen Höhlen eine bodenlose Grube in sich hat, drucke "Du fühlst einen Hauch!".

::: {.program}
Füge deinen Code in _code07.py_ ein.
:::

## Platzierung von Fledermäusen und Warnung vor ihnen
Wir brauchen mehr Nervenkitzel! Lassen wir Fledermäusen hinzu. Sie leben in Höhlen, der Spieler kann sie hören, wenn sie in einer verbundenen Höhle sind ("Du hörst Flügelschläge!"), aber wenn der Spieler unabsichtlich die Höhle mit Fledermäusen betritt, tragen sie den Spieler zu einer _zufälligen_ Höhle.

Die Platzierung der Fledermäuse ist analog zur Platzierung der bodenlosen Gruben. Du brauchst eine Konstante, die die Anzahl der Fledermauskolonien bestimmt (z.B. `ANZAHL_DER fledermaeuse` und setzte diese auf `2` oder eine andere von dir bevorzugte Zahl), eine Variable, die ein Set mit Indizes von Höhlen mit Fledermäusen hält (z.B. `fledermaeuse`), und du musst zufällige leere Höhlen auswählen und sie genau so in `bats` speichern, wie du es bei den bodenlosen Gruben getan hast. Drucke den Ort der Fledermäuse zu Diagnosezwecken aus. 

Die Warnung vor den Fledermäusen folgt auch der gleichen Logik wie bei den bodenlosen Gruben: Wenn eine der verbundenen Höhlen Fledermäuse in sich hat, druckst du `"Du hörst Flügelschläge!"` aus.

::: {.program}
Füge deinen Code in _code08.py_ ein.
:::

## Der Spieler wird von Fledermäusen in eine zufällige Höhle transportiert
Wenn sich der Spieler in einer Höhle mit Fledermäusen befindet, transportieren diese ihn in eine _zufällige_ Höhle, _unabhängig_ davon, ob die Höhle bewohnt ist oder nicht (also jede Höhle ist eine gültige Höhle). So können die Fledermäuse den Spieler in eine Höhle tragen:

1. mit einer weiteren Fledermaus-Kolonie, und diese wird den Spieler wieder transportieren.
2. mit einer bodenlosen Grube, und der Spieler wird hineinfallen.
3. später in die Höhle mit dem Wumpus (der Spieler überlebt das möglicherweise nicht und du implementierst das jetzt nicht).

Denk darüber nach:

1. _wann_ du die Anwesenheit von Fledermäusen überprüfst (vor oder nach der Überprüfung auf eine bodenlose Grube?),
2. überprüfst du einmal (mit Hilfe von `if`) oder ein-oder-mehrere Male (mit Hilfe von `while`)

Teste deinen Code, indem du in eine Höhle mit Fledermäusen gehst (drucke ihren Standort am Anfang aus, damit du weißt, wo du hingehen musst).

::: {.program}
Füge deinen Code in _code09.py_ ein.
:::

## Hinzufügen von Wumpus (und vom ihm gefressen werden).
Bis jetzt hast du einen Spieler hinzugefügt (Einzelspieler, Standort als Integer gespeichert), bodenlose Gruben (mehrzahl, Standorte in einem Set gespeichert) und Fledermäusen (ebenfalls Mehrzahl). Füge Wumpus hinzu!

1. Erstelle eine neue Variable (`wumpus`?) und platziere Wumpus in einer freien Höhle. Drucke den Standort von Wumpus zu Debugging-Zwecken aus.
2. Warne vor Wumpus im selben Code, der vor Gruben und Fledermäusen warnt. Die Logik ist die gleiche, aber die Überprüfung ist einfacher, da du dir nur um einen einzigen Wumpus-Standort Sorgen machen musst. Der kanonische Warnungstext lautet `"Du riechst einen Wumpus!"`. 
3. Überprüfe, ob der Spieler in der gleichen Höhle wie Wumpus ist. Falls dies der Fall ist, ist das Spiel vorbei, da der Spieler von einem hungrigen Wumpus gefressen wird. Dies ähnelt dem _Spielende_ aufgrund des Sturzes in eine bodenlose Grube. Überlege, ob die Überprüfung vor oder nach der Überprüfung auf Fledermäuse erfolgen sollte.

Teste deinen Code, indem du in eine Höhle mit Wumpus gehst (drucke ihren Standort am Anfang aus, damit du weißt, wohin du gehen musst).

::: {.program}
Füge deinen Code in _code10.py_ ein.
:::

## Dem Spieler eine Chance geben.
Geben wir dem Spieler eine Chance. Wenn er in die Höhle mit dem Wumpus kommt, erschreckt er ihn. Dann läuft Wumpus entweder weg zu einer zufälligen angrenzenden Höhle (neu) oder bleibt stehen und frisst den Spieler. Erstelle zunächst eine neue Konstante, die die Wahrscheinlichkeit definiert, dass Wumpus wegrennt, zum Beispiel `P_WUMPUS_AENGSTLICH`. In den Implementierungen, die ich gefunden habe, beträgt sie typischerweise 0,25, aber verwende einen Wert, den du für angemessen hältst.

Wenn also der Spieler in der Höhle mit dem Wumpus ist, ziehe eine zufällige Zahl zwischen 0 und 1 (verwende dafür die Funktion [uniform](https://docs.python.org/3/library/random.html#random.uniform)). Sie ist Teil der [random](https://docs.python.org/3/library/random.html) Bibliothek, daher lautet der Aufruf `random.uniform(...)`. Denke daran, dass du entweder die _gesamte_ Bibliothek importieren und dann deren Funktion durch Voranstellen des Bibliotheksnamens aufrufen kannst oder du importierst nur eine bestimmte Funktion über `from ... import ...`. Sobald du die Zahl zwischen 0 und 1 generiert hast, wenn diese Zahl _kleiner_ ist als die Wahrscheinlichkeit, dass der Wumpus Angst hat, bewege ihn zu einer zufälligen angrenzenden Höhle (Fledermäuse ignorieren Wumpus und es klammert sich an die Decke der Höhlen, bodenlose Gruben sind also kein Problem für ihn). Eine nützliche Funktion, die du bereits verwendet hast, ist [choice()](https://docs.python.org/3/library/random.html#random.choice), auch Teil der [random](https://docs.python.org/3/library/random.html) Bibliothek. Andernfalls, wenn Wumpus nicht weggeschreckt wurde, wird der Spieler gefressen und das Spiel ist vorbei (das einzige Ergebnis in _code10_).

::: {.program}
Füge deinen Code in _code11.py_ ein.
:::

## Flug eines krummen Pfeils
Unser Spieler ist mit _krummen_ Pfeilen bewaffnet, die durch Höhlen fliegen können. Die Regeln für seinen Flug sind folgende:

* Der Spieler entscheidet, in welche Höhle er einen Pfeil schießt und wie weit der Pfeil fliegt (von 1 bis 5 Höhlen).
* Jedes Mal, wenn der Pfeil in die nächste Höhle fliegen muss, wird diese Höhle zufällig aus den angrenzenden Höhlen _ausgewählt_, mit Ausnahme der Höhle, aus der er kam (also der Pfeil kann keine 180° Wende machen und es stehen nur zwei von drei Höhlen zur Auswahl).
* Wenn der Pfeil in eine Höhle mit Wumpus fliegt, ist er besiegt und das Spiel ist gewonnen.
* Wenn der Pfeil in eine Höhle mit dem Spieler fliegt, dann hat er einen unbeabsichtigten Selbstmord begangen und das Spiel ist verloren.
* Wenn der Pfeil seine letzte Höhle erreicht hat (basierend darauf, wie weit der Spieler schießen wollte) und die Höhle leer ist, fällt er auf den Boden.
* Fledermäuse oder bodenlose Gruben haben keinen Einfluss auf den Pfeil.

Die Gesamtzahl der Pfeile, die der Spieler zu Beginn hat, sollte in der Konstante `PFEIL_ANZAHL` definiert werden (z.B. `5`).

Um den Überblick über den Pfeil zu behalten, benötigst du folgende Variablen:

* `pfeil`: aktuelle Position des Pfeils.
* `pfeil_vorherige_höhle`: Index der Höhle, aus der der Pfeil kam, so dass du weißt, wohin er nicht zurückfliegen kann.
* `verbleibende_schussdistanz`: verbleibende zu reisende Distanz.
* `verbleibende_pfeile`: Anzahl der verbleibenden Pfeile (auf `PFEIL_ANZAHL` gesetzt, wenn das Spiel beginnt).

Behalte dieses Gerüst im Hinterkopf und lass uns anfangen, unsere Pfeile zu programmieren.


## Zufällige Höhle, aber keine U-Turn
Du musst eine Funktion programmieren (nennen wir sie `next_arrow_cave()`), die eine zufällige Höhle auswählt, aber nicht die vorherige Höhle, in der der Pfeil war. Es sollte zwei Parameter haben:

* `connected_caves`: eine Liste von verbundenen Höhlen.
* `previous_cave`: Höhle, aus der der Pfeil gekommen ist.

Zuerst, debugge den Code in einer separaten Zelle. Nehme an, dass `connected_caves = CONNECTED_CAVES[1]` (also, der Pfeil ist derzeit in Höhle 1) und `previous_cave = 0` (Pfeil kam aus Höhle 0). Schreibe den Code, der eine der verbleibenden Höhlen zufällig auswählt (in diesem Fall entweder `2` oder `7`), du willst wahrscheinlich Mengenoperationen verwenden (wie bei der effizienten Platzierung von Spielobjekten). Sobald der Code funktioniert, mache daraus eine Funktion, die die nächste Höhle für einen Pfeil zurückgibt. Dokumentiere die Funktion. Teste sie mit anderen Kombinationen von verbundenen und vorherigen Höhlen.

::: {.program}
Teste deinen Code in Übung #7.<br/>
Sobald getestet, packe die Funktion in _utils.py_.
:::

## Zurückgelegte Entfernung
Jetzt, da du eine Funktion hast, die zur nächsten zufälligen Höhle fliegt, implementiere das Fliegen mit einer for-Schleife. Ein Pfeil sollte durch `shooting_distance` Höhlen fliegen (setze es für den Test auf `5`, maximale Entfernung, von Hand). Die _erste_ Höhle ist gegeben (sie wird vom Spieler ausgewählt), setze daher `arrow` auf `1` und `arrow_previous_cave` auf `0` (Spieler ist in Höhle `0` und hat den Pfeil in Höhle `1` geschossen). Drucke aus Debugging-Zwecken den Standort des Pfeils bei jeder Iteration aus. Teste den Code, indem du die `shooting_distance` änderst. Setzen sie insbesondere auf `1`. Der Pfeil sollte bereits in Höhle `1` "herunterfallen".

Verwende für dieses eine abgespeckte Version des Codes mit der Konstante `CONNECTED_CAVES`, der importierten Funktion `next_arrow_cave()` und allen relevanten Konstanten und Variablen für den Pfeil. Gib die Anfangshöhle, die vorherige Höhle und die Entfernung von Hand ein.

::: {.program}
Füge deinen Code in _code12.py_ ein.
:::

## Ein Ziel treffen
Implementiere die Prüfung zum Treffen des Wumpus oder des Spielers in der Schleife. Sollte die Überprüfung vor oder nach dem Fliegen des Pfeils zur nächsten zufälligen Höhle stattfinden? In beiden Fällen schreibe eine passende "Spiel vorbei" Nachricht und brich aus der Schleife aus. Teste den Code, indem du den Wumpus von Hand in die Höhle platzierst, auf die der Spieler schießt oder die nächste. 

Du kannst auf den Code aus dem vorherigen Abschnitt aufbauen, aber füge `player_location` und `wumpus` Variablen hinzu und kodiere sie von Hand für das Debugging. Führe den Code mehrmals aus, um zu überprüfen, dass er funktioniert.

::: {.program}
Füge deinen Code in _code13.py_ ein.
:::

## Bewegen oder schießen?
Wir sind fast fertig, aber bevor wir anfangen können, den Code zusammenzustellen, benötigen wir noch ein paar weitere Dinge. Zum Beispiel konnte der Spieler zuvor nur ziehen, also haben wir einfach nach der nächsten Höhlennummer gefragt. Jetzt hat der Spieler bei jedem Zug die Wahl, einen Pfeil abzuschießen oder sich zu bewegen. Implementiere eine Funktion `input_shoot_or_move()`, die keine Parameter hat und `"s"` für "Schießen" oder `"m"` für "Bewegen" zurückgibt. Frage darin den Spieler nach seiner Wahl, bis er eine von zwei gültigen Optionen auswählt. Konzeptionell ist dies sehr ähnlich zu deiner anderen Eingabefunktion `input_cave()`, die wiederholt eine Eingabe fordert, bis eine gültige gegeben ist. Teste und dokumentiere!

::: {.infobox .program}
Füge `input_shoot_or_move()` in _utils.py_ ein<br/>Teste es in Übung 8.
:::

## Wie weit?
Implementiere die Funktion `input_distance()`, die keine Parameter hat und die gewünschte Schussentfernung zwischen `1` und `5` zurückgibt. Frage erneut wiederholt nach einer _ganzzahligen_ Eingabe (denke daran, du weißt, wie man überprüfen kann, ob die Eingabe eine gültige Ganzzahl ist), wie weit der Pfeil reisen soll, bis eine gültige Eingabe gegeben ist. Dies ist sehr ähnlich zu deinen anderen Eingabefunktionen. Teste und dokumentiere.

::: {.infobox .program}
Füge `input_distance()` in _utils.py_ ein<br/>Teste sie in Übung 9.
:::

## input_cave_with_prompt
Erstellen eine neue Version der Funktion `input_cave()`, nenne sie `input_cave_with_prompt` und füge einen `prompt` Parameter hinzu, damit wir nun entweder nach dem Bewegen zu oder dem Schießen auf die Höhle fragen können (daher die Notwendigkeit des prompts anstelle einer fest codierten Nachricht).

::: {.infobox .program}
Füge `input_cave_with_prompt()` in _utils.py_ ein<br/>Teste sie in Übung 10.
:::

## Alles zusammenfügen
In den letzten Abschnitten hast du alle Teile erstellt, die du für das finale Spiel mit einem krummen Pfeil benötigst. Hier ist ein Pseudocode, wie der finale Code aussehen sollte. Schau dir das an, um besser zu verstehen, wie die neuen Teile in den alten Code integriert werden. Bis jetzt solltest du folgende Konstanten haben (du kannst auch andere Werte haben):

* `CONNECTED_CAVES`
* `NUMBER_OF_BATS` = 2
* `NUMBER_OF_BOTTOMLESS_PITS` = 2
* `P_WUMPUS_SCARED` = 0.25
* `ARROWS_NUMBER` = 5

Folgende Funktionen:

* `find_vacant_cave(...)`, gibt einen Integer-Höhlenindex zurück
* `input_cave_with_prompt(prompt, connected_cave)`, gibt einen Integer-Höhlenindex zurück
* `input_shoot_or_move()`, gibt `"s"` für "schießen" und `"m"` für "bewegen" zurück.
* `input_distance()`, gibt eine Ganzzahl zwischen 1 und 5 zurück
* `next_arrow_cave(connected_caves, previous_cave)`, gibt einen Integer-Höhlenindex zurück

Folgende Variablen:

* `player_location` : Höhlenindex
* `bottomless_pit`: Liste von Höhlenindizes
* `bats`: Liste von Höhlenindizes
* `wumpus`: Höhlenindex
* `remaining_arrows`: Ganzzahl der verbleibenden Pfeile

Dienst-/temporäre Variablen:

* `occupied_caves`: Liste der Höhlenindizes
* `gameover_due_to_arrow` : gibt an, ob das Spiel vorbei ist, weil entweder der Wumpus oder der Spieler von einem Pfeil getroffen wurde
* `arrow`: Standort eines Pfeils, der ursprünglich auf die Wahl des Spielers basiert
* `shooting_distance`: Anzahl der Höhlen, die der Pfeil durchfliegen soll.
* andere pfeilbezogene temporäre Variablen

```
importiere die benötigten Bibliotheken

importiere die benötigten Funktionen aus utils

definiere KONSTANTEN

platziere Spieler, bodenlose Gruben, Fledermäuse und Wumpus
setze die Anzahl der verbleibenden Pfeile auf ARROWS_NUMBER
setze die Variable gameover_due_to_arrow auf False

während WAHR:
    solange der Spieler schießen will und noch Pfeile hat:
        frage nach der Höhle, auf die der Spieler schießen will  (speichere die Antwort in der Variable `arrow`)
        frage, wie weit der Pfeil fliegen soll (speichere die Antwort in der Variable `shooting_distance`)
        
        lass in einer for-Schleife den Pfeil durch die Höhlen fliegen:
            Wenn den Wumpus getroffen -> Glückwunsch Spiel vorbei Nachricht, gameover_due_to_arrow = True und breche aus der Schleife aus
            Wenn den Spieler getroffen -> Oops Spiel vorbei Nachricht, gameover_due_to_arrow = True und breche aus der Schleife aus
            bewege den Pfeil zur nächsten zufälligen Höhle (Funktion next_arrow_cave und Variable arrow)
        verringere die Anzahl der verbleibenden Pfeile (Variable remaining_arrows)
        
    überprüfe, ob das Spiel aufgrund des Pfeils vorbei ist, breche aus der Schleife aus, falls das der Fall ist
        
    frage den Spieler, welche Höhle er betreten möchte und bewege den Spieler
    
    solange der Spieler in der Höhle mit den Fledermäusen ist: 
        bewege den Spieler zu einer zufälligen Höhle
    
    überprüfe die bodenlosen Gruben (Spieler stirbt, breche aus der Schleife aus)
    
    wenn der Spieler in der gleichen Höhle wie der Wumpus ist:
        wenn der Wumpus erschrocken ist
            bewege den Wumpus zu einer zufälligen Höhle
        sonst
            der Spieler ist tot, bricht aus der Schleife aus
```

::: {.infobox .program}
Füge deinen Code in _code14.py_ ein.
:::

## Abschluss
Gut gemacht, das war wirklich ein Abenteuer, diese Höhlen zu erkunden! Zippe und reiche ein.
