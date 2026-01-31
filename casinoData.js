// All casino review pages - add new casinos here
const casinoPages = [
	{ title: 'Luna Casino', url: '/reviews/lunacasino.html', rating: 5 },
	{ title: 'BOYLE Casino', url: '/reviews/boylecasino.html', rating: 5 },
	{ title: 'PlayOJO', url: '/reviews/playojo.html', rating: 5 },
	{ title: 'Swift Casino', url: '/reviews/swiftcasino.html', rating: 5 },
	{ title: 'NetBet', url: '/reviews/netbet.html', rating: 5 },
	{ title: 'BresBet', url: '/reviews/bresbet.html', rating: 4.5 },
	{ title: 'BetTOM', url: '/reviews/bettom.html', rating: 4.5 },
	{ title: 'LiveScore Bet', url: '/reviews/livescorebet.html', rating: 4.5 },
	{ title: 'Kwiff', url: '/reviews/kwiff.html', rating: 4.5 },
	// { title: 'Ladbrokes', url: '/reviews/ladbrokes.html', rating: 5 },
	// { title: 'Gala Bingo', url: '/reviews/galabingo.html', rating: 4.5 },
	// { title: 'Gala Casino', url: '/reviews/galacasino.html', rating: 4 },
	// Add new casino reviews like this:
	// { title: "New Casino Name", url: "/reviews/new-casino.html", rating: 4.5 }
];

// Get total count for stats
function getTotalCasinoCount() {
	return casinoPages.length;
}
