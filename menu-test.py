import cutie

# if cutie.prompt_yes_or_no("Are you brave enough to continue?"):
    # List of names to select from, including some captions
names = [
    "Choose the Option",
    "Create new monitoring",
    "Run Existing monitoring",
    "Sir Lancelot the Brave",
    "Sir Robin the Not-Quite-So-Brave-as-Sir-Lancelot",
    "Sir Bedevere the Wise",
    "Sir Galahad the Pure",
    "Swedish captions:",
    "Møøse",
]
# Names which are captions and thus not selectable
captions = [0, 2, 7]
# Get the name
name = names[cutie.select(names, caption_indices=captions, selected_index=8)]
print(f"Welcome, {name}")
    # Get an integer greater or equal to 0
    # age = cutie.get_number("What is your age?", min_value=0, allow_float=False)
    # # Get input without showing it being typed
    # quest = cutie.secure_input("What is your quest?")
    # print(f"{name}'s quest (who is {age}) is {quest}.")