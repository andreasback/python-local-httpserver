# $0 contains the path and filename of the running program
# dirname will return the path only
echo $0
SCRIPT_DIR=$(dirname $0)

# change into the directory of where this script was run from so that we can reference
# the src folder and the python program can find the www folder to serve content from
cd $SCRIPT_DIR
python3 ./src/python-localhost-server.py
