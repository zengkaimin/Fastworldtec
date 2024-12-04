// Get DOM elements
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const clearButton = document.getElementById('clear-button');
const noResultsMessage = document.getElementById('no-results-message');
const toiletryContainer = document.getElementById('toiletries-container');
const toiletryCards = document.querySelectorAll('.product-page-detail-card');

// Hide no results message initially
noResultsMessage.style.display = 'none';

// Function to filter toiletries
function filterToiletries(searchTerm) {
    let hasResults = false;

    toiletryCards.forEach(card => {
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
    filterToiletries(searchTerm);
});

// Event listener for search input
searchInput.addEventListener('input', () => {
    const searchTerm = searchInput.value.toLowerCase();
    filterToiletries(searchTerm);

    // Show/hide clear button
    clearButton.style.display = searchTerm ? 'block' : 'none';
});

// Event listener for clear button
clearButton.addEventListener('click', () => {
    searchInput.value = '';
    filterToiletries('');
    clearButton.style.display = 'none';
});

// Hide clear button initially
clearButton.style.display = 'none';