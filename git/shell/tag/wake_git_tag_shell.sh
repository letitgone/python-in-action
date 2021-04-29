cd /Users/zhanggj/Downloads/idea-project/wake-starter/"${1}"
git fetch
git checkout "${2}"
git pull
git tag "${3}"
git push origin "${3}"
