# Guess the Number: KI ist dran {#guess-the-number-ai}
Lass uns das Spiel Rate die Zahl _noch einmal_ programmieren^[Das ist das letzte Mal, versprochen!] aber die Rollen _umkehren_. Jetzt wählst _du_ eine Zahl und der Computer wird versuchen, sie zu erraten. Denke über den Algorithmus nach, den ein Computer dafür verwenden könnte, bevor du den nächsten Absatz liest^[Du solltest dir vorstellen, dass ich Dora die Entdeckerin bin, die dich dabei beobachtet, wie du nachdenkst.].

Der optimale Weg, dies zu tun, besteht darin, die Mitte des Intervalls für eine Vermutung zu verwenden. Auf diese Weise schließt du _die Hälfte_ der Zahlen aus, die entweder größer oder kleiner sind als deine Vermutung (oder du errätst die Zahl korrekt, natürlich). Wenn du also weißt, dass die Zahl zwischen 1 und 10 liegt, solltest du die Dinge in der Mitte teilen, also 5 oder 6 wählen, da du nicht 5,5 wählen kannst (wir gehen davon aus, dass du nur ganze Zahlen verwenden kannst). Wenn dein Gegner dir sagt, dass seine Zahl größer ist als deine Wahl, weißt du, dass sie irgendwo zwischen deiner Vermutung und der ursprünglichen Obergrenze liegen muss, z. B. zwischen 5 und 10. Umgekehrt, wenn der Gegner "niedriger" antwortet, liegt die Zahl zwischen der unteren Grenze und deiner Vermutung, z. B. zwischen 1 und 5. Bei deinem nächsten Versuch teilst du das neue Intervall und wiederholst dies, bis du entweder die richtige Zahl errätst oder nur noch ein Intervall mit nur einer Zahl übrig hast. Dann musst du nicht mehr raten.

Um dieses Programm zu implementieren, musst du Funktionen kennen lernen, wie man sie dokumentiert und wie man eigene Bibliotheken verwendet. Hol dir das [Übungsnotebook](notebooks/Guess the number - AI.ipynb), bevor wir anfangen!

## Konzepte des Kapitels.

* Schreiben deiner eigenen [Funktionen](#function).
* Verstehen von variablen [Bereichen](#scopes-for-immutable-values).
* Annahme von [standardisierten Wegen](#numpy-docstring), um deinen Code zu dokumentieren.
* Verwendung deiner eigenen [Bibliotheken](#using-you-own-libraries).

## Spielerantwort{#guess-the-number-players-response}
Lass uns warm werden, indem wir einen Code schreiben, der es einem Spieler ermöglicht, auf den Tipp des Computers zu reagieren. Denke daran, es gibt nur drei Möglichkeiten: deine Zahl ist größer, kleiner oder gleich der Vermutung des Computers. Ich würde vorschlagen, die Symbole `>`, `<` und `=` zu verwenden, um dies zu kommunizieren. Du musst den Code schreiben, der den Spieler auffordert, seine Antwort einzugeben, bis er eines dieser Symbole eingibt. D.h., die Aufforderung zur Eingabe sollte wiederholt werden, wenn sie etwas anderes eingeben. Du musst also definitiv die [input([prompt])](https://docs.python.org/3/library/functions.html#input) und eine [while](#while-loop) Schleife verwenden. Überlege dir eine nützliche und informative Aufforderungsnachricht dafür. Teste, ob es funktioniert. Breakpoints können hier sehr hilfreich sein.

::: {.program}
Füge deinen Code in `code01.py` ein.
:::

## Funktionen {#function}
Du weißt bereits, wie man Funktionen verwendet, jetzt ist es an der Zeit, mehr darüber zu lernen, warum du dich darum kümmern solltest. Der Zweck einer Funktion besteht darin, bestimmten Code, der eine einzige Berechnung durchführt, zu isolieren und ihn somit testbar und wiederverwendbar zu machen. Lass uns den letzten Satz Stück für Stück anhand von Beispielen durchgehen.

### Eine Funktion führt eine einzige Berechnung durch
Ich habe dir bereits [erzählt](#programming-tips), dass das Lesen von Code einfach ist, weil jede Aktion für Computer auf einfache und klare Weise ausgedrückt werden muss. Allerdings können _viele_ einfache Dinge sehr überwältigend und verwirrend sein. Denke an den finalen Code vom letzten Seminar: Wir hatten zwei Schleifen mit bedingten Anweisungen, die darin verschachtelt waren. Füge ein paar mehr hinzu und du hast so viele Zweige zu verfolgen, dass du nie ganz sicher sein kannst, was passieren wird. Das liegt daran, dass unsere Wahrnehmung und unser Arbeitsgedächtnis, die du benutzt, um alle Zweige zu verfolgen, auf nur etwa vier Elemente beschränkt sind^[Die offizielle magische Zahl ist [7±2](https://de.wikipedia.org/wiki/Magische_Zahl_7_plus_oder_minus_2) aber wenn man das Originalpapier liest, stellt man fest, dass dies für die meisten von uns eher vier sind].

Daher sollte eine Funktion _eine_ Berechnung / Aktion durchführen, die konzeptionell klar ist und deren Zweck direkt aus ihrem Namen oder höchstens aus einem einzelnen Satz, der sie beschreibt, verstanden werden sollte^[Dies ist ähnlich wie beim wissenschaftlichen Schreiben, wo ein einzelner Absatz eine einzelne Idee vermittelt. Mir hilft es, zuerst die Idee des Absatzes in einem einzigen Satz zu schreiben, bevor ich den Absatz selbst schreibe. Wenn ein Satz nicht ausreicht, muss ich den Text in mehrere Absätze aufteilen.]. Der Name einer Funktion sollte typischerweise ein _Verb_ sein, denn es geht darum, eine Aktion auszuführen. Wenn du mehr als einen Satz brauchst, um zu erklären, was die Funktion tut, solltest du erwägen, den Code weiter aufzuteilen. Das bedeutet nicht, dass die gesamte Beschreibung/Dokumentation in einen einzigen Satz passen muss. Die vollständige Beschreibung kann lang sein, insbesondere wenn die zugrunde liegende Berechnung komplex ist und es viele Parameter zu berücksichtigen gibt. Dies sind jedoch optionale Details, die dem Leser sagen, _wie_ die Funktion ihre Aufgabe erledigt oder wie ihr Verhalten verändert werden kann. Trotzdem sollten sie in der Lage sein, zu verstehen, _was_ die Aufgabe ist, nur aus dem Namen oder aus einem einzigen Satz. Ich wiederhole mich und betone dies so sehr, weil konzeptionell einfache Funktionen, die nur eine Aufgabe erfüllen, die Grundlage für einen klaren, robusten, wiederverwendbaren Code sind. Und das zukünftige Du wird sehr dankbar sein, dass es mit dem einfach zu verstehenden, isolierten, zuverlässigen Code arbeiten muss, den du geschrieben hast.

### Funktion isoliert Code vom Rest des Programms
Isolierung bedeutet, dass dein Code in einem separaten Bereich ausgeführt wird, in dem nur Funktionselemente (begrenzte Anzahl von Werten, die du von außen mit fester Bedeutung übergibst) und lokale Variablen, die du innerhalb der Funktion definierst, existieren. Du hast keinen Zugriff auf Variablen, die im außenstehenden Skript definiert sind^[Das ist streng genommen nicht wahr, aber das wird uns erst betreffen, wenn wir zu so genannten "veränderlichen" Objekten wie Listen oder Wörterbüchern kommen.] oder auf Variablen, die in anderen Funktionen definiert sind. Umgekehrt haben weder das globale Skript noch andere Funktionen Zugriff auf Variablen und Werte, die du innen verwendest. Das bedeutet, dass du nur den Code _innerhalb_ der Funktion studieren musst, um zu verstehen, wie sie funktioniert. Entsprechend sollte der Code, den du schreibst, _unabhängig_ von jedem globalen Kontext sein, in dem die Funktion verwendet werden kann. Die Isolierung ist sowohl praktisch (kein Zugriff auf Variablen von außen während der Laufzeit bedeutet weniger Chancen, dass Dinge schrecklich schief gehen) als auch konzeptionell (kein weiterer Kontext ist erforderlich, um den Code zu verstehen).

### Funktion macht Code einfacher zu testen
Du kannst sogar mäßig komplexe Programme nur dann erstellen, wenn du sicher sein kannst, was individuelle Codeabschnitte unter jeder möglichen Bedingung tun. Erzeugen sie die richtigen Ergebnisse? Scheitern sie deutlich und heben sie einen richtigen Fehler hervor, wenn die Eingaben falsch sind? Verwenden sie bei Bedarf Standardwerte? Wenn du jedoch alle Teile zusammen testest, bedeutet das eine extreme Anzahl von Durchläufen, da du alle möglichen Kombinationen von Bedingungen für einen Teil testen musst, gegeben alle möglichen Bedingungen für einen anderen Teil usw. Funktionen machen dein Leben viel einfacher. Da sie einen einzigen Einstiegspunkt, eine feste Anzahl von Parametern, einen einzigen Rückgabewert und Isolation (siehe oben) haben, kannst du sie unabhängig von anderen Funktionen und dem Rest des Codes einzeln testen. Dies nennt man _Unit Testing_ und es ist ein intensiver Einsatz von [automatischem Unit Testing](https://docs.python.org/3/library/unittest.html)^[Es ist normal, mehr Code für Tests zu haben als für das eigentliche Programm.] das sicherstellt, dass der Code für die absolute Mehrheit der Programme und Apps, die du verwendest, zuverlässig ist^[Man braucht trotzdem noch Tests für das integrierte System, aber das Testen einzelner Funktionen ist eine klare Voraussetzung.].

### Funktion macht Code wiederverwendbar
Manchmal wird dies als Hauptgrund angegeben, Funktionen zu verwenden. Wenn du den Code in eine Funktion umwandelst, bedeutet das, dass du die Funktion aufrufen kannst, anstatt den Code zu kopieren und einzufügen. Der letztere Ansatz ist eine schreckliche Idee, da es bedeutet, dass du denselben Code an vielen Stellen pflegen musst und du vielleicht nicht einmal sicher bist, an wie vielen. Das ist ein Problem, selbst wenn der Code extrem einfach ist. Hier definieren wir einen _standardisierten_ Weg, ein Initial zu berechnen, indem wir das erste Symbol aus einer Zeichenkette nehmen (du wirst später mehr über Indexierung und Slicing erfahren). Der Code ist so einfach wie möglich.
```python
...
initial = "test"[0]
...
initial_for_file = filename[0]
...
initial_for_website = first_name[0]
...
```

Stell dir vor, du hast beschlossen, es zu ändern und die ersten _zwei_ Symbole zu verwenden. Wiederum ist die Berechnung nicht kompliziert, verwende einfach `[0]` ersetzen mit `[:2]`. Du musst es aber für _allen_ Code tun, der diese Berechnung durchführt. Und du kannst die Option _Alles Ersetzen_ nicht verwenden, weil du manchmal das erste Element für andere Zwecke verwenden könntest. Und wenn du den Code bearbeitest, wirst du zwangsläufig einige Stellen vergessen (ich mache das die ganze Zeit), was die Dinge noch inkonsistenter und verwirrender macht. Code in eine Funktion zu verwandeln bedeutet, dass du nur an _einer_ Stelle ändern und testen musst. Hier ist der ursprüngliche Code, der über eine Funktion implementiert wurde.
```python
def generate_initial(full_string):
    """Erzeugt ein Initial mit dem ersten Symbol.
    
    Parameter
    ----------
    full_string : str
    
    Gibt zurück
    ----------
    str : einzelnes Symbol
    """
    return full_string[0]

...
initial = generate_initial("test")
...
initial_for_file = generate_initial(filename)
...
initial_for_website = generate_initial(first_name)
...
```

and here is the "alternative" initial computation. Note that the code that uses the function _stays the same_
und hier ist die "alternative" Initialberechnung. Beachte, dass der Code, der die Funktion verwendet, _gleich bleibt_
```python
def generate_initial(full_string):
    """Erzeugt ein Initial mit den ersten ZWEI Symbolen.
    
    Parameter
    ----------
    full_string : str
    
    Gibt zurück
    ----------
    str : zwei Symbole lang
    """
    return full_string[:2]

...
initial = generate_initial("test")
...
initial_for_file = generate_initial(filename)
...
initial_for_website = generate_initial(first_name)
...
```
Daher ist es besonders nützlich, Code in eine Funktion umzuwandeln, wenn der wiederverwendete Code komplex ist, aber es zahlt sich sogar aus, wenn die Berechnung so einfach und trivial ist wie im obigen Beispiel. Mit einer Funktion musst du dir nur um einen einzigen Codeblock Gedanken machen und du kannst sicher sein, dass die gleiche Berechnung immer dann ausgeführt wird, wenn du die Funktion aufrufst (und dass dies nicht mehrere Kopien des Codes sind, die möglicherweise identisch sind oder nicht).

Beachte, dass ich den wiederverwendbaren Code als den letzten und den am wenigsten wichtigen Grund zur Verwendung von Funktionen putze. Dies liegt daran, dass die anderen drei Gründe weitaus wichtiger sind. Konzeptuell klaren, isolierten und testbaren Code zu haben, ist vorteilhaft, selbst wenn du diese Funktion nur einmal aufrufst. Es erleichert das Verständnis und das Testen des Codes und hilft dir, seine Komplexität zu reduzieren, indem du Codeblöcke durch deren Bedeutung ersetzt. Sieh dir das folgende Beispiel an. Der erste Code nimmt das erste Symbol, aber diese Aktion (das erste Symbol nehmen) _bedeutet_ an sich nichts, es ist nur eine mechanische Berechnung. Es ist nur der ursprüngliche Kontext `initial_for_file = filename[0]` oder zusätzliche Kommentare, die ihm seine Bedeutung geben. Im Gegensatz dazu sagt dir das Aufrufen einer Funktion namens _compute_initial_ was passiert, da es den Zweck eindeutig macht. Ich vermute, dass der zukünftige Du sehr pro-Eindeutigkeit und anti-Verwirrung ist.
```python
if filename[0] == "A":
    ...
    
if compute_initial(filename) == "A":
    ...
```

## Funktionen in Python
### Definieren einer Funktion in Python
Eine Funktion in Python sieht so aus (beachte die Einrückung und `:` am Ende der ersten Zeile)
```python
def <funktionsname>(param1, param2, ...):
    einige interne Berechnung
    if bedingung:
        return ein Wert
    return ein anderer Wert
```

Die Parameter sind optional, ebenso der Rückgabewert. Die minimalste Funktion wäre daher
```python
def minimal_function():
    pass # pass bedeutet "mache nichts"
```

Du musst deine Funktion (einmal!) definieren, bevor du sie aufrufst (ein- oder mehrmals). Du solltest also Funktionen _vor_ dem Code erstellen, der sie verwendet.

```python
def do_something():
    """
    Das ist eine Funktion namens "do_something". Sie macht eigentlich nichts.
    Sie benötigt keine Eingabe und gibt keinen Wert zurück.
    """
    return
    
def another_function():
    ...
    # Wir rufen sie in einer anderen Funktion auf.
    do_something()
    ...

# Das ist ein Funktionsaufruf (wir verwenden diese Funktion)
do_something()

# Und wir verwenden sie noch einmal!
do_something()

# Und wieder, aber durch einen another_function Aufruf
another_function()
```
::: {.practice}
Mache Übung #1.
:::
Du musst auch im Hinterkopf behalten, dass das erneute Definieren einer Funktion (oder das Definieren einer technisch anderen Funktion, die den gleichen Namen hat) die ursprüngliche Definition _überschreibt_, so dass nur die _neueste_ Version davon beibehalten und verwendet werden kann.

::: {.practice}
Mache Übung #2.
:::

Obwohl das Beispiel in der Übung das Problem leicht erkennen lässt, kann es in einem großen Code, der sich über mehrere Dateien erstreckt und verschiedene Bibliotheken verwendet, nicht so einfach sein, das gleiche Problem zu lösen!

### Funktionsargumente
Einige Funktionen benötigen möglicherweise keine Argumente (auch Parameter genannt), da sie eine feste Aktion ausführen:
```python
def ping():
    """
    Maschine, die "ping!" macht.
    """
    print("ping!")
```

Du musst jedoch möglicherweise Informationen an die Funktion über Argumente weitergeben, um zu beeinflussen, wie die Funktion ihre Aktion ausführt. In Python listest du einfach Argumente innerhalb der runden Klammern nach dem Funktionsnamen auf (es gibt noch mehr Optionen und Funktionen, aber wir halten es zunächst einfach). Beispielsweise könnten wir eine Funktion schreiben, die das Alter einer Person berechnet und ausgibt, basierend auf zwei Parametern 1) ihrem Geburtsjahr, 2) dem aktuellen Jahr:
```python
def print_age(birth_year, current_year):
    """
    Gibt das Alter aus, gegeben das Geburtsjahr und das aktuelle Jahr.
    
    Parameter
    ----------
    birth_year : int
    current_year : int
    """
    print(current_year - birth_year)
```

Es ist eine **sehr gute Idee**, Funktionen, Parametern und Variablen aussagekräftige Namen zu geben. Der folgende Code wird genau das gleiche Ergebnis liefern, aber das Verständnis _warum_ und _wofür_ es das tut, was es tut, wäre viel schwieriger (also benutze **immer** aussagekräftige Namen!):
```python
def x(a, b):
    print(b - a)
```

Wenn du eine Funktion aufrufst, musst du die korrekte Anzahl von Parametern übergeben und sie in der _richtigen Reihenfolge_ übergeben, ein weiterer Grund für Funktionen Argumente, aussagekräftige Namen zu haben^[Dies ist auch nicht streng wahr, aber du musst warten, bis du über benannte Parameter und Standardwerte lernst].

::: {.practice}
Mache Übung #3.
:::

Wenn du eine Funktion aufrufst, werden die Werte, die du an die Funktion _übermittelst_, den Parametern zugewiesen und sie werden als _lokale_ Variablen verwendet (mehr darüber später). Es spielt jedoch keine Rolle, _wie_ du diese Werte erlangt hast, ob sie in einer Variable waren, hart codiert wurden oder von einer anderen Funktion zurückgegeben wurden. Wenn du numerische, logische oder Zeichenkettenwerte (_unveränderliche_ Typen) verwendest, kannst du davon ausgehen, dass jede Verbindung zur ursprünglichen Variablen oder Funktion, die sie erzeugt hat, verschwunden ist (wir werden uns später um _veränderliche_ Typen wie Listen kümmern). Wenn du also eine Funktion schreibst oder ihren Code liest, gehst du einfach davon aus, dass sie bei dem Aufruf auf einen bestimmten Wert gesetzt wurde und du kannst den Kontext, in dem dieser Aufruf gemacht wurde, ignorieren.
```python
# hart codiert
print_age(1976, 2020)

# mit Werten aus Variablen
i_was_born = 1976
today_is = 2023
print_age(i_was_born, today_is)

# mit Wert aus einer Funktion
def get_current_year():
    return 2023

print_age(1976, get_current_year())
```
### Rückgabewert der Funktionen (Ausgabe)
Deine Funktion kann eine Aktion ausführen, ohne einen Wert an den Aufrufer zurückzugeben (das ist es, was unsere Funktion `print_age` getan hat). Du könntest jedoch den Wert stattdessen zurückgeben müssen. Um die Dinge allgemeiner zu gestalten, möchten wir vielleicht eine neue Funktion namens `compute_age` schreiben, die das Alter zurückgibt, anstatt es zu drucken (wir können es immer selbst drucken).
```python
def compute_age(birth_year, current_year):
    """
    Berechnet das Alter, gegeben das Geburtsjahr und das aktuelle Jahr.

    Parameter
    ----------
    birth_year : int
    current_year : int
    
    Gibt zurück
    ----------
    int : age
    """
    return current_year - birth_year
```

Beachte, dass selbst wenn eine Funktion den Wert zurückgibt, dieser nur beibehalten wird, wenn er tatsächlich verwendet wird (in einer Variablen gespeichert, als Wert verwendet etc.). Ein einfacher Aufruf speichert den zurückgegebenen Wert also nicht irgendwo!

::: {.practice}
Mache Übung #4.
:::

### Anwendungsbereiche (für unveränderbare Werte)

Wie wir oben besprochen haben, isoliert das Umwandeln von Code in eine Funktion ihn, sodass er in seinem eigenen _Anwendungsbereich_ läuft. In Python existiert jede Variable in dem _Anwendungsbereich_, in dem sie definiert wurde. Wenn sie im _globalen_ Skript definiert wurde, existiert sie in diesem _globalen_ Anwendungsbereich als _globale_ Variable. Sie ist jedoch nicht zugänglich (zumindest nicht ohne besondere Anstrengungen über einen `global` Operator) innerhalb einer Funktion. Umgekehrt existieren die Parameter einer Funktion und alle _innerhalb einer Funktion_ definierten Variablen nur **innerhalb dieser Funktion**. Sie sind für die Außenwelt vollkommen unsichtbar und können nicht von einem globalen Skript oder von einer anderen Funktion aus abgerufen werden. Ebenso haben alle Änderungen, die du am Funktionsparameter oder an der lokalen Variable vornimmst, keinerlei Auswirkungen auf die Außenwelt. 

Der Zweck von Anwendungsbereichen besteht darin, einzelne Codeabschnitte voneinander zu isolieren, sodass das Ändern von Variablen innerhalb eines Anwendungsbereichs keine Auswirkungen auf alle anderen Anwendungsbereiche hat. Das bedeutet, dass du beim Schreiben oder Debuggen des Codes keine Angst vor Code in anderen Anwendungsbereichen haben musst und dich nur auf den Code konzentrieren musst, an dem du arbeitest. Da Anwendungsbereiche isoliert sind, können sie _gleichnamige Variablen_ haben, die jedoch keine Beziehung zueinander haben, da sie in ihren eigenen parallelen Universen existieren^[Es ist wie zwei Personen mit identischen Namen, immer noch unterschiedliche Personen.]. Wenn du also wissen möchten, welchen Wert eine Variable hat, musst du nur innerhalb des Anwendungsbereichs schauen und alle anderen Anwendungsbereiche ignorieren (auch wenn die Namen übereinstimmen!).

```python
# dies ist die Variable `x` im globalen Anwendungsbereich
x  = 5 

def f1():
  # Das ist die Variable `x` im Anwendungsbereich der Funktion f1
  # Sie hat den gleichen Namen wie die globale Variable, aber
  # hat keine Beziehung zu ihr: viele Leute heißen Sasha, 
  # sind aber immer noch unterschiedliche Personen. Was auch immer
  # mit `x` in f1 passiert, bleibt im Anwendungsbereich von f1.
  x = 3

  
def f2(x):
  # Dies ist der Parameter `x` im Anwendungsbereich der Funktion f2.
  # Wieder keine Beziehung zu anderen globalen oder lokalen Variablen.
  # Es ist ein völlig getrenntes Objekt, es passiert einfach, 
  # dass es den gleichen Namen hat (wieder einfach Namensvettern)
  print(x)
```

::: {.practice}
Mache Übung #5.
:::

## Spielerantwort als Funktion
Lassen wir all diese Theorie über Funktionen in die Praxis umsetzen. Verwende den Code, den du erstellt hast, um die [Spielerantwort](#guess-the-number-players-response) zu erhalten und verwandle ihn in eine Funktion. Sie sollte keine Parameter haben (zumindest vorerst) und sollte die Spielerantwort zurückgeben. Ich schlage vor, dass du sie `input_response` (oder so ähnlich) nennst. Überprüfe, ob der Code funktioniert, indem du diese Funktion aus dem Hauptskript aufrufst.

::: {.program}
Füge deinen Code in `code02.py` ein.
:::

## Eine Funktion debuggen
Jetzt, da du deine erste Funktion hast, kannst du den Sinn von drei Schritt über/Schritt in/Schritt heraus-Tasten verstehen, die dir der Debugger anbietet. Kopiere den folgenden Code in eine separate Datei (nenne sie zum Beispiel `test01.py`).

```python
def f1(x, y):
  return x / y
  
def f2(x, y):
  x = x + 5
  y = y * 2
  return f1(x, y)
  
z = f2(4, 2)
print(z)
```
Setze zuerst einen Breakpoint auf die Zeile im Hauptskript, die die Funktion `f2()` aufruft. Starte den Debugger über **F5** und das Programm wird an dieser Zeile anhalten. Wenn du nun **F10** drückst (Schritt über), geht das Programm zur nächsten Zeile `print(z)`. Wenn du aber stattdessen **F11** drückst (Schritt hinein), wird das Programm _in_ die Funktion hineingehen und zur Zeile `x = x + 5` gehen. Innerhalb der Funktion hast du die gleichen beiden Möglichkeiten, die wir gerade angeschaut haben, aber du kannst auch **Shift+F11** drücken, um aus der Funktion herauszugehen. Hier wird das Programm den gesamten Code durchlaufen, bis du die nächste Zeile _außerhalb_ der Funktion erreichst (du solltest wieder bei `print(z)` ankommen). Experimentiere mit dem Setzen von Breakpoints an verschiedenen Zeilen und dem Über-/Hinein-/Herausschreiten, um dich mit diesen nützlichen Debugging-Tools vertraut zu machen.

Setze nun den Breakpoint innerhalb der `f1()` Funktion und führe den Code über **F5** aus. Schau dir die linke Fensterseite an, du wirst einen _Call Stack_ Reiter sehen. Während die gelb hervorgehobene Zeile im Editor zeigt, wo du gerade bist (sollte innerhalb der `f1()` Funktion sein), zeigt der _Call Stack_ dir, wie du dorthin gekommen bist. In diesem Fall sollte es zeigen:

|    |  |
|:----------|:-------------|---|
| f1 | test01.py | 2:1 |
| f2 | test01.py | 7:1 |
| \<module\> | test01.py | 9:1 |

Die Aufrufe sind von unten nach oben gestapelt, das bedeutet, dass eine Funktion im Hauptmodul in Zeile 9 aufgerufen wurde, du in der Funktion `f2` in Zeile 7 gelandet bist und dann in der Funktion `f1` und in Zeile 2. Experimentiere mit dem Ein- und Austreten aus Funktionen und behalte dabei den _Call Stack_ im Auge. Du wirst diese Informationen vielleicht nicht oft benötigen, aber sie könnten in unseren späteren Projekten mit mehreren verschachtelten Funktionsaufrufen nützlich sein.

## Deine Funktion dokumentieren{#numpy-docstring}
Eine Funktion zu schreiben, ist nur die halbe Arbeit. Du musst sie dokumentieren! [Erinnere dich](#programming-tips), das ist eine gute Gewohnheit, die deinen Code einfach zu benutzen und wiederzuverwenden macht. Es gibt verschiedene Möglichkeiten, den Code zu dokumentieren, aber wir werden die [NumPy Docstring Konvention](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) verwenden. Hier ist ein Beispiel für eine solche dokumentierte Funktion

```python
def generate_initial(full_string):
    """Erzeugt eine Initiale mit dem ersten Symbol.
    
    Parameter
    ----------
    full_string : str
    
    Gibt zurück
    ----------
    str : Einzelnes Symbol
    """
    return full_string[0]
```
Schau dir das [Handbuch](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) an und dokumentiere die `input_response` Funktion. Du wirst den Abschnitt `Parameter` nicht benötigen, da sie derzeit keine Eingaben akzeptiert.

:::{.program}
Aktualisiere deinen Code in `code02.py`.
:::
## Verwendung der Aufforderung
In der Zukunft werden wir nach einer bestimmten Zahl fragen, die eine aktuelle Vermutung des Computers ist, daher können wir keine feste Aufforderungsnachricht verwenden. Ändere die `input_response` Funktion, indem du einen `guess` Parameter hinzufügst. Dann ändere die Aufforderung, die du für die [input()](https://docs.python.org/3/library/functions.html#input) verwendet hast, um den Wert in diesem Parameter einzuschließen. Aktualisiere die Dokumentation der Funktionen. Teste es, indem du mit verschiedenen Werten für den `guess` Parameter aufrufst und eine unterschiedliche Aufforderung zur Antwort siehst.

::: {.program}
Gib deinen Code in `code03.py` ein.
:::

## Aufteilen des Intervalls in der Mitte
Lass uns ein bisschen mehr üben, Funktionen zu schreiben. Denke daran, dass der Computer die Mitte des Intervalls als Vermutung verwenden sollte. Erstelle eine Funktion (nennen wir sie `split_interval()` oder so ähnlich), die zwei Parameter -- `lower_limit` und `upper_limit` - entgegennimmt und _eine Ganzzahl_ zurückgibt, die der Mitte des Intervalls am nächsten liegt. Der einzige knifflige Teil ist, wie du eine potentiell Gleitkommazahl (z.B. wenn du versuchst, sie für das Intervall 1..10 zu finden) in eine Ganzzahl umwandelst. Du kannst dafür die Funktion [int()](https://docs.python.org/3/library/functions.html#int) verwenden. Lies jedoch die Dokumentation sorgfältig durch, da sie _keine_ korrekte Rundung durchführt (was tut sie? Lies die Dokumentation!). Du solltest daher die Zahl auf die nächste Ganzzahl [round()](https://docs.python.org/3/library/functions.html#round) runden, bevor du sie umwandelst.

Schreibe eine Funktion, dokumentiere sie und teste sie, indem du überprüfst, ob die Zahlen korrekt sind.

:::{.program}
Gib deine `split_interval()` Funktion und den Testcode in `code04.py` ein.
:::

## Einzelne Runde
Du hast beide Funktionen, die du brauchst, also lass uns den Code schreiben, um das Spiel zu initialisieren und eine einzelne Runde zu spielen. Die Initialisierung läuft darauf hinaus, zwei Variablen zu erstellen, die den unteren und oberen Grenzwerten des Spielbereichs entsprechen (wir haben bisher 1 bis 10 verwendet, aber das kannst du natürlich immer ändern). Als nächstes sollte der Computer eine Vermutung generieren (dafür hast du deine `split_interval()` Funktion) und den Spieler nach der Vermutung fragen (das ist die `input_response()` Funktion). Sobald du die Antwort hast (in einer separaten Variable gespeichert, denke dir selbst einen Namen aus), aktualisiere entweder die obere oder untere Grenze mit einem [if..elif..else](#if-statement) Ausdruck, basierend auf der Antwort des Spielers (wenn der Spieler gesagt hat, dass seine Zahl höher ist, bedeutet das, dass das neue Intervall von `guess` bis `upper_limit` reicht, und umgekehrt, wenn sie niedriger ist). Drucke eine freudige Nachricht aus, wenn die Vermutung des Computers richtig war.

:::{.program}
Gib beide Funktionen und den Skriptcode in `code05.py` ein.
:::

## Mehrere Runden
Erweitere das Spiel, so dass der Computer so lange rät, bis er schließlich gewinnt. Du weißt bereits, wie man die [while](#while-loop) Schleife verwendet, überlege nur, wie du die Antwort des Teilnehmers als eine Schleifenbedingungsvariable verwenden kannst. Denke auch über den Anfangswert dieser Variable nach und wie du sie verwenden kannst, um `input_response()` nur an einer Stelle aufzurufen.

:::{.program}
Gib den aktualisierten Code in `code06.py` ein.
:::

## Nochmal spielen
Ändere den Code so, dass du dieses Spiel mehrere Male spielen kannst. Du weißt bereits, wie das geht und das Einzige, was du beachten musst, ist, wo genau du die Initialisierung vor jedem Spiel durchführen sollst. Da du das schon für das letzte Spiel implementiert hast, könntest du versucht sein zu sehen, wie du es gemacht hast oder sogar den Code zu kopieren und einzufügen. Allerdings würde ich empfehlen, es von Grund auf neu zu schreiben. Denke daran, dein Ziel ist es nicht, ein Programm zu schreiben, sondern zu lernen, wie man das macht und daher ist der Weg wichtiger als das Ziel.

:::{.program}
Gib den aktualisierten Code in `code07.py` ein.
:::

## Bester Punktestand
Füge den Code hinzu, um die Anzahl der Versuche zu zählen, die der Computer in jeder Runde benötigt hat, und melde den besten Punktestand (wenigste Anzahl von Versuchen), nachdem das Spiel vorbei ist. Du wirst eine Variable brauchen, um die Anzahl der Versuche zu zählen, und eine, um den besten Punktestand zu speichern. Versuche erneut, es zu schreiben, ohne auf dein vorheriges Spiel zu schauen.

:::{.program}
Gib den aktualisierten Code in `code08.py` ein.
:::

## Verwenden deiner eigenen Bibliotheken
Du weißt bereits, wie man [bestehende Bibliotheken verwendet](#using-libraries), aber du kannst auch deine eigenen erstellen und verwenden. Nimm die beiden Funktionen, die du entwickelt hast, und lege sie in eine neue Datei namens `utils.py` (vergiss nicht, einen mehrzeiligen Kommentar am Anfang der Datei hinzuzufügen, um dich daran zu erinnern, was drin ist!). Kopiere den verbleibenden Code (das globale Skript) in `code09.py`. Es wird in seinem aktuellen Zustand nicht funktionieren, da es die beiden Funktionen nicht finden wird (versuche es, um die Fehlermeldung zu sehen), daher musst du aus deinem eigenen Modul `utils` importieren. Das Importieren funktioniert genau so wie bei anderen Bibliotheken. Beachte, dass der Name deines Moduls `utils` ist (ohne die Endung), auch wenn deine Datei `utils.py` heißt.

:::{.program}
Gib die Funktionen in `utils.py` ein, den verbleibenden Code in `code09.py`.
:::

## Ordnung muss sein!{#keep-imports-tidy}
Bisher hast du höchstens eine Bibliothek importiert. Da Python jedoch hoch modular ist, ist es sehr verbreitet, viele Importe in einer einzelnen Datei zu haben. Es gibt einige Regeln, die es einfacher machen, die Importe zu verfolgen. Wenn du Bibliotheken importierst, sollten alle Import-Anweisungen oben in deiner Datei stehen und du solltest vermeiden, sie in zufälliger Reihenfolge zu platzieren. Die empfohlene Reihenfolge ist 1) Systembibliotheken, wie `os` oder `random`; 2) Drittanbieter-Bibliotheken, wie `psychopy`; 3) deine Projektmodule. Und innerhalb jedes Abschnitts solltest du die Bibliotheken _alphabetisch_ anordnen, sodass beispielsweise
```python
import os
import random
```

Das mag für unseren einfachen Code nicht besonders nützlich aussehen, aber wenn deine Projekte wachsen, musst du mehr und mehr Bibliotheken einbeziehen. Wenn du sie in dieser Reihenfolge hältst, ist es einfach zu verstehen, welche Bibliotheken du verwendest und welche nicht standardmäßig sind. Die alphabetische Reihenfolge bedeutet, dass du schnell überprüfen kannst, ob eine Bibliothek enthalten ist, da du schnell den Ort finden kannst, an dem ihre Import-Anweisung erscheinen sollte.

## Videospiele mit Video
Reiche deine Dateien ein und mach dich bereit für mehr Aufregung, denn wir wechseln zu "richtigen" Videospielen mit PsychoPy.
