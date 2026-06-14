import numpy as np

def plot_bar(values, labels, ax, title=None, xlabel=None, ylabel=None, formater=lambda x: x):
    ax.bar (range(len(values)), values)
    for i, val in enumerate(values):
        ax.text(i-.5, val + 1, formater(val), va='center')

    ax.set_xticks(range(len(values)))
    ax.set_xticklabels(labels)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.set_ylim(0, max(values) * 1.05)


def plot_barh(values, labels, ax, title=None, xlabel=None, ylabel=None, formater=lambda x: x):
    ax.barh(range(len(values)), values)
    for i, val in enumerate(values):
        ax.text(val + 1, i, formater(val), va='center')

    ax.set_yticks(range(len(values)))
    ax.set_yticklabels(labels)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.set_xlim(0, max(values) * 1.05)


def plot_pie(values, labels, ax, title=None):
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)


def plot_hist(values, ax, title=None, xlabel=None, ylabel=None, bins=10):
    ax.hist(values, bins=bins, edgecolor='black')

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


def plot_2g_bar(groups, ax, title=None, xticklabels=None):
    x = np.arange(2)
    width=0.25
    for i, (group, values) in enumerate(groups.items()):
        i = (i - 1) * width
        ax.bar(x + i, values, width=width, label=group)

    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(xticklabels)
    ax.legend()


def plot_hbox(groups, ax, title=None, xlabel=None, ylabel=None):
    ax.boxplot(groups.values(), label=groups.keys(), orientation='horizontal')

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


# API is pretty cumbersome with 1 group
def plot_scatter(groups, ax, title=None, xlabel=None, ylabel=None, xlim=None, ylim=None):
    for group, values in groups.items():
        ax.scatter(values[0], values[1], label=group)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if len(groups) > 1:
        ax.legend()

    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)


# API is pretty cumbersome with 1 group
def plot_lines(groups, ax, title=None, xlabel=None, ylabel=None, xlim=None, ylim=None):
    for group, values in groups.items():
        ax.plot(values[0], values[1], label=group, marker='o', linestyle='--')

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if len(groups) > 1:
        ax.legend()

    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)