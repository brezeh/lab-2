#lab 2 breze howard

import random

#printing results and writing to txt file
def main():
    experiments = 50
    results =[]

    for people in range (5, 51, 5):
        probability = birthdayexperiments(people, experiments)
        result = f"total people: {people}, probability of duplicate: {probability:.4f}"
        results.append(result)
        print(results)

    with open('birthdayexperimentsresults.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')

#checks for duplicate birthdays 
def duplicatebirthdays(birthdays):
    return len(birthdays) != len(set(birthdays))

#gets probability of duplicates 
def birthdayexperiments(people, experiments):
    numberofduplicate = 0

    for n in range(experiments):
        birthdays = [random.randint(1,365) for n in range(people)]
        if numberofduplicate != birthdays:
            numberofduplicate += 1
    probability = numberofduplicate / experiments
    return probability

#calls the main function
main()