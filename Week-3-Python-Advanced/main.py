import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
temp_lisbon = [22, 24, 32, 23, 25]
temp_new_york = [34, 32, 31, 30, 28]
temp_sydney = [
    35,
    32,
    28,
    27,
    35,
]
print(plt.style.available)
plt.style.use("fivethirtyeight")

plt.plot(days, temp_lisbon, label="Lisbon", linestyle="--")
plt.plot(days, temp_new_york, label="New York", color="g", linewidth=5)
plt.plot(days, temp_sydney, label="Sydney", marker=".")
plt.title("Temperature forecast for the next 5 days")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.legend()
plt.grid(True)

hours_studied = [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]
breaks_taken = [0, 2, 1, 3, 0, 1, 2, 0, 3, 0, 2, 1, 3, 0, 2]
exam_scores = [52, 54, 57, 59, 63, 67, 72, 76, 78, 82, 85, 88, 90, 93, 95]

plt.figure()
plt.scatter(hours_studied,
            exam_scores,
            label="Hours Studied",
            color="r",
            s=200,
            alpha=0.4)
plt.scatter(breaks_taken,
            exam_scores,
            label="Breaks Taken",
            color="g",
            s=400,
            alpha=0.3)
plt.title("Exam Score")
plt.xlabel("Hours")
plt.ylabel("Score in %")
plt.grid(True)

plt.legend()

condition = ['sunny', 'rainy', 'cloudy']
days = [300, 30, 35]
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.pie(days, labels=condition)
ax1.set_title("Weather Condition")
ax1.legend(days)
ax2.pie(days, labels=condition)
ax2.set_title("Weather Condition")
ax2.legend(days)

plt.tight_layout()

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(years,
         temp_anomalies,
         label="Temperature Anomalies",
         marker=".",
         color="r",
         linewidth=5)
ax1.set_title("Temperature Anomalies")
ax1.grid(True)
ax2.bar(years, co2_emissions, label="CO2 Emissions", color = "purple")
ax2.grid(True)
plt.tight_layout()
plt.legend()
plt.savefig("Temperature and CO2 emmisions.png")
plt.show()



#Display 2 subplots next to each other
#The first one should display the temperature deviation using a linear plot.
#The second one should display the CO2 deviation using a bar chart
#Save the result inside an image
#Make the plots look nice and readable

#Display 3 plot with the temperature forecast for Lisbon, new york and Sydney for the next 5 days (use random data)
#Add legend and label
