"""Blog-post version of figures/xboot_param_ci_comparison.png, without the
human-time-only series. Not part of the main pipeline: it only redraws the intervals
xboot.py saved, so run xboot.py first.

    python blog_ci_comparison.py
"""
import pandas as pd
import plotly

import metr_fit_helpers as metr

plotly.io.templates.default = "plotly_white"

CONDITIONS = ["metr", "metr+x_param"]

frontier_agents, _, official_fits_by_agent = metr.load_frontier_agents_and_dates()
agents_sorted = [
    agent for agent in official_fits_by_agent.set_index("agent")["p50"].sort_values().index
    if agent in frontier_agents
]
ci_by_agent_condition = pd.read_csv(
    metr.HERE / "data" / f"xboot_param_ci_by_agent{metr.VERSION_SUFFIX}.csv"
).query("condition in @CONDITIONS")

fig = metr.dodged_confidence_interval_figure(
    ci_by_agent_condition, agents_sorted, CONDITIONS,
    title=metr.XBOOT_PARAM_CI_TITLE,
    condition_labels=metr.XBOOT_CONDITION_LABELS,
)
fig.write_image(
    metr.HERE / "figures" / f"xboot_param_ci_comparison_no_x_only{metr.VERSION_SUFFIX}.png",
    width=850, height=620, scale=2,
)
