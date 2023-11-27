#setup nginx with puppet

package {
    'nginx':
    ensure => installed,
}

file {'/var/www/html/index.nginx-debian.html':
    content => 'Hello World!',
}

file_line {'configure redirection':
    path  =>  '/etc/nginx/sites-available/default',
    after =>  'server_name _;',
    line  =>  "\n\tlocation /redirect_me {\n\t\treturn 301 https://youtu.be/S3EVrcNQj0o?si=Ot4UNWLXh6sQ4HbR;\n\t}\n",
}

service {'nginx':
    ensure => running,
}