import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")
print("Please scan the QR code within 20 seconds.")
time.sleep(20)


def find_and_send_keys(xpath, keys):
    time.sleep(2)  # Wait for element to be interactable
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(keys)
    return element

def send_message_to_contact(name, message):
    # Search for the contact
    search_box = find_and_send_keys('//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]', name + Keys.ENTER)
    time.sleep(2)  # Wait for search results
    
    # Send the message
    message_box = find_and_send_keys('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]', message)
    send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    time.sleep(1)  # Wait for message to send

def send_messages_to_multiple_contacts(contacts, message):
    for contact in contacts:
        try:
            send_message_to_contact(contact, message)
            print(f"Message sent to {contact}")
        except Exception as e:
            print(f"Failed to send message to {contact}. Error: {str(e)}")

# List of contacts to send messages to
contacts = ["Prashant", "hrithik", "carino", "Kunal"]  # Add more contacts as needed

# Message to send
message = "Hi! This is a Python automated message."

# Send messages to multiple contacts
send_messages_to_multiple_contacts(contacts, message)

print("All messages sent. Press Enter to exit.")
input()

driver.quit()