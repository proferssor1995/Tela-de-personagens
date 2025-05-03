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
