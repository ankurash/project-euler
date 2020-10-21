#!/bin/sh

ver=$(python -c"import sys; print(sys.version_info.major)")
ver3=$(python3 -c"import sys; print(sys.version_info.major)")

py="python"

if [ $(python -c"import sys; print(sys.version_info.major)") -eq 3 ]; then
    py="python"
elif [ $(python3 -c"import sys; print(sys.version_info.major)") -eq 3 ]; then
    py="python3"
else
    echo "python3 interpreter not found. Exiting."
    exit
fi

echo "Python3 interpreter: $py"

for pyfile in $(ls *.py)
do
    echo $(eval "$py $pyfile")
done