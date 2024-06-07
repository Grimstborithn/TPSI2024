function addItem() {
    const value = prompt("Insira um valor:");
    if (value) {
        const listItem = document.createElement("li");
        listItem.textContent = value;
        document.getElementById("itemList").appendChild(listItem);
    }
}

function handleSubmit(event) {
    event.preventDefault();
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const image = document.querySelector('input[name="image"]:checked').value;

    const resultDiv = document.getElementById("contentResult");
    resultDiv.innerHTML = `
        <h1>${title}</h1>
        <div class="result">
            <p>${description}</p>
            <img src="${image}" alt="Imagem escolhida">
        </div>
    `;
}