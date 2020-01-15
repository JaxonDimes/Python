def send_messages(unsent, sent):
    while unsent:
        current_message = unsent.pop(0)
        print(f"Sending Message: {current_message}")
        sent.append(current_message)


def show_messages(sent):
    print("\nSent messages:")
    for message in sent:
        print(message)


unsent = ['lol', 'rofl', 'jk', 'tyl']
sent = []

send_messages(unsent, sent)
show_messages(sent)

# Here is where the program simply moves the sent back into the unsent, creating "Archived Messages".


def archived_messaged():
    send_messages(sent, unsent)
    print(sent)
    print(unsent)


archived_messaged()
