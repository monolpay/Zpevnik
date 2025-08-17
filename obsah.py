import os
#Removes folder and all its contents
def removeFolder(dir):
    for file in os.listdir(dir):
        if os.path.isfile(dir + "/" + file):
            os.remove(dir + "/" + file)
        else:
            removeFolder(dir + "/" + file)
    os.rmdir(dir)
    print(f"Složka {dir} byla smazána.")

while True:
    dir = input("Generovat obsah pro: ")

    dir = "zpevniky/" + dir
    if not os.path.exists(dir):
        print("Zadali jste neplatnou cestu.")
    else:
        break

songs = []
for entry in os.listdir(dir):
    if os.path.isfile(dir + "/" + entry):
        songs.append(entry)
i = 1
for entry in songs:
    title = ""
    if os.path.isfile(dir + "/" + entry):
        file = open(dir + "/" + entry, "rt", encoding="utf-8")
    line = file.readline()
    while title == "":
        if line.startswith("{title:"):
            title = line
        else:
            file.readline()
    if not os.path.exists(dir + "/obsah"):
        os.mkdir(dir + "/obsah")
    if not os.path.exists(dir + "/obsah/obsah_" + entry):
        out = open(dir + "/obsah/obsah_" + entry , "x", encoding="utf-8")
    else:
        out = open(dir + "/obsah/obsah_" + entry, "wt", encoding="utf-8")
    out.write(title)
    print(i,"/", len(songs))
    i += 1

folders = []
print("Kontrola obsahu...")
for entry in os.listdir(dir+ "/obsah"):
    if not entry.startswith("obsah_"):
        if os.path.isfile(dir + "/obsah/" + entry):
            os.remove(dir + "/obsah/" + entry)
            continue
        elif os.path.isdir(dir + "/obsah/" + entry):
            folders.append(entry)
            continue
    songName = entry.replace("obsah_", "")
    if songName not in songs:
        os.remove(dir + "/obsah/" + entry)
        continue
if len(folders) != 0:
    print("Byly nalezeny složky: ", folders)
    print("Přejete si je smazat? (y/n)")
    answer = input()
    if answer.lower() == "y":
        for folder in folders:
            if len(os.listdir(dir + "/obsah/" + folder)) == 0:
                os.rmdir(dir + "/obsah/" + folder)
            else:
                print("Složka", folder, "není prázdná, stejně smazat? (y/n)")
                answer = input()
                if answer.lower() == "y":
                    removeFolder(dir + "/obsah/" + folder)
    else:
        print("Složky nebyly smazány.")
print("Obsah byl vygenerován.")
file.close()
out.close()
exit(0)