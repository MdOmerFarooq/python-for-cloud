# Using Variables to Store and Manipulate Configuration Data in a DevOps Context

# Defining configuration variables for a web server
name = "server"
port = 80
https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {https_enabled}")
print(f"Max Connections: {max_connections}")

# Update configuration values
port = 443
https_enabled = False

# Print the updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {https_enabled}")