"""Te Māra Kiwi primary orchard data for the 2015-2026 harvest history teaching assessment.

The orchard has 9 blocks (4 Green, 4 Gold, 1 Red). Blocks are one dictionary per row. Each block has a contact_name that
matches one unique name in the separate contacts list.
Harvest records are (block_id, date, annual_tonnes, entered_by) tuples; at most one record per block per year.
Every block has one annual harvest total in each year 2024-2026; records from 2015-2019 are intentionally incomplete.
All contact details are fictional; missing phone numbers use None.
"""

from datetime import date


blocks = [
    {"block_id": "K01", "variety": "Green", "area_ha": 3.2, "planting_year": 2004, "total_vines": 3200, "contact_name": "Keira Ashford"},
    {"block_id": "K02", "variety": "Green", "area_ha": 4.5, "planting_year": 2005, "total_vines": 4500, "contact_name": "Daphne Whitlock"},
    {"block_id": "K03", "variety": "Green", "area_ha": 2.8, "planting_year": 2005, "total_vines": 2800, "contact_name": "Lachlan Mercer"},
    {"block_id": "K04", "variety": "Green", "area_ha": 3.7, "planting_year": 2006, "total_vines": 3700, "contact_name": "Bianca Calder"},
    {"block_id": "G01", "variety": "Gold", "area_ha": 3.8, "planting_year": 2004, "total_vines": 3800, "contact_name": "Gideon Marsh"},
    {"block_id": "G02", "variety": "Gold", "area_ha": 4.6, "planting_year": 2005, "total_vines": 4600, "contact_name": "Freya Beaumont"},
    {"block_id": "G04", "variety": "Gold", "area_ha": 4.2, "planting_year": 2006, "total_vines": 4200, "contact_name": "Jasper Holloway"},
    {"block_id": "G05", "variety": "Gold", "area_ha": 3.5, "planting_year": 2006, "total_vines": 3500, "contact_name": "Keira Ashford"},
    {"block_id": "R01", "variety": "Red", "area_ha": 3.3, "planting_year": 2006, "total_vines": 3300, "contact_name": "Freya Beaumont"},
]


contacts = [
    {"name": "Keira Ashford", "contact_email": "keira.ashford@kiwiorchard.org", "contact_phone": "021 555 0142"},
    {"name": "Daphne Whitlock", "contact_email": "daphne.whitlock@gmail.com", "contact_phone": "027 555 0198"},
    {"name": "Lachlan Mercer", "contact_email": "lachlan.mercer@hotmail.com", "contact_phone": "03 325 2811"},
    {"name": "Bianca Calder", "contact_email": "bianca.calder@fultoncontracting.co.nz", "contact_phone": "022 555 0746"},
    {"name": "Gideon Marsh", "contact_email": "gideon.marsh@hotmail.com", "contact_phone": "027 555 2841"},
    {"name": "Freya Beaumont", "contact_email": "freya.beaumont@kiwiorchard.org", "contact_phone": "021 555 0385"},
    {"name": "Jasper Holloway", "contact_email": "jasper.holloway@fultoncontracting.co.nz", "contact_phone": "03 325 4176"},
]


# (block_id, harvest_date, batch_tonnes, entered_by)
harvest_history = [
    ("G01", date(2015, 4, 14), 145.122, "Callum Sutherland"),
    ("G02", date(2016, 4, 13), 175.674, "Callum Sutherland"),
    ("K01", date(2017, 4, 14), 66.976, "Gideon Marsh"),
    ("G04", date(2018, 4, 17), 160.398, "Freya Beaumont"),
    ("K02", date(2018, 4, 17), 117.99, "Elliot Fraser"),
    ("G05", date(2019, 4, 18), 133.665, "Elliot Fraser"),
    ("R01", date(2024, 3, 20), 63.162, "Callum Sutherland"),
    ("K03", date(2024, 4, 12), 72.45, "Gideon Marsh"),
    ("K02", date(2024, 4, 14), 83.835, "Daphne Whitlock"),
    ("G05", date(2024, 4, 17), 131.906, "Lachlan Mercer"),
    ("K04", date(2024, 4, 20), 98.716, "Callum Sutherland"),
    ("G04", date(2024, 4, 21), 153.363, "Jasper Holloway"),
    ("G01", date(2024, 4, 23), 112.66, "Freya Beaumont"),
    ("G02", date(2024, 4, 26), 189.543, "Gideon Marsh"),
    ("K01", date(2024, 4, 26), 90.528, "Keira Ashford"),
    ("R01", date(2025, 3, 21), 48.188, "Callum Sutherland"),
    ("G02", date(2025, 4, 12), 167.969, "Gideon Marsh"),
    ("K01", date(2025, 4, 12), 80.224, "Keira Ashford"),
    ("G04", date(2025, 4, 15), 117.485, "Daphne Whitlock"),
    ("K02", date(2025, 4, 15), 116.438, "Daphne Whitlock"),
    ("K04", date(2025, 4, 15), 101.695, "Elliot Fraser"),
    ("K03", date(2025, 4, 18), 74.704, "Keira Ashford"),
    ("G05", date(2025, 4, 22), 136.01, "Keira Ashford"),
    ("G01", date(2025, 4, 24), 156.579, "Freya Beaumont"),
    ("R01", date(2026, 3, 19), 66.973, "Callum Sutherland"),
    ("G02", date(2026, 4, 17), 173.362, "Gideon Marsh"),
    ("G01", date(2026, 4, 20), 138.757, "Freya Beaumont"),
    ("K03", date(2026, 4, 20), 56.994, "Keira Ashford"),
    ("K01", date(2026, 4, 22), 82.8, "Keira Ashford"),
    ("K02", date(2026, 4, 23), 120.06, "Daphne Whitlock"),
    ("G04", date(2026, 4, 25), 163.212, "Daphne Whitlock"),
    ("G05", date(2026, 4, 26), 103.766, "Lachlan Mercer"),
    ("K04", date(2026, 4, 27), 104.673, "Callum Sutherland"),
]


def display_formatted_row(row, format_string):
    """Display one list or tuple as a row of aligned columns.

    row contains the values to display, with one value for each column.
    format_string contains one set of curly braces for each column. For
    example, "{:<10}" creates a column 10 characters wide and pads unused
    positions with spaces.

    The alignment characters are:
        <  left aligned
        ^  centred
        >  right aligned

    This example creates three columns: left aligned and 5 characters wide,
    centred and 10 characters wide, and right aligned and 15 characters wide:
        format_string = "{:<5}  {:^10}  {:>15}"

    Make each column wider than its heading and its widest expected value;
    otherwise, longer text will make the columns appear out of alignment.

    A different padding character and separators can also be included. This
    example pads with full stops and separates the columns with vertical bars:
        format_string = "{:.<5} | {:.^10} | {:.>15}"

    Values are converted to strings for display. A None value is displayed as
    an empty string. 
    """
    # Build a new list of text values to build from each value in row.
    display_values = []

    # Convert each value to text, using an empty string for a missing value.
    for value in row:
        if value is None:
            display_values.append("")
        else:
            display_values.append(str(value))

    # Apply the formatting in format_string to all items in row    
    # * supplies each value to the corresponding set of braces in format_string.
    print(format_string.format(*display_values))
