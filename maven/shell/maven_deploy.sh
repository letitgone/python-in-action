cd /Users/zhanggj/Downloads/idea-project/wake-starter/"${1}"

mvn clean -P dev;
mvn deploy -P dev;
