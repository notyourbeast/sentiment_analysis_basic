from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Ask user to enter the Google Maps business URL
place_url = input("Enter the Google Maps URL of the business: ")

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=options)

# Open user-provided Google Maps URL
driver.get(place_url)
time.sleep(5)  # Wait for page to load

# Wait for the reviews section to appear
try:
    scrollable_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.m6QErb.DxyBCb.kA9KIf.dS8AEf"))
    )
except:
    print("Error: Reviews section not found! Check the URL.")
    driver.quit()
    exit()

# Scroll multiple times to load more reviews
for _ in range(5):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
    time.sleep(2)

# Extract reviewers' names, ratings, reviews, and review date & time
reviews_data = []
review_elements = driver.find_elements(By.CSS_SELECTOR, "div.jftiEf")

for element in review_elements:
    try:
        # Extract reviewer name
        reviewer_name = element.find_element(By.CSS_SELECTOR, "div.d4r55").text.strip()
    except:
        reviewer_name = "N/A"

    try:
        # Extract rating (Google uses aria-label for rating)
        rating = element.find_element(By.CSS_SELECTOR, "span.kvMYJc").get_attribute("aria-label")
        rating = rating.split()[0]  # Extract only the numeric value
    except:
        rating = "N/A"

    try:
        # Extract review text
        review_text = element.find_element(By.CSS_SELECTOR, "span.wiI7pd").text.strip()
    except:
        review_text = "N/A"

    try:
        # Extract review date & time
        review_date = element.find_element(By.CSS_SELECTOR, "span.rsqaWe").text.strip()
    except:
        review_date = "N/A"

    # Append data to list
    reviews_data.append([reviewer_name, rating, review_text, review_date])

# Close the driver
driver.quit()

# Save extracted data to CSV
df = pd.DataFrame(reviews_data, columns=["Reviewer Name", "Rating", "Review", "Review Date"])
df.to_csv("reviews.csv", index=False, encoding="utf-8")
print("✅ Reviews successfully saved to `reviews.csv`!")
