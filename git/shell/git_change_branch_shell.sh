# shellcheck disable=SC2164
cd "${1}"
# shellcheck disable=SC2164
cd "${2}"
git fetch
git checkout "${3}"
git pull
