// Slots: '🎰',
// 		Blackjack: '🃏',
// 		Roulette: '𖥕',
// 		'Live Tables': '🤵🏻‍♂️',
// 		Sports: '⚽',
// 		Bingo: '🎱',
// 		Jackpots: '💰',
// 		Racing: '🏇',
// 		Casino: '🎲',
// 		'Live Casino': '🎬',
// 		'Live Betting': '📺',
// 		'Virtual Sports': '🎮',
// 		Supercharges: '⚡',
// 		Poker: '♠️',

// Auto-update copyright year
document.getElementById('currentYear').textContent = new Date().getFullYear();

// Casino data
const casinos = [
	{
		id: 'lunacasino',
		name: 'Luna Casino',
		logo: 'luna.png',
		logoBg: 'black',
		rating: 5,
		bonusType: 'Casino Bonus',
		bonus: '100% Up to £50 + 50 Free Spins on Book of Dead. Bonus code: LUNA',
		description:
			'Luna Casino will be your next favourite place to play at. We loved it here and with plenty of fun bonuses to play with you won’t get bored here. They are up to date with the latest games from all your favourite providers.',
		features: ['Slots', 'Live Tables', 'Roulette', 'Blackjack'],
		terms:
			'Automatically credited upon deposit. Cancellation can be requested. First Deposit Only. Min. deposit: £10, max. Bonus £50. Maximum amount of Free Spins is 50. Game: Book of Dead, Spin Value: £0.1. WR of 10x Bonus amount and Free Spin winnings amount (only Slots count) within 30 days. Max bet is 10% (min £0.10) of the free spin winnings and bonus amount or £5 (lowest amount applies). Spins must be used and/or Bonus must be claimed before using deposited funds. Bonuses do not prevent withdrawing deposit balance. Bonus Policy applies.',
		link: 'https://ads.galaxyaffiliates.com/redirect.aspx?mid=5366&sid=15149&cid=&pid=&affid=8275',
		reviewLink: 'reviews/lunacasino.html',
		exclusive: false,
	},
	{
		id: 'boylecasino',
		name: 'BOYLE Casino',
		logo: 'boyle_square.png',
		logoBg: '#001d5e',
		rating: 5,
		bonusType: 'Casino Bonus',
		bonus: 'Get up to 100 Free spins. The more you wager the more you get!',
		description:
			'From high street to online, BOYLE Casino is one of the household names you can trust, with everything under one roof you’ll find your next favourite game.',
		features: [
			'Slots',
			'Live Tables',
			'Sports',
			'Bingo',
			'Roulette',
			'Blackjack',
			'Poker',
		],
		terms:
			'18+. Opt in. Acc. games, game weighting & payment restrictions apply. 100 Free Spins: Exp. 01.12.26. New UK/ROI gaming players. Same day min. stake req. (€/£ 20/50/100 to get 20/50/100 Free Spins (FS)) by 23:59. FS Values £/€0.10 – 0.20. FS valid 72h.  Pragmatic Tournament: Tue 12:00 to Mon 23:59 BST. Play 10+ real money rounds on eligible games to qualify. Score based on multiplier wins, streaks (wins/losses). Max 200 rounds/day. FS value €/£0.10. Use within 48 hrs. T&Cs Apply.',
		link: 'https://promo.boylesports.com/gaming/promo/game8?btag=54248|0f036f7746684ebb9a8e6752ee0e068a',
		reviewLink: '/reviews/boylecasino.html',
		exclusive: false,
	},
	{
		id: 'playojo',
		name: 'PlayOJO',
		logo: 'playojo.png',
		logoBg: '#fff',
		rating: 5,
		bonusType: 'Casino Bonus',
		bonus:
			'80 Wager Free Spins + Money back on Every Bet! No Wagering requirements on anything, EVER!',
		description:
			'There’s no company quite as generous as PlayOJO. From cashback on every spin, to personalised bonuses, and their daily Prize Twister which is your free chance to win free spins, bingo tickets, scratchcards, cash prizes. They’ve won plenty of awards so you know they’re a casino you can trust.',
		features: ['Slots', 'Live Tables', 'Bingo', 'Blackjack', 'Roulette'],
		terms:
			'18+ First deposit only. This offer is only available for first time depositors. Min deposit is £10. 80 Free Spins on Big Bass Bonanza. Spin Value: £0.10. This offer cannot be used in conjunction with any other offer. T&Cs Apply.',
		link: 'https://site.gotoplayojo.com/index.php?aname=csreviews&zone_id=80spins_uk',
		reviewLink: '/reviews/playojo.html',
		exclusive: true,
	},

	{
		id: 'swiftcasino',
		name: 'Swift Casino',
		logo: 'swift.png',
		logoBg: 'rgb(18, 18, 18)',
		rating: 5,
		bonusType: 'Casino',
		bonus: '100% Bonus up to £75 + 50 Free Spins on Book of Dead.',
		description:
			'We’ve got an exclusive here for you with up to a matched £75 in bonus funds that’s more play for your pound! No code needed!',
		features: ['Slots', 'Live Tables', 'Roulette', 'Blackjack'],
		terms:
			'Automatically credited upon deposit. Cancellation can be requested. First Deposit Only. Min. deposit: £10, max. Bonus £75. Maximum amount of Free Spins is 50. Game: Book of Dead, Spin Value: £0.1. WR of 10x Bonus amount and Free Spin winnings amount (only Slots count) within 30 days. Max bet is 10% (min £0.10) of the free spin winnings and bonus amount or £5 (lowest amount applies). Spins must be used and/or Bonus must be claimed before using deposited funds. Bonuses do not prevent withdrawing deposit balance. Bonus Policy applies.',
		link: 'https://games.swiftcasino.com/redirect.aspx?mid=5298&sid=15149&cid=&pid=&affid=8275',
		reviewLink: '/reviews/swiftcasino.html',
		exclusive: true,
	},
	{
		id: 'bestodds',
		name: 'BestOdds',
		logo: 'bestodds.png',
		logoBg: 'rgb(22, 32, 57)',
		rating: 5,
		bonusType: 'Casino',
		bonus: 'Get 5 x 50 Free Spins when you wager £20!',
		description:
			'BestOdds are one of the newer operators on the scene, with a great site and plenty of Sports and Casino offerings we’re finding it a great place to play.',
		features: ['Slots', 'Live Tables', 'Sports', 'Roulette', 'Blackjack'],
		terms:
			'New UK customers only. Wager £20+ on selected Pragmatic Play slots to get 50 Free Spins daily for 5 days. Spins expire 24 hrs after issue. Max Payouts & Full T&Cs apply. Use code 5x50fs',
		link: 'https://bolinkhub.com/wdzr67kan',
		reviewLink: '/reviews/bestodds.html',
		exclusive: false,
	},

	{
		id: 'netbet',
		name: 'NetBet',
		logo: 'netbet.png',
		logoBg: '#101010',
		rating: 5,
		bonusType: 'Casino Bonus',
		bonus:
			'Wager £20 on any slots and get 100 Free Spins. Winnings paid in cash!',
		description:
			'A longstanding casino since 2001. Plenty of slot options and betting with sports AI to help you create your next bet.',
		features: [
			'Slots',
			'Live Tables',
			'Sports',
			'Roulette',
			'Blackjack',
			'Poker',
		],
		terms:
			'18+. New customers only. £20 min deposit. Opt-in and Bet £20+ on any slot, 100 Free Spins on Big Bass Splash, £0.10 per spin. Winnings paid as cash, £100 Max win. Additional T&Cs apply.',
		link: 'https://netbet.livepartners.com/click.php?z=186827',
		reviewLink: 'reviews/netbet.html',
		exclusive: false,
	},

	{
		id: 'bresbet',
		name: 'BresBet',
		logo: 'bresbet.png',
		logoBg: 'rgb(0, 28, 70)',
		rating: 4.5,
		bonusType: 'Casino Bonus',
		bonus:
			'Offer: Get 100 Free Spins when you wager £10 on Huff N Lots Of Puff.',
		description:
			'BresBet have a good focus on loyalty and it is rewarded when you play here. With weekly casino and sports clubs you can get Free Spins and Bets often.',
		features: [
			'Slots',
			'Live Tables',
			'Sports',
			'Blackjack',
			'Roulette',
			'Racing',
		],
		terms:
			'Min £10 wager on Huff N Lots Of Puff to receive 100 x £0.10 free spins. Free spins credited by 12pn noon the day after you qualify. New Customers Only. T&Cs apply. 18+ Use code: CasinoWelcome26',
		link: 'https://refer.bresbet.com/redirect?cid=6908a413b70b75a6c986e44b&oid=6499640c6e61a4ede687608b&mid=69778ff644285b0a54fe2176&customParameter=',
		reviewLink: '/reviews/bresbet.html',
		exclusive: false,
	},

	{
		id: 'bettom',
		name: 'BetTom',
		logo: 'bettom.png',
		logoBg: 'rgb(15, 38, 172)',
		rating: 4.5,
		bonusType: 'Casino Bonus',
		bonus: 'UP TO £50 BONUS FUNDS + 10 FREE SPINS ON BIG BASS SPLASH!',
		description:
			'A relatively new UK brand that has a big focus on their players. Boasting their live chat has real people to speak to and same day withdrawals they already prove themselves as a brand to trust.',
		features: ['Slots', 'Live Tables', 'Sports', 'Roulette', 'Blackjack'],
		terms:
			'Get 50% back on first day casino losses as a free bonus funds up to £50. To be credited within 24 hours. Max free bet per customer £/€50. Qualifying customers will additionally receive 10x 10p free spins on Big Bass Splash. 5x wagering requirement applies to free spins. Customers who qualify for the welcome offer free bet will also receive 10x free spins on Big Bass Splash. Each free spin is worth £0.10. Full T&Cs apply.',
		link: 'https://tracker.bettomaffiliates.com/link?btag=102129792_477209',
		reviewLink: '/reviews/bettom.html',
		exclusive: false,
	},

	{
		id: 'livescorebet',
		name: 'LiveScoreBet',
		logo: 'lsbet.png',
		logoBg: 'rgb(251, 84, 21)',
		rating: 4.5,
		bonusType: 'Sports Bonus',
		bonus: 'Play £10 on slots & get 100 Free Spins!',
		description:
			'Your favourite sports results website has it’s own online Sports betting and Casino to welcome you to. With plenty of promotions and a sleek website design LiveScore Bet is a great place to play at.',
		features: ['Slots', 'Live Tables', 'Sports', 'Roulette', 'Blackjack'],
		terms:
			'**New members only. *Must sign up via offer link. Wager in 7 days of reg. Accept Free Spins to use on King Kong Cash Even Bigger Bananas Jackpot King via pop-up within 24 hrs of qualifying (10p spin value, 3 days expiry). Terms & deposit exclusions apply. 18+',
		link: 'https://wl-nl.livescorebet.com/C.ashx?btag=a_2339b_60c_&affid=717&siteid=2339&adid=60&c= ',
		reviewLink: '/reviews/livescorebet.html',
		exclusive: false,
	},

	{
		id: 'kwiff',
		name: 'Kwiff',
		logo: 'kwiff.png',
		logoBg: '#7a2af4',
		rating: 4.5,
		bonusType: 'Casino Bonus',
		bonus: 'Wager £20 on any slot and get 200 Free Spins.',
		description:
			'Ontop of their great casino selection with new games and kwiff casino exclusives, kwiff have their unique supercharged bets where any sports bet you place can have increased odds.',
		features: ['Slots', 'Live Tables', 'Blackjack', 'Roulette', 'Supercharges'],
		terms:
			'Wager £20 cash on slots within 5 days of first deposit and Get 200 Free Spins on Book of Dead. £0.10 per spin. £250 total max withdrawal. E-wallets and virtual cards excluded. 18+. New customers only. Full T&Cs apply. Gamble Responsibly.',
		link: 'https://promos.kwiff.com/casino/?btag=a_4001b_79c_&affid=1012&source=IncomeAccess&creative=79&campaign_id=&affiliate_id=1012&incomeaccess_click_id=a_4001b_79c_&campaign=a_4001b_79c_&siteid=4001',
		reviewLink: '/reviews/kwiff.html',
		exclusive: false,
	},
];

// State
let currentFilter = 'all';
let currentSort = 'rating';
let compareList = [];

// DOM Elements
const cardsGrid = document.getElementById('cardsGrid');
const filterBtns = document.querySelectorAll('.filter-btn');
const sortSelect = document.getElementById('sortSelect');
const compareBanner = document.getElementById('compareBanner');
const compareChips = document.getElementById('compareChips');
const compareBtn = document.getElementById('compareBtn');
const themeToggle = document.getElementById('themeToggle');
const nav = document.getElementById('nav');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
	// Only run card functions if elements exist
	const cardsGrid = document.getElementById('cardsGrid');
	if (cardsGrid) {
		updateStatsCounter();
		updateFilterCounts();
		renderCards();
		initializeFilters();
		initializeSort();
	}

	// Only animate stats if they exist
	if (document.querySelector('.stats-bar')) {
		animateStats();
	}

	// Always run these
	initializeTheme();
	initializeNav();

	// Calculator Help Modal
	const helpBtn = document.getElementById('calculatorHelpBtn');
	const helpModal = document.getElementById('calculatorHelpModal');

	if (helpBtn && helpModal) {
		const helpOverlay = document.getElementById('calculatorHelpOverlay');
		const helpClose = document.getElementById('calculatorHelpClose');

		helpBtn.addEventListener('click', () => {
			helpModal.classList.add('active');
			document.body.style.overflow = 'hidden';
		});

		function closeHelpModal() {
			helpModal.classList.remove('active');
			document.body.style.overflow = '';
		}

		if (helpClose) helpClose.addEventListener('click', closeHelpModal);
		if (helpOverlay) helpOverlay.addEventListener('click', closeHelpModal);

		document.addEventListener('keydown', (e) => {
			if (e.key === 'Escape' && helpModal.classList.contains('active')) {
				closeHelpModal();
			}
		});
	}
});

// Update filter counts dynamically
function updateFilterCounts() {
	const allCount = document.querySelector('[data-filter="all"] .filter-count');
	const exclusiveCount = document.querySelector(
		'[data-filter="exclusive"] .filter-count',
	);

	if (allCount) allCount.textContent = casinos.length;
	if (exclusiveCount)
		exclusiveCount.textContent = casinos.filter((c) => c.exclusive).length;
}

// Update stats counter from casinoData.js
function updateStatsCounter() {
	const statNumber = document.querySelector('.stat-number[data-target]');
	if (statNumber && typeof getTotalCasinoCount === 'function') {
		const totalCount = getTotalCasinoCount();
		statNumber.setAttribute('data-target', totalCount);
	}
}

// Render casino cards
function renderCards() {
	const filtered = filterCasinos(casinos);
	const sorted = sortCasinos(filtered);

	cardsGrid.innerHTML = sorted
		.map(
			(casino) => `
        <div class="casino-card ${
					casino.exclusive ? 'exclusive' : ''
				}" data-id="${casino.id}">
            <div class="card-header">
                <div class="card-logo" style="background: ${casino.logoBg}">
                    <img src="images/casinologos/${casino.logo}" alt="${
											casino.name
										}">
                </div>
                
                <div class="card-title-group">
                    <h3>${casino.name}</h3>
                    <div class="card-rating">
                        <div class="stars">
                            ${generateStars(casino.rating)}
                        </div>
                    </div>
                </div>
                
                <div class="card-actions">
                    <a href="${
											casino.reviewLink
										}" class="btn btn-secondary">Review</a>
                    <button onclick="openQuickView('${
											casino.id
										}')" class="btn btn-secondary btn-quick-view">Quick View</button>
                    <a href="${
											casino.link
										}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">Claim Offer</a>
                </div>
                
                ${
									casino.exclusive
										? `
                    <div class="exclusive-badge">
                        <span>⭐</span>
                        <span>EXCLUSIVE</span>
                    </div>
                `
										: ''
								}
            </div>
            
            <div class="card-body">
                <div class="bonus-highlight">
                    <div class="bonus-type">${casino.bonusType}</div>
                    <h4 class="bonus-title">${casino.bonus}</h4>
                    <p class="bonus-terms">${casino.terms}</p>
                </div>
                
                <div class="features-grid">
                    ${casino.features
											.map(
												(feature) => `
                        <div class="feature-item">
                            <div class="feature-icon">${getFeatureIcon(
															feature,
														)}</div>
                            <div class="feature-label">${feature}</div>
                        </div>
                    `,
											)
											.join('')}
                </div>
                
                <p class="card-description">${casino.description}</p>
                
                <div class="card-footer">
                    <label class="compare-checkbox">
                        <input type="checkbox" class="compare-input" data-casino="${
													casino.id
												}" ${compareList.includes(casino.id) ? 'checked' : ''}>
                        <span class="compare-label">Add to Compare</span>
                    </label>
                </div>
            </div>
        </div>
    `,
		)
		.join('');

	// Re-attach compare listeners
	attachCompareListeners();
}

// Generate star rating HTML
function generateStars(rating) {
	const fullStars = Math.floor(rating);
	const hasHalfStar = rating % 1 !== 0;
	let starsHTML = '';

	// Full stars
	for (let i = 0; i < fullStars; i++) {
		starsHTML += `
            <svg viewBox="0 0 24 24" class="star filled">
                <path d="M12 .587l3.668 7.431L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.73L12 .587z"/>
            </svg>
        `;
	}

	// Half star
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

	// Empty stars
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
		Roulette: '𖥕',
		'Live Tables': '🤵🏻‍♂️',
		Sports: '⚽',
		Bingo: '🎱',
		Jackpots: '💰',
		Racing: '🏇',
		Casino: '🎲',
		'Live Casino': '🎬',
		'Live Betting': '📺',
		'Virtual Sports': '🎮',
		Supercharges: '⚡',
		Poker: '♠️',
	};

	return icons[feature] || '🎰';
}

// Filter casinos
function filterCasinos(casinos) {
	if (currentFilter === 'all') return casinos;

	if (currentFilter === 'exclusive') {
		return casinos.filter((c) => c.exclusive);
	}

	return casinos;
}

// Show casinos in array order (no sorting)
function sortCasinos(casinos) {
	return casinos;
}

// Initialize filters
function initializeFilters() {
	filterBtns.forEach((btn) => {
		btn.addEventListener('click', () => {
			const filter = btn.dataset.filter;
			currentFilter = filter;

			// Update active state
			filterBtns.forEach((b) => b.classList.remove('active'));
			btn.classList.add('active');

			renderCards();
		});
	});
}

// Initialize sort
function initializeSort() {
	if (!sortSelect) return;

	sortSelect.addEventListener('change', (e) => {
		currentSort = e.target.value;
		renderCards();
	});
}

// Compare functionality
function attachCompareListeners() {
	const checkboxes = document.querySelectorAll('.compare-input');

	checkboxes.forEach((checkbox) => {
		checkbox.addEventListener('change', (e) => {
			const casinoId = e.target.dataset.casino;

			if (e.target.checked) {
				if (compareList.length < 3) {
					compareList.push(casinoId);
				} else {
					e.target.checked = false;
					alert('You can only compare up to 3 casinos');
					return;
				}
			} else {
				compareList = compareList.filter((id) => id !== casinoId);
			}

			updateCompareBanner();
		});
	});
}

function updateCompareBanner() {
	if (compareList.length > 0) {
		compareBanner.classList.add('active');

		compareChips.innerHTML = compareList
			.map((id) => {
				const casino = casinos.find((c) => c.id === id);
				return `
                <div class="compare-chip">
                    <span>${casino.name}</span>
                    <button class="chip-remove" onclick="removeCasino('${id}')">×</button>
                </div>
            `;
			})
			.join('');

		compareBtn.disabled = compareList.length < 2;
	} else {
		compareBanner.classList.remove('active');
	}
}

// Add this new function after updateCompareBanner:
function closeCompareBanner() {
	compareBanner.classList.remove('active');
	// Optional: Keep selections or clear them
	// compareList = []; // Uncomment to clear selections when closing
	// Uncheck all checkboxes if clearing
	// document.querySelectorAll('.compare-input:checked').forEach(cb => cb.checked = false);
}

function removeCasino(casinoId) {
	compareList = compareList.filter((id) => id !== casinoId);

	// Uncheck the checkbox
	const checkbox = document.querySelector(`[data-casino="${casinoId}"]`);
	if (checkbox) checkbox.checked = false;

	updateCompareBanner();
}

// Compare button
compareBtn?.addEventListener('click', () => {
	console.log('Compare button clicked, compareList:', compareList);
	if (compareList.length >= 2) {
		console.log('Opening modal...');
		openCompareModal();
	} else {
		console.log('Need at least 2 casinos');
	}
});

// Open compare modal
function openCompareModal() {
	console.log('openCompareModal called');
	const modal = document.getElementById('compareModal');
	const table = document.getElementById('compareTable');

	console.log('Modal element:', modal);
	console.log('Table element:', table);

	// Get selected casinos
	const selectedCasinos = compareList.map((id) =>
		casinos.find((c) => c.id === id),
	);
	console.log('Selected casinos:', selectedCasinos);

	// Build table HTML
	let tableHTML = '<thead><tr><th class="compare-row-label">Feature</th>';

	// Header row with casino names and logos
	selectedCasinos.forEach((casino) => {
		tableHTML += `
			<th>
				<div class="compare-casino-header">
					<div class="compare-logo" style="background: ${casino.logoBg}">
						<img src="images/casinologos/${casino.logo}" alt="${casino.name}">
					</div>
					<div class="compare-casino-name">${casino.name}</div>
				</div>
			</th>
		`;
	});
	tableHTML += '</tr></thead><tbody>';

	// Rating row
	tableHTML += '<tr><td class="compare-row-label">Rating</td>';
	selectedCasinos.forEach((casino) => {
		tableHTML += `
			<td>
				<div class="compare-cell-content">
					<div class="compare-rating">
						${generateStars(casino.rating)}
					</div>
				</div>
			</td>
		`;
	});
	tableHTML += '</tr>';

	// Exclusive row
	tableHTML += '<tr><td class="compare-row-label">Exclusive</td>';
	selectedCasinos.forEach((casino) => {
		tableHTML += `
			<td>
				<div class="compare-cell-content">
					${
						casino.exclusive
							? '<span class="compare-exclusive-badge">⭐ EXCLUSIVE</span>'
							: '<span class="compare-empty">—</span>'
					}
				</div>
			</td>
		`;
	});
	tableHTML += '</tr>';

	// Bonus row
	tableHTML += '<tr><td class="compare-row-label">Welcome Bonus</td>';
	selectedCasinos.forEach((casino) => {
		tableHTML += `
			<td>
				<div class="compare-cell-content">
					<strong>${casino.bonus}</strong>
				</div>
			</td>
		`;
	});
	tableHTML += '</tr>';

	// Terms row
	tableHTML += '<tr><td class="compare-row-label">Terms</td>';
	selectedCasinos.forEach((casino) => {
		tableHTML += `
			<td>
				<div class="compare-terms">${casino.terms}</div>
			</td>
		`;
	});
	tableHTML += '</tr>';

	// Action row
	tableHTML += '<tr><td class="compare-row-label">Action</td>';
	selectedCasinos.forEach((casino) => {
		tableHTML += `
			<td>
				<div class="compare-cell-content">
					<a href="${casino.link}" target="_blank" rel="noopener noreferrer" class="compare-cta">Claim Offer →</a>
				</div>
			</td>
		`;
	});
	tableHTML += '</tr>';

	tableHTML += '</tbody>';

	table.innerHTML = tableHTML;

	console.log('About to add active class to modal');
	modal.classList.add('active');
	console.log('Modal classes after adding active:', modal.className);
	console.log(
		'Modal computed display:',
		window.getComputedStyle(modal).display,
	);
	console.log('Modal computed z-index:', window.getComputedStyle(modal).zIndex);

	document.body.style.overflow = 'hidden';
	console.log('Modal should now be visible');
}

function initializeTheme() {
	const savedTheme = localStorage.getItem('theme') || 'dark';
	const desktopToggle = document.getElementById('themeToggle');
	const mobileToggle = document.getElementById('mobileThemeToggle');

	// Apply saved theme
	if (savedTheme === 'light') {
		document.body.classList.add('light-theme');
		if (desktopToggle) {
			desktopToggle.querySelector('.theme-icon').textContent = '🌙';
		}
		if (mobileToggle) {
			mobileToggle.querySelector('.theme-icon').textContent = '🌙';
		}
	}

	// Function to toggle theme
	function toggleTheme() {
		document.body.classList.toggle('light-theme');
		const isLight = document.body.classList.contains('light-theme');

		const icon = isLight ? '🌙' : '☀';

		// Update both toggles
		if (desktopToggle) {
			desktopToggle.querySelector('.theme-icon').textContent = icon;
		}
		if (mobileToggle) {
			mobileToggle.querySelector('.theme-icon').textContent = icon;
		}

		localStorage.setItem('theme', isLight ? 'light' : 'dark');
	}

	// Add listeners to both toggles
	if (desktopToggle) {
		desktopToggle.addEventListener('click', toggleTheme);
	}
	if (mobileToggle) {
		mobileToggle.addEventListener('click', toggleTheme);
	}
}

// Animated stats counter
function animateStats() {
	const statNumbers = document.querySelectorAll('.stat-number[data-target]');

	const observer = new IntersectionObserver((entries) => {
		entries.forEach((entry) => {
			if (entry.isIntersecting) {
				const target = parseInt(entry.target.dataset.target);
				animateValue(entry.target, 0, target, 1500);
				observer.unobserve(entry.target);
			}
		});
	});

	statNumbers.forEach((stat) => observer.observe(stat));
}

function animateValue(element, start, end, duration) {
	const range = end - start;
	const increment = range / (duration / 16);
	let current = start;

	const timer = setInterval(() => {
		current += increment;
		if (current >= end) {
			current = end;
			clearInterval(timer);
		}
		element.textContent = Math.floor(current);
	}, 16);
}

// Navbar scroll behavior
function initializeNav() {
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

// Close compare modal (global function for onclick handlers)
window.closeCompareModal = function () {
	const modal = document.getElementById('compareModal');
	modal.classList.remove('active');
	document.body.style.overflow = '';
};

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
	anchor.addEventListener('click', function (e) {
		e.preventDefault();
		const target = document.querySelector(this.getAttribute('href'));

		if (target) {
			target.scrollIntoView({
				behavior: 'smooth',
				block: 'start',
			});

			// Update active nav link
			document.querySelectorAll('.nav-link').forEach((link) => {
				link.classList.remove('active');
			});
			this.classList.add('active');
		}
	});
});

// Quick View Modal Functions
function openQuickView(casinoId) {
	const casino = casinos.find((c) => c.id === casinoId);
	if (!casino) return;

	const modal = document.getElementById('quickViewModal');
	const body = document.getElementById('quickViewBody');

	body.innerHTML = `
		<div class="quick-view-header">
			<div class="quick-view-logo" style="background: ${casino.logoBg}">
				<img src="images/casinologos/${casino.logo}" alt="${casino.name}">
			</div>
			<h2 class="quick-view-name">${casino.name}</h2>
			<div class="quick-view-rating">
				${generateStars(casino.rating)}
			</div>
			${
				casino.exclusive
					? '<span class="compare-exclusive-badge">⭐ EXCLUSIVE</span>'
					: ''
			}
		</div>
		
		<div class="quick-view-bonus">
			<h3>Welcome Bonus</h3>
			<p>${casino.bonus}</p>
		</div>
		
		<p class="quick-view-description">${casino.description}</p>
		
		<div class="quick-view-features">
			${casino.features
				.map(
					(f) =>
						`<span class="quick-view-feature">${getFeatureIcon(f)} ${f}</span>`,
				)
				.join('')}
		</div>
		
		<div class="quick-view-terms">${casino.terms}</div>
		
		<div class="quick-view-actions">
			<a href="${casino.reviewLink}" class="quick-view-btn quick-view-btn-secondary">
				Read Review
			</a>
			<a href="${
				casino.link
			}" target="_blank" rel="noopener noreferrer" class="quick-view-btn quick-view-btn-primary">
				Claim Offer →
			</a>
		</div>
	`;

	modal.classList.add('active');
	document.body.style.overflow = 'hidden';
}

function closeQuickView() {
	const modal = document.getElementById('quickViewModal');
	modal.classList.remove('active');
	document.body.style.overflow = '';
}

// Make it globally accessible
window.openQuickView = openQuickView;
window.closeQuickView = closeQuickView;

// Bonus Calculator - With Safety Checks
document.addEventListener('DOMContentLoaded', () => {
	// Only run if calculator elements exist on the page
	const calcExists = document.querySelector('.calc-tab');

	if (calcExists) {
		// Tab switching
		const tabs = document.querySelectorAll('.calc-tab');
		const contents = document.querySelectorAll('.calculator-content');

		tabs.forEach((tab) => {
			tab.addEventListener('click', () => {
				// Remove active from all
				tabs.forEach((t) => t.classList.remove('active'));
				contents.forEach((c) => c.classList.remove('active'));

				// Add active to clicked
				tab.classList.add('active');
				const tabId = tab.dataset.tab;
				const targetContent = document.getElementById(`${tabId}-calc`);
				if (targetContent) {
					targetContent.classList.add('active');
				}
			});
		});

		// Free Spins Calculator
		const spinInputs = ['spinCount', 'spinValue', 'spinWagering'];
		spinInputs.forEach((id) => {
			const input = document.getElementById(id);
			if (input) {
				input.addEventListener('input', calculateSpins);
				input.addEventListener('keypress', (e) => {
					if (e.key === 'Enter') calculateSpins();
				});
			}
		});

		// Match Bonus Calculator
		const matchInputs = [
			'depositAmount',
			'bonusPercentage',
			'wageringRequirement',
		];
		matchInputs.forEach((id) => {
			const input = document.getElementById(id);
			if (input) {
				input.addEventListener('input', calculateMatch);
				input.addEventListener('keypress', (e) => {
					if (e.key === 'Enter') calculateMatch();
				});
			}
		});

		// Initial calculations only if elements exist
		if (document.getElementById('spinCount')) {
			calculateSpins();
		}
		if (document.getElementById('depositAmount')) {
			calculateMatch();
		}
	}
});

function calculateSpins() {
	// Safety checks
	const spinCountEl = document.getElementById('spinCount');
	const spinValueEl = document.getElementById('spinValue');
	const spinWageringEl = document.getElementById('spinWagering');

	if (!spinCountEl || !spinValueEl || !spinWageringEl) return;

	const spinCount = parseFloat(spinCountEl.value) || 0;
	const spinValue = parseFloat(spinValueEl.value) || 0;
	const wagering = parseFloat(spinWageringEl.value) || 0;

	const totalValue = spinCount * spinValue;
	const mustWagerAmount = totalValue * wagering;

	const totalSpinValueEl = document.getElementById('totalSpinValue');
	const wageringTypeEl = document.getElementById('wageringType');
	const mustWagerEl = document.getElementById('mustWager');
	const mustWagerItemEl = document.getElementById('mustWagerItem');

	if (totalSpinValueEl) {
		totalSpinValueEl.textContent = `£${totalValue.toFixed(2)}`;
	}

	if (wageringTypeEl && mustWagerItemEl) {
		if (wagering === 0) {
			wageringTypeEl.textContent = 'Wager Free ✓';
			wageringTypeEl.style.color = 'var(--gold)';
			mustWagerItemEl.style.display = 'none';
		} else {
			wageringTypeEl.textContent = `${wagering}x Wagering`;
			wageringTypeEl.style.color = 'var(--text-primary)';
			if (mustWagerEl) {
				mustWagerEl.textContent = `£${mustWagerAmount.toFixed(2)}`;
			}
			mustWagerItemEl.style.display = 'block';
		}
	}

	animateResults('spinsResults');
}

function calculateMatch() {
	// Safety checks
	const depositEl = document.getElementById('depositAmount');
	const bonusPercentEl = document.getElementById('bonusPercentage');
	const wageringEl = document.getElementById('wageringRequirement');

	if (!depositEl || !bonusPercentEl || !wageringEl) return;

	const deposit = parseFloat(depositEl.value) || 0;
	const bonusPercent = parseFloat(bonusPercentEl.value) || 0;
	const wagering = parseFloat(wageringEl.value) || 0;

	const bonusAmount = deposit * (bonusPercent / 100);
	const totalBalance = deposit + bonusAmount;
	const amountToWager = (deposit + bonusAmount) * wagering;

	const bonusAmountEl = document.getElementById('bonusAmount');
	const totalBalanceEl = document.getElementById('totalBalance');
	const amountToWagerEl = document.getElementById('amountToWager');

	if (bonusAmountEl) {
		bonusAmountEl.textContent = `£${bonusAmount.toFixed(2)}`;
	}
	if (totalBalanceEl) {
		totalBalanceEl.textContent = `£${totalBalance.toFixed(2)}`;
	}
	if (amountToWagerEl) {
		amountToWagerEl.textContent = `£${amountToWager.toLocaleString('en-GB', {
			minimumFractionDigits: 2,
			maximumFractionDigits: 2,
		})}`;
	}

	animateResults('matchResults');
}

function animateResults(containerId) {
	const container = document.getElementById(containerId);
	if (!container) return;

	const results = container.querySelectorAll('.result-value');
	results.forEach((result) => {
		result.style.animation = 'none';
		setTimeout(() => {
			result.style.animation = 'fadeInUp 0.5s ease';
		}, 10);
	});
}

// Hamburger Menu - DEBUG VERSION
document.addEventListener('DOMContentLoaded', () => {
	const hamburger = document.getElementById('hamburger');
	const mobileMenu = document.getElementById('mobileMenu');
	const body = document.body;

	console.log('Hamburger:', hamburger);
	console.log('Mobile Menu:', mobileMenu);

	if (hamburger && mobileMenu) {
		hamburger.addEventListener('click', () => {
			console.log('Hamburger clicked!');
			hamburger.classList.toggle('active');
			mobileMenu.classList.toggle('active');
			body.classList.toggle('menu-open');
			console.log('Mobile menu classes:', mobileMenu.className);
		});

		// Close menu when clicking a link
		const mobileLinks = document.querySelectorAll('.mobile-nav-link');
		mobileLinks.forEach((link) => {
			link.addEventListener('click', () => {
				hamburger.classList.remove('active');
				mobileMenu.classList.remove('active');
				body.classList.remove('menu-open');
			});
		});
	} else {
		console.error('Hamburger or mobile menu not found!');
	}
});

// Limit compare selections on mobile
function updateCompareBanner() {
	const isMobile = window.innerWidth <= 768;
	const maxCompare = isMobile ? 2 : 3; // Limit to 2 on mobile, 3 on desktop

	if (compareList.length > 0) {
		compareBanner.classList.add('active');

		compareChips.innerHTML = compareList
			.map((id) => {
				const casino = casinos.find((c) => c.id === id);
				return `
                <div class="compare-chip">
                    <span>${casino.name}</span>
                    <button class="chip-remove" onclick="removeCasino('${id}')">×</button>
                </div>
            `;
			})
			.join('');

		compareBtn.disabled = compareList.length < 2;

		// Disable checkboxes if limit reached
		const checkboxes = document.querySelectorAll('.compare-input');
		checkboxes.forEach((checkbox) => {
			if (!checkbox.checked && compareList.length >= maxCompare) {
				checkbox.disabled = true;
				checkbox.parentElement.style.opacity = '0.5';
			} else {
				checkbox.disabled = false;
				checkbox.parentElement.style.opacity = '1';
			}
		});
	} else {
		compareBanner.classList.remove('active');
	}
}

// Re-enable checkboxes when screen size changes
window.addEventListener('resize', () => {
	if (compareList.length > 0) {
		updateCompareBanner();
	}
});

// Bookmark Modal - Smart & Non-Intrusive (Shows to First-Time Visitors)
document.addEventListener('DOMContentLoaded', () => {
	const bookmarkModal = document.getElementById('bookmarkModal');
	const bookmarkOverlay = document.getElementById('bookmarkOverlay');
	const bookmarkClose = document.getElementById('bookmarkClose');
	const bookmarkYes = document.getElementById('bookmarkYes');
	const bookmarkNo = document.getElementById('bookmarkNo');

	// Check user preferences and history
	const hasSeenBookmark = localStorage.getItem('hasSeenBookmark');
	const hasBookmarked = localStorage.getItem('hasBookmarked');
	const lastShown = localStorage.getItem('bookmarkLastShown');
	const totalVisits = parseInt(localStorage.getItem('totalVisits') || '0');
	const shownThisSession = sessionStorage.getItem('bookmarkShownThisSession');
	const now = Date.now();
	const threeDaysMs = 3 * 24 * 60 * 60 * 1000; // Show at most every 3 days

	// Track total visits
	localStorage.setItem('totalVisits', (totalVisits + 1).toString());

	// Detect bookmark keyboard shortcut (Ctrl+D or Cmd+D)
	document.addEventListener('keydown', (e) => {
		if ((e.ctrlKey || e.metaKey) && e.key === 'd') {
			localStorage.setItem('hasBookmarked', 'true');
			localStorage.setItem('hasSeenBookmark', 'never'); // Don't show again
		}
	});

	// Track when user leaves for external link
	document.querySelectorAll('a[target="_blank"]').forEach((link) => {
		link.addEventListener('click', () => {
			sessionStorage.setItem('leftForExternal', 'true');
			sessionStorage.setItem('leftTime', Date.now());
		});
	});

	// Show modal when user returns (with smart conditions)
	window.addEventListener('focus', () => {
		const leftForExternal = sessionStorage.getItem('leftForExternal');
		const leftTime = sessionStorage.getItem('leftTime');

		// Different conditions for first-time vs returning visitors
		const isFirstTimeVisitor = totalVisits === 1;

		// CONDITIONS:
		// First-time visitors: Show if they left for external link and been gone 5+ seconds
		// Returning visitors: All the strict conditions apply
		const shouldShow =
			leftForExternal === 'true' &&
			leftTime &&
			Date.now() - parseInt(leftTime) > 5000 && // 5 seconds minimum
			hasSeenBookmark !== 'never' &&
			hasBookmarked !== 'true' &&
			shownThisSession !== 'true' && // Only once per session
			(isFirstTimeVisitor || // Show to first-timers
				!lastShown ||
				now - parseInt(lastShown) > threeDaysMs); // Or 3+ days for returning

		if (shouldShow) {
			setTimeout(() => {
				if (bookmarkModal) {
					// Update message based on visitor type and page
					const isReviewPage = window.location.pathname.includes('/reviews/');
					const modalTitle = bookmarkModal.querySelector('h3');
					const modalText = bookmarkModal.querySelector('p');

					if (isFirstTimeVisitor) {
						modalTitle.textContent = 'Welcome! 👋';
						modalText.textContent =
							'Bookmark us to easily compare the best UK casino bonuses anytime!';
					} else if (isReviewPage) {
						modalTitle.textContent = 'Find More Great Offers!';
						modalText.textContent =
							'Bookmark this site to quickly compare exclusive casino bonuses.';
					} else {
						modalTitle.textContent = 'Enjoying Our Reviews?';
						modalText.textContent =
							'Bookmark this page to easily find the best casino offers!';
					}

					bookmarkModal.classList.add('active');
					document.body.style.overflow = 'hidden';
					sessionStorage.setItem('bookmarkShownThisSession', 'true'); // Only once per session
				}
			}, 1000);

			sessionStorage.removeItem('leftForExternal');
			sessionStorage.removeItem('leftTime');
		}
	});

	// Close modal functions
	function closeBookmarkModal() {
		if (bookmarkModal) {
			bookmarkModal.classList.remove('active');
			document.body.style.overflow = '';
		}
	}

	if (bookmarkClose) {
		bookmarkClose.addEventListener('click', closeBookmarkModal);
	}

	if (bookmarkOverlay) {
		bookmarkOverlay.addEventListener('click', closeBookmarkModal);
	}

	// "Remind Me Later" - show again in 3 days
	if (bookmarkYes) {
		bookmarkYes.addEventListener('click', () => {
			localStorage.setItem('bookmarkLastShown', Date.now().toString());
			closeBookmarkModal();
		});
	}

	// "Don't Show Again" - never show
	if (bookmarkNo) {
		bookmarkNo.addEventListener('click', () => {
			localStorage.setItem('hasSeenBookmark', 'never');
			closeBookmarkModal();
		});
	}
});
