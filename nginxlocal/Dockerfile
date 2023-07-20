
FROM nginx:latest

# Install openssl to generate SSL certificates
RUN apt-get update && \
    apt-get install -y openssl && \
    rm -rf /var/lib/apt/lists/*

# Generate a self-signed SSL certificate
RUN mkdir /etc/nginx/ssl && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -subj '/CN=www.mydom.com/O=My Company Name LTD./C=US' \
    -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
