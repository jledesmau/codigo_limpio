colors = ["white", "black", "brown"]
for i in range(len(colors)):
  print(i+1, colors[i])
# 1 white
# 2 black
# 3 brown

colors = ["white", "black", "brown"]
for i, colors in enumerate(colors, 1):
  print(i, colors)
  
# 1 white
# 2 black
# 3 brown