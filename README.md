# Test XVWA Reflected XSS with a list of payloads

## Description:
### Selenium with PyTest program to test XVWA web application for reflected XSS vulnerability.
### Prerequisites
1. pip3 install -U selenium
2. pip3 install -U pytest
3. Have firefox installed
4. Have the geckodriver in your system path https://github.com/mozilla/geckodriver/releases
5. Download and run xvwa in a docker https://github.com/s4n7h0/xvwa ---> https://github.com/tuxotron/xvwa_lamp_container (follow instructions)

Run with: "pytest test_XVWAReflectedXSS.py"

### Demo Gif
![](demo.gif)