# Fixing Apache

exec { 'typo in wp-settings.php':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
