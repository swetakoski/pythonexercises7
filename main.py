#Module 7
#Question 1
# seasons=('winter', 'spring', 'summer', 'autumn')
#
#
# user_input=int(input("Enter the number of month: "))
# if 1 <= user_input <= 12:
#     season_index = (user_input - 1) // 3
#     season = seasons[season_index]
# print(f"The season for month {user_input} is {season}.")

#Question 2

# names = set()
# new_names = set()
#
# while True:
#     name = input("Enter a name (or press Enter to finish): ")
#
#     if name == "":
#         break
#
#     if name in names:
#         print("Existing name")
#     else:
#         print("New name")
#         new_names.add(name)
#
#     names.add(name)
# print("\nList of unique names:")
# for name in names:
#     print(name)



thisdict = {
      "name": "Indira Ghandi International Airport",
      "icao": "VIDP"
 }

user_input= input("Do you want to enter a new airport, fetch the information on existing airport or quit?:  ")
if user_input == "New":
      name = input("Enter the name of the airport: ")
      icao = input("Enter the corresponding ICAO code: ")
      thisdict.update({"name": name})
      thisdict.update({"icao": icao})
      print (thisdict)
      print(f"Airport {icao} - {name} added successfully!")



elif user_input=="Fetch":
    icao=input("Enter the ICAO code of the airport: ")
    thisdict.get("name")
    thisdict.get("icao")
    print (thisdict)


else:
    user_input=="quit"
    print("Bye")