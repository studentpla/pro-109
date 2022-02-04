from re import M
import statistics
import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("sp.csv")
readingSc = df["reading score"].to_list()

m = statistics.mean(readingSc)
print ("the mean of the given data is",m)

median = statistics.median(readingSc)
print ("the median of the given data is",median)

mode = statistics.mode(readingSc)
print ("the mode of the given data is",mode)

std = statistics.stdev(readingSc)
print ("the standard deviation of the given data is ",std)

s1, e1 = m-std,m+std
list1 = [result for result in readingSc if result>s1 and result<e1]
print("the percentage of the given data within 1 standard deviation",len(list1)*100/len(readingSc),"%")

s2, e2 = m-2*std,m+2*std
list2 = [result for result in readingSc if result>s2 and result<e2]
print("the percentage of the given data within 2 standard deviation",len(list2)*100/len(readingSc),"%")

s3, e3 = m-3*std,m+3*std
list3 = [result for result in readingSc if result>s3 and result<e3]
print("the percentage of the given data within 3 standard deviation",len(list3)*100/len(readingSc),"%")