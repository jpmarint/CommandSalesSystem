clients='pablo,ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("Client already in the client's list")

def list_clients():
    global clients
    print(clients)


def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(clientName + ',', update_client_name + ',')
    else:
        print("Client is not in the list")

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')

def search_client(client_name) -> bool:
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True

def _add_comma():
    global clients
    clients += ','

def _print_welcome():
    print('WELCOME TO JuanPa Sales')
    print('*' * 50) 
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    return input('What is the client name? ')

if __name__ == '__main__':
    _print_welcome()
    command = input().upper()
    
    match command:
        case "C":
            clientName = _get_client_name()
            create_client(clientName)
            list_clients()
        case "D":
            clientName = _get_client_name()
            delete_client(clientName)
            list_clients()
        case "U":
            clientName = _get_client_name()
            upadatedClientName = input("What is the updated client name? ")
            update_client(clientName, upadatedClientName)
            list_clients()
        case "S":
            clientName = _get_client_name()
            found = search_client(clientName)
            if found:
                print("client is in the client's list")
            else:
                print(f"The client: {clientName} is not in our client's list")
        case _:
            print('Invalid command')

    
