run:
	python daemon.py conf.json
setup:
	pip install -r requirements.txt
	cp res/conf.json conf.json
	echo "Please edit conf.json with your Twitter and Dota details"
test:
	nosetests
