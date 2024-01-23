# Increase limit of fd user can open

# Increase limit of files user can open
exec { 'configure-os-limits-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/4096/" /etc/security/limits.conf && sed -i "/holberton soft/s/4/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
