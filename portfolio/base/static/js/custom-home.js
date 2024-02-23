const text = document.querySelector(".changing-text");

const textLoad = () => {
    setTimeout( () => {
    text.textContent = "o Rafael";
    }, 0);
    setTimeout( () => {
    text.textContent = "Cientista da Computação";
    }, 4000);
    setTimeout( () => {
    text.textContent = "Desenvolvedor Web";
    }, 8000);
    setTimeout( () => {
    text.textContent = "Freelancer";
    }, 12000);
}

textLoad();
setInterval(textLoad, 16000)