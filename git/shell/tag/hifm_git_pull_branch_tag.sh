cd /Users/zhanggj/Downloads/idea-project/hifm/"${1}"
git fetch
git pull

# git branch <new-branch-name> <tag-name>
git branch "${3}" "${2}"

git push origin "${3}"
