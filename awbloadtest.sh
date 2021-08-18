
#!/bin/sh
set -e

source /Users/srikakum/cimservicesautomation/.venv/bin/activate

for ((i=1; i<=50; i=i+1))
do 
      locust --host=https://ibpm-stage.cisco.com/cpe/csa/login --locustfile=tests/load/awb/locustfile.py --slave &
done