// 根据时间自动设置主题
function setThemeByTime() {
    // 获取用户时区
    const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const now = new Date();
    
    // 使用 Intl.DateTimeFormat 获取用户时区的时间
    const formatter = new Intl.DateTimeFormat('en-US', {
        timeZone: userTimeZone,
        hour: 'numeric',
        hour12: false,
        minute: 'numeric'
    });
    
    const timeStr = formatter.format(now);
    const hour = parseInt(timeStr);
    console.log(`Current time in ${userTimeZone}: ${timeStr}`);
    
    // 定义时间段
    const MORNING_START = 6;    // 早上6点
    const EVENING_START = 18;   // 晚上6点
    const NIGHT_START = 22;     // 晚上10点
    
    let theme;
    // 早上 6:00 - 17:59 使用浅色主题
    if (hour >= MORNING_START && hour < EVENING_START) {
        theme = 'light';
        console.log(`Setting light theme (daytime: ${hour} is between ${MORNING_START}:00 and ${EVENING_START}:00)`);
    }
    // 晚上 18:00 - 21:59 使用暖色主题
    else if (hour >= EVENING_START && hour < NIGHT_START) {
        theme = 'sepia';
        console.log(`Setting sepia theme (evening: ${hour} is between ${EVENING_START}:00 and ${NIGHT_START}:00)`);
    }
    // 夜间 22:00 - 5:59 使用深色主题
    else {
        theme = 'dark';
        console.log(`Setting dark theme (night: ${hour} is either >= ${NIGHT_START}:00 or < ${MORNING_START}:00)`);
    }
    
    // 设置主题
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // 初始化主题
    setThemeByTime();
    // 每分钟检查一次时间并更新主题
    setInterval(setThemeByTime, 60000);

    // Smooth scrolling functionality for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        // Add a click event listener to each anchor link
        anchor.addEventListener('click', function (e) {
            // Prevent the default click action
            e.preventDefault();
            // Smoothly scroll to the target section
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add an event listener for when the window has fully loaded
    window.addEventListener('load', () => {
        // Add a delay before adding the 'loaded' class to the body
        setTimeout(() => {
            document.body.classList.add('loaded');
        }, 500); // Delay of 500ms
    });

    // Cookie banner functionality
    // Get the cookie banner element
    const cookieBanner = document.getElementById('cookie-banner');
    // Get the accept cookies button element
    const acceptCookiesButton = document.getElementById('accept-cookies');
    // Get the reject cookies button element
    const rejectCookiesButton = document.getElementById('reject-cookies');

    // Function to set a cookie
    function setCookie(name, value, days) {
        // Initialize the expires string
        let expires = "";
        // If days are provided, set the expiration date
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        // Set the cookie with the name, value, and expiration date
        document.cookie = `${name}=${value || ""}${expires}; path=/`;
    }

    // Function to get a cookie by name
    function getCookie(name) {
        // Create the name=value string
        const nameEQ = `${name}=`;
        // Split the cookies into an array
        const ca = document.cookie.split(';');
        // Loop through the array of cookies
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i].trim();
            // If the cookie is found, return its value
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        // Return null if the cookie is not found
        return null;
    }

    // Function to hide the cookie banner
    function hideBanner() {
        cookieBanner.style.display = 'none';
    }

    // Function to handle the cookie choice
    function handleCookieChoice(accepted) {
        // Set the cookie choice
        setCookie('cookieChoice', accepted ? 'accepted' : 'rejected', 365);
        // Hide the cookie banner
        hideBanner();
        // Log the cookie choice
        console.log(`Cookies ${accepted ? 'accepted' : 'rejected'}`);
    }

    // Get the cookie choice from the cookies
    const cookieChoice = getCookie('cookieChoice');
    // If there is no cookie choice, show the cookie banner
    if (!cookieChoice) {
        cookieBanner.style.display = 'block';
    } else {
        // Handle the existing cookie choice
        handleCookieChoice(cookieChoice === 'accepted');
    }

    // Add event listener to the accept cookies button
    acceptCookiesButton.addEventListener('click', () => handleCookieChoice(true));
    // Add event listener to the reject cookies button
    rejectCookiesButton.addEventListener('click', () => handleCookieChoice(false));

    // Message auto-hide and close button functionality
    // Select all elements with the class 'message'
    document.querySelectorAll('.message').forEach(message => {
        // Automatically hide each message after 5 seconds
        setTimeout(() => message.classList.add('fade-out'), 5000);

        // Find the close button within the message
        message.querySelector('.close-btn').addEventListener('click', () => {
            // Add the 'fade-out' class to hide the message when the close button is clicked
            message.classList.add('fade-out');
        });
    });

    // Back to Top button functionality
    // Get the Back to Top button element
    const backToTopButton = document.getElementById('back-to-top');
    // Variable to store the timeout for hiding the button
    let hideTimeout;
    // Variable to store the timeout for scroll debounce
    let scrollTimeout;

    // Function to show the Back to Top button
    function showBackToTopButton() {
        backToTopButton.classList.add('show');
        // Clear any existing hide timeout
        clearTimeout(hideTimeout);
        // Set a timeout to hide the button after 5 seconds
        hideTimeout = setTimeout(() => {
            backToTopButton.classList.remove('show');
        }, 5000);
    }

    // Add event listener for scrolling
    window.addEventListener('scroll', () => {
        // Show the button when the user scrolls down 100px from the top
        if (window.scrollY > 100) {
            showBackToTopButton();
        } else {
            // Hide the button when the user scrolls back to the top
            backToTopButton.classList.remove('show');
        }
        // Clear any existing scroll timeout
        clearTimeout(scrollTimeout);
        // Set a timeout to hide the button after 5 seconds of no scrolling
        scrollTimeout = setTimeout(() => {
            if (window.scrollY > 100) {
                backToTopButton.classList.remove('show');
            }
        }, 5000);
    });

    // Add event listener for the Back to Top button click
    backToTopButton.addEventListener('click', () => {
        // Smooth scroll to the top
        window.scrollTo({ top: 0, behavior: 'smooth' });
        showBackToTopButton();
    });

    // Show the button when the user touches the screen
    window.addEventListener('touchstart', showBackToTopButton);
});
