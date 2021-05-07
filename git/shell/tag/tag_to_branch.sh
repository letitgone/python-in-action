cd "${1}";
cd "${2}";
git fetch;
git pull;

# git branch <new-branch-name> <tag-name>
git branch "${3}" "${4}"

git push origin "${3}"
