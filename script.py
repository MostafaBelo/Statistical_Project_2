file = open("students_data.csv", "r")
data = file.read()
file.close()

cols = {}

data = data.split("\n")
titles = data[0].split(",")
for i in range(len(titles)):
    cols[titles[i]] = i

data = data[1:]
for i in range(len(data)):
    data[i] = data[i].split(",")

def Get(i, c):
    return data[i][cols[c]]