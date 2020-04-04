# Puppet

exec { 'HTTP_puppet':
  command  => "sudo apt-get -y update && sudo apt-get -y install nginx && sudo echo 'Holberton School' | sudo tee /var/www/html/index.html && sed -i '/sendfile on;/a add_header X-Served-By $HOSTNAME;' /etc/nginx/nginx.conf && sudo service nginx restart",
  provider => 'shell',
}
