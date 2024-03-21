const serverURL = "http://127.0.0.1:1271"

function demoTest() {
    let cow = {
        x: 12,
        y: 14,
        text: "I_am_scared",
    }

    // let url = window.location.href;
    // let url = "http://127.0.0.1:1271/index.html";
    fetch(serverURL, {
        method: "POST",
        mode: "no-cors",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(cow),
    });
}

function getDataFromServer() {
    fetch(serverURL + "/gimme")
    .then(function(response) {
        // When the page is loaded convert it to text
        return response.text()
    })
    .then(function(html) {
        // Initialize the DOM parser
        let parser = new DOMParser();

        // Parse the text
        let body = parser.parseFromString(html, "text/html").body.innerText;

        console.log(body);
    })
    .catch(function(err) {  
        console.log('Failed to fetch page: ', err);  
    });
}

function start() {
    console.log("Start");

    document.getElementById("test").addEventListener("click", demoTest);
    document.getElementById("testB").addEventListener("click", getDataFromServer);
}
start();