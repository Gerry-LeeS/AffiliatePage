const casinoPages = [
	{ title: 'Gala Casino', url: '/Pages/CasinoReviews/galacasino.html' },
	{ title: 'Gala Bingo', url: '/Pages/CasinoReviews/galabingo.html' },
	{ title: 'Ladbrokes', url: '/Pages/CasinoReviews/ladbrokes.html' },
	{ title: 'Coral', url: '/Pages/CasinoReviews/coral.html' },
	{ title: 'NetBet', url: '/Pages/CasinoReviews/netBet.html' },
	{ title: 'BoyleSports', url: '/Pages/CasinoReviews/boyleSports.html' },
	{ title: 'Kwiff', url: '/Pages/CasinoReviews/kwiff.html' },
	{ title: 'PlayOJO', url: '/Pages/CasinoReviews/playojo.html' },
	{ title: 'BresBet', url: '/Pages/CasinoReviews/bresbet.html' },
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
