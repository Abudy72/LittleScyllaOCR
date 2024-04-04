from prompt_toolkit.shortcuts import radiolist_dialog

# Define the menu options
menu_items = [
    ("op1", "OCR Both Teams."),
    ("op2", "OCR Single Team."),
]

def main():
    # Create a radiolist dialog
    app = radiolist_dialog(
        title="OCR Menu",
        text="Choose OCR Type:",
        values=menu_items,
    )

    # Wait for the user to select an option
    app.run()

    # Get the selected option
    selected_option = app.selected_values[0] if app.selected_values else None

    if selected_option is not None:
        print(f"You selected: {selected_option}")

if __name__ == "__main__":
    main()