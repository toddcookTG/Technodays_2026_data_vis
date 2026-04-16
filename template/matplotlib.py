from .templates import ORGANIZATIONS, get_cmap
from .constants import FIGURE_WIDTH_INCHES, FIGURE_HEIGHT_INCHES, FONT_SIZES


def setup_matplotlib_template(organization='TG', colors=None, font=None):
    """
    Setup Matplotlib template with organization-specific styling.
    
    Args:
        organization (str): Organization code ('TG', 'EU', '4FRONT'). Defaults to 'TG'.
        colors (list): Custom color palette. If None, uses organization colors.
        font (str): Custom font family. If None, uses organization font.
    
    Raises:
        ImportError: If matplotlib is not installed
        ValueError: If organization is not supported
    """
    if organization not in ORGANIZATIONS:
        raise ValueError(f"Unsupported organization: {organization}. Choose from: {list(ORGANIZATIONS.keys())}")
    
    org_config = ORGANIZATIONS[organization]
    FONT_FAMILY = font if font is not None else org_config['font']
    FONT_COLOR = org_config['font_color']
    COLORS = colors if colors is not None else org_config['colors']
    
    try:
        import matplotlib.pyplot as plt
        from cycler import cycler
    except ImportError:
        raise ImportError("Matplotlib is required for setup_matplotlib_template(). Install with: pip install matplotlib")
    
    # Font settings
    font_config = {
        'font.sans-serif': FONT_FAMILY,
        'font.family': FONT_FAMILY,
        'font.serif': FONT_FAMILY,
        'font.cursive': FONT_FAMILY,
        'font.fantasy': FONT_FAMILY,
        'font.monospace': FONT_FAMILY
    }
    plt.rcParams.update(font_config)
    
    # Figure dimensions
    plt.rcParams['figure.figsize'] = (FIGURE_WIDTH_INCHES, FIGURE_HEIGHT_INCHES)
    
    # Text size settings
    plt.rc('font', size=FONT_SIZES['small'])  # default text size
    plt.rc('figure', titlesize=FONT_SIZES['large'])  # figure title
    plt.rc('figure', titleweight='bold')  # figure title bold
    plt.rc('axes', titlesize=FONT_SIZES['large'])  # axes titles
    plt.rc('axes', titleweight='bold')  # axes titles bold
    plt.rc('axes', titlepad=FONT_SIZES['large'])  # title padding
    plt.rc('axes', labelsize=FONT_SIZES['tiny'])  # axis labels
    plt.rc('xtick', labelsize=FONT_SIZES['tiny'])  # x tick labels
    plt.rc('ytick', labelsize=FONT_SIZES['tiny'])  # y tick labels
    
    # Tick and spine settings
    tick_spine_config = {
        'xtick.major.size': 0,  # remove x tick marks
        'ytick.major.size': 0,  # remove y tick marks
        'axes.xmargin': 0,
        'axes.ymargin': 0,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True
    }
    plt.rcParams.update(tick_spine_config)
    
    # Legend settings
    plt.rc('legend', title_fontsize=FONT_SIZES['small'])
    plt.rc('legend', fontsize=FONT_SIZES['tiny'])
    plt.rc('legend', frameon=True)
    plt.rc('legend', facecolor="#E6E8EB")
    plt.rc('legend', edgecolor='white')
    plt.rc('legend', borderpad=0.75)
    plt.rc('legend', columnspacing=2.0)
    
    # Background and color settings
    appearance_config = {
        'axes.facecolor': 'white',
        'savefig.facecolor': 'white',
        'patch.edgecolor': 'none'
    }
    plt.rcParams.update(appearance_config)

    # Heatmap styling
    cmap = get_cmap(organization=organization)
    plt.rcParams['image.cmap'] = 'org_heatmap'
    
    # Only register if not already registered
    if 'org_heatmap' not in plt.colormaps:
        plt.colormaps.register(cmap, name='org_heatmap')
    else:
        # Unregister and re-register to update with new colors
        plt.colormaps.unregister('org_heatmap')
        plt.colormaps.register(cmap, name='org_heatmap')
    
    # Print/save settings
    output_config = {
        'figure.dpi': 200.0,  # notebook display sharpness slightly reduced to prevent lag
        'figure.autolayout': True,  # tight layout default
        'savefig.pad_inches': 0.1,  # space around figure
        'savefig.dpi': 400,  # saved image sharpness
        'savefig.bbox': 'tight'
    }
    plt.rcParams.update(output_config)
    
    # Set color cycle
    plt.rc('axes', prop_cycle=cycler('color', COLORS))