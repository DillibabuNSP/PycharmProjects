from random import randint


class Action:
    def enterTextValue(self, element, text):
        flag = False
        try:
            flag = element.is_displayed()
            element.clear()
            element.send_keys(text)
            print("Entered text :" + text)
            flag = True
        except Exception:
            print("Location Not found")
            flag = False
        # finally:
        #     if flag:
        #         print("Successfully entered value")
        #     else:
        #         print("Unable to enter value")
        return flag

    def elementToClick(self, locator):
        flag = False
        try:
            locator.click()
            flag = True
            return True
        except Exception as e:
            return False
        # finally:
        #     if flag:
        #         print("Able to click on")
        #     else:
        #         print("Unable to click on")

    def launchUrl(self, driver, url):
        flag = False
        try:
            driver.navigate().to(url)
            flag = True
            return True
        except Exception as e:
            return False

    # split elements in a list
    def split(self,arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs
