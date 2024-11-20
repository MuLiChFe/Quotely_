document.addEventListener('DOMContentLoaded', function () {
    filmsData = JSON.parse(films);
    // 输出数据到控制台验证

    const filmsRow = document.getElementById('films-row');
    const modal = document.getElementById('bookModal');
    const addToLibraryBtn = document.getElementById('addToLibraryBtn');
    let currentFilmId = null;

    // 动态生成电影卡片
    filmsData.forEach(film => {
        const filmCard = document.createElement('div');
        filmCard.classList.add('card','w-full','p-0');

        filmCard.innerHTML = `
            <div class="" data-bs-toggle="modal" data-bs-target="#bookModal" data-film-id="${film.id}">
                <img src="${film.image_link}" class="card-img-top book-image" alt="${film.display_name}">
                <div class="card-body">
                    <h5 class="card-title">${film.display_name}</h5>
                    <p class="card-text">by ${film.author}</p>
                    <div style="position: absolute; bottom: 10px; right: 5px">
                        <span class="badge bg-secondary">${film.type}</span>
                        <span class="badge bg-light text-dark">Year ${film.year_levels}</span>
                    </div>
                </div>
            </div>
        `;

        filmsRow.appendChild(filmCard);
    });

    // Modal 内容更新
    modal.addEventListener('show.bs.modal', function(event) {
        const button = event.relatedTarget;
        currentFilmId = button.getAttribute('data-film-id');
        const film = filmsData.find(f => f.id == currentFilmId);

        document.getElementById('bookModalLabel').textContent = film.display_name;
        document.getElementById('modalBookImage').src = film.image_link;
        document.getElementById('modalBookImage').alt = film.display_name;
        document.getElementById('modalBookAuthor').textContent = film.author;
        document.getElementById('modalBookType').textContent = film.type;
        document.getElementById('modalBookYear').textContent = film.year_levels;

        // Reset the Add to Library button
        addToLibraryBtn.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle me-2" viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
            </svg>
            Add to Library
        `;
        addToLibraryBtn.classList.remove('btn-success');
        addToLibraryBtn.classList.add('btn-primary');
        addToLibraryBtn.disabled = false;
    });

    // 添加到库的按钮事件
    addToLibraryBtn.addEventListener('click', function() {
        this.innerHTML = 'Added to Library';
        this.classList.remove('btn-primary');
        this.classList.add('btn-success');
        this.disabled = true;
        console.log(`Added ${filmsData.find(f => f.id == currentFilmId).display_name} to library`);
    });
});
