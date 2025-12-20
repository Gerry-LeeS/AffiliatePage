// Search Page JavaScript

// Initialize
document.addEventListener('DOMContentLoaded', () => {
	renderAllReviews();
	initializeSearch();
	updateTotalCount();
});

// Update total count
function updateTotalCount() {
	const countElement = document.getElementById('totalCount');
	if (countElement) {
		countElement.textContent = casinoPages.length;
	}
}

// Render all review cards
function renderAllReviews() {
	const grid = document.getElementById('reviewsGrid');
	if (!grid) return;

	grid.innerHTML = casinoPages
		.map(
			(casino) => `
        <a href="${casino.url}" class="review-card">
            <div class="review-card-content">
                <h3>${casino.title}</h3>
                <div class="review-card-rating">
                    ${generateStars(casino.rating)}
                </div>
                <span class="review-arrow">→</span>
            </div>
        </a>
    `
		)
		.join('');
}

// Generate star rating
function generateStars(rating) {
	const fullStars = Math.floor(rating);
	const hasHalfStar = rating % 1 !== 0;
	let starsHTML = '';

	for (let i = 0; i < fullStars; i++) {
		starsHTML += `
            <svg viewBox="0 0 24 24" class="star filled">
                <path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/>
            </svg>
        `;
	}

	if (hasHalfStar) {
		starsHTML += `
            <svg viewBox="0 0 24 24" class="star half">
                <defs>
                    <clipPath id="half-${rating}">
                        <rect x="0" y="0" width="12" height="24" />
                    </clipPath>
                </defs>
                <path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z" clip-path="url(#half-${rating})" fill="var(--gold)"/>
                <path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z" fill="rgba(212, 175, 55, 0.3)"/>
            </svg>
        `;
	}

	const emptyStars = 5 - Math.ceil(rating);
	for (let i = 0; i < emptyStars; i++) {
		starsHTML += `
            <svg viewBox="0 0 24 24" class="star empty">
                <path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/>
            </svg>
        `;
	}

	return starsHTML;
}

// Initialize search functionality
function initializeSearch() {
	const input = document.getElementById('searchInput');
	const resultsContainer = document.getElementById('searchResults');

	if (!input || !resultsContainer) return;

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
				link.classList.add('search-result-item');
				resultsContainer.appendChild(link);
			});
			resultsContainer.style.display = 'block';
		} else {
			const noResults = document.createElement('div');
			noResults.textContent = 'No casinos found';
			noResults.classList.add('no-results');
			resultsContainer.appendChild(noResults);
			resultsContainer.style.display = 'block';
		}
	});

	// Hide dropdown when clicking outside
	document.addEventListener('click', (e) => {
		if (!e.target.closest('.search-container')) {
			resultsContainer.style.display = 'none';
		}
	});
}
