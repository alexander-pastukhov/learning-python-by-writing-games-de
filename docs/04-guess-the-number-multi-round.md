# Errate die Zahl: Eine Mehr-Runden-Ausgabe {#guess-the-number-multi-round}

Im vorherigen Kapitel hast Du ein "Guess the Number"-Spiel programmiert, das nur einen einzigen Versuch erlaubt. Jetzt werden wir es erweitern, um mehrere Versuche zu ermöglichen und werden andere Extras hinzufügen, um es noch spannender zu machen. Erstelle einen neuen Unterordner und lade das [Übungs-Notebook](notebooks/Guess the number - multi round.ipynb) herunter, bevor wir beginnen!

## Konzepte des Kapitels

* Wiederholen von Code mit [while](#while-loop) Schleife.
* Machen in [Notausgang](#break) aus einer Schleife.

## While-Schleife {#while-loop}
Wenn Du etwas wiederholen möchtest, musst Du Schleifen verwenden. Es gibt zwei Arten von Schleifen: die [while](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) Schleife, welche wiederholt wird, _während_ eine Bedingung wahr ist, und die [for](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) Schleife, die über Elemente iteriert (wir werden sie später verwenden).

Die grundlegende Struktur einer _while_-Schleife ist

```python
# Anweisungen vor der Schleife

while <Bedingung>:
    # die inneren Anweisungen werden
    # so lange ausgeführt, wie
    # die Bedingung wahr ist
    
# Anweisungen nach der Schleife
```
Die `<Bedingung>` hier ist ein Ausdruck, der entweder `True` oder `False` ergibt, genau wie in einer `if...elif...else` [Bedingungsanweisung](#comparisons). Auch gelten dieselben [Einrückungsregeln](#indentation), die bestimmen, welcher Code innerhalb der Schleife und welcher außerhalb ist.

::: {.practice}
Mache Übung #1.
:::

Lass uns die _while_-Schleife verwenden, um dem Spieler zu erlauben, weiter zu raten, bis er es endlich richtig hat. Du kannst den Code, den Du während des letzten Seminars programmiert hast, kopieren und einfügen oder Du kannst ihn von Grund auf neu erstellen (ich würde Dir dringend empfehlen, Letzteres zu tun!). Die allgemeine Programmstruktur sollte folgende sein

```python
# importiere die Zufallsbibliothek, damit du die randint Funktion verwenden kannst

# generiere eine zufällige Zahl und speichere sie in der Variablen number_picked
# hole die Eingabe des Spielers, konvertiere sie in eine Ganzzahl und speichere sie in der Variablen guess

# während die Vermutung des Spielers nicht gleich dem Wert ist, den der Computer ausgewählt hat:
    # gib "meine Zahl ist kleiner" oder "meine Zahl ist größer" aus, indem Du die if-else Anweisung verwendest
    # hole die Eingabe des Spielers, konvertiere sie in eine Ganzzahl und speichere sie in der Variablen guess
    
# gib "Ganz genau!" aus 
# (denn wenn wir hier angekommen sind, bedeutet das, dass die Vermutung gleich der Wahl des Computers ist)
```

::: {.program}
Speichere deinen Code in `code01.py`.
:::

Vergiss nicht, die Datei zu dokumentieren und Breakpoints und Step overs zu verwenden, um den Programmfluss zu erkunden.

## Versuche zählen
Jetzt fügen wir eine Variable hinzu, die die Gesamtzahl der Versuche des Spielers zählt. Dazu erstelle eine neue Variable (nennen wir sie `attempts` oder ähnliches) _vor der Schleife_ und initialisiere sie mit `1` (weil der erste Versuch vor dem Betreten der Schleife vom Spieler gemacht wird). Füge jedes Mal, wenn der Spieler eine Vermutung eingibt, `1` hinzu. Erweitern Sie nach der Schleife die Nachricht `"Ganz genau!"` um Informationen über die Anzahl der Versuche. Nutze [String-Formatierung](##string-formatting), um alles schön aussehen zu lassen, z.B.: `"Ganz genau und du hast nur 5 Versuche gebraucht!"`. Überprüfe, ob die Anzahl der benötigten Versuche mit der Anzahl der vom Programm gemeldeten Versuche übereinstimmt!

::: {.program}
Speichere deinen Code in `code02.py`.
:::

## Abbruch (und Ausstieg) {#break}
Der Code innerhalb der _while_-Schleife wird wiederholt ausgeführt, während die Bedingung `True` ist und, was wichtig ist, der gesamte Code innerhalb wird ausgeführt, bevor die Bedingung erneut bewertet wird. Manchmal musst du jedoch früher abbrechen, ohne den verbleibenden Code auszuführen. Dafür hat Python eine [break](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) Anweisung, die dazu führt, dass das Programm die Schleife sofort verlässt, ohne den Rest des Codes innerhalb der Schleife auszuführen, so dass das Programm mit dem Code _nach_ der Schleife fortfährt.


```python
# dieser Code wird vor der Schleife ausgeführt

while <irgendeine_Bedingung>:
  # dieser Code wird bei jeder Iteration ausgeführt
  
    if <irgendeine_andere_Bedingung>:
        break
  
  # dieser Code wird bei jeder Iteration ausgeführt, aber nicht, wenn du aus der Schleife herausbrichst

# dieser Code wird nach der Schleife ausgeführt
```


::: {.practice}
Mache Übung #2, um dein Verständnis zu vertiefen.
:::

## Begrenzung der Anzahl der Versuche mittels Break
Setzen wir den Spieler unter Druck! Entscheide dich für eine maximale Anzahl an Versuchen, die du erlaubst, und speichere sie als [KONSTANTE](#constants). Wähle einen passenden Namen (z.B. `MAX_ATTEMPTS`) und BEACHTE, GROßBUCHSTABEN für den Namen einer Konstanten! Nun nutze `break` um die `while`-Schleife zu verlassen, wenn die aktuelle Versuchszahl größer als `MAX_ATTEMPTS` ist. Überlege, wann (innerhalb des Codes innerhalb der Schleife) du dies prüfen solltest.

::: {.program}
Speichere deinen Code in `code03.py`.
:::

## Korrekte End-of-Game-Nachricht
Aktualisieren wir die finale Nachricht. Im Moment steht dort "Ganz genau...", weil wir davon ausgegangen sind, dass das Programm die Schleife nur dann verlässt, wenn der Spieler die richtige Antwort gegeben hat. Bei begrenzten Versuchen ist das nicht unbedingt der Fall. Es gibt jetzt zwei Gründe, warum es die while-Schleife verlassen hat:

1. Der Spieler hat die richtige Antwort gegeben.
2. Dem Spieler sind die Versuche ausgegangen.

Verwende die `if-else` Bedingungsanweisung, um eine passende Nachricht auszugeben. Zum Beispiel drucke `"Viel Glück beim nächsten Mal!"`, wenn der Spieler verloren hat (die Versuche ausgegangen sind).

::: {.program}
Speichere deinen Code in `code04.py`.
:::

## Begrenzung der Anzahl der Versuche ohne Break
Obwohl es meine Idee war, die `break` Anweisung hinzuzufügen, solltest du sie sparsam verwenden. Ohne `break` gibt es eine _einzige_ Stelle im Code, die du überprüfen musst, um zu verstehen, wann das Programm die Schleife verlassen wird: die Bedingung. Wenn du jedoch ein `break` hinzufügst, hast du jetzt _zwei_ Stellen, die geprüft werden müssen. Und jedes zusätzliche `break` fügt weitere hinzu. Das bedeutet aber nicht, dass du sie um jeden Preis vermeiden solltest! Du _solltest_ sie verwenden, wenn dadurch der Code leichter zu verstehen ist. Aber überprüfe immer, ob eine modifizierte Bedingung auch den Trick tun könnte.

Probieren wir genau das aus. Ändere deinen Code so ab, dass er _ohne_ die `break` Anweisung funktioniert. Du brauchst eine kompliziertere Bedingung für deine while-Schleife, so dass sie sich wiederholt, solange die Vermutung des Spielers falsch ist und die Anzahl der Versuche noch kleiner ist als die maximal erlaubte. Teste, ob dein Code sowohl funktioniert, wenn du gewinnst als auch wenn du verlierst.

::: {.program}
Speichere deinen Code in `code05.py`.
:::

## Verbleibende Versuche anzeigen
Es geht alles um die Benutzeroberfläche! Ändere die Eingabeaufforderung so, dass sie die Anzahl der _verbleibenden_ Versuche enthält. Z.B. `"Bitte gebe eine Vermutung ein, du hast noch X Versuche übrig"`.

::: {.program}
Speichere deinen Code in `code06.py`.
:::

## Wiederholung des Spiels {#guess-the-number-repeat-game}
Lass uns dem Spieler die Option geben, noch einmal zu spielen. Das bedeutet, dass wir _allen_ aktuellen Code in eine weitere `while`-Schleife packen (das nennt man _verschachtelte Schleifen_), die so lange wiederholt wird, wie der Spieler weiterspielen möchte. Der Code sollte folgendermaßen aussehen:

```python
# importiere die random Bibliothek, damit du die Funktion randint verwenden kannst

# definiere MAX_ATTEMPTS

# definiere eine Variable namens "want_to_play" und setze sie auf True
# solange der Spieler noch spielen möchte
  
  # dein aktueller funktionierender Spielcode kommt hierher
  
  # frage den Benutzer mit der input-Funktion, z.B. "Möchtest du nochmal spielen? J/N"
  # want_to_play sollte True sein, wenn die Benutzereingabe gleich "J" oder "j" ist
  
# allerletzte Nachricht, zum Beispiel "Vielen Dank fürs Spielen!"
```

**Achte besonders auf die Einrückungen, um den Code richtig zu gruppieren!**

::: {.program}
Setze deinen Code in `code07.py`.
:::

## Du benötigst keinen Vergleich, wenn du bereits den Wert hast
In deinem aktualisierten Code hast du eine Variable `want_to_play`, die entweder `True` oder `False` ist. Sie wird in der Schleife verwendet, die sich wiederholt, solange ihr Wert `True` ist. Manchmal schreiben Leute `want_to_play == True`, um das auszudrücken. Obwohl es technisch korrekt und mit Sicherheit korrekt funktionieren wird, ist es auch redundant. Da `want_to_play` nur `True` oder `False` sein kann, verwandelt sich dieser Vergleich in `True == True` (was natürlich `True` ist) oder `False == True` (was `False` ist). Das Vergleichen eines jeden Werts mit `True` ergibt genau denselben Wert. Daher kannst du einfach `while want_to_play:` schreiben und den logischen Wert direkt verwenden.

## Bestes Ergebnis
Ein "richtiges" Spiel behält normalerweise die Leistung der Spieler im Auge. Lass uns die geringste Anzahl von Versuchen aufzeichnen, die der Spieler benötigt hat, um die Zahl zu erraten. Dazu erstellst du eine neue Variable `fewest_attempts` und setzt sie auf `MAX_ATTEMPTS` (das ist so schlecht, wie der Spieler sein kann). Überlege, wo du sie erstellen musst. Du solltest sie nach jeder Spielrunde aktualisieren. Füge die Information über "Bisher das Beste" in die finale Rundennachricht ein.

::: {.program}
Setze deinen Code in `code08.py`.
:::

## Zählen der Spielrunden
Lass uns zählen, wie oft der Spieler das Spiel gespielt hat. Die Idee und Umsetzung ist dieselbe wie beim Zählen der Versuche. Erstelle eine neue Variable, initialisiere sie auf 0, erhöhe sie um 1, wann immer eine neue Runde beginnt. Füge die Gesamtanzahl der gespielten Spiele in die allerletzte Nachricht ein, z.B. "Danke, dass du das Spiel _X_ Mal gespielt hast!"

::: {.program}
Setze deinen Code in `code09.py`.
:::

## Einarmiger Bandit mit mehreren Runden
Am Ende des vorherigen Kapitels hast du ein einarmiger Banditen-Spiel mit einer einzigen Runde programmiert. Du weißt bereits alles, was du brauchst, um eine Version mit mehreren Runden zu implementieren, und ihre Struktur ähnelt der des Mehr-Runden-Zahlenraten-Spiels, das du gerade implementiert hast, ist aber einfacher.

Lass den Spieler mit einem Anfangspot an Geld starten, sagen wir 10 Münzen. Jede Runde kostet 1 Münze, bei drei gleichen bekommt man 10 Münzen ausgezahlt, während man bei einem Paar 2 Münzen ausgezahlt bekommt (du kannst die Auszahlungen nach Belieben ändern). In jeder Runde:

 * Nimm eine Münze aus dem Topf (Preis für das Spiel).
 * Würfle die Würfel (das hast du bereits implementiert).
 * Informiere den Spieler über das Ergebnis (das hast du auch schon implementiert).
 * Füge Münzen zum Topf hinzu, falls nötig.
 * Drucke die Anzahl der im Topf verbliebenen Münzen aus.
 * Frage den Spieler, ob er weitermachen möchte. 
 
Sonderfall: Wenn dem Spieler die Münzen ausgehen, ist das Spiel definitiv vorbei.

::: {.program}
Setze deinen Code in `code10.py`.
:::

## Abschluss
Sehr gut, du hast jetzt zwei richtige funktionierende Computerspiele mit Spielrunden, begrenzten Versuchen, Bestleistung und vielem mehr! Pack den Ordner in eine Zip-Datei und reiche sie ein.
