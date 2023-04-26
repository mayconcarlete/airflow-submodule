from simple_term_menu import TerminalMenu

options = ["Andrew", "Louis", "Exit"]

terminal_menu = TerminalMenu(options)

menu_entry_index = terminal_menu.show()

print("Index: ", menu_entry_index)