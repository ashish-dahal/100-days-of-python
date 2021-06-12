# Simple file import export! Nothing to see here.
with open("./Input/Letters/starting_letter.docx", mode="r") as letter_template, open(
    "./Input/Names/invited_names.txt", mode="r"
) as names:
    template_text = letter_template.read()
    name_list = [name.strip() for name in names.readlines()]

    for name in name_list:
        text = template_text.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.docx", mode="w") as new_file:
            new_file.write(text)
