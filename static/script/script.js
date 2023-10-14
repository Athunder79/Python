addEventListener('load', function () {



    let mobileMenu = document.querySelector('.mobile-menu');
    let menu = document.querySelector('.menu');

    check = 1;

    mobileMenu.addEventListener('click', function () {
        menu.classList.toggle('show');
    });

    let table = document.getElementById('league-table');
    let headers = table.querySelectorAll('th');

    headers.forEach(header => {
        header.addEventListener('click', () => {

            let column = header.cellIndex;
            let rows = Array.from(table.querySelectorAll('tbody tr'));
            let head = rows.shift();
            if (check == 1) {
                rows.sort((b, a) => {
                    check = 0;
                    let aValue = a.cells[column].textContent;
                    let bValue = b.cells[column].textContent;

                    if (isNaN(aValue)) {
                        return aValue.localeCompare(bValue);
                    } else {
                        return aValue - bValue;
                    }
                });
            }
            else {
                rows.sort((a, b) => {
                    check = 1;
                    let aValue = a.cells[column].textContent;
                    let bValue = b.cells[column].textContent;

                    if (isNaN(aValue)) {
                        return aValue.localeCompare(bValue);
                    } else {
                        return aValue - bValue;
                    }
                })
            }

            table.querySelector('tbody').append(...rows);

        });
    });

});