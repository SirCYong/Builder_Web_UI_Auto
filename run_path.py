import os


def run_path():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    case_path = os.path.join(cur_path, "TestCase\\Web")
    return case_path


def test_report_path():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    case_path = os.path.join(cur_path, "Page\\file")
    return case_path


def setting_path():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    case_path = os.path.join(cur_path, "TestCase\\Web\\setting.ini")
    return case_path

if __name__ == '__main__':
    test_report_path()