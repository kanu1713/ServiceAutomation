
#!/bin/sh
set -e

source /Users/srikakum/cimservicesautomation/.venv/bin/activate

for ((i=1; i<=50; i=i+1))
do 
      locust --host=https://customerservice-stg2.cloudapps.cisco.com --locustfile=tests/load/csh/locustfile.py --slave &
done