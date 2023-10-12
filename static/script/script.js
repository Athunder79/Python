document.addEventListener('DOMContentLoaded', function() {
    let table = document.getElementById('league-table');
    let headers = table.querySelectorAll('th');
    
    headers.forEach(header => {
        header.addEventListener('click', () => {
            let column = header.cellIndex;
            let rows = Array.from(table.querySelectorAll('tbody tr'));
            
            rows.sort((a, b) => {
                let aValue = a.cells[column].textContent;
                let bValue = b.cells[column].textContent;
                
                return isNaN(aValue) ? aValue.localeCompare(bValue) : aValue - bValue;
            });
            
            table.querySelector('tbody').append(...rows);
        });
    });
});