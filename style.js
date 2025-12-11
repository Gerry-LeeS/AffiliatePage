const now = new Date();
const month = now.toLocaleString('default', { month: 'long' }); // e.g. "November"
const year = now.getFullYear();

// Footer year
const yearElement = document.getElementById('year');
if (yearElement) {
	yearElement.textContent = year;
}

// Header and subheader months/years
const monthElement = document.getElementById('month');
if (monthElement) {
	monthElement.textContent = month;
}

const yearBonusElement = document.getElementById('year-bonus');
if (yearBonusElement) {
	yearBonusElement.textContent = year;
}

const monthSubElement = document.getElementById('month-sub');
if (monthSubElement) {
	monthSubElement.textContent = month;
}

const yearSubElement = document.getElementById('year-sub');
if (yearSubElement) {
	yearSubElement.textContent = year;
}

const toggleBtn = document.getElementById('theme-toggle');

if (toggleBtn) {
	// Check local storage on load
	if (localStorage.getItem('theme') === 'dark') {
		document.body.classList.add('dark-mode');
		toggleBtn.textContent = '☀️';
	}
	toggleBtn.addEventListener('click', () => {
		document.body.classList.toggle('dark-mode');

		if (document.body.classList.contains('dark-mode')) {
			toggleBtn.textContent = '☀️';
			localStorage.setItem('theme', 'dark');
		} else {
			toggleBtn.textContent = '🌙';
			localStorage.setItem('theme', 'light');
		}
	});
}

let lastScrollY = window.scrollY;
const navbar = document.querySelector('.nav-bar');

if (navbar) {
	window.addEventListener('scroll', () => {
		if (window.scrollY > lastScrollY && window.scrollY > 100) {
			navbar.classList.add('hidden');
		} else {
			navbar.classList.remove('hidden');
		}
		lastScrollY = window.scrollY;
	});
}
// Replace the existing debug code with this more detailed version
document.addEventListener(
	'click',
	(e) => {
		if (e.target.tagName === 'A' || e.target.closest('a')) {
			const link = e.target.tagName === 'A' ? e.target : e.target.closest('a');
			console.log('Raw href attribute:', link.getAttribute('href'));
			console.log('Link.href property:', link.href);
			console.log('Target:', link.target);
			console.log('Link element:', link);
			console.log('Default prevented:', e.defaultPrevented);
		}
	},
	true
);

// Add this to see if preventDefault is being called
document.addEventListener(
	'click',
	(e) => {
		if (e.target.tagName === 'A' || e.target.closest('a')) {
			console.log('Click event:', e);
			console.log('Default prevented:', e.defaultPrevented);
		}
	},
	true
);
