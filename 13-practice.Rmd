# Übung {#practice}

Übung macht den Meister, also lasst uns üben. Hier sind einige Aufgaben, die den Prüfungsaufgaben ähneln. Einige Aufgaben können (und sollten) auf verschiedene Weisen gelöst werden. Erstelle eine separate Datei für jede Aufgabe.

## Problem 01

Generiere eine Liste von 5 zufälligen Ganzzahlen zwischen 0 und 10.

* 01A: Verwende eine for-Schleife, um das kleinste Element in der Liste zu finden. Drucke es aus mit einer netten Nachricht und String-Formatierung.
* 01B: Verwende NumPy, um das größte Element in der Liste zu finden. Drucke es aus mit einer netten Nachricht und String-Formatierung.

## Problem 02

Erstelle ein Wörterbuch mit 5 Einträgen (deiner Wahl von Feldnamen und Werten). Drucke die "Schlüssel: Wert"-Paare mit einer for-Schleife aus.

## Problem 03

Schreibe eine Funktion, die eine zufällige Zahl zwischen 1 und 10 generiert, bis sie den im Parameter `desired_value` spezifizierten Wert erreicht. Sie sollte die _Anzahl der Versuche_ zurückgeben, die benötigt wurden, um diese Zahl zu erhalten. Zum Beispiel, wenn der erste Wert bereits gleich `desired_value` war, sollte sie $1$ zurückgeben. Wenn es beim zweiten Versuch passiert ist, sollte sie $2$ zurückgeben, usw. Dokumentiere die Funktion. Lege die Funktion in _problem03_utils.py_ ab, verwende sie im Skript, wähle eine beliebige, aber gültige Zahl für `desired_value`.

## Problem 04

Rufe die Funktion aus **Problem 03** 100 Mal auf, um eine Liste mit 100 Wartezeiten zu generieren.

* 04A: Berechne die durchschnittliche Wartezeit mit einer for-Schleife.
* 04B: Berechne die mittlere Wartezeit mit NumPy.

## Problem 05

Generiere eine Liste von 100 normalverteilten Werten. Berechne eine neue Liste mit deren Exponenten mittels

* 05A: For-Schleife
* 05B: List comprehension
* 05C: NumPy

## Problem 06

Generiere zwei Listen von zufälligen Ganzzahlen zwischen -5 und 5 (jeweils 10 Werte). Erstelle eine neue Liste, die das größte Element aus jeder Liste enthält. Zum Beispiel, wenn die Listen `(-1, 2, 3...)` und `(-4, 3, 3, ...)` sind, dann sollte die neue Liste `(-1, 3, 3, ...)` sein. Erstelle die neue Liste mittels

* 06A: For-Schleife
* 06B: List comprehension

## Problem 07

Erstelle eine Funktion, die die Reihe $1 + \frac{1}{2} + \frac{1}{3}+ \frac{1}{4}+...$ bis zu einem beliebigen Wert $n$ berechnet. Die Funktion sollte rekursiv sein, indem sie nur einen Wert berechnet und die Berechnung des nächsten Elements an sich selbst weitergibt. Erstelle eine weitere Funktion, die dieselbe Berechnung durchführt, jedoch mit einer for-Schleife. Die Funktionen gehören in _problem07_utils.py_, zeige, dass beide Funktionen im Skript den gleichen Wert zurückgeben.

## Problem 08

Bitte den Benutzer um eine Eingabe, bis sie eine gültige Zahl eingeben, die größer als 35 ist.

