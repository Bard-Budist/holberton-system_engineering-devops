make_puppet_great_again() {
  # Make Binaries Accessible
  for ITEM in /opt/puppetlabs/bin/*; do
    # Skip Bolt if Ubuntu 14.04 to mimick package behavior
    if [[ "$(lsb_release -c -s)" == "trusty" ]]; then
      [[ ${ITEM##*/} == bolt ]] && continue
    fi
    
    # Link to Source
    sudo ln -sf \
      /opt/puppetlabs/puppet/bin/wrapper.sh \
      /usr/local/bin/${ITEM##*/}
  done
}

make_puppet_great_again