#!/bin/sh
echo "Checking if there are java processess that are running with debug enabled."
echo "They are opening remote debug port, which is considered as security incident."
uname -a
date

PROC_WITH_DEBUG=`ps -ef | grep -e "Xdebug" -e "Xrunjdwp" -e "agentlib:jdwp" | grep -v grep`
PROC_WITH_DEBUG_COUNT=`echo ${PROC_WITH_DEBUG} | grep -v "^$" | wc -l`
echo "[debug] PROC_WITH_DEBUG: ${PROC_WITH_DEBUG}"
echo "[debug] PROC_WITH_DEBUG_COUNT: ${PROC_WITH_DEBUG_COUNT}"
if [ "${PROC_WITH_DEBUG_COUNT}" -gt 0 ]; then
  echo "Found processes running with debug enabled: \n ${PROC_WITH_DEBUG}"
  
  echo "Exiting with 1 as this needs to be investigated."
  exit 1
else
  echo "No processes found that are running with debug enabled."
fi
