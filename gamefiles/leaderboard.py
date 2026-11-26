
def write_leaderboard(leaderboard):
    with open ("gamefiles/leaderboard.txt","w",encoding="utf-8") as datei:
        for punkte,name in leaderboard:
            datei.write(f"{punkte}:{name}\n")
    print("Leaderbord erfolgreich gespeichert")

def read_leaderboard():
    geladene_liste = []
    with open("gamefiles/leaderboard.txt","r",encoding="utf-8") as datei:
        for zeile in datei:
            if ":"in zeile:
                punkte,name = zeile.split(":")
                geladene_liste.append((int(punkte),name.strip()))
    geladene_liste.sort(reverse=True)
    return geladene_liste


