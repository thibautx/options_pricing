import matplotlib
import json
import matplotlib.pyplot as plt
from threading import Lock
import mpld3

# matplotlib.use('Agg')
plt.ioff()
lock = Lock()

# Setting up matplotlib sytles using BMH
s = json.load(open("./static/bmh_matplotlibrc.json"))
matplotlib.rcParams.update(s)

# x = range(100)
# y = [a * 2 + random.randint(-20, 20) for a in x]
# pie_fracs = [20, 30, 40, 10]
# pie_labels = ["A", "B", "C", "D"]

def draw_fig(fig_type, x, y):
    """Returns html equivalent of matplotlib figure
    Parameters
    ----------
    fig_type: string, type of figure
            one of following:
                    * line
                    * bar
    Returns
    --------
    d3 representation of figure
    """

    with lock:
        fig, ax = plt.subplots()
        if fig_type == "line":
            ax.plot(x, y)
        elif fig_type == "bar":
            ax.bar(x, y)
        # elif fig_type == "pie":
        #     ax.pie(pie_fracs, labels=pie_labels)
        elif fig_type == "scatter":
            ax.scatter(x, y)
        elif fig_type == "hist":
            ax.hist(y, 10, normed=1)
        elif fig_type == "area":
            ax.plot(x, y)
            ax.fill_between(x, 0, y, alpha=0.2)


    return mpld3.fig_to_html(fig)
