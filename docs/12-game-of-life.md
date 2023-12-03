# Game of Life {#game-of-life}

Übung macht den Meister, also werden wir heute eine Textversion des _Game of Life_ Spiels implementieren. Es wird kaum oder gar kein neues Material geben, denn wir konzentrieren uns darauf, die Fähigkeiten und das Wissen, das du bereits hast, zu nutzen. Stattdessen liegt der Hauptfokus darauf, dieselbe Funktionalität mit verschiedenen Ansätzen zu implementieren, um sowohl gemeinsame als auch lösungsspezifische Aspekte des Codes leichter erkennen zu können.


## Game of Life
Das [Game of Life]() wurde von dem britischen Mathematiker John Horton Conway erschaffen. Es handelt sich hierbei eigentlich nicht um ein Spiel, sondern um eine Simulation, bei der man Anfangsbedingungen festlegt und beobachtet, wie sich die Population entwickelt. Die Regeln, [wie auf Wikipedia beschrieben](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens), sind sehr einfach:

1. Jede lebendige Zelle mit zwei oder drei lebendigen Nachbarn überlebt.
2. Jede tote Zelle mit drei lebendigen Nachbarn wird zu einer lebendigen Zelle.
3. Alle anderen lebendigen Zellen sterben in der nächsten Generation. Ebenso bleiben alle anderen toten Zellen tot.

Trotz der Einfachheit der Regeln erzeugen sie eine bemerkenswerte Evolution einer Zellkultur und führen zu vielen dynamischen oder statischen Konfigurationen. Hier ist ein Beispiel einer Simulation mit einem zufälligen Anfangszustand.

<div style="text-align:center;"><video controls>
    <source src="videos/game-of-life.m4v" type="video/mp4"> 
  </video></div>

Unsere Version wird weniger dynamisch sein, da wir uns an eine textbasierte Ausgabe halten werden, aber das gleiche Verhalten wie im obigen Video zeigen werden. Da dies eher eine Simulation als ein Spiel ist, benötigen wir lediglich drei Funktionen, die

* den Anfangszustand der Welt generieren,
* ihren Zustand im nächsten Zeitpunkt berechnen,
* sie ausdrucken.

Die letzte Funktion hilft uns zu sehen, was die ersten beiden tun, daher werden wir mit dieser beginnen.

## Die Welt ausdrucken
Bevor wir damit beginnen, die Welt zu erschaffen und sie sich entwickeln zu lassen, benötigen wir eine Möglichkeit, sie zu sehen, eine `print_world` Funktion. Da dieses Kapitel in erster Linie um Praxis geht, werden wir die Funktionalität auf drei verschiedene Arten erzeugen:

* unter Verwendung von verschachtelten for-Schleifen
* indem wir Reihen einzeln ausdrucken, indem wir Elemente zu einem String zusammenfügen
* indem wir alle Elemente zu einem einzigen String zusammenfügen und nur einmal ausdrucken.

Hier ist die Übungsmatrix mit einem [Gleiter-Raumschiff-Muster](https://conwaylife.com/wiki/Glider), das du verwenden kannst


```python
import numpy as np

the_world = np.array([[" ", " ", "*", " "],
                      ["*", " ", "*", " "],
                      [" ", "*", "*", " "],
                      [" ", " ", " ", " "]])
```

Hier ist das Wörterbuch, das wir verwenden werden, um zwischen langweiligen, aber einfacher zu tippenen Zeichen und besser aussehenden in unserem Ausgabemedium zu übersetzen.


```python
OUTPUT_MAP = {" ": "⬜", "*" : "⬛"}
```

und so sollte es aussehen, wenn du es ausdruckst:


```
#> ⬜⬜⬛⬜
#> ⬛⬜⬛⬜
#> ⬜⬛⬛⬜
#> ⬜⬜⬜⬜
```

## Ausgabe über verschachtelte for-Schleifen
Der erste Ansatz besteht darin, ein Element nach dem anderen auszudrucken, indem du zuerst über die Reihen und dann über jedes Element der Reihe iterierst. Du weißt, wie man [über Elemente iteriert](#for-loop), also musst du nur noch überlegen, welchen Wert du für den Parameter `end` der [print](https://docs.python.org/3/library/functions.html#print)-Funktion verwenden sollst und wann. Außerdem musst du das Symbol von der internen Darstellung in die Ausgabe mithilfe des `OUTPUT_MAP`-Wörterbuchs übersetzen (keine if-elses notwendig!). Füge den Code in die Funktion `print_world_via_nested_loop` ein, die einen einzelnen Parameter nimmt (es sollte ziemlich offensichtlich sein, welcher das ist). Dokumentiere die Funktion!

::: {.program}
Implementiere `print_world_via_nested_loop` in _print_utils.py_ <br/>
Teste es in _code01.py_.
:::

## Jede Reihe als einzelnen String ausdrucken
Die zweite Lösung besteht darin, über die Reihen zu iterieren, aber [alle Elemente der Reihe zu einem einzigen String zusammenzufügen](#str.join) und dann nur einmal pro Reihe zu drucken. Bevor du jedoch Elemente zu einem einzigen String zusammenführen kannst, musst du sie mit dem `OUTPUT_MAP`-Wörterbuch mithilfe der [Listengenerierung](#list-comprehension) übersetzen. Du kannst das in einer einzigen Zeile machen: Erstelle eine neue Liste mit übersetzten Elementen, [füge sie zusammen](https://docs.python.org/3/library/stdtypes.html#str.join) und drucke sie aus.

::: {.program}
Implementire `print_world_joining_rows` in _print_utils.py_ <br/>
Teste es in _code02.py_.
:::

## Das gesamte Feld als einen einzigen String ausdrucken
Unsere finale Lösung besteht darin, das gesamte Feld in einen einzigen String umzuwandeln und dann nur einmal zu drucken. Du weißt bereits, wie man einen String für eine einzelne Reihe erstellt. Jetzt musst du lediglich eine Liste von Strings erstellen, einen für jede Reihe, mithilfe der [Listengenerierung](#list-comprehension) (ja, das bedeutet verschachtelte Listengenerierungen!) und dann alle mit `"\n"` (neue Zeile) als Trennzeichen zusammenführen. Es wird also ziemlich verschachtelt, da du eine Liste (erzeugt durch Listengenerierung) zusammenführst, deren Elemente Strings sind, die wiederum durch das Zusammenfügen einer Liste von übersetzten Zeichen (die ebenfalls durch Listengenerierung erstellt wird) produziert werden. Wenn das verwirrend klingt, beginne einfach mit dem, was du bereits implementiert hast – eine einzelne Reihe in einen String umzuwandeln – und überlege, wie du die for-Schleife, die du verwendet hast, in eine for-Schleife innerhalb der Listengenerierung umwandeln könntest.

::: {.program}
Implementire `print_world_as_a_single_string` in _print_utils.py_ <br/>
Teste es in _code03.py_.
:::

## Die Welt erschaffen
Im Game of Life ist die Welt ein rechteckiges Gitter, dessen Größe wir mit `WORLD_SIZE = (<W>, <H>)` definieren werden, wobei `<W>` und `<H>` die von dir gewählten Dimensionen sind (zum Beispiel 10 mal 5?). Wir werden die Welt zufällig mit einem spezifischen Anteil an lebendigen Zellen zu Beginn generieren: `P_ALIVE = 0.25` (du kannst das Verhältnis nach Belieben ändern). Wie beim Drucken werden wir mehrere Versionen desselben Verfahrens implementieren.

## Die Welt mit NumPy erschaffen
Der einfachste Weg, die Welt zu erschaffen, ist über [numpy.random.choice()](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html). Du musst nur die Werte angeben, aus denen wir wählen ( `" "` und `"*"`), die Größe der Matrix und die _Wahrscheinlichkeit, jeden Wert auszuwählen_. Wenn du das Letztere nicht angibst, ist es gleich wahrscheinlich, dass jeder Wert gewählt wird, aber in unserem Fall sind die Wahrscheinlichkeiten für `" "` (tote Zelle) und `"*"` (lebende Zelle) unterschiedlich, daher musst du beide angeben.

Implementiere diesen Code in einer Funktion mit dem Namen `create_world_via_numpy`. Sie sollte zwei Parameter nehmen (die Größe der Spielwelt und die Wahrscheinlichkeit einer lebenden Zelle) und eine NumPy-Matrix mit der Welt zurückgeben. Behalte im Kopf, dass NumPy die Größe als `(Anzahl-der-Reihen, Anzahl-der-Spalten)` erwartet. Allerdings ist die Anzahl der Reihen die Höhe und die Anzahl der Spalten die Breite, also denke über die Reihenfolge hier nach! Sobald du den Code implementiert hast, solltest du eine ähnliche Welt sehen ([seede](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html) NumPy mit 42 und du solltest genau die gleiche erhalten). 

::: {.program}
Implementire `create_world_via_numpy` in `creation_utils.py` <br/>
Teste den Code in _code04.py_ mithilfe der von dir gewählten Druckfunktion.
:::


```
#> ⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜
#> ⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜
#> ⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜
#> ⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜
```

## Die Welt mit verschachtelten Schleifen erschaffen
Lass uns dasselbe tun, aber ein Element nach dem anderen erstellen, indem wir eine Liste von Listen aufbauen und diese dann in ein [NumPy-Array](https://numpy.org/doc/stable/reference/generated/numpy.array.html) umwandeln. Hierbei iterierst du über Zeilen und Spalten ([range](https://docs.python.org/3/library/functions.html#func-range) ist definitiv nützlich) und erschaffst mithilfe der Funktion [random.choices](https://docs.python.org/3/library/random.html#random.choices) jeweils ein Element. Es funktioniert genauso wie [numpy.random.choice](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html), aber Wahrscheinlichkeiten werden als "Gewichte" bezeichnet. Sei vorsichtig, denn es gibt auch eine Funktion namens [random.choice](https://docs.python.org/3/library/random.html#random.choice) (im Singular "choice" und nicht im Plural "choices"), die fast auf die gleiche Weise funktioniert, aber es erlaubt nicht, Gewichte/Wahrscheinlichkeiten anzugeben!

Die Gesamtlogik sollte größtenteils unkompliziert sein. Du erstellst für jede Zeile eine Liste und fügst diese Listen zu einer einzigen Liste zusammen. Hierbei verwendest du konventionelle [for-Schleifen](#for-loop). Für die Zeile beginnst du mit einer leeren Liste und [erweiterst](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) sie mit einer Liste, die von [random.choices](https://docs.python.org/3/library/random.html#random.choices) produziert wird (es gibt eine Liste zurück, nicht einen einzelnen Wert, daher müssen wir [erweitern](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) und nicht [anhängen](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)!). Ähnlich beginnst du mit einer leeren Liste für die Welt, in die du [nacheinander](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) eine Zeile hinzufügst.
Sobald du fertig bist, konvertierst du es in ein [NumPy-Array](https://numpy.org/doc/stable/reference/generated/numpy.array.html) und gibst es zurück.

Eingabe und Ausgabe der Funktion sind gleich, es ändert sich nur, wie du die Lösung implementierst. Mein [Zufallskeim](https://docs.python.org/3/library/random.html#random.seed) war wieder 42.



```
#> ⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
#> ⬛⬜⬜⬜⬛⬜⬜⬜⬛⬜
#> ⬛⬜⬜⬛⬜⬜⬛⬜⬛⬜
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
```

::: {.program}
Implementire `create_world_via_nested_loops` in `creation_utils.py` <br/>
Teste den Code in _code05.py_ mithilfe der von dir gewählten Druckfunktion.
:::

## Die Welt mit Listengenerierung erschaffen
Hoffentlich ist dir bereits aufgefallen, dass die for-Schleifen lediglich dazu verwendet werden, eine Liste zu erstellen, also solltest du denken "Das wäre einfacher mit einer Listengenerierung!". Ja, das wäre es, und das ist unsere dritte Implementierung `create_world_via_list_comprehension`. Wir vereinfachen unser Leben, indem wir die ganze Reihe mit einem Aufruf erzeugen, indem wir den `k`-Parameter der Funktion [random.choices](https://docs.python.org/3/library/random.html#random.choices) angeben. Auf diese Weise erhalten wir eine Liste mit `k` Elementen (wofür sollte `k` stehen, für die Breite oder Höhe unserer Welt?) und verwenden Listengenerierung, um eine Liste von Reihen zu erstellen. Anschließend konvertieren wir sie in ein NumPy-Array und geben sie zurück. Gleiche Eingaben und Ausgaben, gleiche Funktionalität, nur eine leicht abweichende Implementierung. Hier gibt uns der gleiche [Zufallskeim](https://docs.python.org/3/library/random.html#random.seed) 42 wieder die gleiche Welt.


```
#> ⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
#> ⬛⬜⬜⬜⬛⬜⬜⬜⬛⬜
#> ⬛⬜⬜⬛⬜⬜⬛⬜⬛⬜
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
```

::: {.program}
Implementire `create_world_via_list_comprehension` in `creation_utils.py` <br/>
Teste den Code in _code06.py_ mithilfe der von dir gewählten Druckfunktion.
:::

## Leben und sterben lassen
Erinnere dich an die Regeln der Simulation:

1. Jede lebende Zelle mit zwei oder drei lebenden Nachbarn überlebt.
2. Jede tote Zelle mit drei lebenden Nachbarn wird zu einer lebenden Zelle.
3. Alle anderen lebenden Zellen sterben in der nächsten Generation. Ebenso bleiben alle anderen toten Zellen tot.

Das bedeutet, dass wir für jede Zelle auf fast die gleiche Weise ihre Nachbarn zählen müssen, wie wir [Minen gezählt haben](#minesweeper-count-mines) im Minesweeper-Spiel. Warum fast? Als wir Minen gezählt haben, wussten wir, dass die Zelle selbst leer ist, sonst wären wir explodiert. Hier müssen wir die Gesamtanzahl der lebenden Zellen zählen, _ohne die Zelle selbst_. Oder du kannst es auch anders ausdrücken: Wir müssen alle Zellen zählen und dann die Zelle selbst von dieser Anzahl abziehen. Hier sind einige Beispiele für die Glider-Welt mit sowohl einfachen als auch Grenzfällen. Denke daran, dass du im letzteren Fall die Grenzen für deine Slices anpassen musst.

![Beispielzählungen der Zellen](images/game-of-life-cell-counts.svg){width=100% style="display: block; margin: 0 auto"}<br/>


## Nachbarn mit Slicing zählen
In unserem ersten Ansatz implementieren wir diese Funktionalität mit NumPy-Array-Slicing, genau wie wir es im Minesweeper-Spiel gemacht haben. Ich schlage vor, dass du den [Abschnitt zur Minenzählung](#minesweeper-count-mines) noch einmal liest, aber nicht einfach den Code kopierst und einfügst, den du dort erstellt hast. Denke daran, wir üben hier, also lohnt es sich, den Code von Grund auf neu zu erfinden. Die gute Nachricht ist, dass es schneller gehen sollte, da du bereits eine Intuition dafür hast, wie es umzusetzen ist.

Erstelle eine Funktion `count_neighbors_via_slicing()`. Sie sollte nur zwei Parameter nehmen --- die Weltmatrix und die Position der Zelle, für die wir die Nachbarn zählen --- und eine ganze Zahl zurückgeben, die von $0$ bis $8$ geht (warum nur bis $8$?). Teste diese Funktion mit der Glider-Weltmatrix, die du oben finden kannst.

::: {.program}
Implementire `count_neighbors_via_slicing` in `evolution_utils.py` <br/>
Teste es in _code07.py_.
:::



## Nachbarn mit verschachtelten for-Schleifen zählen
Was man mit Slicing tun kann, kann man auch mit [for-Schleifen](#for-loop) machen! Implementiere die gleiche Funktion erneut, aber anstatt einfache Slices mit Grenzwerten zu machen, verwende diese Grenzwerte, um über einzelne Zellen zu iterieren. Tipp: [range](https://docs.python.org/3/library/functions.html#func-range) kann sowohl `start`- als auch `stop`-Werte akzeptieren. Ansonsten benötigst du nur einen Zähler, der bei Null beginnt und jedes Mal um Eins erhöht wird, wenn die Zelle lebendig ist.

Der Funktionsname wird `count_neighbors_via_for_loops()` sein und sie sollte die gleichen Eingaben und Ausgaben wie `count_neighbors_via_slicing()` haben. Und natürlich sollten die zurückgegebenen Zählungen identisch sein und mit denen in der Abbildung oben übereinstimmen. Teste sie auf die gleiche Weise wie `count_neighbors_via_slicing()`, um sicherzugehen.

::: {.program}
Implementire `count_neighbors_via_for_loops` in `evolution_utils.py` <br/>
Teste es in _code08.py_.
:::



## Nächste Generation

Die einzige Funktion, die wir benötigen, ist eine, die eine _neue_ Matrix für die Welt von morgen erschafft. Warum _neu_? Weil wir die Matrix für die Zukunft erschaffen müssen, unter Verwendung der Daten aus der Gegenwart. Wenn wir Zellen direkt ändern, würden wir die Nachbarzählungen verfälschen und ob eine Zelle lebt oder stirbt, würde von der Reihenfolge abhängen, in der wir sie untersuchen. Erstelle also eine neue leere Welt (erinnere dich, [numpy.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html) könnte nützlich sein!) und iteriere über alle Reihen und Spalten. Zähle die Nachbarn für jedes Element und wende dann die Regeln an:

1. Jede lebende Zelle mit zwei oder drei lebenden Nachbarn überlebt.
2. Jede tote Zelle mit drei lebenden Nachbarn wird zu einer lebenden Zelle.
3. Alle anderen lebenden Zellen sterben in der nächsten Generation. Ebenso bleiben alle anderen toten Zellen tot.

Wir nennen die Funktion `evolve` und sie sollte die Weltmatrix als Eingabe nehmen und, wiederum, eine _andere_ Matrix als Ausgabe zurückgeben. Sobald du die Funktion implementiert hast, teste sie mit der Glider-Welt. Deine Anfangszustände und die nächsten zwei Zustände sollten wie folgt aussehen:


```
#> Zeit 0
#> ⬜⬜⬛⬜
#> ⬛⬜⬛⬜
#> ⬜⬛⬛⬜
#> ⬜⬜⬜⬜
#> 
#> Zeit 1
#> ⬜⬛⬜⬜
#> ⬜⬜⬛⬛
#> ⬜⬛⬛⬜
#> ⬜⬜⬜⬜
#> 
#> Zeit 2
#> ⬜⬜⬛⬜
#> ⬜⬜⬜⬛
#> ⬜⬛⬛⬛
#> ⬜⬜⬜⬜
```

::: {.program}
Implementire `evolve` in `evolution_utils.py` <br/>
Teste es in _code09.py_.
:::

## Und wiederholen
Du hast jetzt alles, um eine sich entwickelnde Welt zu erschaffen. Implementiere ein Spiel mit einer [while](#while-loop)-Schleife, sodass es den Spieler nach jedem Zeitschritt nach einer Eingabe fragt und wenn die Eingabe nicht leer ist, stoppt das Spiel. Auf diese Weise macht das Spiel eine weitere Runde, wenn du einfach "Enter" drückst. Wenn du etwas anderes eingibst, stoppt es. Überlege dir eine Variable für die while-Schleife (kein `while True:`!), was ihr Anfangszustand sein sollte und wie du sie in der Schleife modifizierst/zuzuweist (es ist kein if-else erforderlich!).

Hier ist ein Beispiel für eine Welt, die mit der Funktion `create_world_via_numpy()` und dem Seed 42 erschaffen wurde. Beachte, wie die Struktur ab Zeitpunkt 6 stabil wird.


```
#> Zeit 0
#> ⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜
#> ⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜
#> ⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜
#> ⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜
#> Zeit 1
#> ⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜
#> ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜
#> ⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜
#> Zeit 2
#> ⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜
#> Zeit 3
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> Zeit 4
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜
#> Zeit 5
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
#> Zeit 6
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
#> Zeit 7
#> ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜
#> ⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜
#> ⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
```


::: {.program}
Implementire Program in _code10.py_.
:::

## Zusammenfassung
Großartig, packe deine Dateien in ein Zip-Archiv und reiche sie ein.

