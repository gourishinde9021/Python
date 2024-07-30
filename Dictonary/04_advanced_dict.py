server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
print(server_config.get("server1"))
print(server_config["server1"]["status"])
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

server = input(str("Enter server name: "))
status = get_server_status(server)
print(f"Status of server {server} is {status}")