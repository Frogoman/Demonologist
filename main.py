import csv
import os
from prettytable import PrettyTable



def createDifficultyTable(results_list):
    difficultyCount = [0,0,0]
    difficultyReward = [0,0,0]
    difficultyLoss = [0,0,0]
    ghostCount = []
    ghostCountName = []

    for data in results_list:
        if data[0].lower() == "easy":
            difficultyCount[0] += 1
            difficultyReward[0] += int(data[2])
            difficultyLoss[0] += int(data[3])
        elif data[0].lower()== "medium":
            difficultyCount[1] += 1
            difficultyReward[1] += int(data[2])
            difficultyLoss[1] += int(data[3])
        elif data[0].lower()== "hard":
            difficultyCount[2] += 1
            difficultyReward[2] += int(data[2])
            difficultyLoss[2] += int(data[3])

        if data[1] not in ghostCountName:
            ghostCountName.append(data[1])
            ghostCount.append(1)
        else:
            ghostCount[ghostCountName.index(data[1])] += 1

    # Create a new table
    table = PrettyTable()

    # Add the columns to the table
    table.field_names = ["Difficulty", "Count", "Average Reward", "Average Loss"]

    # Add the rows to the table
    #round(difficultyReward[0] / difficultyCount[0], 2)
    table.add_row(["Easy", difficultyCount[0], round(difficultyReward[0] / difficultyCount[0], 2) if difficultyCount[0] != 0 else "-", round(difficultyLoss[0] / difficultyCount[0], 2) if difficultyCount[0] != 0 else "-"])
    table.add_row(["Medium", difficultyCount[1], round(difficultyReward[1] / difficultyCount[1], 2) if difficultyCount[1] != 0 else "-", round(difficultyLoss[1] / difficultyCount[1], 2) if difficultyCount[1] != 0 else "-"])
    table.add_row(["Hard", difficultyCount[2], round(difficultyReward[2] / difficultyCount[2], 2) if difficultyCount[2] != 0 else "-", round(difficultyLoss[2] / difficultyCount[2], 2) if difficultyCount[2] != 0 else "-"])

    # Print the table
    print(table)
    print("")

def createGhostTable(results_list):
    ghostCount = []
    ghostCountName = []

    for data in results_list:
        if data[1].lower() not in ghostCountName:
            ghostCountName.append(data[1].lower())
            ghostCount.append(1)
        else:
            ghostCount[ghostCountName.index(data[1].lower())] += 1

    # Create a new table
    table = PrettyTable()

    # Add the columns to the table
    table.field_names = ["Ghost", "Count"]

    # Add the rows to the table
    for i in range(len(ghostCountName)):
        table.add_row([ghostCountName[i].capitalize(), ghostCount[i]])

    # Print the table
    print(table)
    print("")


def main():
    # Initialize an empty list to store the values
    values_list = []

    # Open the input file for reading
    with open('results.csv', mode='r') as input_file:
        # Create a reader object for the CSV file
        csv_reader = csv.reader(input_file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Add the row to the values list as a separate array
            values_list.append(row)

    # Ask for user input until the user chooses to stop
    while True:
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print the list of values
        createDifficultyTable(values_list)
        createGhostTable(values_list)

        # Get user input for the three values
        value1 = input("Difficulty: ").lower()

        # Ask the user if they want to enter more values
        if value1.lower() == 'none':
            break

        value2 = input("Ghost: ").lower()
        value3 = input("Reward: ").lower()
        value4 = input("Loss: ").lower()

        # Create a new array for the user inputs and add it to the values list
        user_inputs = [value1, value2, value3, value4]
        values_list.append(user_inputs)


        # Open the output file for writing
        with open('results.csv', mode='w', newline='') as output_file:
            # Create a writer object for the CSV file
            csv_writer = csv.writer(output_file)

            # Write the values to the CSV file as separate rows
            csv_writer.writerows(values_list)



main()        
