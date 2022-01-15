import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

deck_name = "TestDeck"

questions = ["good morning",
        "good afternoon",
        "good evening",
        "good night",
        "goodbye",
        "see you soon",
        "oh my God",
        "you're welcome",
        "I'm from",
        "how are you?",
        "hey there!",
        "I agree",
        "more",
        "but",
        "still",
        "and",
        "the same",
        "a question",
        "an answer",
        "maybe",
        "possibly",
        "perhaps",
        "excuse me",
        "pardon",
        "none",
        "like so",
        "for example",
        "against",
        "thing",
        "something",
        "everything",
        "to the right",
        "to the left",
        "nothing",
        "only",
        "with",
        "without",
        "already",
        "each",
        "a little",
        "half",
        "not even",
        "this way",
        "if",
        "really",
        "opposite",
        "close",
        "three years ago",
        "too few",
        "a few",
        "together",
        "possibly",
        "one time",
        "lots of time"]

answers = ["god morgen",
        "god eftermiddag",
        "god aften",
        "godnat",
        "farvel",
        "Vi ses",
        "Åh gud",
        "selv tak",
        "jeg er fra",
        "Hvordan har du det?",
        "Hej med dig!",
        "jeg er enig",
        "mere",
        "men",
        "stadig",
        "og",
        "det samme",
        "et spørgsmål",
        "et svar",
        "måske",
        "eventuelt",
        "måske",
        "undskyld",
        "om forladelse",
        "ingen",
        "ligesom",
        "for eksempel",
        "mod",
        "ting",
        "noget",
        "alt",
        "til højre",
        "til venstre",
        "ikke noget",
        "kun",
        "med",
        "uden",
        "allerede",
        "hver",
        "en lille",
        "halvt",
        "ikke engang",
        "denne måde",
        "hvis",
        "virkelig",
        "modsatte",
        "tæt",
        "tre år siden",
        "for få",
        "nogle få",
        "sammen",
        "eventuelt",
        "en gang",
        "masser af tid"]

driver = webdriver.Firefox()
driver.get("http://www.brainscape.com")

# Login
login_btn = driver.find_element(By.CLASS_NAME, "login-button")
action = ActionChains(driver).move_to_element(login_btn).click()
action.perform()

driver.find_element(By.ID, "email").send_keys("o.iustin@gmail.com")
driver.find_element(By.ID, "password").send_keys("?Prlbrd_68")

time.sleep(1)
login_btn = driver.find_element(By.XPATH, "//div[@label='Log In']")
action = ActionChains(driver).move_to_element(login_btn).click()
action.perform()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "detail-scroll-element")))

# Create new deck
driver.execute_script('document.getElementById("detail-scroll-element").scrollTo(0, document.getElementById("detail-scroll-element").scrollHeight)')

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

    driver.execute_script('document.getElementById("deck-card-list").scrollTo(0, document.getElementById("deck-card-list").scrollHeight)')



