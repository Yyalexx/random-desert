
WIDTH_SIDEPANEL = "582px";
sidepanel = document.querySelector(".sidepanel");

const btn = document.querySelector('.btn');
btn.addEventListener('click', () => {

    if (sidepanel.style.width != "0px") {
        sidepanel.style.width = "0";
    } else {
        sidepanel.style.width = "582px";
    };
});




const square = document.querySelector('.lemon');
square.ondragstart = () => false;

const getCoords = (elem) => {
    const box = elem.getBoundingClientRect();
    return {
        top: box.top + pageYOffset,
        left: box.left + pageXOffset
    };
}

square.addEventListener('mousedown', (e) => {
    const coords = getCoords(square);
    // console.log('coords', coords);
    const shiftX = e.pageX - coords.left;
    // console.log('shiftX', shiftX);
    const shiftY = e.pageY - coords.top;
    // console.log('shiftY', shiftY);

    const moveAt = (e) => {
        square.style.left = e.pageX - shiftX + 'px';
        square.style.top = e.pageY - shiftY + 'px';
    }
    const theEnd = () => {
        document.removeEventListener('mousemove', moveAt);
        document.removeEventListener('mouseup', theEnd);
    }

    square.style.position = 'absolute';
    moveAt(e);
    square.style.zIndex = 1000; // делаем над другими элементами

    document.addEventListener('mousemove', moveAt);
    document.addEventListener('mouseup', theEnd);
});



// let gpt = { 'title': 'Фаршированные беконом.', 'ingredients': '- 500 грамм говядины\n- 200 грамм бекона', 'cooking': '1. Нарежьте.\n\n2. Добавьте.\n\n3. Жрите.' }

// el = document.querySelector('.settings');
// el.textContent = gpt.ingredients;