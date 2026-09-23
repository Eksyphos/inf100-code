from pathlib import Path
import json

content = Path("cryptids_fixed.json").read_text(encoding="utf-8")
data = json.loads(content)

print(data["kryptider"][-1]["navn"],"\n")

liste = data["kryptider"]
for kryptid in range(len(liste)):
    print(f"{kryptid+1}. {liste[kryptid]["navn"]}: {liste[kryptid]["kjennetegn"]}\n")
    
for kryptid in range(len(liste)):
    if liste[kryptid]["navn"] == "Selma":
        info = liste[kryptid]
        infovalues = info.keys()
        for key in infovalues:
            print(f"{key} : {info[key]}")
