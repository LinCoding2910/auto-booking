*** Settings ***
Library    Browser
Library    timing.py
Suite Setup    Wait Until Booking Opens    ${BOOKING_OPENS_AT}    ${TIMEZONE}

*** Variables ***
${BROWSER}          chromium
${HEADLESS}         False
${LOGIN_URL}        https://www.kotapermaionline.com.my/login.aspx
${MEMBERSHIP_NO}    %{MEMBERSHIP_NO}
${PASSWORD}         %{PASSWORD}
${SPORT}            role=radio[name='Pickleball']
${BOOKING_DATE}     22/Sep/2026
${BOOKING_OPENS_AT}    2026-09-14 16:07
${TIMEZONE}            Asia/Kuala_Lumpur
${TABLE}            Court 2
${TEE_TIME}         8:00 AM
${BOOKING_LIST}     https://www.kotapermaionline.com.my/bookingListfacility.aspx

*** Test Cases ***
Book Table Tennis
    New Browser    ${BROWSER}    headless=${HEADLESS}
    New Context    viewport={'width': 1920, 'height': 1080}
    New Page    ${LOGIN_URL}

    Fill Text    css=#ctl00_cpMain_txtUserName    ${MEMBERSHIP_NO}
    Fill Text    css=#ctl00_cpMain_txtPassword    ${PASSWORD}
    Click        role=link[name='Log On']
    Click        role=link[name='Click Here']
    Switch Page  NEW

    Click         ${SPORT}

    Select Options By    css=#ctl00_cpMain_cboDate        value    ${BOOKING_DATE}
    Select Options By    css=#ctl00_cpMain_cboSession     value    ${TABLE}
    Select Options By    css=#ctl00_cpMain_cboTeeTime     value    ${TEE_TIME}
    Click                role=link[name='Next']
    Click                role=link[name='Next']

    Click    css=#ctl00_cpMain_chkTerm
    Click    role=link[name='Confirm']
