document.getElementById("generate-btn").addEventListener("click", async () => {
    let code = editor.getValue();
    let response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code })
    });
    let data = await response.json();
    editor.setValue(data.generated_code);
});

document.getElementById("run-btn").addEventListener("click", async () => {
    let code = editor.getValue();
    let response = await fetch("/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code })
    });
    let data = await response.json();
    document.getElementById("output").textContent = data.output;
});

document.getElementById("debug-btn").addEventListener("click", async () => {
    let code = editor.getValue();
    let response = await fetch("/debug", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code })
    });
    let data = await response.json();
    document.getElementById("output").textContent = data.debug_info;
});

document.getElementById('generate-btn').addEventListener('click', function () {
    document.getElementById('output').textContent = '🚀 AI is generating code...';
});

document.getElementById('run-btn').addEventListener('click', function () {
    document.getElementById('output').textContent = '⚡ Running the code...';
});

document.getElementById('debug-btn').addEventListener('click', function () {
    document.getElementById('output').textContent = '🐞 Debugging the code...';
});
