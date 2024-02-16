source bin/activate && make html
git add --all && git commit -m "update" && git push
rm -rf /Volumes/ssa/*
cp -r ./build/html/* /Volumes/ssa/