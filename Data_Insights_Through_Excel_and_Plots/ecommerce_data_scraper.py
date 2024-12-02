import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import time

class DataExtraction:

    def __init__(self):
        self.url = "https://webscraper.io/test-sites/e-commerce/more"
        self.driver = webdriver.Firefox()
        self.data_dir = "EcomData"
        os.makedirs(self.data_dir, exist_ok=True)

    def click_load_more_button(self):
        while True:
            try:
                load_more_button = self.driver.find_element(By.CSS_SELECTOR, ".btn")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
                load_more_button.click()
                time.sleep(2)  # Small delay to allow products to load
            except (ElementNotInteractableException):
                print("No more 'Load More' button to click.")
                break
    
    def click_button(self, category_button_selector):
        category_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, category_button_selector)))
        category_button.click()
        time.sleep(3)  
    
    def extract_data(self):
        extracted_data = []
        # Locate the main container that holds all products
        products_container = self.driver.find_element(By.CSS_SELECTOR, ".ecomerce-items")
        
        # Locate individual product elements within the main container
        products = products_container.find_elements(By.CSS_SELECTOR, "div.col-md-4")
        
        for product in products:
            # Extract title, price, and rating for each product
            title = product.find_element(By.CLASS_NAME, "title").text  # Extract title text
            price = product.find_element(By.CLASS_NAME, "price").text  # Extract price text
            description = product.find_element(By.CLASS_NAME, "description").text # Extract description text
            stars = product.find_elements(By.CSS_SELECTOR, ".ws-icon.ws-icon-star")
            rating = len(stars)  # Count the number of star elements for the rating
            reviews_text = product.find_element(By.CSS_SELECTOR, ".review-count").text # Extract review count text
            reviews_count = int(reviews_text.split()[0]) # Extract the numeric part of the review count

            # Print the extracted details
            #print(f"Title: {title}, Price: {price}, Description: {description}, Rating: {rating} stars, Reviews: {reviews_count}")
            
            # Store the data in the list as a dictionary
            extracted_data.append({
                "Product": title,
                "Price": price,
                "Description": description,
                "Rating": f"{rating} stars",  # Concatenate 'stars' after the rating
                "Reviews": reviews_count
            })
        
        return extracted_data
    
    def save_data_to_excel(self, data, filename):
        df = pd.DataFrame(data)
        excel_path = os.path.join(self.data_dir, filename)
        df.to_excel(excel_path, index=False, engine='openpyxl')  # Use to_excel to save data to Excel file
        print(f"Data saved to {excel_path}")
    
    def extract_laptops_data(self):
        self.driver.get(self.url)
        time.sleep(3)
        self.click_button('#side-menu > li:nth-child(2) > a:nth-child(1)')
        self.click_button('ul.nav:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
        self.click_load_more_button()
        data = self.extract_data()
        self.save_data_to_excel(data, "laptops_data.xlsx")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
    
    def extract_tablets_data(self):
        self.click_button('ul.nav:nth-child(2) > li:nth-child(2) > a:nth-child(1)')
        self.click_load_more_button()
        data = self.extract_data()
        self.save_data_to_excel(data, "tablets_data.xlsx")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
    
    def extract_phones_data(self):
        self.click_button('#side-menu > li:nth-child(3) > a:nth-child(1)')
        self.click_button('.subcategory-link')
        self.click_load_more_button()
        data = self.extract_data()
        self.save_data_to_excel(data, 'phones_data.xlsx')

    def quit_browser(self):
        self.driver.quit()
    
    def run(self):
        self.extract_laptops_data()
        self.extract_tablets_data()
        self.extract_phones_data()
        self.quit_browser()

if __name__ == '__main__':
    browse = DataExtraction()
    browse.run()

