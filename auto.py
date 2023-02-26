import webbrowser
browser_option = {
    1: "Google",
    2: "Amazon Web Service",
    3: "Youtube",
    4: "Github",
    5: "Leetcode"
}
print(browser_option)
browser_input = input("Enter a website to go to: ")


def open_browser(option):
    url = {
        "1": "https://www.google.com/",
        "2": "https://aws.amazon.com/",
        "3": "https://www.youtube.com/",
        "4": "https://github.com/",
        "5": "https://leetcode.com/"
    }
    control = webbrowser.get("safari")
    control.open_new(url[option])


open_browser(browser_input)


