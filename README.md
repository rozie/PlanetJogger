PlanetJogger
========
This is set of files (config files, templates, etc.) used to create PlanetJogger - a feed
agregator of blogs that once were hosted on blog site jogger.pl.
Test version is avaliable at https://zakr.es/planetjogger/


Requirements
---------
* working web server (apache/lighttpd/nginx)
* [nanoplanet](https://github.com/rozie/nanoplanet)

Rules
---------
* in general, blogs are named after original name on Jogger platform (BLOGNAME.jogger.pl becomes BLOGNAME)
* when possible, HTTPS should be used to grab the feed
* if multiple feeds are available, full feed with articles should be chosen
* please send changes as pull requests

Files
---------
* planetconfig.yaml- planet config file
* index.html.tmpl - main page template file
* about.html.tmpl - about page template file

Usage
---------
* clone this repository
* adjust config file (look for CHANGME)
* run nanoplanet

How to commit
---------
* Fork repo on GitHub 
* Comment your changes 
* Send pull request
* Use only upsteam Planet Venus engine (no changes in engine files!)
* Stick to standards and minimal browser requirements (use HTML & CSS, avoid JS)

Old version
---------
Old version used Planet Venus, all files are located in old_planet_venus directory.