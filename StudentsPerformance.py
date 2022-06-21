import statistics
import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

#reading scores data
df = pd.read_csv('StudentsPerformance.csv')
data = df["reading score"].tolist()
# print(data)

# Calculating mean
mean = statistics.mean(data)
print("Mean = ",mean)
stdDeviation = statistics.stdev(data)
print("Std Deviation= ", stdDeviation)
median = statistics.median(data)
print("Median = ",median)
mode = statistics.mode(data)
print("Mode = ", mode)

#Finding 1st std deviation n end values, & 2nd std deviation n end values
first_std_deviation_start ,first_std_deviation_end = mean-stdDeviation,mean+stdDeviation
second_std_deviation_start,second_std_deviation_end = mean -(2*stdDeviation),mean+(2*stdDeviation)
third_std_deviation_start,third_std_deviation_end = mean -(3*stdDeviation),mean+(3*stdDeviation)

# print("first std = ",first_std_deviation_end)

# Plotting the chart, and lines for mean, 1 std deviation, 2nd std deviation
fig = ff.create_distplot([data],["reading scores"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean ,mean],y =[0,0.17],mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start ,first_std_deviation_start],y =[0,0.17],mode = "lines", name = "STD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end ,first_std_deviation_end],y =[0,0.17],mode = "lines", name = "STD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start ,second_std_deviation_start],y =[0,0.17],mode = "lines", name = "STD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end ,second_std_deviation_end],y =[0,0.17],mode = "lines", name = "STD DEVIATION 2"))

fig.show()
listOfData_within_1_std_deviation = [result for result in data if result >first_std_deviation_start and result<first_std_deviation_end]
listOfData_within_2_std_deviation = [result for result in data if result >second_std_deviation_start and result<second_std_deviation_end]
listOfData_within_3_std_deviation = [result for result in data if result >third_std_deviation_start and result<third_std_deviation_end]

print("list within 1 std deviation = ",len(listOfData_within_1_std_deviation)*100/len(data) ,"%")
print("{}% of data lies within 2nd std devition  ".format(len(listOfData_within_2_std_deviation)*100/len(data)))
print(" {}% of data lies within 3rd std deviation ".format(len(listOfData_within_3_std_deviation)*100/len(data)))

    