class Login:
    def __init__(self, driver):
        self.driver = driver

        self.username_xpath = "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]"
        self.password_xpath = "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]"

        self.login_button_class = "oxd-button"

        self.invalid_message_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"


    def input_username(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
    
    def login_button(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button_class).click()
   
    def invalid_message(self):
        self.driver.find_element(By.XPATH, self.invalid_message_xpath).text