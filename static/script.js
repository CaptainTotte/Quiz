const categoriesUrl = '/categories';
const questionsUrl = (points) => `/questions/${points}`;
const points = ['200', '400', '600', '800', '1000'];
const gameBoard = document.getElementById('game-board');
const modal = document.getElementById('modal');
const questionContent = document.getElementById('question-content');

// Ladda kategorier och frågor
async function loadGame() {
    const categoriesResponse = await fetch(categoriesUrl);
    const categoriesData = await categoriesResponse.json();
    const categories = categoriesData.categories;

    // Skapa rubrikrad
    const headerRow = gameBoard.insertRow();
    categories.forEach(category => {
        const th = document.createElement('th');
        th.innerText = category;
        headerRow.appendChild(th);
    });

    // Skapa frågerader
    points.forEach(point => {
        const row = gameBoard.insertRow();
        categories.forEach(category => {
            const cell = row.insertCell();
            cell.innerText = point;
            cell.onclick = () => showQuestion(category, point); // Visa fråga vid klick
        });
    });
}

// Visa frågan i modalen
async function showQuestion(category, point) {
    const response = await fetch(questionsUrl(point));
    const questionsData = await response.json();
    const question = questionsData.questions.find(q => q.category === category);
    
    if (question) {
        if (question.type === 'text') {
            questionContent.innerHTML = `<p style="font-size: 3rem; font-weight: bold; text-align: center;">${question.content}</p>`;
        } else if (question.type === 'image') {
            questionContent.innerHTML = `
                <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                    <img src="${question.content}" alt="Question" style="max-width: 70%; max-height: 70%; object-fit: contain;">
                </div>
            `;
        } else if (question.type === 'video') {
            // Kolla om videon är från YouTube eller Vimeo
            let videoUrl = question.content;
            if (videoUrl.includes('youtube.com') || videoUrl.includes('youtu.be')) {
                // YouTube-video: Ta bort titel och kontroller
                videoUrl = videoUrl.replace(/(\?|&)list=.*/, ''); // Ta bort spellisteparameter
                videoUrl += (videoUrl.includes('?') ? '&' : '?') + 'autoplay=1&controls=0&modestbranding=1&rel=0&disablekb=1';
                questionContent.innerHTML = `
                    <div class="video-container">
                        <iframe src="${videoUrl}" title="Video Question" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                        <div class="youtube-overlay"></div>
                    </div>
                `;
            } else if (videoUrl.includes('vimeo.com')) {
                // Vimeo-video: Ta bort titel och kontroller
                videoUrl = videoUrl.replace(/(\?|&)title=.*/, ''); // Ta bort befintlig titelparameter
                videoUrl += (videoUrl.includes('?') ? '&' : '?') + 'autoplay=1&title=0&byline=0&portrait=0';
                questionContent.innerHTML = `<iframe src="${videoUrl}" title="Video Question" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>`;
            }
        }

        modal.style.display = 'flex'; // Visa modalen som flex
    }
}

// Stäng modalen när 'ESC' trycks
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        closeModal();
    }
});

function closeModal() {
    modal.style.display = 'none';
    questionContent.innerHTML = ''; // Rensa innehåll vid stängning
}

window.onload = loadGame; // Ladda spelet när sidan laddas