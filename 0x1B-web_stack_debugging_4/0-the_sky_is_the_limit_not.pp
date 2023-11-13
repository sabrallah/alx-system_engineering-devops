# Puppet manifest to fix failed requests issue in Nginx

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable Nginx default site
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
