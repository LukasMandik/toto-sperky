window.addEventListener('DOMContentLoaded', function() {
    const searchInputs = document.querySelectorAll('.search-input');
    const suggestionsBoxes = document.querySelectorAll('.suggestions-box');
    const searchForms = document.querySelectorAll('.search-form'); // Získajte všetky formuláre

    if (typeof(Storage) !== "undefined") {
        searchInputs.forEach((searchInput, index) => {
            const suggestionsBox = suggestionsBoxes[index];
            const searchForm = searchForms[index]; // Získajte príslušný formulár

            // Načítajte posledný hľadaný výraz z localStorage
            const lastQuery = localStorage.getItem('lastSearchQuery');
            if (lastQuery) {
                searchInput.value = lastQuery;
            } else {
                searchInput.value = '';
            }

            searchInput.addEventListener('input', function() {
                const query = searchInput.value;
                if (query.length > 0) {
                    // Nastavte kurzor na koniec textu
                    setTimeout(() => {
                        searchInput.setSelectionRange(query.length, query.length);
                    }, 0);
                    fetch(`/search_suggestions?q=${query}`)
                        .then(response => response.json())
                        .then(data => {
                            suggestionsBox.innerHTML = '';
                            data.forEach(item => {
                                const suggestionItem = document.createElement('div');
                                suggestionItem.classList.add('suggestion-item');

                                if (item.image_url) {
                                    const suggestionImage = document.createElement('img');
                                    suggestionImage.classList.add('suggestion-image');
                                    suggestionImage.src = item.image_url;
                                    suggestionImage.alt = item.name;
                                    suggestionItem.appendChild(suggestionImage);
                                } else if (item.video_url) {
                                    const suggestionVideo = document.createElement('video');
                                    suggestionVideo.classList.add('suggestion-video');
                                    suggestionVideo.src = item.video_url;
                                    suggestionVideo.controls = false;
                                    suggestionVideo.autoplay = true;
                                    suggestionVideo.muted = true;
                                    suggestionVideo.loop = true; // Pridanie loop
                                    suggestionVideo.playsInline = true; // Zabránenie automatickému zväčšeniu videa na mobile
                                    suggestionItem.appendChild(suggestionVideo);
                                }

                                const suggestionTextContainer = document.createElement('div');
                                suggestionTextContainer.classList.add('text');

                                const suggestionTextName = document.createElement('p');
                                suggestionTextName.innerHTML = highlightText(item.name, query);
                                
                                const suggestionTextTypeContainer = document.createElement('div');
                                suggestionTextTypeContainer.classList.add('type-container');

                                const suggestionTextFoundIn = document.createElement('p');
                                suggestionTextFoundIn.textContent = 'Nájdené v';
                                const suggestionTextType = document.createElement('p');
                                suggestionTextType.innerHTML = highlightText(item.type, query);

                                suggestionTextTypeContainer.appendChild(suggestionTextFoundIn);
                                suggestionTextTypeContainer.appendChild(suggestionTextType);

                                const suggestionTextDescription = document.createElement('p');
                                suggestionTextDescription.innerHTML = highlightText(item.description, query, true);

                                suggestionTextContainer.appendChild(suggestionTextName);
                                suggestionTextContainer.appendChild(suggestionTextDescription);
                                suggestionTextContainer.appendChild(suggestionTextTypeContainer);
                                suggestionItem.appendChild(suggestionTextContainer);

                                suggestionItem.addEventListener('click', function() {
                                    searchForm.submit(); // Použite príslušný formulár
                                });
                                suggestionsBox.appendChild(suggestionItem);
                            });
                        });
                } else {
                    suggestionsBox.innerHTML = '';
                }
            });

            // Pridaj event listener pre focus a blur
            searchInput.addEventListener('focus', function() {
                suggestionsBox.style.display = 'block';
                suggestionsBox.style.maxHeight = '0';
                setTimeout(() => {
                    suggestionsBox.style.maxHeight = '240px';
                }, 10); // Malé oneskorenie pre plynulý efekt
            });

            searchInput.addEventListener('blur', function() {
                setTimeout(() => {
                    suggestionsBox.style.maxHeight = '0';
                    setTimeout(() => {
                        suggestionsBox.style.display = 'none';
                    }, 300); // Čas pre plynulý efekt
                }, 200); // Malé oneskorenie, aby sa umožnilo kliknutie na návrhy
            });
        });
    } else {
        console.error("localStorage nie je podporovaný na tomto zariadení.");
    }

    function highlightText(text, query, isDescription = false) {
        const regex = new RegExp(`(${query})`, 'gi');
        if (isDescription) {
            const match = text.match(regex);
            if (match) {
                const start = Math.max(text.indexOf(match[0]) - 40, 0);
                const end = Math.min(start + match[0].length + 120, text.length);
                return text.substring(start, end).replace(regex, '<span class="highlight">$1</span>');
            }
        }
        return text.replace(regex, '<span class="highlight">$1</span>');
    }
});