# Klasse zur Realisierung einer Stoppuhr
class StopWatch:
    import time
    global time

    # Konstruktor zur Initialisierung der Member-Variablen
    def __init__(self):
        # Zeitpunkte zum Messen (Start + Stop)
        self.__startTime = 0.0
        self.__stopTime = 0.0

        # Wird gerade Zeit gestoppt
        self.__running = False

    # Methode zum Starten eines Vorgangs
    # Es werden keine Werte an die Funktion übergeben
    # oder von der Funktion zurückgegeben. Nur interne
    # Member werden gesetzt.
    def start(self):
        if not self.__running:
            self.__startTime = time.time()
            self.__running = True

    # Methode zum Stoppen eines Vorgangs
    # Es werden keine Werte an die Funktion übergeben
    # oder von der Funktion zurückgegeben. Nur interne
    # Member werden gesetzt.
    def stop(self):
        if self.__running:
            self.__stopTime = time.time()
            self.__running = False

    # Methode zum Berechnen der vergangenen Zeit. Da
    # die Berechnung auf Basis der internen Variablen
    # stattfindet, werden keine Werte an die Methode
    # übergeben. Als Ergebnis wird die vergangene Zeit
    # als String zurückgegeben.
    def elapsedTime(self):
        if self.__running:
            # Zeit läuft noch
            # nehme aktuelle Zeit
            stoppedTime = time.time() - self.__startTime
        else:
            # Zeit läuft nicht (mehr)
            # nehme gestoppte Zeit
            stoppedTime = self.__stopTime - self.__startTime

        # Bestimme Sekunden und Hundertstel
        seconds = int(stoppedTime)
        hundreds = int(stoppedTime * 1000) % 1000

        # Gebe Zeit formatiert aus
        return str(seconds) + "." + str(hundreds)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

sw = StopWatch()

def setup():
    size(400, 50)

def draw():
    global sw
    background(255)
    textSize(32)
    text(str(sw.elapsedTime()), 10, 30)
    fill(0, 102, 153)

def keyTyped():
    if key == '1':
        sw.start()
    elif key == '2':
        sw.stop()
