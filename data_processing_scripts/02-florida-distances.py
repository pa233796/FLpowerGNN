# Extract pairwise county distances for Florida counties from the
# County Distance Database (Https://Doi.Org/10.60592/Afwp-Pj35)

import csv

def main():
    result = {}
    with open('sf12010countydistancemiles.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        next(reader) # Skip header row
        for countyCodeA, value, countyCodeB in reader:
            if not (countyCodeA.startswith("12") and countyCodeB.startswith("12")):
                continue # Skip non-Florida counties
            # Keep unique pairwise entries
            a = int(countyCodeA)
            b = int(countyCodeB)
            key = (min(a,b), max(a,b))
            result.setdefault(key, value)

    #with open('distances_florida.csv', 'w') as csvfile:
    #    writer = csv.writer(csvfile)
    #    for key, value in sorted(result.items()):
    #        writer.writerow([ *key, value ])
    
    with open('florida_distances.edgelist', 'w') as outfile:
        for key, value in sorted(result.items()):
            print(*key, result[key], file=outfile)


if __name__ == '__main__':
    main()
