#!/bin/bash

OUTFILE="/book/docs/99-reference/pictures.rst"

# Check if we are in Docker container
if [ ! -f /.dockerenv ]; then
  echo "Run in the Docker container!"
  exit 1
fi
# Remove stale out file
if [ -f "${OUTFILE}" ]; then
  rm ${OUTFILE}
fi
# source the global functions
echo ".. include:: ../global.rst" > /book/docs/images/header.rst
# add the title to this section
echo "===============" >> /book/docs/images/header.rst
echo "Picture Credits" >> /book/docs/images/header.rst
echo "===============" >> /book/docs/images/header.rst
echo " " >> /book/docs/images/header.rst
cat /book/docs/images/*.html > /book/docs/images/pics.html
pandoc -t rst -o /book/docs/images/pics.rst /book/docs/images/pics.html
rm /book/docs/images/pics.html
cat /book/docs/images/header.rst /book/docs/images/pics.rst > ${OUTFILE}
rm /book/docs/images/*.rst