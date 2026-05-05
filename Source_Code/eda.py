import os
import matplotlib.pyplot as plt

ai_count = len(os.listdir("dataset/ai_code"))
human_count = len(os.listdir("dataset/human_code"))

labels = ["AI", "Human"]
values = [ai_count, human_count]

plt.bar(labels, values)
plt.title("Dataset Distribution")
plt.savefig("static/eda_plot.png")