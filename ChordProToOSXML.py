import os

while True:
    dir = input("Jaky zpevnik chcete prevest? ")

    dir = "zpevniky/" + dir
    if not os.path.exists(dir):
        print("Zadali jste neplatnou cestu.")
    else:
        break

songs = []
for entry in os.listdir(dir):
    if os.path.isfile(dir + "/" + entry):
        songs.append(entry)

if not os.path.exists(dir + "/osxml"):
    os.mkdir(dir + "/osxml")

i = 1; #to show the remaing items count (to count)
for entry in songs:
    if os.path.isfile(dir + "/" + entry):
        file = open(dir + "/" + entry, "rt", encoding="utf-8").readlines()
    
    if not os.path.exists(dir + "/osxml/" + entry):
        out = open(dir + "/osxml/" + entry , "x", encoding="utf-8")
    else:
        out = open(dir + "/osxml/" + entry, "wt", encoding="utf-8") 
    
    out.write("<!DOCTYPE song>\n")
    out.write("<song>\n")
    for i in range(len(file)-1):
        line = file[i]
        v = 0
        if line.startswith("{title:"):
            title = line.replace("{title:", "").replace("}", "").strip()
            out.write(f"<title>{title}</title>\n")
        elif line.startswith("{artist:"):
            artist = line.replace("{artist:", "").replace("}", "").strip()
            out.write(f"<author>{artist}</author>\n")
        elif line.startswith("{start_of_verse:") and v == 0:
            v += 1
            out.write("lyrics>\n")
            out.write("[V1]\n")
        elif line.startswith("{start_of_verse:") and v != 0:
            v += 1
            out.write("[V" + str(v) + "]\n")
        elif line.startswith("{start_of_chorus:"):
            out.write("[C]\n")
        elif line.startswith("{start_of_bridge:"):
            out.write("[B]\n")
        elif line.startswith("{"):
            continue
        elif line.strip() == "":
            out.write("\n")
        else:
            out.write(". \n") #start chord line
            out.write("_") #start lyric line
            if "[" in line and "]" in line:
                parts = line.split("]")
                for part in parts:
                    if part.strip() == "":
                        continue
                    if "[" in part:
                        chord = part.split("[")[1].strip()
                        for i in range(len(part.split("["))-1):
                            out[i-1].write(" ")
                        out[i-1].write(chord)
                        lyric = part.split("]")[1].strip()
                        out[i].write(lyric)
                    else:
                        lyric = part.strip()
                        out[i].write(lyric)
                out.write("\n")