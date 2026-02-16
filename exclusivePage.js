// Exclusive casinos data (filtered from main casinos array)
const exclusiveCasinos = [
	{
		id: 'swiftcasino',
		name: 'Swift Casino',
		logo: 'swift.png',
		logoBg: 'rgb(18, 18, 18)',
		rating: 5,
		bonus: '100% Bonus up to £75 + 50 Free Spins on Book of Dead!',
		description:
			'We’ve got an exclusive here for you with up to a matched £75 in bonus funds that’s more play for your pound! No code needed!',
		features: ['Slots', 'Live Tables', 'Roulette', 'Blackjack'],
		terms:
			'Automatically credited upon deposit. Cancellation can be requested. First Deposit Only. Min. deposit: £10, max. Bonus £75. Maximum amount of Free Spins is 50. Game: Book of Dead, Spin Value: £0.1. WR of 10x Bonus amount and Free Spin winnings amount (only Slots count) within 30 days. Max bet is 10% (min £0.10) of the free spin winnings and bonus amount or £5 (lowest amount applies). Spins must be used and/or Bonus must be claimed before using deposited funds. Bonuses do not prevent withdrawing deposit balance. Bonus Policy applies.',
		link: 'https://games.swiftcasino.com/redirect.aspx?mid=5298&sid=15149&cid=&pid=&affid=8275',
		reviewLink: 'reviews/swiftcasino.html',
		exclusive: true,
		exclusiveTag: 'Up to £75!',
	},
	{
		id: 'playojo',
		name: 'PlayOJO',
		logo: 'playojo.png',
		logoBg: 'white',
		rating: 5,
		bonus: '80 free spins!',
		description:
			'Get 80 Free Spins on Big Bass Bonanza with your first deposit. Winnings paid in cash!',
		features: ['Sports', 'Slots', 'Live Casino', 'Blackjack'],
		terms:
			'18+ First deposit only. This offer is only available for first time depositors. Min deposit is £10. 80 Free Spins on Big Bass Bonanza. Spin Value: £0.10.  This offer cannot be used in conjunction with any other offer. T&Cs Apply.',
		link: 'https://site.gotoplayojo.com/index.php?aname=csreviews&zone_id=80spins_uk',
		reviewLink: 'reviews/playojo.html',
		exclusive: true,
		exclusiveTag: 'BEST VALUE',
	},
];

// Initialize
document.addEventListener('DOMContentLoaded', () => {
	updateExclusiveCount();
	renderExclusiveCards();
	initializeNav();
	initializeSmoothScroll();
});

// Update exclusive count
function updateExclusiveCount() {
	const countElement = document.getElementById('exclusiveCount');
	if (countElement) {
		countElement.textContent = exclusiveCasinos.length;
	}
}

// Render exclusive cards
function renderExclusiveCards() {
	const grid = document.getElementById('exclusiveCardsGrid');
	if (!grid) return;

	grid.innerHTML = exclusiveCasinos
		.map(
			(casino) => `
        <div class="exclusive-casino-card" data-id="${casino.id}">
            <div class="exclusive-card-badge">${casino.exclusiveTag}</div>
            
            <div class="exclusive-card-header">
                <div class="exclusive-card-logo" style="background: ${
									casino.logoBg
								}">
                    <img src="images/casinologos/${casino.logo}" alt="${
											casino.name
										}">
                </div>
                <h3>${casino.name}</h3>
                <div class="exclusive-card-rating">
                    ${generateStars(casino.rating)}
                    <span class="rating-value">${casino.rating}/5</span>
                </div>
            </div>
            
            <div class="exclusive-card-body">
                <div class="exclusive-bonus">
                    <span class="bonus-label">⭐ Exclusive Bonus</span>
                    <h4 class="bonus-text">${casino.bonus}</h4>
                </div>
                
                <p class="exclusive-description">${casino.description}</p>
                
                <div class="exclusive-features">
                    ${casino.features
											.slice(0, 4)
											.map(
												(feature) => `
                        <span class="feature-tag">${getFeatureIcon(
													feature,
												)} ${feature}</span>
                    `,
											)
											.join('')}
                </div>
                
                <p class="exclusive-terms">${casino.terms}</p>
            </div>
            
            <div class="exclusive-card-footer">
                <a href="${
									casino.reviewLink
								}" class="btn-exclusive-secondary">Read Review</a>
                <a href="${
									casino.link
								}" target="_blank" class="btn-exclusive-primary">
                    Claim Exclusive Offer
                    <span class="btn-arrow">→</span>
                </a>
            </div>
        </div>
    `,
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

// Get feature icon
function getFeatureIcon(feature) {
	const icons = {
		Slots: '🎰',
		Blackjack: '🃏',
		Roulette: '🎡',
		'Live Tables': '🎪',
		Sports: '⚽',
		Bingo: '🎱',
		Jackpots: '💰',
		'Live Casino': '🎬',
		Supercharges: '⚡',
	};
	return icons[feature] || '🎰';
}

// Navbar scroll behavior
function initializeNav() {
	const nav = document.getElementById('nav');
	let lastScroll = 0;

	window.addEventListener('scroll', () => {
		const currentScroll = window.pageYOffset;

		if (currentScroll > 100) {
			nav.classList.add('scrolled');
		} else {
			nav.classList.remove('scrolled');
		}

		lastScroll = currentScroll;
	});
}

// Smooth scroll
function initializeSmoothScroll() {
	document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
		anchor.addEventListener('click', function (e) {
			e.preventDefault();
			const target = document.querySelector(this.getAttribute('href'));

			if (target) {
				target.scrollIntoView({
					behavior: 'smooth',
					block: 'start',
				});
			}
		});
	});
}
