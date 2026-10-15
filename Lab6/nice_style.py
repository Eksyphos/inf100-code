from pathlib import Path

def good_style(source_code):
    lines = source_code.splitlines()
    for line in lines:
        if len(line)>=80:
            return False
    return True

def good_style_from_file(filename):
    content = Path(filename).read_text(encoding='utf-8')
    check = good_style(content)
    return check
