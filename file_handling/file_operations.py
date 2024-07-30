def update_server_config(file_path, key, value):

    with open(file_path, "r") as file:
        lines = file.readlines()
        print(lines)
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + " = " + value + "\n")
            else:
                file.write(line)

# Path to the server configuration file
server_config_file = "example.conf"
key = "MAX_CONNECTIONS"
new_key = 1000

update_server_config(server_config_file, key, new_key)