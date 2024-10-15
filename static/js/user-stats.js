document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.getElementById('search-button');
    const searchIconImg = document.getElementById('search-icon-img');
    const searchBar = document.getElementById('search-bar');
    const searchContainer = document.getElementById('search-container');

    let isSearchOpen = false;

    function updateSearchIcon() {
        if (searchBar.value.trim() !== "") {
            searchIconImg.src = "/static/images/send.png"; // Cambia a "send"
        } else if (isSearchOpen) {
            searchIconImg.src = "/static/images/close-searchbox.png"; // Torna a "close"
        } else {
            searchIconImg.src = "/static/images/search-icon.png"; // Torna a "search"
        }
    }

    searchButton.addEventListener('click', function() {
        if (searchBar.value.trim() !== "") {
            // Logica per eseguire la ricerca
            const query = searchBar.value.trim();
            console.log('Searching for:', query);
            // Puoi aggiungere qui la logica per gestire la ricerca
        } else {
            isSearchOpen = !isSearchOpen;
            searchContainer.classList.toggle('show');
            updateSearchIcon();

            if (!isSearchOpen) {
                searchBar.value = ""; // Reset input quando si chiude
            }
        }
    });

    searchBar.addEventListener('input', updateSearchIcon);
});
