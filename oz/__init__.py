"""
Class for automated operating system installation.

Oz is a set of classes to do automated operating system installation.  It
has built-in knowledge of the proper things to do for each of the supported
operating systems, so the data that the user must provide is very minimal.
This data is supplied in the form of an XML document that describes what
type of operating system is to be installed and where to get the
installation media.  Oz handles the rest.

The simplest Oz program (without error handling or any advanced features)
would look something like:

import oz.TDL
import oz.GuestFactory

tdl_xml = \"\"\"
<template>
  <name>rhel9_s390x</name>
  <os>
    <name>RHEL</name>
    <version>9</version>
    <arch>s390x</arch>
    <install type='iso'>
      <iso>https://mirror.stream.centos.org/9-stream/BaseOS/s390x/iso/CentOS-Stream-9-latest-s390x-dvd1.iso</iso>
    </install>
  </os>
  <description>RHEL 9 for s390x</description>
</template>
\"\"\"

tdl = oz.TDL.TDL(tdl_xml)
guest = oz.GuestFactory.guest_factory(tdl, None, None)
guest.generate_install_media()
guest.generate_diskimage()
guest.install()
"""
