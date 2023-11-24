# Rate das Tier {#guess-the-animal}

Heute programmieren wir ein Spiel, bei dem der Computer versucht, ein Tier zu erraten, an das du gedacht hast, und lernt aus seinen Fehlern, während er allmählich seinen Wortschatz aufbaut. Trotz der Einfachheit des Algorithmus, bietet es uns die Möglichkeit, über Wörterbücher, die kritischen Unterschiede zwischen veränderlichen und unveränderlichen Objekten, Rekursion und Dateisystem zu lernen. Wie üblich, schnapp dir das [Übungs-Notizbuch](notebooks/guess-the-animal.ipynb) bevor wir starten.

## Konzepte des Kapitels
* [Wörterbücher](#dictionaries)
* [Rekursion](#recursion)
* Veränderliche (Engl.: [Mutable](#mutable-objects)) vs. unveränderliche (Engl.: [Immutable](#variables-as-boxes-immutable-objects)) Objekte
* Speichern/Lesen von Objekten via [Pickle](#pickle) und [JSON](#json)

## Spielstruktur
Die Art und Weise, wie das Spiel gespielt wird, ist sehr einfach: In jeder Runde fragt der Computer dich, ob ein Tier eine bestimmte Eigenschaft hat oder ob es ein spezifisches Tier ist. Es beginnt nur mit einem Tier, sagen wir "Hund". Also fragt es dich "Ist das Tier, an das du denkst, ein Hund?". Wenn ja, ist das Spiel vorbei und du kannst es erneut tun. Wenn es jedoch kein Hund ist, fragt der Computer "Wer ist es dann?", sagen wir, du antwortest "Ente" und dann fragt der Computer auch "Was macht die Ente?" und du antwortest "quaken". Der wichtige Punkt hier ist, dass der Computer diese Information beim nächsten Mal, wenn du das Spiel spielst, nutzt. Es beginnt mit der Frage "quakt das Tier?", wenn ja, rät es "Ente", wenn nicht, fällt es auf das einzige Tier zurück, das es noch hat, und rät "Hund". Wenn es kein Hund ist, fragt es dich erneut "Wer ist es?", du sagst "Katze". "Was macht die Katze?", "miauen". Unten siehst du den Entscheidungsbaum, den der Computer in jeder Runde nutzen kann, und wie er die Informationen hinzufügt, die er aus seinen Fehlern gelernt hat.

![Entscheidungsbaum wächst über die Runden.](images/guess-the-animal-decision-tree.png){width=100%}
 
## Ja/Nein-Eingabe
In unserem Spiel werden wir _viele_ Ja/Nein-Fragen stellen, also fangen wir an mit der Programmierung der Funktion `input_yes_no`, die einen Eingabeaufforderungstext als Einzelargument nimmt und solange nach einer Antwort fragt, bis sie eine gültige erhält. Sie sollte `True` zurückgeben, wenn die Antwort "Ja" war und `False` für "Nein". Für die Bequemlichkeit sollte sie den Aufforderungstext mit der Nachricht `'Gib "j" für ja und "n" für nein ein.'` voranstellen, z.B. wenn der Eingabeaufforderungstext `"Ist es ein Pony?"` war, sollte die tatsächliche Eingabeaufforderung `'Gib "j" für ja und "n" für nein ein. Ist es ein Pony?'` sein. Dies sollte dir jetzt leicht fallen, da du während des [Jage den Wumpus](#hunt-the-wumpus) Spiels schon mehrere ähnliche Funktionen implementiert hast. Dokumentiere(!) es, teste es in Übung 1, und gib den Code in `utils.py` ein.

::: {.program}
Füge `input_yes_no` in _utils.py_ ein. <br/> Teste es in Übung 1.
:::

## Wörterbücher {#dictionaries}
Im Entscheidungsbaum haben wir zwei Arten von Knoten: 1) den Aktionsentscheidungsknoten ("quaken?") mit zwei Kanten (_ja_ und _nein_), die zu anderen Knoten führen, und 2) die tierischen Blattknoten ("Ente", "Hund", "Katze" usw.). Jeder Knoten hat folgende Eigenschaften:

* `Art`: Knoten-_Art_ entweder `"Aktion"` oder `"Tier"`
* `Text`: Knoten-_Text_, der entweder eine Aktion oder den Namen des Tieres enthält
* `ja` : Unterbaum für die Antwort "ja" (nur relevant für _Aktions_-Knoten)
* `nein` : Unterbaum für die Antwort "nein" (ebenfalls nur relevant für _Aktions_-Knoten)

Das verlangt nach einem Container und wir _könnten_ jeden Knoten mit seinen Unterbäumen in eine Liste stecken und numerische Indizes verwenden, um auf einzelne Elemente zuzugreifen: z.B. wäre `knoten[0]` die Knotenart, während `knoten[2]` den Ja-Unterbaum enthalten würde usw. Aber Indizes haben an sich keine Bedeutung, daher ist es nicht unmöglich, aber erfordert zusätzliche Anstrengungen herauszufinden, wie sich `knoten[0]` von `knoten[2]` unterscheidet. Python hat eine Lösung für Fälle wie diesen: [Wörterbücher](https://docs.python.org/3/library/stdtypes.html#dict).

Ein Wörterbuch ist ein Container, der Informationen in _Schlüssel : Wert_-Paaren speichert. Dies ist ähnlich, wie du in einem echten Wörterbuch eine Bedeutung oder Übersetzung (Wert) eines Wortes (Schlüssel) nachschlägst, daher der Name. Um ein Wörterbuch zu erstellen, verwendest du _geschweifte_ Klammern `{<Schlüssel1> : <Wert1>}, {<Schlüssel2> : <Wert2>, ...}` oder erstellst es über `dict(<Schlüssel1>=<Wert1>, <Schlüssel2>=<Wert2>, ...)`. Beachte, dass die zweite Variante restriktiver ist, da die Schlüssel den Regeln für Variablennamen folgen müssen, während in der geschweiften-Klammern-Version Schlüssel beliebige Zeichenketten sein können.
```python
buch = {"Autor" : "Walter Moers",
        "Titel": "Die 13½ Leben des Käpt'n Blaubär"}
       
# oder, äquivalent
buch = dict(Autor="Walter Moers",
            Titel="Die 13½ Leben des Käpt'n Blaubär")
```

Wenn du ein Wörterbuch erstellt hast, kannst du jedes Feld über seinen Schlüssel abrufen oder ändern, z.B. `print(buch["Autor"])` oder `buch["Autor"] = "Moers, W."`. Du kannst auch neue Felder hinzufügen, indem du ihnen Werte zuweist, z.B., `buch["Erscheinungsjahr"] = 1999`. Kurz gesagt, du kannst die Kombination von `<Wörterbuch-Variable>[<Schlüssel>]` genauso verwenden wie eine normale Variable. Dies ähnelt der Verwendung der Kombination `Liste[Index]`, der einzige Unterschied ist, dass `Index` eine Ganzzahl sein muss, während `Schlüssel` ein hashbarer^[Unveränderliche Werte sind [hashbar](https://docs.python.org/3/glossary.html#term-hashable), während veränderliche, wie Wörterbücher und Listen, es nicht sind. Dies liegt daran, dass sich veränderliche Objekte _ändern_ können, während das Programm läuft und daher als Schlüssel unbrauchbar sind. D.h., es ist schwer nach einem Schlüssel zu suchen, wenn der Schlüssel zur Zeit, wenn du auf das Wörterbuch zugreifen musst, anders sein kann.] Wert sein kann.

## Das Ein-Trick-Pony
Beginnen wir am Anfang, indem wir ein Wörterbuch mit einem einzigen Tier erstellen, das verwendet werden kann, um die Frage "Ist es ein <Tier>?" zu stellen. Erstelle ein Wörterbuch gemäß der oben dargelegten Struktur und überlege, welche Felder du benötigst (Hinweis, nicht alle vier) und welche Werte sie haben sollten. In Zukunft werden wir diesen Baum modifizieren, daher ist es, obwohl du ihn hart codierst, immer noch eine Variable, keine Konstante, also verwende den entsprechenden Namensstil. 

Als Nächstes benötigst du einen einfachen Code, der die Node `"Art"` überprüft und, wenn sie `"Tier"` ist, "Ist es ein <Tier>?" fragt (welches Feld musst du dafür verwenden?) mit der Funktion `input_yes_no`, die du zuvor implementiert hast. Gratuliere dir im Moment selbst, wenn die Antwort "ja" war (der Computer hat es richtig geraten!) aber unternehme sonst keine Aktion.

::: {.program}
Geben Sie Ihren Code in _code01.py_ ein.
:::


## Einen neuen Trick lernen
In der endgültigen Implementierung wird unser Entscheidungsbaum durch Versuch und Irrtum wachsen, aber zunächst lassen wir einen kleinen Entscheidungsbaum von Hand fest einprogrammieren. Erstelle zuerst ein Verzeichnis von Verzeichnissen für den Entscheidungsbaum in _Runde 2_. Es hat nur drei Knoten, der höchste ist ein Aktionsbaum mit zwei Unterbäumen. Jeder Unterbaum ist ein Blattknoten für Tiere. Wenn du dir nicht sicher bist, wie du das machen sollst, schreibe zuerst ein Verzeichnis für die Tierknoten. Dann schreibe den "Aktion"-Knoten und setze entweder Referenzen auf Tierverzeichnisse in die Felder "yes" und "no" oder füge die tatsächlichen Verzeichnisse ein. Da Unterbäume selbst Verzeichnisse sind, bedeutet das, dass du ein Verzeichnis in ein entsprechendes Feld einfügst. Daher wird `decision_tree['yes']` zu `{"kind" : "animal", "text" : "duck"}` und deshalb wird `decision_tree['yes']['animal']` zu `"duck"`. Sobald du es definiert hast, erkunde es von Hand in einem Jupyter-Notebook. Versuche verschiedene Felder und verschiedene Ebenen, wie im oben gezeigten Beispiel.

Jetzt, wo wir zwei Arten von Knoten haben, müssen wir den Abfragecode so aktualisieren, dass er bei einem _Tier_-Knoten nach "Ist es <Tier>?" fragt (du hast diesen Code schon), aber bei einem _Aktions_-Knoten nach "Tut es <Aktion>?". Implementiere das, aber unternimm noch keine Aktion für die Antwort auf die Aktion-Knoten-Frage. Packe den Code in eine Funktion `ask_question` ein, die nur das Baumverzeichnis als Parameter nimmt. Dokumentiere die Funktion und teste, dass sie funktioniert, indem du Bäume aus Runde 1 und Runde 2 verwendest (sollte unterschiedliche Fragen stellen!)

::: {.program}
Füge die Funktion `ask_question` in _utils.py_ ein.<br/>
Teste den Code in _code02.py_.
:::

## Rekursion
Unsere Bäume haben viele Knoten in verschiedenen Tiefen. Aber wenn wir an einem Knoten arbeiten müssen (eine relevante Frage stellen), ist das Einzige, was zählt, der Knoten selbst, nicht der Baum, zu dem er gehört, oder wo er in diesem Baum ist. Zum Beispiel, betrachte die untenstehenden Abbildungen mit vollständigen und verkürzten Entscheidungsbäumen. Sobald wir beim Knoten "miaut?" angekommen sind, macht es keinen Unterschied, ob wir von einem höheren Knoten kamen oder ob es der höchste Knoten selbst war. Die Frage, die wir stellen und die Entscheidung, die wir treffen, sind die gleichen. Ebenso macht es für uns keinen Unterschied, ob wir beim Knoten "Katze" nach langer Suche landen oder ob es der einzige Knoten war, den wir hatten.

![Verkürzter Entscheidungsbaum.](images/guess-the-animal-truncated.png){width=100%}

Das bedeutet, dass wir nur eine Funktion benötigen, die auf den Knoten reagiert und diese _gleiche_ Funktion wird auf einen relevanten Unter-Knoten für den _Aktions_-Knoten angewendet. D.h., die Funktion ruft sich selbst auf! Dies wird als Rekursion bezeichnet und ein klassisches Beispiel^[Eigentlich ist es etwas irreführend, da man für die Fakultät keine Rekursion benötigt, eine For-Schleife reicht aus. Aber es ist ein schönes und einfaches Spielzeugbeispiel, also gehen wir hier mit der Masse mit.] zur Veranschaulichung des Konzepts ist die Berechnung einer [Fakultät](https://de.wikipedia.org/wiki/Fakultät_(Mathematik)):
$$!n = n \times (n - 1) \times (n - 2) \times ...\times3\times2\times1$$

Es ist leicht zu erkennen, dass die Berechnung hier von Natur aus rekursiv ist, da die Formel wie folgt umgeschrieben werden kann:
$$!n = n \times !(n - 1)$$

Die einzige Ausnahme ist, wenn $n = 1$, daher lautet die vollständige Formel:
$$\ !n = \begin{cases}
  1 & \text{if n = 1} \\
  n \times !(n - 1) & \text{if n > 1}
\end{cases}$$

Deine Aufgabe ist es, eine Funktion zu schreiben (dokumentiere sie!), die eine Fakultät für eine gegebene positive ganze Zahl mit der obigen Formel berechnet. Solange $n > 1$ sollte es sich selbst verwenden, um die Fakultät der verbleibenden Zahlen zu berechnen. Teste die Funktion, um zu überprüfen, ob die Berechnung korrekt funktioniert. Setze einen Haltepunkt in die Funktion und verwende einen Debugger, um zu sehen, wie die Rekursion funktioniert.

::: {.program}
Implementiere und teste die `factorial` Funktion in Übung 2.
:::

## Erkundung des Entscheidungsbaums
Lassen uns die Idee der Rekursion anwenden, um den Entscheidungsbaum zu erkunden, während wir das Spiel spielen. Du kannst für den Moment den Entscheidungsbaum, der unten in der Figur gezeigt wird, hardcodieren. Du kannst Wörterbücher direkt verschachteln, aber ich fand es einfacher, ein `meow_action` Wörterbuch für den zweiten Unterbaum separat zu definieren und es dann dem `"no"` Feld des Quack-Wörterbuchs aus dem `code02` zuzuweisen.

![Entscheidungsbaum für drei Tiere.](images/guess-the-animal-three.png){width=100%}

Als Nächstes müssen wir die Funktion `ask_question` erweitern, nennen wir die neue Version `explore_tree`. Der Schlüssel und einzige Änderung: Wenn der Knoten ein _Aktions_-Knoten ist, geht die Funktion eine Ebene tiefer und ruft _sich selbst_ (Rekursion!) mit dem entsprechenden "Ja" oder "Nein" Unterbaum auf, der durch die Antwort des Spielers bestimmt wird.

Unser Hauptproblem hier ist, dass die von der Funktion `input_yes_no` zurückgegebenen Werte nicht mit den entsprechenden Feldschlüsseln übereinstimmen, daher müssen wir die logischen Werte in die Strings `"yes"` und `"no"` "umwandeln". Es gibt zwei Möglichkeiten, dies zu tun, eine, die für binäre Fälle wie unsere funktioniert, verwendet [bedingte Ausdrücke](https://docs.python.org/3/reference/expressions.html#conditional-expressions), eine andere ist allgemeiner und funktioniert zur Übersetzung einer beliebigen Anzahl von Dateien mit [Wörterbüchern](#dictionaries).

Die bedingte Zuweisung ist eine Syntactic Sugar, die eine if-else-Anweisung für spezielle Fälle der Wertauswahl basierend auf Bedingungen vereinfacht. Hier ist ein Beispiel für eine vollständige und kompakte Version des gleichen Codes, beachte, dass du _prinzipiell_ die Aufrufe verschachteln könntest, um eine "if else if else"-Struktur zu erstellen, aber das ist garantiert, dass der Code unleserlich wird, daher würde ich immer eine Standard-If-elif-else für Fälle wie diesen verwenden.


```python
a_value = 1

# standard if-else
if a_value > 0:
  value_kind = "positive"
else:
  value_kind = "zero or negative"
  
# conditional assignment
value_kind = "positive" if a_value > 0 else "zero or negative"
```

Implementiere und teste den Code zur Umwandlung eines logischen Werts, der in einer `user_response` Variable gespeichert ist, mit bedingten Ausdrücken in Übung 3.

::: {.program}
Implementiere und teste Bedingte Ausdrücke<br/>
in Übung 3.
:::

Bedingte Ausdrücke funktionieren gut für binäre Fälle, werden aber umständlich und unlesbar, selbst wenn du nur drei Werte zum Umwandeln hast. Eine einfachere Lösung besteht darin, Wörterbücher zu verwenden, die <Original> → <Übersetzung> als Feld: Schlüsselpaar definieren: "{Original: Übersetzung}". Dann kannst du einfach den Originalwert als Schlüssel verwenden und die Übersetzung direkt erhalten. In Übung 4, implementiere die gleiche Umwandlung von logischen zu "Ja"/"Nein"-Strings wie zuvor, aber mit Wörterbüchern.

::: {.program}
Implementiere die Übersetzung mit Wörterbüchern<br/>
in Übung 4.
:::

Kehren wir zurück zu `explore_tree`: Sobald du eine Benutzerantwort für einen _Aktions_-Knoten erhältst, wandele sie mit einer der beiden Methoden (wähle diejenige, die du einfacher zu lesen und zu verstehen findest) in einen "Ja"/"Nein"-Schlüssel um. Die Funktion sollte sich selbst aufrufen (wieder Rekursion!) und den entsprechenden Unterbaum als Parameter übergeben. Einmal implementiert, rufe es mit dem hardcodierten Baum auf und teste es, indem du verschiedene Antworten gibst. Der Baum ist klein, du solltest also schnell alle Pfade ausprobieren können. Es sollte ein positives "Juhu!" (oder eine beliebige von dir gewählte Nachricht) geben, wenn du am Ende zustimmst, dass die Vermutung des Computers über ein Tier korrekt war, und keine Ausgabe, wenn du "Nein" gesagt hast.

::: {.program}
Implementiere die Funktion `explore_tree` in _utils.py_<br/>
Verwende sie im Code _code03.py_.
:::

Unser nächster Schritt ist das Schreiben des Codes, der den Baum erweitert, aber bevor wir damit beginnen, musst du mehr über veränderbare Objekte und die Vorteile und Gefahren, die sie mit sich bringen, lernen.

## Variablen als Schachteln (unveränderliche Objekte)
In diesem Spiel wirst du [Wörterbücher](#dictionaries) verwenden. Diese sind _veränderlich_, wie [Listen](#listen), im Gegensatz zu "normalen" _unveränderlichen_ Werten (Ganzzahlen, Fließkommazahlen, Zeichenketten). Du musst diesen Unterschied lernen, da diese beiden Arten von Objekten (Werten) unter bestimmten Umständen sehr unterschiedlich reagieren, was sowohl gut (Macht!) als auch schlecht (merkwürdiges, unerwartetes Verhalten!) ist.

Vielleicht erinnerst du dich an die Metapher _variable-as-a-box_, die ich verwendet habe, um [Variablen](#variables) einzuführen. Kurz gesagt, eine Variable kann als eine "Schachtel" gedacht werden, auf der der Name der Variable geschrieben steht und ein Wert "innen" gespeichert wird. Wenn du diesen Wert benutzt oder ihm eine andere Variable zuweist, kannst du davon ausgehen, dass Python _eine Kopie_ davon macht^[Nicht wirklich, aber das macht es einfacher zu verstehen.] und diese _Kopie_ in eine andere Variable "Schachtel" steckt. Wenn du den Wert einer Variable _ersetzt_, nimmst du den alten Wert heraus, zerstörst ihn (indem du ihn in das nächste Schwarze Loch wirfst, nehme ich an), erstellst einen neuen und steckst ihn in die Variable "Schachtel". Wenn du eine Variable auf Basis ihres aktuellen Zustands _änderst_, passiert dasselbe. Du nimmst den Wert heraus, erzeugst einen neuen Wert (indem du zum ursprünglichen hinzufügst oder eine andere Operation ausführst), zerstörst den alten und legst den neuen zurück in die Variable "Schachtel". Der wichtige Punkt ist, dass, obwohl eine _Variable_ verschiedene unveränderliche Werte haben kann (wir haben die `imole` Variable in jeder Runde [geändert](#random-mole)), der unveränderliche _Wert_ selbst sich nie ändert. Er wird _ersetzt_ durch einen anderen unveränderlichen Wert, aber _ändert sich nie_^[Ein Metaphernversuch: Du kannst verschiedene Hemden tragen, daher ändert sich dein _Look_ (Variable), aber jedes einzelne Hemd (potentielle Werte) bleibt gleich (wir ignorieren hier Verschleiß) unabhängig davon, ob du es trägst (Wert ist einer Variable zugewiesen) oder nicht.].

Die Schachtel-Metapher erklärt, warum [Anwendungsbereiche](#scopes-for-immutable-values) so funktionieren, wie sie es tun. Jeder Anwendungsbereich hat sein eigenes Set an Schachteln und wann immer du Informationen zwischen Anwendungsbereichen austauscht, zum Beispiel von einem globalen Skript zu einer Funktion, wird eine Kopie eines Werts (aus einer Variable) erstellt und in eine neue Schachtel (z.B. ein Parameter) innerhalb der Funktion gestellt. Wenn eine Funktion einen Wert zurückgibt, wird er kopiert und in eine der Schachteln im globalen Skript (Variable, der du den zurückgegebenen Wert zugewiesen hast) gestellt, usw.

Dies gilt jedoch nur für _unveränderliche_ Objekte (Werte) wie Zahlen, Zeichenketten, logische Werte usw., aber auch [Tupel](https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple) (siehe unten für was diese sind). Wie du aus dem Namen erraten kannst, bedeutet das, dass es auch andere _veränderbare_ Objekte gibt und diese verhalten sich sehr unterschiedlich.

## Variablen als Post-its (veränderbare Objekte) {#mutable-objects}
Beispiele für veränderbare Objekte sind Listen oder Wörterbücher^[Kommt gleich!], also Dinge, die sich ändern können. Der entscheidende Unterschied ist, dass _unveränderliche_ Objekte als fest in ihrer Größe betrachtet werden können. Eine Zahl benötigt so viele Bytes zum Speichern, das Gleiche gilt für eine gegebene Zeichenkette (obwohl eine andere Zeichenkette mehr oder weniger Bytes benötigen würde). Trotzdem ändern sie sich nicht, sie werden erstellt und zerstört, wenn sie nicht mehr benötigt werden, aber niemals wirklich aktualisiert.

_Veränderbare_ Objekte können geändert werden^[Fortführend mit der Aussehens-Metapher: Du kannst dein Aussehen ändern, indem du ein anderes (unveränderliches) Hemd benutzt oder indem du deine Frisur _änderst_. Deine Haare sind veränderbar, du trägst nicht an verschiedenen Tagen eine andere, um anders auszusehen, du musst sie modifizieren, um anders auszusehen.]. Du kannst beispielsweise Elemente zu deiner Liste hinzufügen, entfernen oder sie mischen. Das Gleiche gilt für [Wörterbücher](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries). Ein solches Objekt _unveränderlich_ zu machen, wäre rechnerisch ineffizient: Jedes Mal, wenn du einen Wert hinzufügst, wird eine (lange) Liste zerstört und mit nur diesem einen zusätzlichen Wert neu erstellt. Aus diesem Grund _aktualisiert_ Python einfach das ursprüngliche Objekt. Für weitere Recheneffizienz werden diese Objekte nicht kopiert, wenn du sie einer anderen Variable zuweist oder als Parameterwert verwendest, sondern werden _per Referenz übergeben_. Das bedeutet, dass die Variable nicht mehr eine "Schachtel" ist, in die du Werte legst, sondern ein "Aufkleber", den du auf ein Objekt (eine Liste, ein Wörterbuch) klebst. Und du kannst so viele Aufkleber auf ein Objekt kleben, wie du willst _und es wird immer noch dasselbe Objekt sein_!

Was zum Teufel meine ich damit? Denke daran, dass eine Variable nur ein Aufkleber (einer von vielen) auf einem veränderbaren Objekt ist, und versuche herauszufinden, was die Ausgabe unten sein wird:

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

::: {.practice}
Mach Übung #5.
:::

Hä? Das ist genau das, was ich mit "Aufklebern auf demselben Objekt" meinte. Zuerst erstellen wir eine Liste und kleben einen `x` Aufkleber darauf. Dann weisen wir _die gleiche Liste_ `y` zu, mit anderen Worten, wir kleben einen `y` Aufkleber _auf die gleiche Liste_. Da sowohl `x` als auch `y` Aufkleber auf dem _gleichen_ Objekt sind, sind sie effektiv Synonyme. In dieser speziellen Situation, sobald du `x = y` festlegst, ist es egal, welchen Variablennamen du verwendest, um _das_ Objekt zu ändern, sie sind nur zwei Aufkleber, die nebeneinander an der _gleichen_ Liste hängen. Nochmals zur Erinnerung, das ist _nicht_ das, was bei _unveränderlichen_ Werten wie Zahlen passieren würde, wo die Dinge sich so verhalten würden, wie du es erwartest.

Diese Theorie von Variablen als Aufkleber, auch bekannnt als "Wertübergabe per Referenz", hat sehr wichtige Auswirkungen auf Funktionsaufrufe, da sie deinen Umfang bricht, ohne dir jemals eine Warnung zu geben. Schau dir den untenstehenden Code an und versuche herauszufinden, welche Ausgabe es geben wird.

```python 
def change_it(y):
    y.append(4)

x = [1, 2, 3]
change_it(x)
print(x)
```
::: {.practice}
Mache Übung #6.
:::

Wie haben wir es geschafft, eine _globale_ Variable von innerhalb der Funktion zu ändern? Haben wir nicht den _lokalen_ Parameter der Funktion geändert? Ja, genau das ist das Problem bei der Übergabe per Referenz. Dein Funktionsparameter ist nur ein weiterer Sticker auf dem _gleichen_ Objekt. Selbst wenn es also _aussieht_, als müsstest du dir keine Sorgen um globale Variablen machen (dafür hast du ja die Funktion geschrieben und über Scopes gelernt!), musst du das doch. Wenn dich das verwirrt, bist du in guter Gesellschaft. Dies ist eine der unerwartetsten und verwirrendsten Stellen in Python, die immer wieder Leute^[Naja, zumindest mich!] überrascht. Lass uns noch ein paar Übungen machen, bevor ich dir zeige, wie du das Scope-Problem bei veränderbaren Objekten lösen kannst.

::: {.practice}
Mach die Übung #7.
:::

## Tupel: eine eingefrorene Liste {#tuple}
Die klugen Leute, die Python entwickelt haben, waren sich des Problems, das die _Variable-als-Sticker_-Methode schafft, sehr bewusst. Darum haben sie eine **unveränderliche** Version einer Liste hinzugefügt, genannt [Tupel](https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple). Es handelt sich um eine "eingefrorene" Liste von Werten, über die du iterieren kannst, auf deren Elemente du per Index zugreifen kannst oder herausfinden, wie viele Elemente sie hat, aber du _kannst sie nicht ändern_. Kein Anhängen, Entfernen, Ersetzen von Werten, etc. Für dich bedeutet das, dass eine Variable mit einer eingefrorenen Liste eher eine Box als ein Sticker ist und dass sie sich genau wie jedes andere "normale" **unveränderliche** Objekt verhält. Du kannst ein `Tupel` erstellen, indem du runde Klammern verwendest.
```python
ich_bin_ein_tupel = (1, 2, 3)
```
Du kannst über es iterieren, z.B.

```python
ich_bin_ein_tupel = (1, 2, 3)
for number in ich_bin_ein_tupel:
    print(number)
#> 1
#> 2
#> 3
```

wie ich aber schon sagte, wird das Anhängen einen Fehler verursachen

```python
ich_bin_ein_tupel = (1, 2, 3)

# wirft AttributeError: 'tuple' object has no attribute 'append'
ich_bin_ein_tupel.append(4)
#> 'tuple' object has no attribute 'append'
```
Das Gleiche passiert, wenn du es versuchst zu ändern

```python
ich_bin_ein_tupel = (1, 2, 3)

# wirft TypeError: 'tuple' object does not support item assignment
ich_bin_ein_tupel[1] = 1 
#> 'tuple' object does not support item assignment
```
Das bedeutet, dass wenn du eine Liste von Werten an eine Funktion übergeben musst und du nicht möchtest, dass sie eine Verbindung zur ursprünglichen Variable hat, solltest du stattdessen _ein Tupel von Werten_ an die Funktion übergeben. Die Funktion hat immer noch eine Liste von Werten, aber die Verbindung zum ursprünglichen Listenobjekt ist jetzt unterbrochen. Du kannst eine Liste in ein Tupel umwandeln, indem du `tuple()` verwendest. Wenn du bedenkst, dass `tuple()` eine eingefrorene Kopie der Liste erstellt, was wird dann im Folgenden passieren?
```python
x = [1, 2, 3]
y = tuple(x)
x.append(4)
print(y)
```
::: {.practice}
Mach die Übung #8.
:::

Wie du wahrscheinlich herausgefunden hast, erstellt Python bei `y = tuple(x)` **eine Kopie** der Listeneinträge, friert sie ein (sie sind jetzt unveränderlich) und legt sie in die "y"-Box. Daher hat alles, was du mit der ursprünglichen Liste machst, keinen Einfluss auf das unveränderliche "y".

Umgekehrt kannst du ein Tupel "auftauen", indem du es mit `list()` in eine Liste umwandelst. Bitte beachte, dass dies **eine neue Liste** erstellt, die keinen Bezug zu jeder anderen existierenden Liste hat, auch wenn die Werte gleich sind oder ursprünglich von einer von ihnen stammen!

::: {.practice}
Mach die Übung #9.
:::

Erinnerst du dich, dass ich gerade gesagt habe, dass `list()` eine neue Liste erstellt? Das bedeutet, dass du es verwenden kannst, um direkt eine Kopie einer Liste zu erstellen, ohne einen Zwischenschritt über ein Tupel. Auf diese Weise kannst du zwei _verschiedene_ Listen mit _identischen_ Werten erstellen. Du kannst das gleiche Ergebnis auch erzielen, indem du eine gesamte Liste ausschneidest, z.B. ist `list(x)` das Gleiche wie `x[:]`.

::: {.practice}
Mach die Übung #10.
:::

Hier hat `y = list(x)` eine neue Liste erstellt (die eine genaue Kopie derjenigen war, auf der der "x"-Sticker klebte) und der "y"-Sticker wurde auf diese neue Liste geklebt, während der "x" am Original hängen blieb.

Wenn dir jetzt der Kopf schwirrt, muss ich dir leider sagen, dass es noch schlimmer wird. Der folgende Absatz behandelt ein ziemlich fortgeschrittenes Szenario, aber ich möchte, dass du davon weißt, da die Dinge extrem kontraintuitiv funktionieren und ich persönlich schon ein paar Mal auf dieses Problem gestoßen bin und es hat mich immer _ewig_ gekostet, das Problem herauszufinden. Deshalb möchte ich, dass du dir zumindest dessen bewusst bist. Was ist, wenn du ein Tupel (unveränderlich!) hast, das eine Liste (veränderlich) enthält? Wie ich dir schon früher sagte, kannst du den Eintrag selbst nicht ändern, aber dieser Eintrag ist nur eine Referenz auf die Liste (ein Sticker auf einem _veränderlichen_ Objekt!), so dass du selbst wenn das Tupel unveränderlich ist, immer noch mit der Liste selbst herumhantieren kannst. Darüber hinaus wird das Anfertigen einer Kopie eines Tupels lediglich eine Kopie der Referenz erstellen, die immer noch auf die gleiche Liste zeigt! Also könntest du denken, dass, weil alles Tupel sind, alles unveränderlich und gut verhält, und von dem erwischt werden^[Wenn dich das zum Schreien bringen will, sag es mir und wir machen es zusammen.]. Hier ist ein Beispiel für ein solches Durcheinander:


```python
tuple_1 = tuple([1, ["A", "B"], 2])
tuple_2 = tuple_1

# Das funktioniert (korrekterweise) nicht.
tuple_1[0] = ["C", "D"]
#> 'tuple' object does not support item assignment

# Aber wir können das erste Element der Liste zu "C" ändern und das zweite zu "D"
# Die Referenz zur Liste ist eingefroren, aber die Liste selbst ist veränderlich!
tuple_1[1][0] = "C"
tuple_2[1][1] = "D"

print(tuple_1)
#> (1, ['C', 'D'], 2)
print(tuple_2)
#> (1, ['C', 'D'], 2)
```

Verwirrend? Wetten, dass! Wenn du dich von dieser ganzen unveränderlich/veränderlich, Tupel/Liste, Kopie/Referenz-Verwirrung überwältigt fühlst, bist du nur ein normaler Mensch. Ich verstehe die (rechnerischen) Gründe, warum man die Dinge auf diese Weise macht, ich bin mir dieser Unterschiede und wie nützlich sie sein können bewusst, aber trotzdem überraschen sie mich immer wieder! Also, ein Rat, sei vorsichtig und überprüfe deinen Code immer mit dem Debugger, wenn du Listen oder Wörterbücher zuweist, sie an Funktionen übergibst, Kopien anfertigst, Listen in Listen hast, etc. Sei dir bewusst, dass die Dinge vielleicht nicht so funktionieren, wie du denkst, dass sie sollten!

## Erweitern des Baumes
Zurück zur Aufgabe, den Baum zu erweitern. Jeder Knoten, den wir in einem Baum haben, ist ein [Wörterbuch](https://docs.python.org/3/library/stdtypes.html#dict), welches veränderlich ist und das macht es einfach, wenn auch ein bisschen verwirrend. Das Gute ist, wir können den Baum von _innen_ der Funktion aus verändern. Wie ich dir oben gezeigt habe, gibst du nicht das Wörterbuch selbst an die Funktion weiter, sondern eine _Referenz_ darauf, also wird alles, was du mit irgendeinem Wörterbuch innerhalb des Baumes machst, in der globalen Baumvariable reflektiert. Das verwirrende dabei ist, dass wir im Hinterkopf behalten müssen, dass wir immer mit einer _Referenz_ arbeiten, also wenn wir die Daten kopieren müssen, wird eine einfache Zuweisung nicht ausreichen (weil sie nur die Referenz kopiert, erinnerst du dich?) Wir haben zwei Optionen, die in der unten stehenden Abbildung dargestellt sind. Der ursprüngliche Baum hat nur einen Knoten, dargestellt durch <span style="color=red;">Dict #1.</span>. Wenn wir den Baum erweitern, muss dieser Knoten nach unten versetzt werden und zu einem Blatt eines Aktionsknotens werden, der nun zum Ausgangspunkt wird. Wir können ein neues Aktionsknoten-Wörterbuch (_Dict #2_) erstellen, einen neuen Tierknoten für die Katze (_Dict #3_) und sie wie in Option #1 anordnen. In diesem Fall müssen wir jedoch sicherstellen, dass die Referenz in der Variable `tree` aktualisiert wird, so dass sie nun auf _Dict #2_ zeigt. Alternativ können wir <span style="color=red;">Dict #1.</span> als obersten Knoten behalten, aber seinen Inhalt komplett ersetzen und ihn in einen Aktionsknoten umwandeln. Die ursprünglichen Informationen werden in ein neues _Dict #3_ kopiert. Lass uns beide Ansätze ausprobieren, angefangen mit Option #1.

![Zwei Optionen zum Erweitern des Baums.](images/guess-the-animal-extend.png){width=100%}


## Den Baum durch Zurückgeben einer neuen Referenz erweitern
Lass uns wie gewohnt in kleinen Schritten vorgehen. Schreibe zuerst einen Code, der einen _Tier_-Knoten nimmt (setze die `tree` Variable per Hand) und erstelle einen Baum mit drei Knoten, wie in Option #1 oben. Du musst zwei zusätzliche Wörterbücher erstellen und sie auf die Felder `"ja"` und `"nein"` setzen, damit du ein Wörterbuch erhältst, das dem Baum in Option #1 entspricht. Harte zunächst das neue Tier und die neue Aktion. Sobald dein Code funktioniert, ersetze die fest codierten Werte durch `input` Aufrufe, die den Benutzer fragen: "Wer ist es?" und "Was macht <Tier>?".

::: {.practice}
Teste den Code in Übung #11.
:::

Das gibt uns den Code, den wir für die `explore_and_extend_tree_via_return` Funktion benötigen (Ich weiß, dass ist ein Mundvoll), die die `explore_tree` Funktion, die du zuvor implementiert hast, erweitert. Denke darüber nach, wo der neue Code hinkommt.

Eine wichtige Änderung ist, dass die Funktion nun eine Referenz zum Baum (dem Wörterbuch mit dem Baum) zurückgeben muss. Es handelt sich entweder um den _ursprünglichen_ Baum oder, falls du ihn erweitert hast, um den _neuen_ Baum. Das bedeutet auch, dass den Aktionsknoten entweder die `"ja"` oder `"nein"` Wörterbücher eine Referenz zugewiesen werden muss, die von einem rekursiven Aufruf der Funktion `explore_and_extend_tree_via_return` zurückgegeben wird. Zum Beispiel, wenn nichts passiert ist, wird die gleiche Referenz auf das ursprüngliche Wörterbuch zurückgegeben und zugewiesen. Wenn wir jedoch einen _neuen_ Baum erstellt haben, müssen die Referenzen auf diesen _neuen_ Baum nun im Feld `"ja"` oder `"nein"` gespeichert werden. Wenn wir das nicht tun, wird das Feld immer noch auf den ursprünglichen Knoten zeigen und unsere Änderungen sind unsichtbar. Das Gleiche gilt für die oberste Ebene, da dies bedeutet, dass wir nicht nur unseren globalen `tree` an die Funktion übergeben, sondern auch die zurückgegebene Referenz wieder zuweisen müssen. Überlege, wann/wo du das aktualisierte oder ursprüngliche Wörterbuch zurückgeben und wann/wo du den zurückgegebenen Wert einem "ja"/"nein" Feld zuweisen musst.

Aktualisiere die Funktion (überprüfe doppelt, welche Funktion du rekursiv aufrufst, es sollte `explore_and_extend_tree_via_return` sein, nicht die ursprüngliche `explore_tree`!) und teste sie, indem du mit einem einzelnen Tierknotenbaum beginnst und ihn in einer endlosen Schleife aufrufst (wir verwenden vorerst den Notstopp über den Debugger als Exit-Strategie). Ich würde vorschlagen, das Wörterbuch nach jedem Aufruf (Erkunden und Erweitern des Baums) auszudrucken, um zu sehen, wie es wächst, sowie einen Haltepunkt innerhalb oder nach der Funktion zu setzen, um den Prozess zu erforschen, den Aufrufstapel zu sehen und die Parameterwerte für jede Stufe zu prüfen.

::: {.program}
Implementiere die Funktion in _utils.py_<br/>
Verwende sie im Code _code04.py_.
:::

## Den Baum durch Modifikation eines Wörterbuchs am Ort erweitern
Die zweite Option (siehe Illustration oben) ist einfacher, weil wir nichts zurückgeben müssen. Sie ist jedoch weniger transparent, da wir Dinge hinter den Kulissen verändern und diese Änderungen nicht offensichtlich durch eine Rückgabe signalisiert werden. Schreibe zuerst den Code, der _zwei_ neue Tierknoten erstellt und den Inhalt des ursprünglichen Knotens durch eine neue Aktion ersetzt (wie zuvor, codiere zuerst das neue Tier und die neue Aktion hart, später ersetze es durch `input` Aufrufe wie in der vorherigen Funktion). Du kannst prüfen, ob der `tree` das gleiche Objekt referenziert, indem du seine [id](https://docs.python.org/3/library/functions.html#id) überprüfst. Sie sollte gleich bleiben, auch wenn der Inhalt anders ist (die `id` für den obersten Knoten sollte sich in Übung #11 ändern, gehe zurück zum Code und überprüfe).

Wichtiger Hinweis! Denke daran, dass `tree` eine _Referenz_ ist, daher wird dir `no_animal = tree` nicht helfen, die ursprünglichen Informationen in einem neuen Knoten zu speichern, da dies bedeutet, dass sowohl `tree` als auch `no_animal` auf dasselbe Wörterbuch verweisen werden. Denke daran, dass es die Referenz auf ein Wörterbuch ist, die kopiert wird, nicht der tatsächliche Inhalt des Wörterbuchs. Mache `no_animal = tree` und drucke dann die [id](https://docs.python.org/3/library/functions.html#id) für beide (die gleiche) aus und schreibe `tree is no_animal` (`is` überprüft, ob zwei Objekte identisch sind, d.h. dieselben Objekte, daher wird es `True` sein). Seltsamerweise wird, sobald du danach `tree["no"] = no_animal` schreibst, es _sich selbst_ referenzieren (`tree is tree["no"]` wird `True` sein)!


```python
# Zuweisung kopiert Referenz, das Objekt bleibt jedoch gleich.
dict1 = {"a": 1}
dict2 = dict1
print(id(dict1), id(dict2), dict1 is dict2)
#> 2256991031872 2256991031872 True

# Das Objekt referenziert sich selbst!
dict1["a"] = dict1
print(id(dict1), id(dict1["a"]), dict1 is dict1["a"])
#> 2256991031872 2256991031872 True
```

Es gibt zwei Wege, dieses Problem zu lösen. Du kannst ein neues Wörterbuch erstellen, indem du die _Feld-_ Werte einzeln zuweist. Da unsere "Tier"-Wörterbuchfeldwerte unveränderliche Zeichenketten sind, wird dieses Vorgehen ein _anderes_ Objekt mit dem gleichen _Inhalt_ erstellen.


```python
dict1 = {"a": 1}
dict2 = {"a" : dict1["a"]}

# gleicher Inhalt!
print(dict1 == dict2)
#> True

# verschiedene Objekte
print(id(dict1), id(dict2), dict1 is dict2)
#> 2256990820544 2256991072704 False
```

Alternativ kannst du entweder eine flache [Kopie](https://docs.python.org/3/library/copy.html#copy.copy) oder eine [tiefe Kopie](https://docs.python.org/3/library/copy.html#copy.deepcopy) von einem Objekt erstellen, indem du die [copy](https://docs.python.org/3/library/copy.html) Bibliothek verwendest. Die erstere - [copy](https://docs.python.org/3/library/copy.html#copy.copy) - erstellt eine "flache" Kopie indem sie den Kontext "wie er ist" kopiert. In diesem Fall wird eine Referenz zu einem anderen Objekt kopiert, so wie sie ist, und verweist immer noch auf das gleiche Objekt. Die [deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy) geht tiefer und erstellt eine Kopie für das Objekt, auf das das Original verweist. Letzteres ist rechenintensiver (du erstellst Kopien von _allem_!), aber es garantiert, dass eine Kopie erstellt wird, die keine versteckten Verbindungen zum Original hat. Also, im Zweifelsfall, nimm die [deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy). In unserem Fall gibt es keinen Unterschied, da unser ursprüngliches Wörterbuch gerade mal zwei unveränderliche Zeichenketten hat, so dass sowohl [copy](https://docs.python.org/3/library/copy.html#copy.copy) als auch [deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy) das Gleiche tun würden.

In unserem Code verwenden wir die letztere Option über die [copy](https://docs.python.org/3/library/copy.html) Bibliothek. Schreibe den Code, der den Baum erweitert, indem er den Inhalt des ursprünglichen Knotens ersetzt und neue Tierknoten in Übung 12 hinzufügt. Beachte, dass du einen Baum nicht mit der Notation `tree = {...}` verändern kannst, da dies ein _neues_ Objekt erzeugen würde. Um vor Ort zu verändern, musst du die Felder einzeln über die Zuweisung `tree[field] = value` ändern.

::: {.practice}
Teste den Code in Übung #12.
:::

Jetzt, wo der Code funktioniert, kannst du ihn in einer neuen Funktion namens `explore_and_modify_tree` verwenden, die auf der `explore_tree` Funktion aufbaut. Wiederum verwende den neuen Code, wenn du dich im _Tier_-Knoten befindest und die Vermutung falsch war (Antwort war "nein"). Diese Funktion ist einfacher als `explore_and_extend_tree_via_return`, da du dir keine Gedanken über Rückgabewerte und deren Rückzuweisung machen musst. Teste sie auf die gleiche Weise in einer endlosen Schleife, wie du es für `explore_and_extend_tree_via_return` getan hast. Überprüfe doppelt, welche Funktion du beim rekursiven Aufruf aufrufst!

::: {.program}
Implementiere die Funktion in _utils.py_<br/>
Verwende sie im Code _code05.py_.
:::

## Kann ich jetzt nach Hause gehen?
Unser Programm funktioniert gut, aber die aktuelle Idee ist, buchstäblich, für immer zu spielen. Wir sollten freundlicher sein, also frage den Spieler nach jeder Runde, ob er wieder spielen möchte und fahre nur fort, wenn die Antwort "ja" war (denke daran, du hast bereits eine Funktion, um "ja" / "nein" Fragen zu stellen, verwende sie!).

::: {.program}
Aktualisiere die Schleife im Code _code06.py_.
:::

## Den Baum über pickle für die zukünftige Verwendung speichern {#pickle}

Unser Spiel funktioniert, unser Entscheidungsbaum wächst mit jeder Runde, aber das Problem ist, dass wir jedes Mal von vorne anfangen, wenn wir das Programm starten. Das ist verschwenderisch und macht keinen Spaß, daher sollten wir unseren Baum am Ende jedes Spiels speichern und ihn immer wieder laden, wenn das Programm erneut gestartet wird. Eine Option ist die Verwendung der [pickle](https://docs.python.org/3/library/pickle.html) Bibliothek, die es dir ermöglicht, Python-Objekte zu [dump](https://docs.python.org/3/library/pickle.html#pickle.dump) und zu [laden](https://docs.python.org/3/library/pickle.html#pickle.load). Hier ist, wie es funktioniert (benutze das unbekannte `with open("dict1.p", "wb") as pickle_file:` als):

```python
import pickle

dict1 = {"a": 1}
print(dict1)
#> {'a': 1}

# Wörterbuch in eine Datei dumpen
with open("dict1.p", "wb") as pickle_file:
  pickle.dump(dict1, pickle_file)

# Ein Wörterbuch aus einer Datei laden
with open("dict1.p", "rb") as pickle_file:
  dict2 = pickle.load(pickle_file)
print(dict2)
#> {'a': 1}
```

In unserem Programm müssen wir den Baum zu Beginn aus einer Datei (ich habe sie `animal_tree.p` genannt) [laden](https://docs.python.org/3/library/pickle.html#pickle.load) und entweder am Ende (sobald der Spieler nicht mehr spielen möchte) oder nach jeder Runde [dumpen](https://docs.python.org/3/library/pickle.html#pickle.dump) (das bedeutet, dass die neueste Version des Baumes _sogar_ gespeichert wird, wenn der Spieler über einen Notausstieg aussteigt).

Beachte, dass wir einen _ursprünglichen_ Baum benötigen, der sogar vor dem ersten Ausführen des Programms erstellt wurde. Erstelle diesen Baum (einzelner Tierknoten) und [dumpe](https://docs.python.org/3/library/pickle.html#pickle.dump) ihn in einer separaten Skript oder Jupyter-Zelle in die Datei. Das ist der Baum, den du lesen, ändern und in _code07_ schreiben musst. Sobald du die ursprüngliche Datei erstellt hast, lade sie zurück und überprüfe, ob das Wörterbuch das ist, das du gedumpt hast.

Sobald das Laden am Anfang und das Dumpen am Ende eingebaut sind, teste es, indem du Ein-Runden-Spiele spielst und das Programm neu startest. Der Baum sollte erhalten bleiben und weiter wachsen.

::: {.program}
Implementiere das Programm in _code07.py_.
:::

## Den Baum über JSON für die zukünftige Verwendung speichern {#json}

Pickle ist ein Python-spezifisches Serialisierungsformat, sodass du diesen Baum nicht anderswo verwenden kannst (du kannst ihn nicht an deinen Freund weitergeben, der R oder C verwendet). Außerdem handelt es sich um ein _binäres_ Format (also nicht vom Menschen lesbar) und es ist **nicht sicher** (siehe die große rote Warnung am Anfang der [offiziellen Dokumentation](https://docs.python.org/3/library/pickle.html)), sodass du niemals einer Pickle-Datei vertrauen solltest, es sei denn, sie ist von dir selbst.

Eine alternative Methode sind [JSON](https://en.wikipedia.org/wiki/JSON)-Dateien, die häufig im interaktiven Web verwendet werden (JSON steht für JavaScript Object Notation), sie sind vom Menschen lesbar (es handelt sich um eine Textdatei, die du in jedem Editor öffnen kannst) und werden von jeder anderen Software unterstützt (jede Sprache, die dein Freund verwendet, wird eine JSON-Bibliothek haben, um mit deiner Datei zu arbeiten).

Die Verwendung von JSON ist sehr ähnlich wie die Verwendung von Pickle:

```python
import json

dict1 = {"a": 1}
print(dict1)
#> {'a': 1}

# Wörterbuch in eine Datei dumpen
with open("dict1.json", "w") as json_file:
  json.dump(dict1, json_file)

# Ein Wörterbuch aus einer Datei laden
with open("dict1.json", "r") as json_file:
  dict2 = json.load(json_file)
print(dict2)
#> {'a': 1}
```
  
Wie zuvor benötigst du ein Startwörterbuch für dein Programm. Du kannst von vorne anfangen (definiere ein alleinstehendes Tierknoten-Wörterbuch und speichere es) oder du kannst dein gepickeltes Wörterbuch laden, es aber in ein JSON dumpen (dies verwendet den Baum, den du bereits erstellt hast). Beachte, dass du im Gegensatz zu [pickle](#pickle)-Dateien den Inhalt der Datei im VS Code betrachten kannst.

::: {.program}
Implementiere das Programm in _code08.py_.
:::

## Zusammenfassung
Glückwunsch, du hast nun ein selbstlernendes KI-System programmiert! Verpacke alle Dateien in eine Zip-Datei und reiche sie ein.
