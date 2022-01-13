# Initialize my data variable
data = {'date': [],
        'time': [],
        'tempout': []}


# Read the data file
filename = "data/wxobs20170821.txt"
with open(filename,'r') as datafile:
    # Read the first three lines (header)
 for _ in range(3):
    datafile.readline()
 # Read and parse the rest of the file
 for line in datafile:
     split_line = line.split()
     data['date'].append(split_line[0])
     data['time'].append(split_line[1])
     data['tempout'].append(split_line[2])


