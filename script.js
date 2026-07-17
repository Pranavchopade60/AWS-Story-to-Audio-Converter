const API = "";

async function uploadStory() {

    const file = document.getElementById("file").files[0];

    if (!file) {

        alert("Please select a TXT file.");

        return;

    }

    const story = await file.text();

    document.getElementById("msg").innerHTML = "Uploading story...";

    const response = await fetch(API + "/upload", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            filename: file.name,

            story: story

        })

    });

    const data = await response.json();

    document.getElementById("msg").innerHTML =
        "✅ " + data.message;

    if (data.audio_url) {

        const player = document.getElementById("player");

        player.src = data.audio_url;

        document.getElementById("audioSection").style.display = "block";

        document.getElementById("details").style.display = "block";

        document.getElementById("storyName").innerHTML = file.name;

        document.getElementById("uploadTime").innerHTML =
            new Date().toLocaleString();

    }
}