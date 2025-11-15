capitals = {"France" : "Paris",
            "Germany" : "Berlin",
            "India" : "New Delhi"}

#Nested List in Dictionaries

travel = {"France" : ["Paris" , "Lille"],
          "Germany" : ["Berlin" , "Stuttgart"],
          "India": ["New Delhi", "Mumbai", "Bengaluru"]
          }

#print Bengaluru
print(travel["India"][2])


nested_list = ["A", "B", ["C", "D"]] #print D
print(nested_list[2][1])



#list nested inside dictionaries
#print Stuttgart

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])

