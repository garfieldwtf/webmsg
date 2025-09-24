# Webmsg - Custom Message Web Server

A lightweight Docker container that displays a customizable message through a beautiful web interface. Perfect for testing deployments, displaying dynamic content, or as a simple web server template.

## Features

- 🎨 **Beautiful UI**: Gradient background with modern card design
- 📱 **Responsive Design**: Works perfectly on desktop and mobile devices
- 🔄 **Auto-refresh**: Refresh button to reload the page
- ⚙️ **Customizable**: Easy message customization via environment variables
- 🐳 **Docker Ready**: Pre-configured for containerized deployment
- 🐍 **Python Powered**: Built on Python's built-in HTTP server

## Quick Start

### Method 1: Using Docker Hub (Recommended)

```bash
docker run -d \
  --name webmsg \
  -p 8080:8080 \
  -e MESSAGE="Welcome to my server!" \
  --restart unless-stopped \
  garfieldwtf/webmsg:latest
```

### Method 2: Using Docker Compose

Create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  webmsg:
    image: garfieldwtf/webmsg:latest
    container_name: webmsg
    ports:
      - "8080:8080"
    environment:
      - MESSAGE="Hello from Docker Compose!"
    restart: unless-stopped
```

Then run:
```bash
docker-compose up -d
```

### Method 3: Building from Source

```bash
# Clone the repository
git clone https://github.com/garfieldwtf/webmsg.git
cd webmsg

# Build the image
docker build -t webmsg .

# Run the container
docker run -d -p 8080:8080 -e MESSAGE="Custom built message!" webmsg
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `MESSAGE` | `"Hello, Docker World!"` | The message displayed on the webpage |

### Ports

| Port | Description |
|------|-------------|
| `8080` | Web server port (configurable via port mapping) |

## Usage Examples

### Basic Usage
```bash
docker run -d -p 8080:8080 garfieldwtf/webmsg
```

### Custom Message
```bash
docker run -d -p 8080:8080 -e MESSAGE="Welcome to Production!" garfieldwtf/webmsg
```

### Different Port Mapping
```bash
docker run -d -p 80:8080 -e MESSAGE="Server Message" garfieldwtf/webmsg
```

### Multiple Instances
```bash
# Instance 1
docker run -d -p 8080:8080 -e MESSAGE="Server 1" --name webmsg-1 garfieldwtf/webmsg

# Instance 2  
docker run -d -p 8081:8080 -e MESSAGE="Server 2" --name webmsg-2 garfieldwtf/webmsg
```

## Building from Source

### Prerequisites
- Docker installed on your system
- Git (for cloning the repository)

### Build Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/garfieldwtf/webmsg.git
   cd webmsg
   ```

2. **Build the Docker image**
   ```bash
   docker build -t webmsg .
   ```

3. **Run the container**
   ```bash
   docker run -d -p 8080:8080 webmsg
   ```

### Project Structure
```
webmsg/
├── Dockerfile          # Docker container definition
├── app.py             # Python web server application
└── README.md          # This file
```

## Accessing the Application

After starting the container, open your web browser and navigate to:

- **Local deployment**: `http://localhost:8080`
- **Remote deployment**: `http://your-server-ip:8080`

## Docker Compose Examples

### Production Setup
```yaml
version: '3.8'
services:
  webmsg:
    image: garfieldwtf/webmsg:latest
    container_name: webmsg-production
    ports:
      - "80:8080"
    environment:
      - MESSAGE="Production Environment"
    restart: always
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.webmsg.rule=Host(`example.com`)"
```

### Development Setup
```yaml
version: '3.8'
services:
  webmsg:
    build: .
    container_name: webmsg-dev
    ports:
      - "8080:8080"
    environment:
      - MESSAGE="Development Server"
    volumes:
      - ./app.py:/app/app.py:ro
    restart: unless-stopped
```

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Use a different port
   docker run -d -p 8081:8080 garfieldwtf/webmsg
   ```

2. **Container exits immediately**
   ```bash
   # Check logs
   docker logs webmsg
   
   # Run in foreground for debugging
   docker run -p 8080:8080 garfieldwtf/webmsg
   ```

3. **Message not updating**
   ```bash
   # Restart container with new environment
   docker stop webmsg
   docker rm webmsg
   docker run -d -p 8080:8080 -e MESSAGE="New Message" garfieldwtf/webmsg
   ```

### Viewing Logs
```bash
docker logs webmsg
```

### Container Management
```bash
# Stop container
docker stop webmsg

# Start container
docker start webmsg

# Remove container
docker rm webmsg

# View running containers
docker ps
```

## Customization

### Modifying the Styling

Edit the `app.py` file to change the CSS styles in the `do_GET` method. The current features include:

- Gradient background (orange to yellow)
- Responsive card layout
- Hover effects on buttons
- Mobile-friendly design

### Adding Features

The Python script uses the standard `http.server` module. You can extend functionality by:

- Adding new routes
- Implementing POST handlers
- Adding authentication
- Connecting to databases

## Security Considerations

- 🔒 The server binds to `0.0.0.0` (all interfaces)
- 🔒 No authentication is implemented by default
- 🔒 Use behind a reverse proxy for production deployments
- 🔒 Consider adding SSL/TLS termination

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Support

If you encounter any problems or have questions, please open an issue on GitHub:  
https://github.com/garfieldwtf/webmsg/issues

## Repository

- **GitHub**: https://github.com/garfieldwtf/webmsg
- **Docker Hub**: `garfieldwtf/webmsg:latest`

---

**Happy coding!** 🚀
