file { '/etc/default/nginx':
    ensure  => 'present',
    replace => 'yes',
    content => 'ULIMIT="-n 4096"',
    mode    => '0644',
  }
