# Base Site

[![Build status](https://dev.azure.com/ricardobchaves/Ricardo/_apis/build/status/isabelesite)](https://dev.azure.com/ricardobchaves/Ricardo/_build/latest?definitionId=4)[![Build Status](https://travis-ci.org/ricardochaves/base_site.svg?branch=master)](https://travis-ci.org/ricardochaves/base_site) [![Coverage Status](https://coveralls.io/repos/github/ricardochaves/base_site/badge.svg)](https://coveralls.io/github/ricardochaves/base_site) [![Maintainability](https://api.codeclimate.com/v1/badges/950aa9850083739cf9cd/maintainability)](https://codeclimate.com/github/ricardochaves/base_site/maintainability) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/911740aaaaf441a7a45cc45d8ce200a9)](https://www.codacy.com/app/ricardochaves/base_site?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ricardochaves/base_site&amp;utm_campaign=Badge_Grade) [![Issue Stats](http://issuestats.com/github/ricardochaves/base_site/badge/pr)](http://issuestats.com/github/ricardochaves/base_site) [![Issue Stats](http://issuestats.com/github/ricardochaves/base_site/badge/issue?style=flat-square)](http://issuestats.com/github/ricardochaves/base_site) [![Updates](https://pyup.io/repos/github/ricardochaves/base_site/shield.svg)](https://pyup.io/repos/github/ricardochaves/base_site/) [![Python 3](https://pyup.io/repos/github/ricardochaves/base_site/python-3-shield.svg)](https://pyup.io/repos/github/ricardochaves/base_site/)

A skeleton with Django and Docker

## Execute

Clone the project

```
git clone https://github.com/ricardochaves/base_site.git
```

Go to `base_site` dir

```
cd base_site
```

Execute the `docker-compose.yml`

```
docker-compose up
```

Acess `localhost:5005`

## Tips

### Docker

https://blog.sneawo.com/blog/2017/09/07/how-to-install-pillow-psycopg-pylibmc-packages-in-pythonalpine-image/

### CKEditor

The project uses CKEditor using the [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) package



upstream isabele_app_server {
  server unix:/var/www/isabele/run/gunicorn.sock fail_timeout=0;
}
server {
    listen 80;
    server_name isabelelucchesi.com;
    return 301 $scheme://www.isabelelucchesi.com$request_uri;
}
server {
    listen 80;
    server_name www.isabelelucchesi.com;
    client_max_body_size 3m;
    access_log /var/www/isabele/logs/nginx-access.log;
    error_log /var/www/isabele/logs/nginx-error.log;
location /static/ {
        autoindex off;
        alias /var/www/isabele/static/;
    }
location /media/ {
        autoindex off;
        alias /var/www/isabele/media/;
    }
location / {
        try_files $uri @isabele_backend;
    }
location @isabele_backend {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass http://isabele_app_server;
    }
}



scp manage.py root@104.237.5.105:/var/www/isabele/
scp requirements.txt root@104.237.5.105:/var/www/isabele/
scp SiteIsabele-0cf6ea54da5e.json root@104.237.5.105:/var/www/isabele/
scp -r base_site root@104.237.5.105:/var/www/isabele/
scp -r mainapp root@104.237.5.105:/var/www/isabele/

