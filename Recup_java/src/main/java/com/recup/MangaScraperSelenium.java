package com.recup;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.List;

public class MangaScraperSelenium {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "/home/tranl/Documents/PP/Récup-test/recup/chromedriver");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--disable-dev-shm-usage");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-gpu");
        options.addArguments("--headless");
        options.addArguments("--remote-debugging-port=9222");
        options.addArguments("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36");

        WebDriver driver = new ChromeDriver(options);

        try {
            driver.get("https://mangas-origines.fr/catalogues/");

            List<WebElement> mangaElements = driver.findElements(By.cssSelector(".series-card__title"));

            for (WebElement mangaElement : mangaElements) {
                String mangaName = mangaElement.getText();
                System.out.println(mangaName);
            }
        } finally {
            driver.quit();
        }
    }
}
