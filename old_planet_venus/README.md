PlanetJogger
========
This is set of files (config files, templates, etc.) used to create PlanetJogger - a feed
agregator of blogs that once were hosted on blog site jogger.pl.
Test version is avaliable at https://zakr.es/planetjogger/


Requirements
---------
* working web server (apache/lighttpd/nginx)
* Linux with shell access (tested with Debian Buster)
* Planet Venus https://github.com/rubys/venus installed (planet-venus package in Debian, tested with 0~git9de2109-3 version and Debian Jessie)
* xsltproc installed

Rules
---------
* in general, blogs are named after original name on Jogger platform (BLOGNAME.jogger.pl becomes BLOGNAME)
* when possible, HTTPS should be used to grab the feed
* if multiple feeds are available, full feed with articles should be chosen
* please send changes as pull requests
* this is test version, so please assume it will be published to /var/www/planetjogger and hosted on https://zakr.es/planetjogger/ during tests

Files
---------
* planet-jogger.ini - planet config file
* index.html.tmpl - main page template file
* js_index.html.tmpl - template file with JS to shorten visible part of articles (use this one or the one above)
* atom.xml.xslt - original file from planet venus is used
* jogger_migration.txt - file with data about old Jogger blogs and new ones
* make_ini.pl - helper to generate .ini file in alphabetical order (perl make_ini.pl < jogger_migration.txt)
* Dockrefile - helper to create test environment with Docker
* jogger_logo_mini.png - minified Jogger's logo to use on planet
* joggerpl-logo.png - original Jogger's logo used in header (license unknown)

Usage
---------
* clone this repository
* adjust config file (look for CHANGME)
* run planet planet-jogger.ini and observe the output

How to commit
---------
* Fork repo on GitHub 
* Comment your changes 
* Send pull request
* Use only upsteam Planet Venus engine (no changes in engine files!)
* Stick to standards and minimal browser requirements (use HTML & CSS, avoid JS)
