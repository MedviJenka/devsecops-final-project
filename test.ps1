docker run --detach --name nginx-proxy --publish 80:80 --volume /var/run/docker.sock:/tmp/docker.sock:ro nginxproxy/nginx-proxy:1.6
docker run --detach --name your-proxied-app --env VIRTUAL_HOST=foo.bar.com nginx
