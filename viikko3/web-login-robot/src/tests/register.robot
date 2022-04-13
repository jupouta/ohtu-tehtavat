*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  kissa
    Set Password  kal123
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kissa
    Set Password  kalle123
    Set Password  kalle456
    Submit Credentials
    Register Should Fail With Message  Password does not match confirmation

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  ka123
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  ka123
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}