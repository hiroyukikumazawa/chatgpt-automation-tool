async function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getSpanByContent(tag, content) {
    const spanElements = document.querySelectorAll(tag);
    for (const spanElement of spanElements) {
        if (spanElement.textContent.trim() === content) {
            return spanElement;
        }
    }
    return null;
}

async function run() {
    const contentToFind = "New chat";
    const spanElement = await getSpanByContent('div', contentToFind);
    await spanElement.click();
    await delay(1000);
    const textarea = await document.getElementById("prompt-textarea");
    my_prompt = "__request_text__";
    textarea.value = my_prompt;
    const inputEvent = await new Event('input', { bubbles: true });
    await textarea.dispatchEvent(inputEvent);
    await delay(100);
    await textarea.nextSibling.click();
    await delay(__max_timeout__);
    const paste_tags = document.querySelectorAll(".ml-auto");
    const paste_tag = paste_tags[paste_tags.length - 1];
    const resp_text = paste_tag.parentElement.parentElement.parentElement.textContent.trim();

    const url = 'http://localhost:7463/gpt35result/';

    const headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    };

    const data = {
        result_text: resp_text
    };

    fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    }).then(response => response.json()).then(data => console.log(data)).catch(error => console.error('Error:', error));
    return resp_text;
}

run();
