import matplotlib.pyplot as plt

story = """
In the heart of a bustling metropolis, there was a man named Michael grappling with the weight of his past. Past failures and setbacks cast a long shadow over his ambitions, making every step towards success feel like an uphill battle.

Enter a wise mentor who recognized Michael's internal struggle. "To succeed consistently, you need to break free from the chains of your past," the mentor advised.

Taking these words to heart, Michael decided to confront his history head-on. He documented his disappointments, mistakes, and heartaches on paper. Watching the document turn to ash, he made a symbolic gesture of bidding farewell to the ghosts that haunted him.

With a newfound commitment to consistency, Michael shifted his focus to the present. Each day, he tackled challenges with a clear mind and a resilient spirit, unburdened by the ghosts of past failures. This commitment to staying in the moment became the linchpin of his success.

Over time, Michael's consistency paid off. Milestone after milestone, he proved that letting go of the past is often the key to unlocking a future of achievement. As he reached new heights, the shadows of his history gradually dissipated, becoming mere echoes in the background.

In embracing this practical wisdom, Michael discovered the transformative power of staying focused on the present. Success, he realized, often hinges on the ability to learn from the past without being tethered to it—a valuable lesson that many aspiring achievers find on their journey toward consistent and meaningful success.
"""

key_points = [
    "Weight of past",
    "Wise mentor's advice",
    "Documenting past",
    "Symbolic farewell",
    "Shift to the present",
    "Commitment to consistency",
    "Milestones of success",
    "Shadows dissipate",
    "Transformative wisdom",
    "Learning from the past"
]

plt.figure(figsize=(10, 6))  
plt.plot(key_points, [1] * len(key_points), marker='o', linestyle='-', color='b')
plt.title("Michael's Journey to Success")
plt.xlabel("Key Points")
plt.yticks([])

plt.savefig("Story_matplotlib.png", bbox_inches="tight")  
plt.show()



