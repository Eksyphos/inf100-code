import matplotlib.pyplot as plt
from pathlib import Path
def import_csv(path):
    content = Path(path).read_text()
    data = content.splitlines()
    return data

def filter_data(data):
    filtered_coords = {}
    for line in data[2:]:
        line = line.split(';')
        if line[15] in filtered_coords:
            continue
        else:
            coords = (line[-1],line[-2],line[19])
            filtered_coords.update({line[15]:coords})
    return filtered_coords

def plot_coords(data):
    x_coords_s = []
    y_coords_s = []
    x_coords_i = []
    y_coords_i = []
    for key in data:
        x,y,inland = data[key]
        if inland !='LAND':
            x_coords_s.append(float(x))
            y_coords_s.append(float(y))
        else:
            x_coords_i.append(float(x))
            y_coords_i.append(float(y))

    plt.scatter(x_coords_s,y_coords_s,color='blue',alpha=0.5,label='sjø')
    plt.scatter(x_coords_i,y_coords_i,color='red',alpha=0.5,label='land')
    plt.legend()

def get_coords(path):
    data = import_csv(path)
    filtered_data = filter_data(data)
    plot_coords(filtered_data)

if __name__ == '__main__':
    get_coords('Akvakulturregisteret.csv')
    plt.title('Oppdrettsannlegg i Norge')
    plt.show()

