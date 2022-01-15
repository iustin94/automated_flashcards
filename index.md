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


```from selenium import webdriver
  
  driver = webdriver.Firefox()
  driver.get("http://www.brainscape.com")

    


# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/iustin94/automated_flashcards/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
