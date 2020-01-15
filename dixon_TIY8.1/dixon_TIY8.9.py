mess = ['lol', 'rofl', 'jk', 'tyl']
def show_messages(list):
    for message in list:
        print(f"Sent message: {message.title()}")
    print(list)


show_messages(mess)
