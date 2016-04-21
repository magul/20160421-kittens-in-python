FROM ubuntu

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y apache2 python-setuptools libapache2-mod-wsgi

WORKDIR /etc/apache2/sites-available
ADD 000-default.conf .

WORKDIR /var/www/html
ADD kittens.wsgi .
ADD kitten.data .
ADD kitten.color .

RUN service apache2 restart
