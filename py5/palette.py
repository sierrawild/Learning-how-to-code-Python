"""
Color Palettes for py5 Creative Coding
========================================

Import this module to access curated color palettes for your py5 sketches.

Usage:
    from color_palettes import OCEAN, SUNSET, random_palette
    
    def setup():
        size(800, 600)
        background(OCEAN['bg'])
        fill(OCEAN['colors'][0])
"""

import random, py5


# ============================================================================
# NATURE PALETTES
# ============================================================================

OCEAN = {
    'name': 'Ocean Depths',
    'bg': (15, 25, 45),
    'colors': [
        (28, 107, 160),   # Deep blue
        (46, 134, 171),   # Ocean blue
        (72, 191, 227),   # Sky blue
        (134, 230, 255),  # Foam
        (185, 251, 192),  # Seafoam green
    ]
}

FOREST = {
    'name': 'Forest Floor',
    'bg': (25, 35, 30),
    'colors': [
        (52, 78, 65),     # Deep green
        (88, 129, 87),    # Moss
        (163, 177, 138),  # Sage
        (218, 215, 205),  # Birch
        (133, 88, 53),    # Earth
    ]
}

SUNSET = {
    'name': 'Desert Sunset',
    'bg': (20, 15, 30),
    'colors': [
        (253, 181, 21),   # Gold
        (247, 127, 0),    # Orange
        (252, 65, 54),    # Red-orange
        (155, 35, 65),    # Deep red
        (82, 35, 65),     # Purple shadow
    ]
}

CHERRY_BLOSSOM = {
    'name': 'Cherry Blossom',
    'bg': (245, 240, 235),
    'colors': [
        (255, 183, 197),  # Light pink
        (255, 138, 172),  # Pink
        (218, 112, 148),  # Rose
        (140, 93, 113),   # Mauve
        (93, 79, 84),     # Charcoal
    ]
}


# ============================================================================
# RETRO / VINTAGE PALETTES
# ============================================================================

VAPOR = {
    'name': 'Vaporwave',
    'bg': (1, 0, 30),
    'colors': [
        (255, 113, 206),  # Hot pink
        (179, 97, 255),   # Purple
        (94, 181, 255),   # Cyan
        (1, 247, 161),    # Mint
        (255, 204, 170),  # Peach
    ]
}

RETRO_FUTURE = {
    'name': 'Retro Future',
    'bg': (18, 18, 28),
    'colors': [
        (0, 234, 255),    # Cyan
        (255, 0, 110),    # Magenta
        (255, 204, 0),    # Yellow
        (170, 0, 255),    # Purple
        (0, 255, 161),    # Green
    ]
}

COMMODORE = {
    'name': 'Commodore 64',
    'bg': (83, 77, 155),
    'colors': [
        (158, 158, 239),  # Light blue
        (120, 106, 189),  # Blue
        (111, 79, 37),    # Brown
        (134, 122, 222),  # Lavender
        (184, 199, 111),  # Yellow-green
    ]
}


# ============================================================================
# BOLD / GRAPHIC PALETTES
# ============================================================================

NEON_NIGHTS = {
    'name': 'Neon Nights',
    'bg': (10, 5, 15),
    'colors': [
        (255, 0, 255),    # Magenta
        (0, 255, 255),    # Cyan
        (255, 255, 0),    # Yellow
        (255, 0, 127),    # Hot pink
        (0, 255, 127),    # Spring green
    ]
}

MONDRIAN = {
    'name': 'Mondrian',
    'bg': (240, 240, 235),
    'colors': [
        (225, 32, 38),    # Red
        (0, 83, 156),     # Blue
        (254, 221, 0),    # Yellow
        (30, 30, 30),     # Black
        (240, 240, 235),  # White
    ]
}

BAUHAUS = {
    'name': 'Bauhaus',
    'bg': (240, 235, 220),
    'colors': [
        (214, 40, 57),    # Red
        (247, 181, 56),   # Yellow
        (0, 111, 184),    # Blue
        (45, 45, 45),     # Black
        (240, 235, 220),  # Cream
    ]
}


# ============================================================================
# PASTEL / SOFT PALETTES
# ============================================================================

SORBET = {
    'name': 'Sorbet',
    'bg': (255, 250, 245),
    'colors': [
        (255, 190, 152),  # Peach
        (255, 209, 220),  # Pink
        (251, 229, 214),  # Cream
        (211, 226, 227),  # Mint
        (196, 223, 223),  # Aqua
    ]
}

LAVENDER_FIELD = {
    'name': 'Lavender Field',
    'bg': (245, 243, 250),
    'colors': [
        (177, 156, 217),  # Lavender
        (149, 125, 173),  # Purple
        (210, 193, 219),  # Light purple
        (230, 221, 212),  # Beige
        (188, 189, 172),  # Sage
    ]
}


# ============================================================================
# EARTHY / MUTED PALETTES
# ============================================================================

TERRACOTTA = {
    'name': 'Terracotta',
    'bg': (245, 240, 230),
    'colors': [
        (204, 102, 68),   # Terracotta
        (187, 134, 100),  # Clay
        (153, 153, 119),  # Olive
        (221, 204, 170),  # Sand
        (102, 85, 68),    # Brown
    ]
}

AUTUMN = {
    'name': 'Autumn',
    'bg': (45, 40, 35),
    'colors': [
        (191, 64, 64),    # Rust
        (217, 136, 64),   # Burnt orange
        (242, 191, 86),   # Gold
        (140, 115, 75),   # Ochre
        (89, 60, 31),     # Brown
    ]
}


# ============================================================================
# MONOCHROME / GRAYSCALE
# ============================================================================

INK = {
    'name': 'Ink',
    'bg': (250, 248, 245),
    'colors': [
        (25, 25, 30),     # Black
        (60, 60, 65),     # Charcoal
        (100, 100, 105),  # Dark gray
        (160, 160, 165),  # Gray
        (210, 210, 215),  # Light gray
    ]
}

NOIR = {
    'name': 'Noir',
    'bg': (15, 15, 18),
    'colors': [
        (35, 35, 40),     # Dark gray
        (75, 75, 80),     # Medium gray
        (130, 130, 135),  # Gray
        (190, 190, 195),  # Light gray
        (240, 240, 245),  # Off-white
    ]
}


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

# List of all available palettes
ALL_PALETTES = [
    OCEAN, FOREST, SUNSET, CHERRY_BLOSSOM,
    VAPOR, RETRO_FUTURE, COMMODORE,
    NEON_NIGHTS, MONDRIAN, BAUHAUS,
    SORBET, LAVENDER_FIELD,
    TERRACOTTA, AUTUMN,
    INK, NOIR
]


def draw_sample_squares(pallet):
    for i in range(len(pallet['colors'])):
        py5.push_style()
        
        py5.fill(*pallet['colors'][i])
        py5.square(150 + (i*100), 50, 75)
        
        # bg
        py5.fill(*pallet['bg'])
        py5.square(20,50,85)
        
        py5.pop_style()

def random_palette():
    """Return a random palette from all available palettes."""
    return random.choice(ALL_PALETTES)


def random_color_from_palette(palette):
    """Return a random color from the given palette's colors list."""
    return random.choice(palette['colors'])


def print_all_palettes():
    """Print all available palette names."""
    print("Available palettes:")
    for palette in ALL_PALETTES:
        print(f"  - {palette['name']}")


def get_palette_by_name(name):
    """
    Get a palette by its name (case-insensitive).
    Returns None if not found.
    """
    name_lower = name.lower()
    for palette in ALL_PALETTES:
        if palette['name'].lower() == name_lower:
            return palette
    return None


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == '__main__':
    # Show all available palettes
    print_all_palettes()
    print()
    
    # Example: Print OCEAN palette details
    print(f"Palette: {OCEAN['name']}")
    print(f"Background: {OCEAN['bg']}")
    print("Colors:")
    for i, color in enumerate(OCEAN['colors'], 1):
        print(f"  {i}. {color}")