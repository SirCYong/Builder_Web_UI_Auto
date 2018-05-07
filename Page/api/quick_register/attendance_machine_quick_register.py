# -*- utf-8
import datetime


def quick_register(ws_driver, sid, identityNum, visitorName, sex, birthday, overdue, identityImage, faceImage, phone_num, characteristic_value):
    '''

    :param sid:
    :param ws_driver:
    :param identityNum:用户身份证号
    :param visitorName:身份证上的名字
    :param sex: 性别 男 or 女
    :param birthday:身份证上的出生日期 例如 1999-1-1
    :param overdue:身份证的过期时间 例如 2008/08/15-2018/08/15
    :param identityImage:身份证上的照片 /tmp/xxx.jpg
    :param faceImage: 人脸照片 /files/b66dd03a-1fa3-45f2-9603-a6284098a413.jpg
    :param characteristic_value: 人脸特征值 random_face_eigenvalues()
    :return:
    '''
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    parameter = {
        "command":
            {
                "path": "employee.consumer.QuickRegister"
            },
        "parameters":
            {
                "flag": 1,
                "sid": sid,
                "identityNum": identityNum,
                "visitorName": visitorName,
                "issuingOrgan": "杭州市富阳公安局",
                "address": "浙江省杭州市城区派出所",
                "sex": sex,
                "nationality": "汉",
                "birthday": birthday,
                "indate": overdue,
                "identityImage": identityImage,
                "createTime": create_time,
                "faceImage": faceImage,
                "phone_num": phone_num,
                "characteristic_value": characteristic_value
            }
    }
    result = ws_driver.web_socket_request(parameter)
    assert result['code'] == 1000
    print(result)
    return result

