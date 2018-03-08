.PHONY: docs

docs:
	mkdir -p docs
	pydoc -w `find src -name '*.py'`
	mv *.html docs

deploy:
	pytest --pep8
	mkdir -p docs
	pydoc -w `find src -name '*.py'`
	mv *.html docs

env:
	virtualenv -p python3 optgame-env
	source optgame-env/bin/activate

clean:
	rm -rf dist build optgame-env
