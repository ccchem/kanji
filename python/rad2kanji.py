rads = {}

with open('/data/dic/joyo_kanji_rad.csv') as file:
    # Skip header
    file.readline()

    for line in file:
        line = line.strip()
        tokens = line.split(',')
        kanji = tokens[2]
        
        for rad in tokens[3].split(' '):
            entry = rads.get(rad)
            if not entry:
                entry = []
                rads[rad] = entry
            entry.append(kanji)

for rad, kanjies in rads.items():
    data = "{}|{}|{}".format(rad, len(kanjies), " ".join(kanjies))
    print(data)
