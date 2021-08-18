
#!/bin/sh
set -e

source /Users/srikakum/cimservicesautomation/.venv/bin/activate

for ((i=1; i<=50; i=i+1))
do 
      locust --host=https://omservices-orderinfo-temp-ts1.cisco.com --locustfile=tests/load/cg1/locustfile.py --slave &
done