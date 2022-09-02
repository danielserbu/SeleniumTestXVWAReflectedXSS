import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

webpage = "http://localhost/xvwa/vulnerabilities/reflected_xss"
fileToCheck = "/etc/passwd"

xsspayloads = open('xsspayloads-example', 'r')
payloads = xsspayloads.readlines()

driver = webdriver.Firefox()
@pytest.mark.parametrize("xsspayload", payloads)  #xsspayload from payloads list
def test_xvwa_reflected_xss(xsspayload):
  print("Loading page " + webpage)
  driver.get(webpage)

  sbox = driver.find_element("name", "item")
  print("Sending payload to target field " + xsspayload)
  sbox.send_keys(xsspayload)

  verify = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div/div/button")
  verify.click()
  
  print("Checking if vulnerable..")
  print("If output is included in xsspayload inserted, then we conclude it is vulnerable")
  obj = driver.switch_to.alert
  output = obj.text
  time.sleep(2)
  obj.accept()
  assert output not in xsspayload
  driver.close()
