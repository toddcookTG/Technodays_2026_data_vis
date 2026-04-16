import os
import sys

def load_century_gothic_font():
    """
    Load Century Gothic font from local TTF files on macOS.
    On Windows, Century Gothic is installed by default.
    
    Returns:
        str: Font family name
    """
    if sys.platform == "darwin":
        # macOS - need to load from file
        try:
            import matplotlib.font_manager as fm
            
            # Path to the Century Gothic TTF file in resources folder
            script_dir = os.path.dirname(__file__)
            font_path = os.path.join(script_dir, 'resources', 'centurygothic.ttf')
            
            if os.path.exists(font_path):
                # Register the font
                fm.fontManager.addfont(font_path)
                font_prop = fm.FontProperties(fname=font_path)
                
                print("Century Gothic font loaded successfully from resources folder")
                return font_prop.get_name()
            else:
                print(f"Century Gothic font file not found at {font_path}")
                print("Falling back to Avenir")
                return 'Avenir'
                
        except Exception as e:
            print(f"Failed to load Century Gothic font: {e}")
            print("Falling back to Avenir")
            return 'Avenir'
    else:
        # Windows - Century Gothic is installed by default
        return 'Century Gothic'


def load_finlandica_font():
    """
    Load Finlandica font from local TTF files.
    
    Returns:
        str: Font family name if successful, 'Arial' as fallback
    """
    try:
        import matplotlib.font_manager as fm
        
        # Path to the Finlandica TTF files
        script_dir = os.path.dirname(__file__)
        regular_font = os.path.join(script_dir,'resources','Finlandica-VariableFont_wght.ttf')
        italic_font = os.path.join(script_dir, 'resources', 'Finlandica-Italic-VariableFont_wght.ttf')
        
        if os.path.exists(regular_font):
            # Register the regular font
            fm.fontManager.addfont(regular_font)
            font_prop = fm.FontProperties(fname=regular_font)
            
            # Also register italic if available
            if os.path.exists(italic_font):
                fm.fontManager.addfont(italic_font)
            
            print("Finlandica font loaded successfully")
            print(f"Make sure that you have the Finlandica font installed on your system by double/right clicking the .ttf file and press install.")
            return font_prop.get_name()
        else:
            print(f"Finlandica font files not found in {script_dir}")
            return 'Arial'
            
    except Exception as e:
        print(f"Failed to load Finlandica font: {e}")
        return 'Arial'


# Organization-specific configurations
ORGANIZATIONS = {
    'TG': {
        'colors': [
            '#C73C3A',  # red
            '#6698AF',  # blue
            '#F8C558',  # yellow
            '#A69EC1',  # purple
            '#BAD7DA',  # light blue grey
            '#4E9F82',  # green
            '#782322',  # bordeaux red
            '#395D6D',  # dark blue grey
            '#c6d360',  # light green
            '#f29059',  # orange
            '#f4dee3',  # rose
            '#C18608',  # dark yellow
            '#5D5280',  # dark purple
            '#C4C4C4',  # grey
            '#2d2926'   # black
        ],
        'font': load_century_gothic_font(),
        'font_color': '#000000'
    },
    'EU': {
        'colors': [
            '#003399',  # EU blue
            '#FFCC00',  # EU yellow
            '#0066CC',  # light blue
            '#004080',  # dark blue
            '#FFE066',  # light yellow
            '#666666',  # grey
            '#003366',  # navy
            '#FFD700',  # gold
        ],
        'font': 'Arial',  
        'font_color': '#000000'
    },
    '4FRONT': {
        'colors': [
            '#E2781E',
            '#FFBE41',
            '#706F6F',
            '#BEBEBE',
            '#0056B0',
            '#84D3FF',
            "#884812"
        ],
        'font': 'Arial',
        'font_color': '#000000'
    },

    'BF': {
        'colors': [
            '#002ea2',  # BF Blue
            '#ffaa50',  # Orange
            '#7ddc5a',  # Green
            '#967dff',  # Lilac
            '#c846a5',  # Magenta
        ],
        'font': load_finlandica_font(),
        'font_color': '#000000'
    }
}







def get_colors(organization='TG'):
    """
    Get color palette for a specific organization.
    
    Args:
        organization (str): Organization code ('TG', 'EU', '4FRONT'). Defaults to 'TG'.
    
    Returns:
        list: Color palette for the specified organization.
        
    Raises:
        ValueError: If organization is not supported
    """
    if organization not in ORGANIZATIONS:
        raise ValueError(f"Unsupported organization: {organization}. Choose from: {list(ORGANIZATIONS.keys())}")
    
    return ORGANIZATIONS[organization]['colors']


from matplotlib.colors import LinearSegmentedColormap
def get_cmap(organization='TG'):
    """
    Get a LinearSegmentedColormap for a specific organization.
    
    Args:
        organization (str): Organization code ('TG', 'EU', '4FRONT'). Defaults to 'TG'.
    
    Returns:
        LinearSegmentedColormap: Color map for heatmaps.
    """

    # set color range from light shade of primary organization color to primary color
    COLOR = get_colors(organization)[0]
    cmap = LinearSegmentedColormap.from_list("org_heatmap", [lighten_hex(COLOR), COLOR])
    
    # set nan values to light grey
    cmap.set_bad('#f0f0f0')

    return cmap



def get_font(organization='TG'):
    """
    Get font family for a specific organization.
    
    Args:
        organization (str): Organization code ('TG', 'EU', '4FRONT'). Defaults to 'TG'.

    Returns:
        str: Font family for the specified organization.
    """




def lighten_hex(hex_color: str, factor: float = 0.85) -> str:
    """
    Return a lighter shade of a hex color by mixing it with white.

    Args:
        hex_color: A hex string of the form '#RRGGBB'.
        factor: Float in [0, 1]. Higher means closer to white.
                0 returns the original color.
                1 returns pure white.

    Returns:
        Hex string '#RRGGBB' representing the lightened color.
    """
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    r_l = int(r + (255 - r) * factor)
    g_l = int(g + (255 - g) * factor)
    b_l = int(b + (255 - b) * factor)

    return "#{:02X}{:02X}{:02X}".format(r_l, g_l, b_l)   