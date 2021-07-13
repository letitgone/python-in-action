cd /Users/zhanggj/Downloads/idea-project/wake-starter/"${1}"

mvn clean -P "${2}"
mvn deploy -P "${2}"
