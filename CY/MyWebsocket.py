from websocket import create_connection

worker_not_exist_name = '18205010265'
test_pass = '123456'


def builder_base_api():
    ws = create_connection("ws://%s/wsapi" % ('perftest.zlddata.cn'))
    yield BuilderBaseFunc(ws, conf_testdomain)  # provide the fixture value
    print("teardown websocket")
    ws.close()


def test_worker_register(builder_base_api):
    # param_required_list = ['username', 'password', 'code']
    bbf = builder_base_api
    command = "WorkerRegister"
    # test register without sending request for code
    parameter = gen_parameter(
        username=worker_not_exist_name, password=test_pass)
    resp = bbf.request(get_requestDict(command, parameter))
    assert (resp['code'] == 2115 and resp['detail'])
    # test sending code but input error code
    parameter = gen_parameter(
        username=worker_not_exist_name, password=test_pass, code='1111')
    resp = bbf.RegPhoneVerifyCode(parameter)
    assert (resp['code'] == 1000 and resp['msg'] == u"成功:发送注册验证码")
    resp = bbf.request(get_requestDict(command, parameter))
    assert resp['code'] == 2108
    # test password length <4
    parameter = gen_parameter(
        username=worker_not_exist_name, password='1234', code='11111')
    resp = bbf.request(get_requestDict(command, parameter))
    assert (resp['code'] == 2115 and resp['detail'])



def gen_parameter(**kw):
    parameter = {}
    param = kw
    if len(param) == 0:
        return parameter
    for k, v in param.items():
        parameter[k] = v
    return parameter

conf_apiconfig = {
                  # "SearchProject": "employee.consumer.", "LeaveRecordList": "project.consumer.",
                  # "SearchWorker": "employer.consumer.", "ProjectAreaAddUpdate": "project.consumer.",
                  # "LocationCardUpdate": "employer.consumer.", "WorkerBankNoList": "employee.consumer.",
                  # "WorkCertificateUpdate": "employee.consumer.", "AttendResultTeamStatList": "operation.consumer.",
                  # "WorkTimePayList": "project.consumer.", "AttendanceMachineAllowUserList": "project.consumer.",
                  # "WorkExperienceDelete": "employee.consumer.", "GateUpdate": "employer.consumer.",
                  # "WorkExperienceAdd": "employee.consumer.", "RealTimePeopleNum": "operation.consumer.",
                  # "WorkerDetailList": "employee.consumer.", "WorkerBankNoAdd": "employee.consumer.",
                  # "AttendanceCardAdd": "employer.consumer.", "RegPhoneVerifyCode": "employee.consumer.",
                  # "ProcessCreate": "workflow.consumer.", "SearchCompany": "employer.consumer.",
                  # "WorkExperienceList": "employee.consumer.", "CompanyUpdate": "employer.consumer.",
                  # "ListHisLoc": "project.consumer.", "GenAttendanceResult": "workflow.consumer.",
                  # "IPCameraList": "employer.consumer.", "ProjectAreaDelete": "project.consumer.",
                  # "HeartBeat": "operation.consumer.", "AttendanceMachineAdd": "project.consumer.",
                  "EmployeeRegister": "employee.consumer.", "CompanyQualificationUpdate": "employer.consumer.",
                  "EducationAdd": "employee.consumer.", "CompanyAdd": "employer.consumer.",
                  "PayBillList": "project.consumer.", "TimePayStatistics": "operation.consumer.",
                  "ProjectList": "employer.consumer.", "RequestList": "workflow.consumer.",
                  "WorkerBankNoDelete": "employee.consumer.", "CompanyQualificationAdd": "employer.consumer.",
                  "AttendResultList": "project.consumer.", "RequestCancel": "workflow.consumer.",
                  "TeamUpdate": "project.consumer.", "TaskUpdate": "workflow.consumer.",
                  "WorkerDetailUpdate": "employee.consumer.", "ProjectAreaList": "project.consumer.",
                  "SetUserGroup": "employer.consumer.", "AttendanceInstantList": "project.consumer.",
                  "IPCameraUpdate": "employer.consumer.", "AmendAttendRecordList": "project.consumer.",
                  "IPCameraDelete": "employer.consumer.", "PeopleNumPerDay": "operation.consumer.",
                  "PaySalary": "project.consumer.", "LocationCardAdd": "employer.consumer.",
                  "SubScribeAttendNotify": "operation.consumer.", "LocationCardDelete": "employer.consumer.",
                  "WorkCertificateDelete": "employee.consumer.", "WorkExperienceUpdate": "employee.consumer.",
                  "AttendanceMachineList": "project.consumer.", "LawList": "employer.consumer.",
                  "ResetPWPhoneVerifyCode": "employee.consumer.", "WorkPieceList": "project.consumer.",
                  "TeamList": "project.consumer.", "WorkCertificateCreate": "employee.consumer.",
                  "PiecePayStatistics": "operation.consumer.", "ResetPassword": "employee.consumer.",
                  "GenProjectPayBill": "project.consumer.", "PrimeContractList": "employer.consumer.",
                  "EducationList": "employee.consumer.", "GateList": "employer.consumer.",
                  "WorkOvertimeRecordList": "project.consumer.", "ProjectPayProcessList": "project.consumer.",
                  "Logout": "employee.consumer.", "AreaLocValidHour": "project.consumer.",
                  "AttendanceCardDelete": "employer.consumer.", "ProjectManagerUpdate": "employer.consumer.",
                  "TeamAdd": "project.consumer.", "ProjectDeviceUnbind": "project.consumer.",
                  "PersonalIdUpdate": "employee.consumer.", "HomeInfoList": "employee.consumer.",
                  "PrimeContractPriceList": "employer.consumer.", "NationalityList": "employee.consumer.",
                  "PayProcessList": "project.consumer.", "PersonalIdList": "employee.consumer.",
                  "WorkerContractList": "project.consumer.", "IPCameraAdd": "employer.consumer.",
                  "CompanyQualificationDelete": "employer.consumer.", "CompanyUserList": "employer.consumer.",
                  "CompanyList": "employer.consumer.", "CompanyQualificationList": "employer.consumer.",
                  "CompanyBankNoUpdate": "employer.consumer.", "EducationDelete": "employee.consumer.",
                  "GateDelete": "employer.consumer.", "AttendanceInstantAdd": "project.consumer.",
                  "WorkCertificateList": "employee.consumer.", "EducationUpdate": "employee.consumer.",
                  "AttendanceMachineUpdate": "project.consumer.", "TeamDelete": "project.consumer.",
                  "GroupsList": "employee.consumer.", "WorkerRegister": "employee.consumer.",
                  "HomeInfoUpdate": "employee.consumer.", "ProjectPayBillList": "project.consumer.",
                  "CompanyDelete": "employer.consumer.", "LocationCardList": "employer.consumer.",
                  "AttendanceCardUpdate": "employer.consumer.", "GateAdd": "employer.consumer.",
                  "PrimeContractDelete": "employer.consumer.", "Login": "employee.consumer.",
                  "AttendanceMachineAuthentication": "project.consumer.",
                  "AttendanceMachineLogout": "project.consumer.", "SubContractList": "employer.consumer.",
                  "MyCompanyContractList": "employer.consumer.", "ProjectApprovalNoList": "employer.consumer.",
                  "AttendanceCardList": "employer.consumer.", "WorkTypeList": "employee.consumer.",
                  "AttendResultConfirm": "project.consumer.", "WorkerDelete": "employee.consumer."}


def get_requestDict(command, parameters):
    requestDict = {"command": {"path": conf_apiconfig[command] + command}, "parameters": parameters}
    return requestDict


if __name__ == 'main':
    parameter = gen_parameter(
        username=worker_not_exist_name, password=test_pass)
    # test_worker_register()
    a = get_requestDict('WorkerRegister', parameter)
