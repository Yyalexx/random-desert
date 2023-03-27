const modal = document.querySelector(".modal");
const btnModalClose = document.querySelector('.modal__btn__close');

document.addEventListener('DOMContentLoaded', () => {
    modal.style.display = 'block';
});

btnModalClose.addEventListener('click', () => {
    modal.style.display = 'none';
})


const dropdowns = document.querySelectorAll('.dropdown');
for (let dropdown of dropdowns) {
    const btn = dropdown.querySelector('.dropbtn');
    const menu = dropdown.querySelector('.dropdown-content');
    const img = dropdown.querySelector('.dropbtn img');

    const toggleMenu = function () {
        menu.classList.toggle("show");
        img.classList.toggle("rotate");
    }

    btn.addEventListener('click', function (e) {
        // console.log('click dropdown', menu.id);
        e.preventDefault();
        toggleMenu();
    });

    document.addEventListener('click', function (e) {
        const target = e.target;
        const its_menu = target == menu || menu.contains(target);
        const its_btn = target == btn || btn.contains(target);
        const menu_is_active = menu.classList.contains('show');

        if (!its_menu && !its_btn && menu_is_active) {
            // console.log('hiding menu', menu.id);
            toggleMenu();
        }
    });
}


const ingredients = [
    ['Говядина', 'Свинина', 'Баранина', 'Курица', 'Индейка', 'Рыба', 'Морепродукты'],
    ['Грибы', 'Огурцы', 'Помидоры', 'Капуста', 'Морковь', 'Баклажан', 'Кабачок'],
    ['Картофель', 'Рис', 'Макароны', 'Яйца', 'Молоко', 'Сыр', 'Сметана']
];

const ingredientsListNodes = document.querySelectorAll('.ingredients-list');
for (let i = 0; i < ingredientsListNodes.length; i++) {
    let ingreds = '';
    for (let j = 0; j < ingredients[i].length; j++) {
        let ingred = `
            <li class="ingredient">
                <input type="checkbox" class="custom-checkbox" name="ingredients" value="${ingredients[i][j]}" id="ingredient${i}${j}" form="search-form">
                <label for="ingredient${i}${j}">${ingredients[i][j]}</label>
            </li>
        `
        ingreds += ingred;
    }
    ingredientsListNodes[i].insertAdjacentHTML('afterbegin', ingreds);
}


const cuisines = [
    ['Австрийская', 'Американская', 'Арабская', 'Белорусская', 'Британская', 'Греческая', 'Грузинская'],
    ['Европейская', 'Испанская', 'Итальянская', 'Китайская', 'Мексиканская', 'Паназиатская', 'Русская'],
    ['Средиземноморская', 'Турецкая', 'Тайская', 'Узбекская', 'Украинская', 'Французская', 'Японская']
];

const cuisinesListNodes = document.querySelectorAll('.cuisines-list');
for (let i = 0; i < cuisinesListNodes.length; i++) {
    let cuisinesUl = '';
    for (let j = 0; j < cuisines[i].length; j++) {
        let cuisine = `
            <li class="cuisine">
                <input type="checkbox" class="custom-checkbox" name="cuisine" value="${cuisines[i][j]} кухня" id="cuisine${i}${j}" form="search-form">
                <label for="cuisine${i}${j}">${cuisines[i][j]}</label>
            </li>
        `
        cuisinesUl += cuisine;
    }
    cuisinesListNodes[i].insertAdjacentHTML('afterbegin', cuisinesUl);
}


const categories = [
    ['Выпечка и десерты', 'Завтраки', 'Закуски', 'Напитки', 'Основные блюда', 'Паста и пицца', 'Ризотто'],
    ['Салаты', 'Соусы и маринады', 'Супы', 'Сэндвичи'],
];

const categoriesListNodes = document.querySelectorAll('.categories-list');
for (let i = 0; i < categoriesListNodes.length; i++) {
    let categoriesUl = '';
    for (let j = 0; j < categories[i].length; j++) {
        let category = `
            <li class="category">
                <input type="checkbox" class="custom-checkbox" name="meal_type" value="${categories[i][j]}" id="category${i}${j}" form="search-form">
                <label for="category${i}${j}">${categories[i][j]}</label>
            </li>
        `
        categoriesUl += category;
    }
    categoriesListNodes[i].insertAdjacentHTML('afterbegin', categoriesUl);
}
