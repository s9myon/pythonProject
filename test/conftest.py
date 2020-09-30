import pytest

from application.modules.db.DB import DB

db = DB()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        db.insertTestResult(report.nodeid, report.outcome == 'passed')
        print('123321', report.nodeid, report.outcome)
