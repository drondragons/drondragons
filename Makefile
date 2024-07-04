.PHONY: run install test clean

.DEFAULT_GOAL:=run

run:
	python main.py

REPORT_TITLE="Testing report"

install:
	pip install --requirement requirements.txt

create-allure-dirs:
	mkdir -p allure allure/allure-results allure/allure-report allure/allure-single-report

run-tests:
	pytest --random-order --verbose --clean-alluredir --alluredir=allure/allure-results

generate-report:
	allure --verbose generate allure/allure-results --clean \
	--report-dir allure/allure-report --report-name $(REPORT_TITLE)

generate-single-report:
	allure --verbose generate allure/allure-results --clean \
	--report-dir allure/allure-single-report --report-name $(REPORT_TITLE) --single-file

open-report:
	allure --verbose open allure/allure-report

test: create-allure-dirs run-tests generate-report generate-single-report open-report

clean:
	rm -rf allure/
	rm -rf .pytest_cache/
	find . -name '__pycache__' -exec rm -rf {} + 

# docs:
# 	$(MAKE) -C docs html