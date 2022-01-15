## Automated flashcards uploader using web-browser automation
I have a goal of learning a foreign language. To do that I thought that the best way would be to make myself a set of flashcards with the most common 1000 words in that language and memorize them all. Memorizing them is already a big ammount of work and me being a lazy problemsolver I decided to see if I can automate this task.

At first, I tried inputting some myself, it took on average 12 seconds per word, maybe that's not a lot of time at first glance however, multiply that time by 1000, add in some overhead time that comes from mental fatigue and eye strain, plus some time lost due to any human error that you might make and you will quickly rank up that time. This applies to any repetitive task that needs to be done because, it's not big enough to properly automate it, but it's important and someone has to do it. At best, for my task, I would end up spending 1200 seconds or 20 minutes to input a list of 1000 words, asuming that I would not get at all sidetracked, I would make no mistakes, and I would keep up the same pace as I started. Easy, right?

In reality the whole process would have likelly taken me close to a day to fill in properly. So, I decided to make a script to do it for me.

# Making the script
For this I used python, my preffered language, and the library [Selenium](https://www.selenium.dev/) for python, which is something that was on my radar before and now I got a change to use it a bit. Yay! In hind sight, I could have probably done the same thing with the BeautifullSoup library, the selenium approach seemed more intuitive however as I had to model my logic by how I would navigate the website as a user.

Selenium is a umbrella project which provides functionality for browser interativity automation. Basically you can program any interaction that a normal user would have with the web interface by using python. I can navigate on pages, input and retrieve data and everything is done in a high fidelity way to a normal user experience. What I mean by this is that, if the item that I'm trying to access is not in the browser viewport, selenium will raise an exception and fail the process. If I try to click on a button even though the browser did not finish rendering the view, again selenium will throw an error. This is all because selenium has a primary goal of automating UI testing, rather than having humans perform manual QA tests. 

## Setup
For selenium to work, I needed to download a driver library for the browser that I am using. In my case firefox has the [gekodriver](https://github.com/mozilla/geckodriver/releases) Setting the driver up was very easy, all I had to do was download the appropriate version for my browser, and afterwards save the binary file in the virtual environment that I created for the project.

## Scripting the logic
Once everything was set up correctly, all I had to do was to program the logic as if I was the one interacting with the website.

### Opening the browser
First step, was to open the browser. To do this, I imported the webdriver from selenium, initialized my browser, and gave it the link to my webpage where I wanted to navigate to.

![image](https://user-images.githubusercontent.com/13846875/149632984-ae759824-4097-47fb-a202-890a93d1d25a.png)

```
  from selenium import webdriver
  
  driver = webdriver.Firefox()
  driver.get(MY_WEB_LINK)
```



### Loging in
After the web page is loaded, I will normally look for the login button, input my credentials and click the log in button. All the individual elements from the webpage can be referenced by using the **find_element** method of the web driver class. You can find the elements based on most if not all the html attributes. Due to the nature of web-development, this is a higly customizable part where manual work of identifying these elements and properly referencing them comes into play. It took a bit of time to get it right, but finally I was able to log in, input data and trigger a login. One thing to pay attention to is to rendering times. Actions take time to be processed by the browser and the service you are interacting with while your script runs in a split second. Because of this my script crashed, it was trying to click buttons that where not there yet. To mitigate this issue, I adde manual waiting times of 1 second, at all places where a user would normally wait for a response from the website. After the log in action, I added an extra long wait on the web driver, basically to wait for the web request to be processed by the server, which takes time.

![image](https://user-images.githubusercontent.com/13846875/149633049-16f7007c-fa73-4ad2-8f2f-f44782353cd8.png)

```
  login_btn = driver.find_element(By.CLASS_NAME, "login-button")
  action = ActionChains(driver).move_to_element(login_btn).click()
  action.perform()

  driver.find_element(By.ID, "email").send_keys("email")
  driver.find_element(By.ID, "password").send_keys("password")

  time.sleep(1)
  login_btn = driver.find_element(By.XPATH, "//div[@label='Log In']")
  action = ActionChains(driver).move_to_element(login_btn).click()
  action.perform()

  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "detail-scroll-element")))

```

### Creating my test flashcard deck
After the whole loging process happened, finally I got to program the logic for creating my flashcards deck. In the first line, I encountered the issue that my list of present decks whas long enough that the button for creatinga new deck was out of sight for a user. For this, I had to use javascript to scroll down in the list view, so I can expose the save button. This is all done in the first line of the next block by finding the list item, taking it's total height, and scrolling by that value down.

![image](https://user-images.githubusercontent.com/13846875/149633084-cb70ae74-dec6-4138-9cb3-e2d3333fc8a6.png)

```
# Create new deck
driver.execute_script('document.getElementById("detail-scroll-element").scrollTo(0, document.getElementById("detail-scroll-element").scrollHeight)')
```

Now that I could see the create new deck button, I can click it, and fill the modal that pops up with a name and click continue, in the same way as with the login modal. This creates a new deck in my list, and a button "Add cards is not available for it to take me to the next view. I click the button, then wait until the element with id "question" is in view. That's when I know that I am in the add cards view.

```
time.sleep(1)
new_deck_button = driver.find_element(By.CLASS_NAME, "create-new-deck-row")
action = ActionChains(driver).move_to_element(new_deck_button).click()
action.perform()

driver.find_element(By.ID, "new-deck-name").send_keys(deck_name)

time.sleep(1)
continue_btn = driver.find_element(By.XPATH, "//div[@label='Continue']")
action = ActionChains(driver).move_to_element(continue_btn).click()
action.perform()

time.sleep(1)
add_cards_btn = driver.find_element(By.XPATH, "//div[@label='Add Cards']")
action = ActionChains(driver).move_to_element(add_cards_btn).click()
action.perform()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "question")))

```

### Adding my cards
Now that I made it to the add cards view, it's pretty much more of the same things I did before, fill in two text fields, wait for the view to updated and make the "Save" button available, click sayd save button, create new card, and repeat indeffinatelly. This all being done in a for loop over a list of defined questions and answers that I created at the top of the script.

![image](https://user-images.githubusercontent.com/13846875/149633104-6f064b26-3ffe-4e63-af7a-4857671a4062.png)

```
for question, answer in zip(questions, answers):
    question_field = driver.find_element(By.XPATH, "//textarea[@id='question']").send_keys(question)
    answer_field = driver.find_element(By.XPATH, "//textarea[@id='answer']").send_keys(answer)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@label='Save']")))
    time.sleep(1)
    save_btn = driver.find_element(By.XPATH, "//div[@label='Save']")
    action = ActionChains(driver).move_to_element(save_btn).click()
    action.perform()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='add-card-option create-card-option']")))
    time.sleep(1)
    save_btn = driver.find_element(By.XPATH, "//div[@class='add-card-option create-card-option']")
    action = ActionChains(driver).move_to_element(save_btn).click()
    action.perform()
```

After the script finishes I can call quit on the web browser and that's it. Job done. It took me aproximatelly 4 hours to learn how to use this framework and program the script. Compare that to same amount of tedious work done to input these words and having to do that every time I want to relearn these things. Ironically the website has a solution for uploading these things in bulk for you, however I noticed that feature too late.

Now I can go play guitar while this does it thing!
![Demo](https://github.com/iustin94/automated_flashcards/blob/main/demo.gif?raw=true)


# Takeaways
Selenium is a reall good tool for automating browser interactions. I'll deffinatelly look to use it more for automating UI tests for general usecases of applications. On top of this, the ability to automate administrative tasks like this is very satisfying. You can automate basically anything. The drawback is that it's all done through the front-end layer of a website so your implementations might break anytime due to changes in the websites front-end, the advantage is that it is a very fast way of making something work ar tweek it along the way.
