# Increases open file descriptors that a worker process can have

# Increase the ULIMIT
exec { 'fix--for-nginx':
  command => '/usr/local/bin/sed -i "s/15/4096/" /etc/default/nginx ; /usr/sbin/service nginx restart',
}
