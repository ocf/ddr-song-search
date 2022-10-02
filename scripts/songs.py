import json
import simfile
import fileinput
import sys
from msdparser.parser import MSDParserError

def simfileToJson(s):
    return {
        'title': s.title,
        'subtitle': s.subtitle,
        'artist': s.artist,
        'titletranslit': s.titletranslit,
        'subtitletranslit': s.subtitletranslit,
        'artisttranslit': s.artisttranslit,
        'genre': s.genre,
        'credit': s.credit,
        'samplestart': s.samplestart,
        'samplelength': s.samplelength,
        'selectable': s.selectable,
        'instrumenttrack': s.instrumenttrack,
        'timesignatures': s.timesignatures,
        'banner': s.banner,
        'background': s.background,
        'lyricspath': s.lyricspath,
        'cdtitle': s.cdtitle,
        'music': s.music,
        'bgchanges': s.bgchanges,
        'fgchanges': s.fgchanges,
        'keysounds': s.keysounds,
        'attacks': s.attacks,
        'tickcounts': s.tickcounts,
        'offset': s.offset,
        'bpms': s.bpms,
        'stops': s.stops,
        'delays': s.delays,
        'charts': [chartToJson(c) for c in s.charts]
    }

def chartToJson(c):
    return {
        'stepstype': c.stepstype,
        'description': c.description,
        'difficulty': c.difficulty,
        'meter': c.meter,
        'radarvalues': c.radarvalues
    }

if __name__ == '__main__':
    info = {} 
    for line in fileinput.input():
        pack = line.split('/')[-2]
        if pack not in info: info[pack] = []
        try:
            info[pack].append(simfileToJson(simfile.open(line[:-1], False)))
        except MSDParserError as e:
            print(f'MSDParserError: {line[:-1]} ({e})', file=sys.stderr)
        except PermissionError:
            print(f'PermissionError: {line[:-1]}', file=sys.stderr)
        except UnicodeDecodeError:
            print(f'UnicodeDecodeError: {line[:-1]}', file=sys.stderr)
    print(json.dumps(info, indent=4, ensure_ascii=False))
    
