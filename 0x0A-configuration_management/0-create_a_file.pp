#creating a file in /tmp using puppet  with content I love Puppet
# persmittion '0744'
# ownder 'www-data'
# group 'www-data

file { 'school':
  path    => '/tmp/school',
  mode    => '0744',
  recurse => false,
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
