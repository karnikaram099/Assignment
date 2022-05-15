class Dataset:
    out = []
class Userinput:
    def data_in(self):
        for i in range(1, 11):
            distance = float(input("Enter distance:"))
            time = float(input("Enter time taken:"))
            Dataset.out.append([distance, time])
class Measure:
    def measure(self):
        var = Dataset.out
        for i in var:
            res = i[0]/i[1]
            i.append(res)
class ShowResults:
    def display(self):
        for i in Dataset.out:
            print(i)

object1 = Userinput()
object1.data_in()
object2 = Measure()
object2.measure()
object3 = ShowResults()
object3.display()

import csv
header = ['distance', 'time', 'speed']
result = Dataset.out
with open("GRL_file.csv", "w") as file:
    write = csv.writer(file)
    data = write.writerow(header)
    data1 = write.writerows(result)
