import pandas as pd
import math
import random

names_file = "db/random_names.txt"
with open(names_file, "r") as file:
    full_names = [name.strip() for name in file]

output_file = "db/insert_persons.sql"
with open(output_file, "w") as file:
    file.write("")

cities_file = "db/cities_inhabitants_locations.csv"
cities_df = pd.read_csv(cities_file)
for ind, row in cities_df.iterrows():
    city = row["Name"]
    population = row["Population"]
    latitude = row["latitude"]
    longitude = row["longitude"]

    # number of people for the current city
    n = int(population / 10000)
    radius = math.sqrt(n) / 40

    for n in range(n):
        full_name = random.choice(full_names)
        username = full_name.replace(" ", "").lower()
        latitude_offset = random.uniform(0, radius)
        longitude_offset = random.uniform(0, radius)
        location = "point(" + str(latitude + latitude_offset) + "," +  str(longitude + longitude_offset) + ")"

        query = "INSERT INTO person(full_name, username, location)\n" +\
            "VALUES ('{full_name}', '{username}', {location})\n\n"\
            .format(full_name=full_name, username=username, location=location)

        with open(output_file, "a") as file:
            file.write(query)