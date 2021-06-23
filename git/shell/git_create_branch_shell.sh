cd "${1}"
cd "${2}"
git fetch
git pull
git checkout -b "${4}" origin/"${3}"
git push origin "${4}"
