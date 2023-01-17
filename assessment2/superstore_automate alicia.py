from pathlib import Path
import matplotlib.pyplot as plt # ensure you have intalled matplotlib before importing it. available in the project brief.
import csv

#--------------- PART 1: This part of the program is completed for you --------------#

# create a file to csv file.
fp = Path.cwd()/"superstore_transaction.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create 3 empty lists to store profit and quantity by each cluster
    cluster1 = [] 
    cluster2 = []
    cluster3 = []

    # append profit and quantity as a list back to each empty list
    for row in reader:
                
        if row[4] == "Cluster 1":
            cluster1.append([row[13], row[14]])
        elif row[4] == "Cluster 2":
            cluster2.append([row[13], row[14]])
        else:
            cluster3.append([row[13], row[14]])

#---------------------------- PART 2: Insert your own code ---------------------------#
# 1. Calculate the total profit and total quantity using cluster 1,2,3 variables from part 1
# 2. Write the calculated profit to a txt file. Name it as cluster_report.txt.


def calculate_profit(cluster):
    profit = 0   #set profit = 0 variable to use in the for loop
    for item in cluster:
        if item[0][0] == '-': #check the profits in each element in the list, whether or not it is negative with a negative sign 
            profit -= float(item[0].replace(',', '')[2:]) 
        else:
            profit += float(item[0].replace(',','')[1:])
    return(profit)

def calculate_quantity(cluster):
    quantity = 0
    for item in cluster:
        quantity += float(item[1]) 
    return(quantity)

print('PROFIT REPORT')
print('=============')
print(f'Cluster 1: ${calculate_profit(cluster1)}')
print(f'Cluster 2: ${calculate_profit(cluster2)}')
print(f'Cluster 3: ${calculate_profit(cluster3)}')

print('QUANTITY REPORT')
print('=============')
print(f'Cluster 1: {calculate_quantity(cluster1)}')
print(f'Cluster 2: {calculate_quantity(cluster2)}')
print(f'Cluster 3: {calculate_quantity(cluster3)}')

file_path = Path.cwd() / 'cluster_report2.txt'

file_path.touch()

with file_path.open(mode ='w') as file:
    file.write(f'PROFIT REPORT\n=============\nCluster 1: ${calculate_profit(cluster1)}\nCluster 2: ${calculate_profit(cluster2)}\nCluster 3: ${calculate_profit(cluster3)}\n\nQUANTITY REPORT\n=============\nCluster 1: {calculate_quantity(cluster1)}\nCluster 2: {calculate_quantity(cluster2)}\nCluster 3: {calculate_quantity(cluster3)}21')



#--------------- PART 3: This part of the program is completed for you  --------------#

# This part of the program plots the profits and quantities by clusters.
# The values profits and quantities are hard-coded, so it is not link to part 2. 
# Even if part 2 does not work, part 3 can still be executed.
# Simply execute the code and the plot will be saved as an image file.
# Click on the png file in the explorer panel to see the barplot.

# Do not worry about how the code below works.
# It is an example of visualising data using Python. 
# You will learn about data visulisation in analytics module in year 2. 

cluster_profit = [133426, 43684, 109224] # hardcoded profit by clusters 
cluster_quantity = [18632, 8716, 10524] # hardcoded quantity sold by clusters. 
fig, axs = plt.subplots(2, figsize = (10,7))
fig.suptitle("SuperStore Business Performance")
cluster = ["cluster 1", "cluster 2", "cluster 3"]
axs[0].bar(cluster, cluster_profit)
axs[1].bar(cluster, cluster_quantity)
axs[0].set_xlabel("Profit by Clusters")
axs[1].set_xlabel("Quantity Sold by Clusters")
axs[0].set_ylabel("Profit ($)")
axs[1].set_ylabel("Quantity (000s)")
fig.savefig("cluster_barplot.png") 
plt.imread("cluster_barplot.png")
plt.show()