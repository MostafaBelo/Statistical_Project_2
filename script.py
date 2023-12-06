file = open("students_data.csv", "r")
data = file.read()
file.close()

cols = {}

data = data.split("\n")
titles = data[0].split(",")
for i in range(len(titles)):
    cols[titles[i]] = i

data = data[1:]
n = len(data)
for i in range(n):
    data[i] = data[i].split(",")

def Get(i, c):
    global data
    return data[i][cols[c]]

grades = {}

for i in range(n):
    if (Get(i, "School") in grades):
        grades[Get(i, "School")][0] += float(Get(i, "Grade"))
        grades[Get(i, "School")][1] += 1
    else:
        grades[Get(i, "School")] = [float(Get(i, "Grade")),1]

# max_school = 0
grades_sort = []
for i in grades:
    grades[i][0] = grades[i][0]/grades[i][1]
    grades_sort.append((grades[i][0], grades[i][1], i))
    # if (max_school == 0):
    #     max_school = i

    # if (grades[i] > grades[max_school]):
    #     max_school = i

grades_sort.sort()

print(grades_sort)

# print(max_school)
# 56877, highest mean schools