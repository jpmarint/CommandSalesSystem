clients='pablo,ricardo,'

def create_client(client_name):
    global clients
    clients += client_name
    _add_comma()

def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','

def _print_welcome():
    print('WELCOME TO JuanPa Sales')
    print('*' * 50) 
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')



if __name__ == '__main__':
    _print_welcome()
    command = input().upper()
    if command == "C":
        clientName = input("What is the cliente name? ")
        create_client(clientName)
        list_clients()
    elif command == "D":
        pass
    else:
        print('Invalid command')
