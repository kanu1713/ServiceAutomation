from subprocess import Popen

processes = []

for counter in range(1):

    #chrome_cmd = 'pytest -svv ./tests/step_defs/pega/test_create_case.py  --html=CIM_Automation_Test_Report.html --self-contained-html'
    #chrome_cmd = 'pytest -vv ./tests/step_defs/pega/test_create_case_attachment.py --html=CIM_Automation_Test_Report.html --self-contained-html'
    #test_create_case_attachment
    #chrome_cmd = 'pytest -svv ./tests/step_defs/pega/test_bulksearchcase.py --html=CIM_Automation_Test_Report.html --self-contained-html'
    #chrome_cmd = 'pytest -svv ./tests/step_defs/savm/test_searchterritory.py'
    #chrome_cmd = 'pytest -svv ./tests/step_defs/csh/test_search_case_ui.py'
    #chrome_cmd = 'pytest -svv ./tests/step_defs/csh/test_create_case_ui.py'
    chrome_cmd = 'pytest -svv ./tests/step_defs/csh/test_create_case_ui_new.py --html=CIM_Automation_Test_Report.html --self-contained-html'
    #chrome_cmd = 'pytest -svv --capture=sys ./tests/step_defs/cg1/test_gettransactions.py'
    #chrome_cmd = 'pytest -svv ./tests/step_defs/pega/test_search_case.py'
    #chrome_cmd = 'pytest -vv --capture=sys ./tests/step_defs/pega/test_create_case.py --html=CIM_Automation_Test_Report.html --self-contained-html'
    #chrome_cmd = 'pytest -svv ./tests/step_defs/awb/test_createcase_ui.py'
    #chrome_cmd = 'pytest -vv --capture=sys ./tests/step_defs/email/test_emailsimulator.py --html=CIM_Automation_Test_Report.html --self-contained-html'
    # chrome_cmd = 'export BROWSER=chrome && SIMPLE_SETTINGS=settings_stage pytest -svv ./tests/step_defs/test_search_case_ui.py --html=CIM_Automation_Test_Report.html --self-contained-html'
    # chrome_cmd = 'export BROWSER=chrome && SIMPLE_SETTINGS=settings_stage pytest -svv ./tests/step_defs/test_create_case.py --html=./Test_Results/CIM_Automation_Test_Report_API.html --self-contained-html'
    # chrome_cmd = 'export BROWSER=chrome && SIMPLE_SETTINGS=settings_stage pytest -vs --html=./Test_Results/CIM_Automation_Test_Report.html --self-contained-html'
    #'pytest --html=CIM_Automation_Test_Report.html --self-contained-html'
    #firefox_cmd = 'export BROWSER=firefox && SIMPLE_SETTINGS=settings_stage pytest'
    #chrome_cmd = 'pytest -vv --capture=sys --html=CIM_Automation_Test_Report.html --self-contained-html'
    #firefox_cmd = 'pytest -vv --capture=sys --html=CIM_Automation_Test_Report.html --self-contained-html'
    processes.append(Popen(chrome_cmd, shell=True))
    #processes.append(Popen(firefox_cmd, shell=True))

for counter in range(1):
    processes[counter].wait()
