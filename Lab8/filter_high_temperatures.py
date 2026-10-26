from pathlib import Path
def filter_high_temperatures(path_input,path_output,threshold_temp):
    content = Path(path_input).read_text(encoding='utf-8')
    lines = content.splitlines()
    high_temps = ''
    for i in range(len(lines)):
        line=lines[i].split(' ')
        if float(line[1])>=threshold_temp:
             high_temps += f'{line[0]} {line[1]}\n'  
    Path(path_output).write_text(high_temps,encoding='utf-8')          
