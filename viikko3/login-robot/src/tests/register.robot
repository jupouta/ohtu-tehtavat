*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  kissa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle456
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  un  kalle456
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  kissa  katt123
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kissa  kattkisse
    Output Should Contain  Password should contain numbers

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command