cd "${1}"
cd "${2}"
git fetch
git checkout "${3}"
git pull
git tag "${4}"
git push origin "${4}"

git branch <new-branch-name> <tag-name>
git branch "${5}" "${4}"
git push origin "${5}"