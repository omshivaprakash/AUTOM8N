#!/bin/bash

if [ -x /usr/sbin/lvectl ] ; then
  /usr/sbin/lvectl apply all
fi
