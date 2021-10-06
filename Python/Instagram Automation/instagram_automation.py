from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password

		self.driver = webdriver.Chrome()


	def closeBrowser(self):
		self.driver.close()


	def login(self):
		# Instagram direct URL
		driver = self.driver
		driver.get('https://www.instagram.com/')
		time.sleep(2)
		# "//a[@href='/accounts/login/?source=auth_switcher']"
		login_btn = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_btn.click()
		time.sleep(2)
		# "//input[@name='username']"
		username_elem = driver.find_element_by_xpath("//input[@name='username']")
		username_elem.clear()
		username_elem.send_keys(self.username)
		# "//input[@name='password']"
		password_elem = driver.find_element_by_xpath("//input[@name='password']")
		password_elem.clear()
		password_elem.send_keys(self.password)
		password_elem.send_keys(Keys.RETURN)
		time.sleep(2)


	def like_photo(self, hashtag):
		driver = self.driver
		driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
		time.sleep(2)

		for i in range(1, 3):
			driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
			time.sleep(2)

		# Finding the photos by link
		hrefs = driver.find_elements_by_tag_name('a')
		pics_href = [elem.get_attribute('href') for elem in hrefs]
		pics_href = [href for href in pics_href if hashtag in href]
		print(hashtag + ' photos: ' + str(len(pics_href)))

		for pic in pics_href:
			driver.get(pic)
			driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
			try:
				driver.find_element_by_link_text('Like').click()
				time.sleep(18)
			except Exception as e:
				time.sleep(2)


esau_ig = InstagramBot("<user>", "password")
esau_ig.login()

hashtags = ['amazing', 'beaultiful', 'adventure']
[esau_ig.like_photo(tag) for tag in hashtags]
