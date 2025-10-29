document.getElementById('year').textContent = new Date().getFullYear();

const toggleBtn = document.getElementById('theme-toggle');

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


 let lastScrollY = window.scrollY;
  const navbar = document.querySelector('.nav-bar');

  window.addEventListener('scroll', () => {
    if (window.scrollY > lastScrollY && window.scrollY > 100) {
      navbar.classList.add('hidden');
    } else {
      navbar.classList.remove('hidden');
    }
    lastScrollY = window.scrollY;
  });
