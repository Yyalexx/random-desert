const colors = ["#FFA6B8", "#4682DC", "#019389", "#FFC100"];

document.addEventListener("DOMContentLoaded", function (event) {
    colorize();
    randomizeRating();
    randomizeTime();
});

function colorize() {
    images = document.querySelectorAll('.card__image');
    for (let img of images) {
        img.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    }
}

function randomizeRating() {
    ratings = document.querySelectorAll('.rating');
    for (let r of ratings) {
        randRating = Math.floor((4 + Math.random()) * 10) / 10;
        r.textContent = String(randRating);
    }
}

function randomizeTime() {
    times = document.querySelectorAll('.time');
    for (let t of times) {
        randTime = Math.floor(15 + 30 * Math.random());
        t.textContent = String(randTime);
    }
}



