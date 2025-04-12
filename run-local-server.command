echo $0
SCRIPT_DIR=$(dirname $0)

cd $SCRIPT_DIR

python3 ${SCRIPT_DIR}/src/python-localhost-server.py
