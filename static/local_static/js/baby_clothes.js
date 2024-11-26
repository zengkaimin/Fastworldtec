// Get DOM elements
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const clearButton = document.getElementById('clear-button');
const noResultsMessage = document.getElementById('no-results-message');
const babyClothesContainer = document.getElementById('baby-clothes-container');
const babyClothesCards = document.querySelectorAll('.product-page-detail-card');

// Hide no results message initially
noResultsMessage.style.display = 'none';

// Function to filter baby clothes
function filterBabyClothes(searchTerm) {
    let hasResults = false;

    babyClothesCards.forEach(card => {
        const title = card.getAttribute('data-title').toLowerCase();
        const description = card.getAttribute('data-description').toLowerCase();

        if (title.includes(searchTerm) || description.includes(searchTerm)) {
            card.style.display = 'block';
            hasResults = true;
        } else {
            card.style.display = 'none';
        }
    });

    // Show/hide no results message
    noResultsMessage.style.display = hasResults ? 'none' : 'block';
}

// Event listener for search form submission
searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const searchTerm = searchInput.value.toLowerCase();
    filterBabyClothes(searchTerm);
});

// Event listener for search input
searchInput.addEventListener('input', () => {
    const searchTerm = searchInput.value.toLowerCase();
    filterBabyClothes(searchTerm);

    // Show/hide clear button
    clearButton.style.display = searchTerm ? 'block' : 'none';
});

// Event listener for clear button
clearButton.addEventListener('click', () => {
    searchInput.value = '';
    filterBabyClothes('');
    clearButton.style.display = 'none';
});

// Hide clear button initially
clearButton.style.display = 'none'; 