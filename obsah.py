import os

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
print("Obsah byl vygenerován.")
file.close()
out.close()
exit(0)