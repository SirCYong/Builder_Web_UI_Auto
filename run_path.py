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


def file_path(file_type='xlsx'):
    global new_path
    path = test_report_path()
    if file_type == 'xlsx':
        new_path = os.path.join(path, "xlsx.xlsx")
    elif file_type == 'docx':
        new_path = os.path.join(path, "docx.docx")
    elif file_type == 'pdf':
        new_path = os.path.join(path, "pdf.pdf")
    elif file_type == 'png':
        new_path = os.path.join(path, "png.png")
    elif file_type == 'pptx':
        new_path = os.path.join(path, "pptx.pptx")
    elif file_type == 'zip':
        new_path = os.path.join(path, "zip.zip")
    elif file_type == 'jpg':
        new_path = os.path.join(path, "jpg.jpg")
    elif file_type == '1':
        new_path = os.path.join(path, "1.jpg")
    else:
        print('暂不支持的文件类型')
    return new_path

if __name__ == '__main__':
    a = test_report_path()
    print(a)

