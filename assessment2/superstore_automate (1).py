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
# create 3 variables to store the value for total quantity of clusters 1,2 and 3 individually
totquan1 = 0
totquan2 = 0
totquan3 = 0
# create 3 variables to store the value for total profit of clusters 1,2 and 3 individually
totprofit1 = 0
totprofit2 = 0
totprofit3 = 0
#create an empty list final answer to store all the calculated values
final_answer = []
#use for loop to iterate through cluster 1 to get quantity of each sublist
for i in cluster1:
    #add all the quantitities in cluster 1 together to totquan1
    totquan1 += float(i[1])
#use for loop to iterate through cluster 2 to get quantity of each sublist
for j in cluster2:
    #add all the quantitities in cluster 2 together to totquan2
    totquan2 += float(j[1])
#use for loop to iterate through cluster 3 to get quantity of each sublist
for k in cluster3:
    #add all the quantitities in cluster 3 together to totquan3
    totquan3 += float(k[1])
#append all 3 values to final answer as separate list items
final_answer.append(totquan1)
final_answer.append(totquan2)
final_answer.append(totquan3)
#use for loop to iterate through cluster 1 to get profit of each sublist
for a in cluster1:
    #remove the dollar sign and commar from each monetary value so that they can be converted from string to integer
    a[0] = a[0].replace('$',"").replace(",","")
    #add all the profits in cluster1 together to totprofit1
    totprofit1 += float(a[0])
#use for loop to iterate through cluster 2 to get profit of each sublist
for b in cluster2:
    #remove the dollar sign and commar from each monetary value so that they can be converted from string to integer
    b[0] = b[0].replace('$',"").replace(",","")
    #add all the profits in cluster2 together to totprofit2
    totprofit2 += float(b[0])
#use for loop to iterate through cluster 3 to get profit of each sublist
for c in cluster3:
    #remove the dollar sign and commar from each monetary value so that they can be converted from string to integer
    c[0] = c[0].replace('$',"").replace(",","")
    #add all the profits in cluster3 together to totprofit3
    totprofit3 += float(c[0])
#append all 3 values to final answer as separate list items
final_answer.append(totprofit1)
final_answer.append(totprofit2)
final_answer.append(totprofit3)
#use path.cwd to write the values to a new file called cluster_report.txt
fp = Path.cwd()/"cluster_report.txt"
#use the fp.open method and encoding UTF-8 to write the file
with fp.open(mode ="w", encoding = "UTF-8", newline="") as file:
    #create a new variable called writer and store the csv.writer in it
    writer = csv.writer(file)
    #use the writer variable to format and write all values of total profit and total quantity into the text file line by line by taking values from the final answer list
    writer.writerow(["PROFIT REPORT"])
    writer.writerow(['================='])
    writer.writerow([f'Cluster 1: ${final_answer[3]}'])
    writer.writerow([f'Cluster 2: ${final_answer[4]}'])
    writer.writerow([f'Cluster 3: ${final_answer[5]}'])
    writer.writerow(['                                    '])
    writer.writerow(["QUANTITY REPORT"])
    writer.writerow(['================='])
    writer.writerow([f'Cluster 1: {final_answer[0]}'])
    writer.writerow([f'Cluster 2: {final_answer[1]}'])
    writer.writerow([f'Cluster 3: {final_answer[2]}'])




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












