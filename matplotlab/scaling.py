from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,4))
ax = fig.add_axes([0.0, 0.0, 1, 1])
dots = [[0.05, 0.25, 0.45, 0.25, 0.05],[0.25,0.45, 0.25, 0.05, 0.25]]




line = Line2D(dots[0], dots[1], transform=fig.transFigure, figure=fig, color="r")
ax.lines.extend([line])

dots_new = []
for dot in dots:
    dot_list = [w * 2 for w in dot]
    dots_new.append(dot_list)

print dots_new

line = Line2D(dots_new[0], dots_new[1], transform=fig.transFigure, figure=fig, color="r")
ax.lines.extend([line])
fig.show()


