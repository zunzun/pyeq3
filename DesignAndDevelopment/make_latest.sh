zip -x "*.pyc" -x "*.svn*" -r pyeq3_latest.zip pyeq3/
tar --exclude=.svn* --exclude=*pyc -czvf pyeq3_latest.tgz pyeq3/
