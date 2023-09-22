# Install Flask 2.1.0
package { 'python3-pip':
  ensure => present,
}

package { 'flask':
  ensure => present,
  provider => 'pip3',
  version => '2.1.0',
}
