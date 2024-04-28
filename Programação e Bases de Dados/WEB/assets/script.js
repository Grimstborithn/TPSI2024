function escreverP (){
    let novoParagrafo = prompt("Escreva o texto a adicionar :");
    elemento = document.getElementById("saida").textContent;
    document.getElementById("saida").innerHTML= elemento + novoParagrafo;
}
function apagarP() {
    document.getElementById("saida").innerHTML = "";
    document.getElementById("direita").innerHTML = "";
}