const musica = document.getElementById('musica');

function aumentarVolume() {
    if (musica.volume < 1) {
        musica.volume = Math.min(1, musica.volume + 0.1);
    }
}

function diminuirVolume() {
    if (musica.volume > 0) {
        musica.volume = Math.max(0, musica.volume - 0.1);
    }
}

function tocarMusica() {
    musica.muted = false;
    musica.volume = 1;
    musica.play().catch(e => console.log("Erro ao reproduzir:", e));
}
