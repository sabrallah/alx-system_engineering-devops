# Configure SSH client to use school private key
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}

# Disable password authentication for SSH
file_line { 'Disable password authentication':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}
