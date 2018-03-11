# Statische Klasse, die nur aus statischen Methoden besteht
class Lyrics:

    # Statische Methode, die die URL zu einem Songtext aufbaut.
    # Als Eingabewerte werden Musiker und Titel an die Methode
    # übergeben. Als Ergebnis wird der generierte URL zurückgegeben
    @staticmethod
    def getLyricsURL(artist, title):
        # Konvertiere artist und title in Kleinschreibung
        artist = artist.lower()
        title = title.lower()

        # Ersetze Leerzeichen mit Unterstrich
        artist = artist.replace(' ', '_')
        title = title.replace(' ', '_')

        # Baue URL
        url = "http://lyrics.wikia.com/api.php?func=getSong&artist="
        url += artist + "&song=" + title

        # Gebe URL zurück
        return url


# Startpunkt des Hauptprogramms
# Zu Demonstrations- und Testzwecken wird die oben programmierte
# statische Klassenmethode verwendet.

# Lese Interpret und Titel ein
interpret = "Die Fantastischen Vier"
titel = "MFG"

print Lyrics.getLyricsURL(interpret, titel)



