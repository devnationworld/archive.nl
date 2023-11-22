# archive.nl-
An auto-generated web landing page for Developer Nation newsletter send-outs which can also be adapted to create an archive page for any newsletter. 

## Usage 

- Using Docker : 
```docker run -p 5000:5000 iayanpahwa/archive.nl:latest-amd64```

- Using docker-compose :
```
version: '3'
services:
  archive-nl:
    container_name: archive-nl
    image: iayanpahwa/archive.nl:latest-amd64
    ports:
      - 5000:5000
    environment:
      - PUID=1000
      - PGID=1000
    restart: unless-stopped
    network_mode: host
```
