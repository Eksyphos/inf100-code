from pathlib import Path
import os
import csv

def combine_csv_in_dir(dirpath, result_path):

    filelist = Path(dirpath).glob('*.csv')
    csv_list = []
    csv_file = ''
    for file in filelist:
        content = Path(file).read_text(encoding='utf-8')
        lines = content.splitlines()
        if len(csv_list)>0:
            lines=lines[1:]
        for line in lines:
            csv_list.append(line)
    print(csv_list)
    for line in csv_list:
        csv_file+=f'{line}\n'
    Path(result_path).write_text(csv_file,encoding='utf-8')
    

if __name__=="__main__":
    print("Tester combine_csv_in_dir... ", end="")
    # Mappen samples må ligge i samme mappe som denne filen
    dirpath = os.path.join(os.path.dirname(__file__), "samples")
    combine_csv_in_dir(dirpath, "combined_table.csv")
    with open("combined_table.csv", "rt", encoding='utf-8') as f:
        content = f.read()
    assert("""\
    uibid,karakter,kommentar
    abc104,C,hei
    abc105,D,"med komma, her er jeg"
    abc106,E,tittit
    abc101,A,Her er min kommentar
    abc102,B,"Jeg er glad, men her er komma"
    abc103,C,Katching
    """ == content or """\
    uibid,karakter,kommentar
    abc101,A,Her er min kommentar
    abc102,B,"Jeg er glad, men her er komma"
    abc103,C,Katching
    abc104,C,hei
    abc105,D,"med komma, her er jeg"
    abc106,E,tittit
    """ == content)
    print("OK")