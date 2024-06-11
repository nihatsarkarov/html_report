import pytest

def pytest_configure(config):
    config._metadata['Project'] = 'Image Editing CLI'
    config._metadata['Tester'] = 'Your Name'

def pytest_html_report_title(report):
    report.title = "Image Editing CLI Test Report"

def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')

def pytest_html_results_table_row(report, cells):
    cells.insert(2, '<td>' + report.description + '</td>')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    docstring = getattr(item.function, '__doc__', None)
    if docstring:
        report.description = docstring.strip()
    else:
        report.description = "No description provided"