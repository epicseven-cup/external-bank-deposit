import puppeteer from 'puppeteer';

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto('https://engine.ubnetdef.org/ranks');

    await page.setViewport({ width: 1080, height: 1024 });

    await new Promise(r => setTimeout(r, 3000));
    
    await page.screenshot({
        path: 'screenshot.png',
    });
    await browser.close();
})();