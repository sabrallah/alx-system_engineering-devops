# Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

exec { 'fix-wordpress':
  command => '/bin/sed -i "s/short_open_tag = Off/short_open_tag = On/g" /etc/php5/apache2/php.ini',
  path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  require => Package['apache2'],
}
