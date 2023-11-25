# config ssh

file_line { 'private key only' :
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school'
    match  => '#IdentityFile'
}

file_line { 'refuse password' :
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no'
    match  => '#PasswordAuthentication'
}
