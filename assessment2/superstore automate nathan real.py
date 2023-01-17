from pathlib import Path
# ensure you have intalled matplotlib before importing it. available in the project brief.
import matplotlib.pyplot as plt
import csv

# --------------- PART 1: This part of the program is completed for you --------------#

# create a file to csv file.
fp = Path.cwd() / "superstore_transaction.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

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

# ---------------------------- PART 2: Insert your own code ---------------------------#
# 1. Calculate the total profit and total quantity using cluster 1,2,3 variables from part 1

# Total Profit from Customer Cluster 1
# initialise the variable to store the total profit from cluster 1
Total_Profit_Cluster1 = 0
# initialise the variable to store the total quantity from cluster 1
Total_Quantity_Cluster1 = 0
for i in cluster1:  # loop through the cluster 1 list
    Total_Profit_Cluster1 = Total_Profit_Cluster1 + int(  # convert the profit to integer and add to the total profit
        # remove the $ and , from the profit
        i[0].replace("$", "").replace(",", ""), base=10
    )  # convert the quantity to integer and add to the total quantity
    Total_Quantity_Cluster1 = Total_Quantity_Cluster1 + int(i[1])

# Total Profit from Customer Cluster 2
# initialise the variable to store the total profit from cluster 2
Total_Profit_Cluster2 = 0
# initialise the variable to store the total quantity from cluster 2
Total_Quantity_Cluster2 = 0
for i in cluster2:  # loop through the cluster 2 list
    Total_Profit_Cluster2 = Total_Profit_Cluster2 + int(  # convert the profit to integer and add to the total profit
        # remove the $ and , from the profit
        i[0].replace("$", "").replace(",", ""), base=10
    )   # convert the quantity to integer and add to the total quantity
    Total_Quantity_Cluster2 = Total_Quantity_Cluster2 + int(i[1])

# Total Profit from Customer Cluster 3
# initialise the variable to store the total profit from cluster 3
Total_Profit_Cluster3 = 0
# initialise the variable to store the total quantity from cluster 3
Total_Quantity_Cluster3 = 0
for i in cluster3:  # loop through the cluster 3 list
    # convert the profit to integer and add to the total profit
    Total_Profit_Cluster3 += int(i[0].replace("$",
                                 "").replace(",", ""), base=10)
    # convert the quantity to integer and add to the total quantity
    Total_Quantity_Cluster3 += int(i[1])

# 2. Write the calculated profit to a txt file. Name it as cluster_report.txt.

file = open("cluster_report.txt1", "w")  # open the file in write mode
text = "PROFIT REPORT\n"  # initialise the text variable to store the report
text += "==============\n"  # add the report header
# add the total profit from cluster 1
text += "Cluster 1: $" + str(Total_Profit_Cluster1) + ".0\n"
# add the total profit from cluster 2
text += "Cluster 2: $" + str(Total_Profit_Cluster2) + ".0\n"
# add the total profit from cluster 3
text += "Cluster 3: $" + str(Total_Profit_Cluster3) + ".0\n"
text += "\nQUANTITY REPORT\n"  # add the quantity report header
text += "================\n"
# add the total quantity from cluster 1
text += "Cluster 1: " + str(Total_Quantity_Cluster1) + ".0\n"
# add the total quantity from cluster 2
text += "Cluster 2: " + str(Total_Quantity_Cluster2) + ".0\n"
# add the total quantity from cluster 3
text += "Cluster 3: " + str(Total_Quantity_Cluster3) + ".0\n"
file.write(text)  # write the text to the file
file.close  # close the file


# --------------- PART 3: This part of the program is completed for you  --------------#

# This part of the program plots the profits and quantities by clusters.
# The values profits and quantities are hard-coded, so it is not link to part 2.
# Even if part 2 does not work, part 3 can still be executed.
# Simply execute the code and the plot will be saved as an image file.
# Click on the png file in the explorer panel to see the barplot.

# Do not worry about how the code below works.
# It is an example of visualising data using Python.
# You will learn about data visulisation in analytics module in year 2.

cluster_profit = [133426, 43684, 109224]  # hardcoded profit by clusters
cluster_quantity = [18632, 8716, 10524]  # hardcoded quantity sold by clusters.
fig, axs = plt.subplots(2, figsize=(10, 7))
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
