import jcconv3


def get_el_value(line, start):
    end = line.index('<', start)
    return line[start:end]


class Printer:
    def print(self, kanji):
        reading = kanji.ja_kun
        if len(reading) == 0:
            reading = []
            for ja_on in kanji.ja_on:
                reading.append(ja_on + '・' + jcconv3.kata2hira(ja_on))
        
        print(kanji.kanji, kanji.grade, reading)


class Kanji:
    def __init__(self, kanji):
        self.kanji = kanji
        self.grade = None
        self.ja_on = []
        self.ja_kun = []
    
    def add_ja_kun(self, value):
        tmp = value.replace('.', '')
        if tmp.startswith('-') or tmp.endswith('-'):
            return
        self.ja_kun.append(tmp)

    def add_ja_on(self, value):
        tmp = value.replace('.', '')
        self.ja_on.append(tmp)


printer = Printer()
data = None

with open('/data/dic/kanjidic2.xml') as file:
    for line in file:
        if line.startswith('<literal>'):
            data = Kanji(line[9:10])
        elif line.startswith('<grade>'):
            data.grade = get_el_value(line, 7)
        elif line.startswith('<reading r_type="ja_on">'):
            data.add_ja_on(get_el_value(line, 24))
        elif line.startswith('<reading r_type="ja_kun">'):
            data.add_ja_kun(get_el_value(line, 25))
        elif line.startswith('</character>'):
            if data.grade == '4':
                printer.print(data)
                #break

