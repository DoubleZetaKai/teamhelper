import networkx
import csv


def getGefx():
    network = networkx.Graph()

    with open('airport1.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[5] != '' and row[6] != '' and row[7] != '' and row[3] != '':
                network.add_node(row[5],
                                 country=row[3], port_name=row[2], Latitude=float(row[6]), Longitude=float(row[7]))

    with open('202102.csv', 'r') as f:
        reader = csv.reader(f)
        edge = []
        for row in reader:
            if row[0] != '' and row[1] != '':
                network.add_edge(row[0], row[1])

    networkx.write_gexf(network, '2021021.gexf')


if __name__ == '__main__':
    getGefx()
