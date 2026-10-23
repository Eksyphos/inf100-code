from pathlib import Path
import json
def convert_students_to_csv(sourcepath,destpath):
    content = Path(sourcepath).read_text(encoding='utf-8')
    data = json.loads(content)
    csv = transform_to_csv(data)
    write_the_csv(csv,destpath)

def transform_to_csv(data):
    body = ''
    for student in data['students']:
        values = [str(x) for x in student.values()]
        body += ';'.join(values)+'\n'
    keys = [str(x) for x in student.keys()]
    csv = ';'.join(keys)+'\n' + body
    return csv

def write_the_csv(data,destpath):
    Path(destpath).write_text(data,encoding='utf-8')

if __name__ == "__main__":
    convert_students_to_csv("students.json", "students.csv")
    convert_students_to_csv("students2.json", "students2.csv")