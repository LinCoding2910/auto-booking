*** Settings ***
Library    Browser
*** Test Cases ***
Open Website 
    New Browser    firefox    headless=False
    New Page    https://www.wikipedia.org
    Sleep    30 seconds
    Take Screenshot
    Close Browser