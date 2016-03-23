PlanetJogger
========
This is set of files (config files, templates, etc.) used to create PlanetJogger - a feed
agregator of blogs that once was hosted on blog site jogger.pl.

Requirements
---------
* working web server (apache/lighttpd/nginx)
* Linux with shell access
* Planet Venus installed (planet-venus package in Debian, tested with 0~git9de2109-3 version and Debian Jessie)
* xsltproc installed

Rules
---------
* in general, blogs are named after original name on Jogger platform (BLOGNAME.jogger.pl becomes BLOGNAME)
* when possible, HTTPS should be used to grab the feed
* if multiple feeds are available, full feed with articles should be chosen
* please send changes as pull requests
* this is test version, so please assume it will be published to /var/www/planetjogger and hosted on https://zakr.es/planetajoggera during tests

Files
---------
* planet-jogger.ini - planet config file
* index.html.tmpl - main page template file
* atom.xml.xslt - original file from planet venus is used

Usage
---------
* clone this repository
* adjust config file (look for CHANGME)
* run planet planet-jogger.ini and observe the output
