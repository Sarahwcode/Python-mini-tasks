import csv
import matplotlib.pyplot as plt


def generate_population_dictionary_from_csv(datafile):
  """Generate a dictionary with population data from a CSV file."""
  population_per_continent = {}
  """Dictionary to store population data for each continent."""

  with open(datafile, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      continent = row["continent"]
      year = row["year"]
      population = row["population"]
      print(continent, year, population)

      if continent not in population_per_continent:
        population_per_continent[continent] = {"population": [], "years": []}

      population_per_continent[continent]["population"].append(int(population))
      population_per_continent[continent]["years"].append(int(year))

  return population_per_continent


def generate_population_plots_from_dictionary(population_dictionary):
  """Generate population plots from a dictionary."""
  for continent in population_per_continent:
    years = population_per_continent[continent]["years"]
    population = population_per_continent[continent]["population"]
    plt.plot(years, population, label=continent, marker="o", alpha=0.5)

  plt.title("Population Growth")
  plt.xlabel("Year")
  plt.ylabel("Population(in billions)")
  plt.grid(True)
  plt.tight_layout()
  plt.legend()
  plt.show()


datafile = "data.csv"
"""Path to the CSV file containing population data."""
population_per_continent = generate_population_dictionary_from_csv(datafile)
"""Dictionary to store population data for each continent."""
generate_population_plots_from_dictionary(population_per_continent)
