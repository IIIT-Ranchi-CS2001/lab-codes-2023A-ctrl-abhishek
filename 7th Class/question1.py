import matplotlib.pyplot as plt

mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]
mp_percentages = [seats / sum(mp_seats) * 100 for seats in mp_seats]

raj_parties = ['BJP', 'INC', 'BSP', 'Others']
raj_seats = [115, 69, 2, 13]
raj_percentages = [seats / sum(raj_seats) * 100 for seats in raj_seats]

plt.figure(figsize=(10, 6))
plt.pie(mp_percentages, labels=mp_parties, autopct='%1.1f%%',
        explode=[0.1 if percent == max(mp_percentages) else 0 for percent in mp_percentages],
        startangle=140, colors=['orange', 'blue', 'green', 'grey'])
plt.title("Madhya Pradesh Assembly Elections 2023")
plt.show()

plt.figure(figsize=(10, 6))
plt.pie(raj_percentages, labels=raj_parties, autopct='%1.1f%%',
        explode=[0.1 if percent == max(raj_percentages) else 0 for percent in raj_percentages],
        startangle=140, colors=['orange', 'blue', 'green', 'grey'])
plt.title("Rajasthan Assembly Elections 2023")
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

axs[0].pie(mp_percentages, labels=mp_parties, autopct='%1.1f%%',
           explode=[0.1 if percent == max(mp_percentages) else 0 for percent in mp_percentages],
           startangle=140, colors=['orange', 'blue', 'green', 'grey'])
axs[0].set_title("Madhya Pradesh Assembly Elections 2023")

axs[1].pie(raj_percentages, labels=raj_parties, autopct='%1.1f%%',
           explode=[0.1 if percent == max(raj_percentages) else 0 for percent in raj_percentages],
           startangle=140, colors=['orange', 'blue', 'green', 'grey'])
axs[1].set_title("Rajasthan Assembly Elections 2023")

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x_indexes = range(len(mp_parties))

ax.bar(x_indexes, mp_seats, width=bar_width, label="Madhya Pradesh", color='orange')

ax.bar([x + bar_width for x in x_indexes], raj_seats, width=bar_width, label="Rajasthan", color='blue')

ax.set_xlabel("Party", fontsize=12)
ax.set_ylabel("Seats Won", fontsize=12)
ax.set_title("Assembly Elections 2023 - Seat Share", fontsize=14)
ax.set_xticks([x + bar_width / 2 for x in x_indexes])
ax.set_xticklabels(mp_parties)
ax.legend()

plt.tight_layout()
plt.show()