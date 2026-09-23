from pathlib import Path
import json

content = Path("cryptids_fixed.json").read_text(encoding="utf-8")
data = json.loads(content)


my_cryptid = {
    "navn": "Bybjørnen",
    "sted": "Bergen sentrum",
    "observasjoner": 3,
    "farlig": False,
    "kjennetegn": ["regnjakke", "spiser boller"]
}

print(json.dumps(my_cryptid))
print(json.dumps(my_cryptid, ensure_ascii=False, indent=2))

tester = {"liste": [1, 2, 3], "tuppel": (1, 2, 3), "desimal": 7.0,
          "sant": True, "ingenting": None}
test = json.dumps(tester)
print(tester)
print(test)
print(json.loads(test))

content = json.dumps(my_cryptid, indent=2, ensure_ascii=False)
Path("my_cryptid.json").write_text(content, encoding="utf-8")