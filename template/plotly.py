from .constants import FIGURE_WIDTH_PIXELS, FIGURE_HEIGHT_PIXELS, MAP_FOCUS
from .templates import ORGANIZATIONS


def setup_plotly_template(organization='TG', colors=None, font=None, map_focus='WORLD'):
    """
    Setup Plotly template with organization-specific styling.
    
    Args:
        organization (str): Organization code ('TG', 'EU', '4FRONT'). Defaults to 'TG'.
        colors (list): Custom color palette. If None, uses organization colors.
        font (str): Custom font family. If None, uses organization font.
        map_focus (str): Geographic focus ('WORLD', 'EU', 'NL'). Defaults to 'WORLD'.
    
    Raises:
        ImportError: If plotly is not installed
        ValueError: If organization or map_focus is not supported
    """
    if organization not in ORGANIZATIONS:
        raise ValueError(f"Unsupported organization: {organization}. Choose from: {list(ORGANIZATIONS.keys())}")
    
    if map_focus not in MAP_FOCUS:
        raise ValueError(f"Unsupported map focus: {map_focus}. Choose from: {list(MAP_FOCUS.keys())}")
    
    org_config = ORGANIZATIONS[organization]
    FONT_FAMILY = font if font is not None else org_config['font']
    FONT_COLOR = org_config['font_color']
    COLORS = colors if colors is not None else org_config['colors']
    
    try:
        import plotly.graph_objects as go
        import plotly.io as pio
    except ImportError:
        raise ImportError("Plotly is required for setup_plotly_template(). Install with: pip install plotly")
    
    # Create template object
    template = go.layout.Template()
    
    # Font settings
    template.layout.font.family = FONT_FAMILY
    template.layout.font.color = FONT_COLOR
    template.layout.plot_bgcolor = 'rgba(0,0,0,0)'
    
    # Figure dimensions
    template.layout.width = FIGURE_WIDTH_PIXELS
    template.layout.height = FIGURE_HEIGHT_PIXELS
    
    # Color settings
    template.layout.colorway = COLORS
    template.layout.colorscale.sequential = [COLORS[1], COLORS[0]]
    
    # Axis styling
    axis_config = {
        'linewidth': 1.3,
        'showline': True,
        'linecolor': 'black',
        'showgrid': False,
        'ticks': '',
        'automargin': True,
        'ticksuffix': " "
    }
    
    for axis in ['xaxis', 'yaxis']:
        for key, value in axis_config.items():
            setattr(getattr(template.layout, axis), key, value)
    
    # Y-axis specific settings
    template.layout.yaxis.rangemode = "tozero"
    template.layout.xaxis.title.standoff = 10
    template.layout.yaxis.title.standoff = 15
    
    # Margins
    template.layout.margin = dict(b=0, r=0, l=0)
    
    # Legend styling
    template.layout.legend = {
        'bgcolor': '#f7f7f7',
        'orientation': "v",
        'xanchor': "left",
        'x': 1.05,
        'yanchor': "middle",
        'y': 0.5,
        'bordercolor': "white",
        'borderwidth': 0
    }
    
    # Title positioning
    template.layout.title = {
        "yref": "paper",
        "y": 1,
        "yanchor": "bottom"
    }
    
    # Heatmap styling
    template.data.heatmap = [go.Heatmap(xgap=1.5, ygap=1.5)]
    
    # Colorbar styling
    template.layout.coloraxis = {
        'colorbar': {
            'outlinewidth': 0,
            'ticks': '',
            'lenmode': 'fraction',
            'len': 0.6,
            'thicknessmode': 'pixels',
            'thickness': 10,
            'nticks': 4,
            'tickmode': 'auto'
        }
    }
    
    # Geographic map styling
    map_config = MAP_FOCUS[map_focus]
    template.layout.geo = {
        'bgcolor': 'rgba(0,0,0,0)',
        'landcolor': "#B6B6B6",
        'showland': True,
        'showcoastlines': False,
        'showframe': False,
        'lataxis_range': map_config['lataxis_range'],
        'lonaxis_range': map_config['lonaxis_range'],
        'resolution': 110
    }
    
    # Register and set as default template
    pio.templates[organization] = template
    pio.templates.default = organization
    
    return template