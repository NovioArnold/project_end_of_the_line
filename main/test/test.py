import pytest


testfiles = ['test_jobs.py', 'test_industries.py', 'test_router.py']
def main():
    for tests in testfiles:
        pytest.main(['-v', '-x', '-s', tests])

if __name__ == '__main__':
    main()
