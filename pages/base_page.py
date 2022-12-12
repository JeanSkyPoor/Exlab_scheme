class BasePage():    
    
    def __init__(self, browser, link) -> None:
        """Creating BasePage class\n
        
        Args:
         - browser: fixture or browser driver
         - link: URL address 
        """

        self.browser = browser
        self.link = link


    def open(self) -> None:
        """Open Page using added browser and link using self.browser and self.link"""

        self.browser.get(self.link)