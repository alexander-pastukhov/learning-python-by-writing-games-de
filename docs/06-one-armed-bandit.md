# Einarmiger Bandit, aber mit Listen und Schleifen {#One-armed-bandit}

In diesem Kapitel werden wir das Spiel des Einarmigen Banditen mehrmals neu programmieren. Das ist vielleicht nicht die aufregendste Aussicht, aber es gibt uns ein einfaches Spiel, das du bereits zu programmieren weißt, sodass wir uns auf Listen und For-Schleifen konzentrieren können. Hol dir das [Übungsnotebook](notebooks/One-armed bandit.ipynb), bevor wir starten.


## Konzepte des Kapitels
* Speichern von vielen Elementen in [Listen](#lists).
* Iterieren über Elemente mit der [for](#for-loop) Schleife.
* Erstellen eines [Bereichs](#range) von Werten.
* Schleifen über [nummerierte](#enumerate) Indizes und Werte.
* Listen erstellen mit [Listenabstraktion](#list-comprehension).

## Listen {#lists}
Bisher haben wir Variablen verwendet, um einzelne Werte zu speichern: die Wahl des Computers, die Vermutung des Spielers, die Anzahl der Versuche, das PsychoPy-Fensterobjekt usw. Aber manchmal müssen wir mehr als einen Wert verarbeiten. Dieses Problem hatten wir bereits im [computerbasierten Raten-der-Zahl](#guess-the-number-ai) Spiel, als wir den verbleibenden Zahlenbereich speichern mussten. Wir haben das Problem gelöst, indem wir zwei Variablen verwendet haben, eine für die untere und eine für die obere Grenze. Allerdings ist klar, dass dieser Ansatz nicht gut skalierbar ist und manchmal wissen wir vielleicht nicht einmal, wie viele Werte wir speichern müssen. Die [Listen](https://docs.python.org/3/library/stdtypes.html#lists) von Python sind die Lösung für dieses Problem.

Eine Liste ist eine veränderbare^[Mehr dazu und zu Tupeln, den unveränderlichen Verwandten der Liste, später.] Sequenz von Elementen, auf die über ihren nullbasierten Index zugegriffen werden kann. Wenn du die Idee der [Variablen-als-Box](#variables) fortschreitest, kannst du dir Listen als eine Box mit nummerierten Steckplätzen vorstellen. Um ein bestimmtes Stück zu speichern und abzurufen, musst du sowohl den _Variablennamen_ als auch den _Index des Elements_, an dem du interessiert bist, in dieser Box kennen. Dann arbeitest du mit einer Variable-plus-Index auf genau dieselbe Weise wie mit einer normalen Variable, indem du auf ihren Wert zugreifst oder ihn änderst, genau wie vorher.

Eine Liste wird durch eckige Klammern definiert `<variable> = [<wert1>, <wert2>, ... <wertN>]`. Auf einen einzelnen Platz innerhalb einer Liste wird ebenfalls über eckige Klammern zugegriffen `<variable>[<index>]`, wobei der Index wiederum **nullbasiert** ist^[Das ist typisch für "klassische" Programmiersprachen, aber weniger für solche, die auf lineare Algebra / Data Science ausgerichtet sind. Sowohl Matlab als auch R verwenden einen indexbasierten Index, so dass du vorsichtig sein und überprüfen musst, ob du die richtigen Indizes verwendest.]. Das bedeutet, dass das _erste_ Element `variable[0]` ist und, wenn es _N_ Elemente in der Liste gibt, ist das letzte Element `variable[N-1]`. Du kannst die Gesamtzahl der Elemente in einer Liste herausfinden, indem du ihre Länge über eine spezielle [len()](https://docs.python.org/3/library/functions.html#len) Funktion erhältst. So kannst du auf das letzte Element über `variable[len(variable)-1]` zugreifen^[Es gibt einen einfacheren Weg, dies zu tun, den du in Kürze lernen wirst.]. Beachte die `-1`: Wenn deine Liste 3 Elemente hat, ist der Index des letzten Elements 2, wenn sie 100 hat, dann 99, usw. Ich verbringe so viel Zeit damit, weil dies eine recht häufige Quelle von Verwirrung ist.

::: {.practice}
Mache Übung #1 um zu sehen, wie Listen definiert und indiziert werden.
:::

Listen erlauben dir auch, auf mehr als einen Slot/Index gleichzeitig zuzugreifen, und zwar über [slicing](https://docs.python.org/3/library/functions.html#slice). Du kannst den Index der Elemente über die Notation `<start>:<stop>` angeben. Zum Beispiel gibt dir `x[1:3]` Zugang zu zwei Elementen mit den Indizes 1 und 2. Ja, _zwei_ Elemente: der Slicing-Index geht vom `start` bis **aber nicht einschließlich** zum `stop`. Wenn du also _alle_ Elemente einer Liste abrufen willst, musst du `x[0:length(x)]` schreiben, und um nur das letzte Element zu bekommen, schreibst du immer noch `x[len(x)-1]`. Verwirrend? Ich denke schon! Ich verstehe die Logik, aber ich finde dieses stop-is-not-included Konzept gegenintuitiv und ich muss mich immer wieder bewusst daran erinnern. Leider ist dies die Standardmethode, um Zahlenfolgen in Python zu definieren, daher musst du dir dies merken.

::: {.practice}
Mache Übung #2, um die Intuition zu entwickeln.
:::

Beim Slicing kannst du entweder `start` oder `stop` weglassen. In diesem Fall geht Python davon aus, dass ein fehlendes `start` `0` bedeutet (der Index des ersten Elements) und ein fehlendes `stop` `len(<list>)` bedeutet (also ist das letzte Element eingeschlossen). Wenn du _beide_ weglässt, z.B. `meine_schönen_zahlen[:]`, gibt es alle Werte zurück, da dies äquivalent zu `meine_schönen_zahlen[0:len(meine_schönen_zahlen)]` ist.^[Beachte, dass dies fast, aber nicht ganz das Gleiche ist wie einfach nur `meine_schönen_zahlen` zu schreiben, denn `meine_schönen_zahlen[:]` gibt eine _andere_ Liste mit _identischem_ Inhalt zurück. Der Unterschied ist subtil, aber wichtig und wir werden später darauf zurückkommen, wenn wir über veränderbare und unveränderbare Typen sprechen.]

::: {.practice}
Mache Übung #3.
:::

Du kannst auch _negative_ Indizes verwenden, die relativ zur Länge der Liste berechnet werden^[Wenn du von R kommst, ist das negative Indexing in Python völlig anders.]. Wenn du zum Beispiel das _letzte_ Element der Liste abrufen willst, kannst du `meine_schönen_zahlen[len(meine_schönen_zahlen)-1]` oder einfach nur `meine_schönen_zahlen[-1]` sagen. Das vorletzte Element wäre `meine_schönen_zahlen[-2]`, usw. Du kannst negative Indizes für das Slicing verwenden, aber vergiss nicht den Haken _einschließlich-dem-Start-aber-ausgenommen-dem-Stopp_: `meine_schönen_zahlen[:-1]` gibt alle Elemente außer dem letzten Element der Liste zurück, nicht die gesamte Liste!

::: {.practice}
Mache Übung #4.
:::

Das Slicing kann erweitert werden, indem ein `Schritt` über die Notation `start:stop:Schritt` angegeben wird. `Schritt` kann negativ sein, was ermöglicht, Indizes in umgekehrter Reihenfolge zu erstellen:

```python
meine_schönen_zahlen = [1, 2, 3, 4, 5, 6, 7]
meine_schönen_zahlen[4:0:-1]
#> [5, 4, 3, 2]
```

Aber du musst auf das Vorzeichen des Schritts achten. Wenn es in die falsche Richtung geht und `stop` nicht erreicht werden kann, gibt Python eine leere Liste zurück.

```python
meine_schönen_zahlen = [1, 2, 3, 4, 5, 6, 7]
meine_schönen_zahlen[4:0:1]
#> []
```

Schritte können mit ausgelassenen und negativen Indizes kombiniert werden. Um jedes _ungerade_ Element der Liste zu bekommen, schreibst du `meine_schönen_zahlen[::2]`:  

```python
meine_schönen_zahlen = [1, 2, 3, 4, 5, 6, 7]
meine_schönen_zahlen[::2]
#> [1, 3, 5, 7]
```

::: {.practice}
Mache Übung #5.
:::

Wenn du versuchst, auf Indizes _außerhalb_ eines gültigen Bereichs zuzugreifen, wird Python einen [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError)^[Wenn du mit R und seiner laxen Haltung gegenüber Indizes vertraut bist, wirst du das sehr befriedigend finden.] auslösen. Wenn du also versuchst, das 6^te^ Element (Index 5) einer fünfelementigen Liste zu holen, wird ein einfacher und unmissverständlicher Fehler generiert. Wenn jedoch deine _Scheibe_ größer ist als der Bereich, wird sie ohne zusätzliche Warnung oder einen Fehler abgeschnitten. Daher wird für eine fünfelementige Liste `my_pretty_numbers[:6]` oder `my_pretty_numbers[:600]` beide alle Nummern zurückgeben (effektiv ist dies gleichwertig mit `my_pretty_numbers[:]`). Zudem, wenn die Scheibe leer ist (`2:2`, kann 2 nicht einschließen, weil es ein Stop-Wert ist, obwohl es auch von 2 aus startet) oder die gesamte Scheibe außerhalb des Bereichs liegt, wird Python eine leere Liste zurückgeben, wiederum wird weder eine Warnung noch ein Fehler generiert.

::: {.practice}
Mache Übung #6.
:::

In Python sind Listen dynamisch, daher kannst du immer Elemente hinzufügen oder entfernen, siehe [die Liste der Methoden](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists). Du kannst ein neues Element am Ende der Liste über die Methode `.append(<new_value>)` hinzufügen

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers.append(10)
my_pretty_numbers
#> [1, 2, 3, 4, 5, 6, 7, 10]
```

Oder du kannst `insert(<index>, <new_value>)` _vor_ einem Element mit diesem Index verwenden. Leider bedeutet dies, dass du einen beliebig großen Index verwenden kannst und es fügt einen neuen Wert als _letztes_ Element ein, ohne einen Fehler zu erzeugen.

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers.insert(2, 10)
my_pretty_numbers.insert(500, 20)
my_pretty_numbers
#> [1, 2, 10, 3, 4, 5, 6, 7, 20]
```

Du kannst ein Element mit seinem Index über `pop(<index>)` entfernen, beachte, dass das Element auch _zurückgegeben_ wird. Wenn du den Index weglässt, entfernt `pop()` das _letzte_ Element der Liste. Hier kannst du nur gültige Indizes verwenden.

```python
my_pretty_numbers = [1, 2, 3, 4, 5, 6, 7]
my_pretty_numbers.pop(-1)
#> 7
my_pretty_numbers.pop(3)
#> 4
my_pretty_numbers
#> [1, 2, 3, 5, 6]
```

::: {.practice}
Mache Übung #7.
:::

## Neukonzeption des Einarmigen Banditen-Spiels mit Listen
Puh, das war _viel_ über Listen^[Und wir haben gerade einmal an der Oberfläche gekratzt!]. Aber [Work hard, play hard](https://de.wiktionary.org/wiki/work_hard,_play_hard)! Lass uns zum Einarmigen Banditen-Spiel zurückkehren, das du bereits implementiert hast, und es mithilfe von Listen neu gestalten. Letztere machen viel Sinn, wenn man mit mehreren Slots arbeitet. Erinnere dich an die Regeln: Du hast drei Slots mit [zufälligen Zahlen](https://docs.python.org/3/library/random.html#random.randint) zwischen 1 und 5, wenn alle drei Zahlen übereinstimmen, gibst du "Drei Gleiche!" aus, wenn nur zwei Zahlen übereinstimmen, druckst du "Ein Paar!". Implementiere dieses Spiel mit einer Liste anstelle von drei Variablen. In der ersten Version, verwende die Notation `<variable> = [<value1>, <value2>, ..., <valueN>]`, um sie zu definieren. Beachte außerdem, dass du bei der Verwendung von [String-Formatierung](#string-formatierung) alle Werte in einem Tuple (eine eingefrorene Liste, mehr dazu in späteren Kapiteln) oder einer Liste übergibst. Die gute Nachricht: Deine drei Werte befinden sich in der Liste, daher kannst du sie für die String-Formatierung verwenden, denke nur an die Anzahl der Slots, die du innerhalb des Format-Strings definieren musst.

Ich weiß, es wird verlockend sein, einfach den bereits implementierten Code zu kopieren und zu bearbeiten, aber wir sind hier, um zu lernen, daher empfehle ich dringend, ihn von Grund auf neu zu schreiben. Es ist ein sehr einfaches Programm, es neu zu machen ist sehr einfach, aber es hilft dir, mehr zu üben.

::: {.program}
Setze deinen Code in _code01.py_ um.
:::

Jetzt mache dasselbe, aber beginne mit einer leeren Liste und [füge](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) zufällige Zahlen hinzu.

::: {.program}
Setze deinen Code in _code02.py_ um.
:::

## For-Schleife{#for-loop}
In dem oben genannten Code mussten wir über drei Maulwürfe (Kreise) iterieren, die wir in einer Liste hatten. Python bietet dafür ein spezielles Werkzeug: eine
[For-Schleife](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements), die über die Elemente jeder Sequenz iteriert (unsere Liste ist eine Sequenz!). Hier ist ein Beispiel:

```python
numbers = [2, 4, 42]
for a_number in numbers:
    print("Der Wert der Variable a_number in dieser Iteration beträgt %d"%(a_number))
    a_number = a_number + 3
    print("  Jetzt haben wir es um 3 erhöht: %d"%(a_number))
    print("  Jetzt verwenden wir es in einer Formel a_number / 10: %g"%(a_number / 10))
#> Der Wert der Variable a_number in dieser Iteration beträgt 2
#>   Jetzt haben wir es um 3 erhöht: 5
#>   Jetzt verwenden wir es in einer Formel a_number / 10: 0.5
#> Der Wert der Variable a_number in dieser Iteration beträgt 4
#>   Jetzt haben wir es um 3 erhöht: 7
#>   Jetzt verwenden wir es in einer Formel a_number / 10: 0.7
#> Der Wert der Variable a_number in dieser Iteration beträgt 42
#>   Jetzt haben wir es um 3 erhöht: 45
#>   Jetzt verwenden wir es in einer Formel a_number / 10: 4.5
```

Hier wird der Code innerhalb der `for`-Schleife dreimal wiederholt, weil es drei Elemente in der Liste gibt. Bei jeder Iteration wird der nächste Wert aus der Liste einer temporären Variable `a_number` zugewiesen (siehe Ausgabe). Sobald der Wert einer Variablen zugewiesen ist, kannst du ihn wie jede andere Variable verwenden. Du kannst ihn ausgeben lassen (erster `print`), du kannst ihn ändern (zweite Zeile innerhalb der Schleife), seinen Wert verwenden, wenn du andere Funktionen aufrufst, usw. Um das besser zu würdigen, kopiere diesen Code in eine temporäre Datei (nenne sie `test01.py`), setze einen [Breakpoint](#debugging) auf die erste `print` Anweisung und dann verwende **F10**, um durch die Schleife zu springen und zu sehen, wie sich der Wert der Variable `a_number` bei jeder Iteration ändert und dann in der zweiten Zeile innerhalb der Schleife modifiziert wird.

Beachte, dass du die gleiche [break](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#break-and-continue-statements-and-else-clauses-on-loops) Anweisung verwenden kannst wie bei der [while](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) Schleife.

::: {.practice}
Mache Übung #8.
:::

## Verwendung der For-Schleife zur Erzeugung von Slots
Verwende die [For-Schleife](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements) zweimal. Zuerst, wenn du die drei Slots erstellst: Beginne mit einer leeren Liste und füge drei zufällige Nummern mit einer For-Schleife hinzu. Zweitens, beim Ausdrucken der Slots. Ich habe oben darauf hingewiesen, dass es einfacher ist, die Formatierung vorzunehmen, wenn man drei Werte in einer Liste hat, aber hier sollst du, um der Übung willen, jeden Slot separat mit einer For-Schleife ausdrucken.

::: {.program}
Setze deinen Code in _code03.py_ um.
:::

## range() Funktion: Code N-mal wiederholen{#range}
Manchmal musst du den Code mehrmals wiederholen. Stelle dir zum Beispiel vor, dass du in einem Experiment 40 Versuche hast. Daher musst du den versuchsbezogenen Code 40 Mal wiederholen. Natürlich kannst du von Hand eine 40 Elemente lange Liste erstellen und darüber iterieren, aber Python hat dafür eine praktische [range()](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#the-range-function) Funktion. `range(N)` erzeugt N Ganzzahlen von 0 bis N-1 (gleiche Regel wie beim Slicing, dass bis zu, aber nicht einschließlich gilt), über die du in einer For-Schleife iterieren kannst. 

```python
for x in range(3):
    print("Der Wert von x ist %d"%(x))
#> Der Wert von x ist 0
#> Der Wert von x ist 1
#> Der Wert von x ist 2
```

Du kannst das Verhalten der [range()](https://docs.python.org/3/library/stdtypes.html#range) Funktion ändern, indem du einen Startwert und eine Schrittgröße angibst. Aber in ihrer einfachsten Form ist `range(N)` ein praktisches Werkzeug, um den Code so oft zu wiederholen. Beachte, dass du zwar immer eine temporäre Variable in einer `for` Schleife benötigst, sie manchmal aber überhaupt nicht verwendest. In solchen Fällen solltest du `_` (Unterstrich) als Variablennamen verwenden, um anzuzeigen, dass sie nicht verwendet wird.

```python
for _ in range(2):
    print("Ich werde zweimal wiederholt!")
#> Ich werde zweimal wiederholt!
#> Ich werde zweimal wiederholt!
```

Alternativ kannst du `range()` verwenden, um durch die Indizes einer Liste zu schleifen (denke daran, du kannst immer auf ein einzelnes Listenelement über `var[index]` zugreifen). Mache genau das^[Beachte, das ist nicht eine _bessere_, sondern eine _alternative_ Möglichkeit, dies zu tun.]! Ändere deinen Code so, dass du die [range()]((https://docs.python.org/3/library/stdtypes.html#range)) Funktion in der For-Schleife verwendest (wie kannst du die Anzahl der Iterationen, die du benötigst, aus der Länge der Liste berechnen?), verwende die temporäre Variable als _Index_ für die Liste, um jedes Element zu zeichnen^[Stilhinweis: Wenn eine Variable ein _Index_ von etwas ist, neige ich dazu, sie `isomething` zu nennen. Wenn sie zum Beispiel einen Index zu einem aktuellen Maulwurf hält, würde ich sie `imole` nennen. Das ist _meine_ Art, das zu tun. Andere verwenden das `i_` Präfix oder ein `_i` Suffix. Aber so oder so, es ist eine nützliche Benennungskonvention. Denke daran, je einfacher es ist, die Bedeutung einer Variable aus ihrem Namen zu verstehen, desto einfacher ist es für dich, den Code zu lesen und zu ändern.]. Wenn du unsicher bist, setze einen Breakpoint innerhalb (oder kurz vor) der Schleife und schreite durch deinen Code, um zu verstehen, welche Werte eine temporäre Schleifenvariable erhält und wie sie verwendet wird.

## Informationen zum Slot-Index hinzufügen
In der vorherigen Version des Spiels hatten wir keine Möglichkeit, den Slot-Index anzugeben. Es ist zwar offensichtlich an der Reihenfolge im Ausdruck erkennbar, aber es wäre schöner, wenn wir explizit `"Slot #1: 2"` ausdrucken würden. Verwende die Funktion [range()](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#the-range-function) um Indizes von Slots zu generieren, schlaufe über diese Indizes und drucke sie in "Slot #<slot-index> : <slot-wert-für-diesen-index>" aus. Beachte jedoch, dass die Indizes in Python bei Null beginnen, unsere Slots aber bei 1 starten (kein Slot Null!). Überlege dir, wie du dies in einem Ausdruck korrigieren könntest.

::: {.program}
Gib deinen Code in _code04.py_ ein.
:::

## Über Index und Element gleichzeitig schleifen mit Listenaufzählung {#enumerate}
Es passiert ziemlich oft, dass du sowohl über die Indizes als auch über die Elemente einer Liste schleifen musst, daher hat Python eine praktische Funktion dafür: [enumerate()](https://docs.python.org/3/library/functions.html#enumerate)! Wenn du anstelle einer Liste über [enumerate(<list>)](https://docs.python.org/3/library/functions.html#enumerate) iterierst, erhältst du ein Tupel mit `(Index, Wert)`. Hier ist ein Beispiel:

```python
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print('%d: %s'%(index, letter))
#> 0: a
#> 1: b
#> 2: c
```

Verwende [enumerate](https://docs.python.org/3/library/functions.html#enumerate), um gleichzeitig über den Index und das Element zu schleifen und einen Slot nach dem anderen auszudrucken. Sieh dir den `start` Parameter der Funktion an, um sicherzustellen, dass dein Index jetzt bei 1 beginnt.

::: {.program}
Gib deinen Code in _code05.py_ ein.
:::

## List Comprehension {#list-comprehension}
Die List Comprehension bietet eine elegante und leicht zu lesende Möglichkeit, Elemente einer Liste zu erzeugen, zu ändern und/oder zu filtern und dabei eine neue Liste zu erstellen. Die allgemeine Struktur lautet
```python
new_list = [<Transformation-des-Elements> for item in old_list if <Bedingung-gegeben-das-Element>]
```
Schauen wir uns Beispiele an, um zu verstehen, wie es funktioniert. Stell dir vor, du hast eine Liste `numbers = [1, 2, 3]` und du musst jede Zahl um 1 erhöhen^[Ein sehr willkürliches Beispiel!]. Du kannst es machen, indem du eine neue Liste erstellst und 1 zu jedem Element im <transformiere-das-Element> Teil hinzufügst:

```python
numbers = [1, 2, 3]
numbers_plus_1 = [item + 1 for item in numbers]
```

Beachte, dass dies äquivalent ist zu
```python
numbers = [1, 2, 3]
numbers_plus_1 = []
for item in numbers:
    numbers_plus_1.append(item + 1)
```

Oder stelle dir vor, du musst jedes Element in einen String umwandeln. Das kannst du einfach so machen
```python
numbers = [1, 2, 3]
numbers_as_strings = [str(item) for item in numbers]
```
Wie wäre die äquivalente Form mit einer normalen for-Schleife? Schreibe beide Versionen des Codes in Jupiter cells und überprüfe, ob die Ergebnisse gleich sind.

::: {.practice}
Mache Übung #9 im Jupyter Notebook.
:::

Implementiere nun den unten stehenden Code mit Hilfe der List Comprehension. Überprüfe, ob die Ergebnisse übereinstimmen.
```python
strings = ['1', '2', '3']
numbers = []
for astring in strings:
    numbers.append(int(astring) + 10)
```

::: {.practice}
Mache Übung #10 im Jupyter Notebook.
:::

Wie oben bemerkt, kannst du auch eine bedingte Anweisung verwenden, um zu filtern, welche Elemente an die neue Liste weitergegeben werden. In unserem Zahlenbeispiel können wir Zahlen beibehalten, die größer als 1 sind
```python
numbers = [1, 2, 3]
numbers_greater_than_1 = [item for item in numbers if item > 1]
```

Manchmal wird die gleiche Aussage in drei Zeilen statt in einer geschrieben, um das Lesen zu erleichtern:
```python
numbers = [1, 2, 3]
numbers_greater_than_1 = [item 
                          for item in numbers
                          if item > 1]
```

Natürlich kannst du die Transformation und Filterung in einer einzigen Aussage kombinieren. Schreibe einen Code, der alle Elemente unter 2 herausfiltert und 4 zu ihnen hinzufügt.

::: {.practice}
Mache Übung #11 im Jupyter Notebook.
:::

## Verwendung von List Comprehension zur Erstellung von drei Slots
Lass uns List Comprehension verwenden, um in einer einzigen Zeile drei Slots zu erstellen. Die gute Nachricht ist, dass wir uns das Erstellen einer leeren Liste und die Verwendung von `append` ersparen. Die schlechte Nachricht ist, dass du darüber nachdenken musst, über welche Werte du schleifen möchtest, wenn du drei Zufallszahlen erzeugen willst. Tipp: schau dir die Funktion [range()](#range) erneut an und überlege, ob du die temporäre Schleifenvariable tatsächlich verwenden wirst.

::: {.program}
Gib deinen Code in _code06.py_ ein.
:::

## Fertig für den Tag
Ausgezeichnet! Verpacke den Ordner mit dem Code und dem Notebook in eine Zip-Datei und reiche sie ein!

