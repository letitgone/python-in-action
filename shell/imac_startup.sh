cd /Users/zhanggj/Downloads/development-environment/nacos/bin
sh startup.sh -m standalone
cd /Users/zhanggj/Downloads/development-environment/redis-6.0.6/
./bin/redis-server etc/redis.conf
cd /Users/zhanggj/Downloads/development-environment/seata/
sh bin/seata-server.sh -p 8002 -h ${1} -m db -n 1 &
cd /Users/zhanggj/Downloads/development-environment/rocketmq-all-4.5.2-bin-release/
nohup sh bin/mqnamesrv &
nohup sh bin/mqbroker -n localhost:9876 &
