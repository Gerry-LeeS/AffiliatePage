// All casino review pages - add new casinos here
const casinoPages = [
	{ title: 'Luna Casino', url: '/reviews/lunacasino', rating: 5 },
	{ title: 'BOYLE Casino', url: '/reviews/boylecasino', rating: 5 },
	{ title: 'PlayOJO', url: '/reviews/playojo', rating: 5 },
	{ title: 'Swift Casino', url: '/reviews/swiftcasino', rating: 5 },
	{ title: 'BestOdds', url: '/reviews/bestodds', rating: 5 },
	{ title: 'NetBet', url: '/reviews/netbet', rating: 5 },
	{ title: 'BresBet', url: '/reviews/bresbet', rating: 4.5 },
	{ title: 'BetTOM', url: '/reviews/bettom', rating: 4.5 },
	{ title: 'LiveScore Bet', url: '/reviews/livescorebet', rating: 4.5 },
	{ title: 'Kwiff', url: '/reviews/kwiff', rating: 4.5 },
	// { title: 'Ladbrokes', url: '/reviews/ladbrokes', rating: 5 },
	// { title: 'Gala Bingo', url: '/reviews/galabingo', rating: 4.5 },
	// { title: 'Gala Casino', url: '/reviews/galacasino', rating: 4 },
	// Add new casino reviews like this:
	// { title: "New Casino Name", url: "/reviews/new-casino", rating: 4.5 }
];

// Get total
function getTotalCasinoCount() {
	return casinoPages.length;
}