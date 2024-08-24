# testing how well our web server setup featuring Nginx
# is doing under pressure
exec { 'fix-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/usr/bin/:/bin/',
}

exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
}
