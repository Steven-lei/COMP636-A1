# ============== Te Māra Kiwi - Orchard Management System (OMS) ==============
# Student Name: 
# Student ID : 
# ============================================================================

# Complete the functions in this file. 
# Do not delete or rename the supplied menu functions, or change the menu numbering or function calls. 
# You may create your own helper functions.


from datetime import date, datetime

from orchard_data import ( display_formatted_row, blocks, contacts, harvest_history,)


# Use these supplied parameter values in your functions.
# Do not change these constants or the entries in the threshold dictionary.
FIRST_HARVEST_YEAR = 2015      # Earliest permitted harvest record year.
LATEST_HARVEST_YEAR = 2026     # Latest permitted and summary-report year.
MIN_HARVEST_TONNES = 0.001     # Minimum tonnes for ONE recorded batch.
MAX_HARVEST_TONNES = 200.0     # Maximum tonnes for ONE annual harvest record.
LOW_YIELD_TONNES_HA = {
    "Green": 23.0,
    "Gold": 33.5,
    "Red": 16.5,
}

# Helper function to search a contact by name
def find_orchard_contact(contact_name):
    """Return a contact matched by name, or None if no match exists.

    The supplied contact directory has one row per name. A missing contact
    must not cause the block listing or follow-up report to crash.
    """
    for contact in contacts:
        if contact["name"] == contact_name:
            return contact
    return None


# ------------------------ Additional functions -------------------------
# Add helper functions here.


# ---------------------------- Menu functions ----------------------------

def list_orchard_blocks():
    """Show all blocks in ID order and their separately stored contacts."""
    print("\nORCHARD BLOCKS")

    if not blocks:
        print("No orchard blocks are available.")
        return

    ordered_blocks = sorted(blocks, key=lambda block: block["block_id"])

    # Keep the listing readable by using one table for block details and
    # another for the contact directory information.
    block_format = "{:<6} {:<8} {:>9} {:>9} {:>11}  {:<22}"
    display_formatted_row(
        ["ID", "Variety", "Area (ha)", "Planted", "Total vines", "Contact name"],
        block_format,
    )
    for block in ordered_blocks:
        display_formatted_row(
            [
                block["block_id"],
                block["variety"],
                format(block["area_ha"], ".1f"),
                block["planting_year"],
                block["total_vines"],
                block["contact_name"],
            ],
            block_format,
        )

    input("\nPress Enter to return to the menu.")


def block_harvest_history():
    pass  # Replace this line with your own code.


def rank_orchard_harvest_records():
    pass  # Replace this line with your own code.


def add_block_harvest_record():
    pass  # Replace this line with your own code.


def orchard_summary_report():
    pass  # Replace this line with your own code.


# ------------------------------ Main menu ------------------------------

# -------------- DO NOT MAKE CHANGES BELOW THIS POINT --------------


def display_orchard_menu():
    """Display the program menu."""
    print("\n==== TE MĀRA KIWI - ORCHARD MANAGEMENT SYSTEM ====")
    print(f"Harvest history: {FIRST_HARVEST_YEAR}-{LATEST_HARVEST_YEAR} | Summary year: {LATEST_HARVEST_YEAR}")
    print("1 - List Orchard Blocks")
    print("2 - Block Harvest History")
    print("3 - Ranked List of Blocks by Yield")
    print("4 - Add Block Harvest Record")
    print("5 - Summarise Orchard Harvest")
    print("X - Exit")

# -------------- DO NOT MAKE CHANGES TO THE MENU -------------- 

def run_orchard_program():
    """Run the menu until the user chooses to quit."""
    menu_choice = ""

    while menu_choice != "X":
        display_orchard_menu()
        menu_choice = input("Select an option: ").strip().upper()

        if menu_choice == "1":
            list_orchard_blocks()
        elif menu_choice == "2":
            block_harvest_history()
        elif menu_choice == "3":
            rank_orchard_harvest_records()
        elif menu_choice == "4":
            add_block_harvest_record()
        elif menu_choice == "5":
            orchard_summary_report()
        elif menu_choice != "X":
            print("Select an option from 1 to 5, or X to exit.")

run_orchard_program()
print("\n=== Thank you for using the TE MĀRA KIWI - ORCHARD MANAGEMENT SYSTEM! ===\n")

