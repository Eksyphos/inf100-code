from pathlib import Path
import json

def main():
    filnavn = input()
    threshold = int(input())
    data = load_emission_data(filnavn)
    deviations = get_deviations(data)
    count = count_values_larger_than(deviations,threshold)
    print(f"Antall avvik større enn {threshold}: {count}")

def load_emission_data(filename):
    input_file = str(filename)
    file_content = Path(input_file).read_text(encoding='utf-8')
    data = json.loads(file_content)
    return data

def get_deviations(data):
    deviations = []
    days = len(data["data"])
    for day in range(days):
        segment = data["data"][day]["intensity"]
        fcast = segment["forecast"]
        actual = segment["actual"]
        if type(fcast) and type(actual) == int:
            deviations.append(abs(fcast-actual))
        #else:   deviations.append("typeError")
    return deviations

def count_values_larger_than(values, threshold):
    count = 0
    for number in values:
        if number > threshold:
            count +=1
    return count


if __name__ == "__main__":
    main()
