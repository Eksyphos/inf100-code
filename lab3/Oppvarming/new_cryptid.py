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

data["kryptider"].append(my_cryptid)
data["versjon"] = 4
data["sist_oppdatert"] = "16.09.2026"

content = json.dumps(data, ensure_ascii=False, indent=2)
Path("new_cryptids.json").write_text(content, encoding="utf-8")