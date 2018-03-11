# Funktion zur Berechnung der Wettpunkte. Die dazu notwendigen Werte
# werden als Integer-Werte an die Funktion übergeben. Das Ergebnis
# wird als Ganzzahlwert zurückgegeben.
def computeBetScore(home, guest, betHome, betGuest):
    # bei genauer Voraussage
    if home == betHome and guest == betGuest:
        # verlasse die Funktion und gib den Wert 3 als Ergebnis zurück
        return 3

    # Tendenz nach unten richtig
    if home > betHome and guest > betGuest:
        # verlasse die Funktion und gib den Wert 1 als Ergebnis zurück
        return 1

    # Tendenz nach oben richtig
    if home < betHome and guest < betGuest:
        # verlasse die Funktion und gib den Wert 1 als Ergebnis zurück
        return 1

    # Tendenz bei Unentschieden
    if home == betHome and guest == betGuest:
        # verlasse die funktion und gib Wert 1 als Ergebnis zurück
        return 1

    # ansonsten
    return 0


# Funktion zur Berechnung des Wettergebnisses für alle Wetten
# Als Eingabeparameter wird ein zweidimensionales Integer-Array
# angegeben. Das Ergebnis ist ebenfalls vom Typ Integer
def computeCompleteBetScore(data):
    # Initialisierung der Variablen
    result = 0

    # Durchlaufe das Array
    for d in data:
        # Berechne das Ergebnis als das bisherige Ergebnis + den
        # Wettpunkte für die aktuelle Wette, die mit Index [j]
        # angegeben  wird.
        result += computeBetScore(d[0], d[1], d[2], d[3])
    # Gib die Summe aller erzielten Wettpunkte zurück.
    return result


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

# Das zweidimensionale Array besteht aus drei Zeilen = Wetten
# und jeweils den Werten home, guest, betHome, betGuest
data = [[3, 2, 3, 2],
        [1, 1, 1, 0],
        [2, 2, 1, 1]]

print computeCompleteBetScore(data)

