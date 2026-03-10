colors = ("red", "green", "blue")
for index, color in enumerate(colors):
    print(f"Color {index} is {color}")


data = {"a": 1, "b": 2}
labels = ["x", "y"]

for (k,v) ,l in zip(data.items(),labels):
    print(f"{k}:{l}")