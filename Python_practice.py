counties = "Arapahoe", "Denver", "Jefferson"
for county in counties:
    print(county)
print(counties)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
print("-------------------")

for num in range (6):
    print(num)

print("-------------------")

print(len(counties))

print("-------------------")

for i in range(len(counties)):
    print(counties[i])

print("-----------------------")

counties_tuples = ("Arapahoe","Denver","Jefferson")
print(counties_tuples)

for i in range(len(counties_tuples)):
      print(counties_tuples[i])
print("-----------------------")

for county in counties_tuples:
      print(county)

for county in counties_tuples:
      print(counties)
print("___________________________")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for n in counties_dict:
    print(counties_dict.get(n))

print("---------------------")
for key, value in counties_dict.items():
    print(key, value)
print("---------------------")
for i in counties_dict.items():
    print(i)
for key, value in counties_dict.items():
    print(key + " county has " + str(value) + " registered voters.")

print("--------------------")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
      print(voting_data[i]) 

for county_dict in voting_data:
    for value in county_dict.keys():
        print(value)

print("----------------")
for county_dict in voting_data:
     for key, value in county_dict.items():
         print(key, value)
print("--------------------------")

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#print(f"I received {(my_votes / total_votes)* 100}% of the total votes.")

#--------------------------------------------------

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters} registered voters.")

print("-----------------------------")

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
   # f"You received {candidate_votes} number of votes. "
   # f"The total number of votes in the election was {total_votes}. "
   # f"You received {candidate_votes / total_votes * 100:,.2f}% of the total votes.")

#print(message_to_candidate)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registerded votes.')

print("-------------------------------")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

for values in voting_data:
    print(f'{values["county"]} county has {values["registered_voters"]} registerded votes. Hello')

