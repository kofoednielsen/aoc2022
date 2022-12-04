#!/bin/bash
LINES=`cat input.txt`
TOTAL=0
for LINE in $LINES
do
  IFS=',' read -ra ELVES <<< "$LINE"
  IFS='-' read -ra ELF_1 <<< "${ELVES[0]}"
  IFS='-' read -ra ELF_2 <<< "${ELVES[1]}"
  if [ "${ELF_1[0]}" -le "${ELF_2[1]}" ] && [ "${ELF_1[1]}" -ge "${ELF_2[0]}" ]
  then
    ((TOTAL+=1))
  fi
done

echo $TOTAL
