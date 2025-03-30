async function correctText() {
    const text = document.getElementById("inputText").value;
    const response = await fetch("/api/correct", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });
    const result = await response.json();
    document.getElementById("outputText").innerText = result.corrected_text;
}
