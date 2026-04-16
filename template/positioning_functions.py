import matplotlib.pyplot as plt


def cm_to_figure_units_vertical(fig, cm):
    """Convert cm to vertical figure coordinate units (0-1)."""
    fig_height_inches = fig.get_figheight()
    fig_height_cm = fig_height_inches * 2.54
    return cm / fig_height_cm

def cm_to_figure_units_horizontal(fig, cm):
    """Convert cm to horizontal figure coordinate units (0-1)."""
    fig_width_inches = fig.get_figwidth()
    fig_width_cm = fig_width_inches * 2.54
    return cm / fig_width_cm


def finalize_figure_with_legend_and_disclaimer(
    fig, 
    ax, 
    legend_labels=None, 
    legend_title=None, 
    legend_ncol=3,
    disclaimer=None,
    bottom_margin=0.20
):
    """
    Finalize figure with proper spacing, optional legend below x-axis, and optional disclaimer.
    
    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure object
    ax : matplotlib.axes.Axes
        The axes object
    legend_labels : list or None
        If provided, creates a legend with these labels. If None, no legend is added.
    legend_title : str or None
        Title for the legend (only used if legend_labels is provided)
    legend_ncol : int
        Number of columns in the legend (default: 3)
    disclaimer : str or False or None
        If string: adds disclaimer text below legend/plot
        If False or None: no disclaimer is added
    bottom_margin : float
        Fraction of figure height to reserve at bottom (default: 0.20)
    
    Example:
    --------
    finalize_figure_with_legend_and_disclaimer(
        fig, ax,
        legend_labels=['Item 1', 'Item 2'],
        legend_title='Categories',
        disclaimer='Data source: XYZ 2024'
    )
    """
    # Remove any existing legend first
    if ax.get_legend() is not None:
        ax.get_legend().remove()
    
    # First reserve space and constrain the plot area
    plt.subplots_adjust(bottom=bottom_margin)
    plt.tight_layout(rect=[0, bottom_margin, 1, 1])
    
    # Force a draw to get accurate positions
    fig.canvas.draw()
    
    # Add legend if labels are provided
    if legend_labels is not None:
        # Get x-axis label position in figure coordinates BEFORE creating legend
        xlabel = ax.xaxis.get_label()
        xlabel_bbox = xlabel.get_window_extent(renderer=fig.canvas.get_renderer())
        xlabel_bbox_fig = xlabel_bbox.transformed(fig.transFigure.inverted())
        xlabel_bottom = xlabel_bbox_fig.y0
        
        # Create legend with bbox_to_anchor in figure coords from the start
        # Place it temporarily to measure its size
        legend = ax.legend(
            legend_labels, 
            title=legend_title, 
            loc='upper center',
            ncol=legend_ncol,
            bbox_to_anchor=(0.5, 0.5),
            bbox_transform=fig.transFigure
        )
        
        # Force another draw after legend creation
        fig.canvas.draw()
        
        # Get legend dimensions
        legend_bbox = legend.get_window_extent(renderer=fig.canvas.get_renderer())
        legend_bbox_fig = legend_bbox.transformed(fig.transFigure.inverted())
        legend_height = legend_bbox_fig.height
        
        # Position legend just below xlabel with small gap
        gap = cm_to_figure_units_vertical(fig, 0.1)
        legend_y = xlabel_bottom - gap - legend_height
        print(f"Legend y-position: {legend_y:.3f}, Legend height: {legend_height:.3f},  xlabel bottom: {xlabel_bottom:.3f}")
        legend.set_bbox_to_anchor((0.5, legend_y + legend_height), transform=fig.transFigure)
        
        # Add disclaimer below legend if provided
        if disclaimer:
            disclaimer_gap = cm_to_figure_units_vertical(fig, 0.4)
            text_y = legend_y - disclaimer_gap
            fig.text(cm_to_figure_units_horizontal(fig, 0.5), text_y, disclaimer, 
                    ha='left', fontsize=6, style='italic', color='grey',
                    transform=fig.transFigure)
    else:
        # No legend, add disclaimer below x-axis label if provided
        if disclaimer:
            xlabel = ax.xaxis.get_label()
            xlabel_bbox = xlabel.get_window_extent(renderer=fig.canvas.get_renderer())
            xlabel_bbox_fig = xlabel_bbox.transformed(fig.transFigure.inverted())
            xlabel_bottom = xlabel_bbox_fig.y0
            
            disclaimer_gap = cm_to_figure_units_vertical(fig, 0.4)
            text_y = xlabel_bottom - disclaimer_gap
            fig.text(cm_to_figure_units_horizontal(fig, 0.5), text_y, disclaimer, 
                    ha='left', fontsize=6, style='italic', color='grey',
                    transform=fig.transFigure)