import matplotlib.pyplot as plt


def add_guideline(plot, y, label):
    """
    Adds a guideline to the plot at the y coordinate with the given label
    :param plot: The plot to add to
    :param y: The placement of the guideline
    :param label: The label of the guideline
    """
    plot.axhline(y, color="gray")
    plot.text(
        1.02, y, label,
        va='center', ha="left", bbox=dict(facecolor="w", alpha=0.5),
        transform=plot.get_yaxis_transform()
    )


def plot_response_graph(
        response_dict, average_number_of_respondents, total_number_of_respondents,
        x_tickets=None, title=None, x_label=None
):
    """
    Plots a respondent graph
    :param response_dict: The dictionary containing the categories and values
    :param average_number_of_respondents: Used to show a baseline of average respondents
    :param total_number_of_respondents: Used to show the number of respondents for each category compared to the total number
    :param x_tickets: Custom x tick labels
    :return: The plot
    """
    if not x_tickets:
        x_tickets = response_dict.keys()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    if title:
        ax.set_title(title)
    if x_label:
        ax.set_xlabel(x_label)
    ax.set_ylabel("# of Respondents")
    ax.set_xticklabels(x_tickets, rotation=45)
    add_guideline(ax, total_number_of_respondents, "Total respondents")
    add_guideline(ax, average_number_of_respondents, "Average number of responses")
    ax.bar(x_tickets, response_dict.values())
