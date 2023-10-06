# Software {#Software}
Für dieses Buch und das Seminar müssen wir installieren

* PsychoPy.
* IDE Ihrer Wahl. Meine Anleitungen werden für Visual Studio Code sein, das eine sehr gute Python-Unterstützung bietet.
* Jupyter Notebook zum Ausprobieren kleiner Code-Snippets.

Ich werde keine detaillierten Anleitungen zur Installation der notwendigen Software geben, sondern Sie eher auf die offiziellen Handbücher verweisen. Dies macht diesen Text zukunftssicherer, da sich spezifische Details leicht ändern könnten^[Wenn Sie Teil des Seminars sind, fragen Sie mich, wann immer Sie Probleme haben oder unsicher sind, wie Sie vorgehen sollen].

## PsychoPy {#install-psychopy}
Wenn Sie Windows verwenden, laden Sie die [Standalone PsychoPy](https://www.psychopy.org/download.html) Version herunter und installieren Sie diese. Verwenden Sie die neueste (und beste) Ihnen vorgeschlagene PsychoPy-Version (PsychoPy 2023.2.2 mit Python 3.8 zum Zeitpunkt des Schreibens) und folgen Sie den Anweisungen.

Wenn Sie Mac oder Linux verwenden, sind die Installation von PsychoPy über pip oder Anaconda Ihre Optionen. Bitte folgen Sie den aktuellen [Anweisungen](https://www.psychopy.org/download.html#manual-installations).

## VS Code {#install-vs-code}
[Visual Studio Code](https://code.visualstudio.com/) ist ein kostenloser, leichtgewichtiger Open-Source-Editor mit starker Unterstützung für Python. Laden Sie den Installer für Ihre Plattform herunter und folgen Sie den Anweisungen.

Befolgen Sie als nächstes das Tutorial [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial). Wenn Sie Windows und die Standalone-Installation von PsychoPy verwenden, **überspringen** Sie den Abschnitt _Install a Python interpreter_, da Sie bereits eine Python-Installation haben, die mit PsychoPy gebündelt ist. Dies ist der Interpreter, den Sie im Abschnitt _Select a Python interpreter_ verwenden sollten. In meinem Fall ist der Pfad `C:\Program Files\PsychoPy3\python.exe`.

Installieren und aktivieren Sie einen Linter, eine Software, die syntaxtische und stilistische Probleme in Ihrem Python-Quellcode hervorhebt. Folgen Sie dem [Handbuch](https://code.visualstudio.com/docs/python/linting) auf der Webseite von VS Code.


## Jupyter Notebooks {#jupyter-notebooks}
[Jupyter Notebooks](https://jupyter.org/) bieten eine sehr bequeme Möglichkeit, Text, Bilder und Code in einem einzigen Dokument zu mischen. Sie erleichtern auch das Ausprobieren verschiedener kleiner Code-Snippets parallel ohne das Ausführen von Skripten. Wir werden uns für unser erstes Kapitel und gelegentliche Übungen oder Code-Tests später darauf verlassen. Es gibt zwei Möglichkeiten, wie Sie sie verwenden können: 1) in VS Code mit der Jupyter-Erweiterung, 2) in Ihrem Browser mit der klassischen Oberfläche.

### Jupyter Notebooks in VS Code
Folgen Sie [der Anleitung](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), wie Sie das Jupyter-Paket installieren und Notebooks in VS Code verwenden.

### Jupyter Notebooks in Anaconda
Die einfachste Möglichkeit, Jupyter Notebooks zusammen mit vielen anderen nützlichen Data-Science-Tools zu verwenden, ist über das [Anaconda](https://www.anaconda.com/products/individual) Toolkit. Beachten Sie jedoch, dass dies eine _zweite_ Python-Distribution in Ihrem System installiert. Dies könnte wiederum zu Verwirrung führen, wenn Sie mit Skripten in VS Code arbeiten und versehentlich den Anaconda-Interpreter statt den PsychoPy-Interpreter aktiv haben. Keine Panik, folgen Sie den [Select a Python interpreter](https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter) Anweisungen und stellen Sie sicher, dass Sie den PsychoPy-Interpreter als den aktiven haben.

Ansonsten laden Sie Anaconda herunter und installieren Sie es. Die Website hat einen ausgezeichneten [Getting started](https://docs.anaconda.com/anaconda/user-guide/getting-started/) Abschnitt.

## Ordnung halten {#files-folder}
Bevor wir anfangen, schlage ich vor, dass Sie einen Ordner namens _games-with-python_ (oder so ähnlich) erstellen. Wenn Sie sich dafür entschieden haben, Jupyter Notebooks über Anaconda zu nutzen, sollten Sie diesen Ordner in Ihrem Benutzerordner erstellen, da Anaconda dort die Dateien erwartet. Dann erstellen Sie einen neuen Unterordner für jedes Kapitel / Spiel. Für das Seminar müssten Sie einen Ordner mit allen Dateien zippen und hochladen.

