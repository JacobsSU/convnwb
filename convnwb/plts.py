"""Visualizations for checking conversions."""

from convnwb.modutils import safe_import, check_dependency

plt = safe_import('.pyplot', 'matplotlib')

###################################################################################################
###################################################################################################

@check_dependency(plt, 'matplotlib')
def plot_alignment(sync1, sync2, n_pulses=None):
    """Plot the alignment between synchronization pulses.

    Parameters
    ----------
    sync1, sync2 : 1d array
        Sync pulse times for each sync pulse stream.
    n_pulses : int, optional
        Restrict the visualization to a restricted number of pulses.
    """

    _, ax = plt.subplots(figsize=(20, 4))
    ax.eventplot([sync1, sync2], linelengths=[0.9, 0.9], colors=['g', 'b'])
    ax.set_xlabel('Time (ms)')
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Sync Neural', 'Sync Behavioral'])
    ax.set_title('Synchronization pulses')

    if n_pulses:
        ax.set_xlim(sync1[0], sync1[n_pulses])
