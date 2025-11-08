const casinoPages = [
	{ title: 'Gala Casino', url: '/Pages/CasinoReviews/galacasino.html' },
	{ title: 'Gala Bingo', url: '/Pages/CasinoReviews/galabingo.html' },
	// Add new ones like this:
	// { title: "New Casino Name Review", url: "/reviews/new-casino.html" }
];

const input = document.getElementById('searchInput');
const resultsContainer = document.getElementById('searchResults');

input.addEventListener('input', function () {
	const query = this.value.toLowerCase().trim();
	resultsContainer.innerHTML = '';

	if (query === '') {
		resultsContainer.style.display = 'none';
		return;
	}

	const filteredPages = casinoPages.filter((page) =>
		page.title.toLowerCase().includes(query)
	);

	if (filteredPages.length > 0) {
		filteredPages.forEach((page) => {
			const link = document.createElement('a');
			link.href = page.url;
			link.textContent = page.title;
			resultsContainer.appendChild(link);
		});
		resultsContainer.style.display = 'block';
	} else {
		resultsContainer.style.display = 'none';
	}
});

// Hide dropdown when clicking outside
document.addEventListener('click', (e) => {
	if (!e.target.closest('.search-container')) {
		resultsContainer.style.display = 'none';
	}
});
