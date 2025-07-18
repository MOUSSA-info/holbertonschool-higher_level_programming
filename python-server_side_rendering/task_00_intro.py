import os

def generate_invitations(template, attendees):
    # Check type of template
    if not isinstance(template, str):
        print("Error: Template is not a string. No output files generated.")
        return
    # Check type and validity of attendees list
    if not isinstance(attendees, list) or any(not isinstance(a, dict) for a in attendees):
        print("Error: Attendees is not a list of dictionaries. No output files generated.")
        return
    # Check for empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    # Check for empty attendees
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # List of placeholders to fill
    placeholders = ['name', 'event_title', 'event_date', 'event_location']

    for idx, attendee in enumerate(attendees, 1):
        # Prepare the replacement dictionary, substituting "N/A" for missing values or None
        replacement = {}
        for key in placeholders:
            value = attendee.get(key)
            if value is None or value == "":
                replacement[key] = "N/A"
            else:
                replacement[key] = str(value)
        # Generate the personalized text
        personalized = template
        for key in placeholders:
            personalized = personalized.replace("{" + key + "}", replacement[key])
        # Generate the file name
        filename = f"output_{idx}.txt"
        # Write to file
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
