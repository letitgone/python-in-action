cd "${1}"
cd "${2}"
git rm -r --cached Dockerfile
git rm -r --cached Release_Dockerfile
git rm -r --cached Dev_Dockerfile
git rm -r --cached Client_Dockerfile
git rm -r --cached Bug_Dockerfile
git rm -r --cached Prod_Dockerfile