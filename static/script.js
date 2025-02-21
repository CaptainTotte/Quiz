const categoriesUrl = '/categories';
const questionsUrl = (points) => `/questions/${points}`;
const points = ['200', '400', '600', '800', '1000'];
const gameBoard = document.getElementById('game-board');
const modal = document.getElementById('modal');
const questionContent = document.getElementById('question-content');
const resetButton = document.getElementById('reset-button');

// Load categories and questions
async function loadGame() {
    const categoriesResponse = await fetch(categoriesUrl);
    const categoriesData = await categoriesResponse.json();
    const categories = categoriesData.categories;

    // Create header row
    const headerRow = gameBoard.insertRow();
    categories.forEach(category => {
        const th = document.createElement('th');
        th.innerText = category;
        headerRow.appendChild(th);
    });

    // Create question rows
    points.forEach(point => {
        const row = gameBoard.insertRow();
        categories.forEach(category => {
            const cell = row.insertCell();
            cell.innerText = point;
            cell.dataset.category = category; // Store category in dataset
            cell.dataset.points = point; // Store points in dataset
            cell.onclick = () => showQuestion(category, point, cell); // Pass the clicked cell
        });
    });
}

// Show the question in modal
async function showQuestion(category, point, clickedCell) {
    const response = await fetch(questionsUrl(point));
    const questionsData = await response.json();
    const question = questionsData.questions.find(q => q.category === category);

    if (question) {
        // Calculate the position of the clicked cell relative to the viewport
        const rect = clickedCell.getBoundingClientRect();
        const centerX = window.innerWidth / 2 - rect.left - rect.width / 2;
        const centerY = window.innerHeight / 2 - rect.top - rect.height / 2;

        // Set custom properties for the animation
        clickedCell.style.setProperty('--start-x', `${-centerX}px`);
        clickedCell.style.setProperty('--start-y', `${-centerY}px`);
        clickedCell.style.setProperty('--start-top', `${rect.top}px`);
        clickedCell.style.setProperty('--start-left', `${rect.left}px`);

        // Add zoom-in effect to the clicked cell
        clickedCell.classList.add('zoom-in');

        // Wait for the animation to finish before showing the modal
        clickedCell.addEventListener('animationend', () => {
            clickedCell.classList.remove('zoom-in');
            clickedCell.classList.add('hidden'); // Hide the cell after animation

            // Show the modal and set its content
            modal.style.display = 'flex';

            if (question.type === 'text') {
                questionContent.innerHTML = `
                    <div style="margin: 30px;">
                        <p style="font-size: 3rem; font-weight: bold; text-align: center;">${question.content}</p>
                    </div>
                `;
            } else if (question.type === 'image') {
                questionContent.innerHTML = `
                    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                        <img src="${question.content}" alt="Question" style="max-width: 70%; max-height: 70%; object-fit: contain;">
                    </div>
                `;
            } else if (question.type === 'video') {
                let videoUrl = question.content;
                if (videoUrl.includes('youtube.com') || videoUrl.includes('youtu.be')) {
                    videoUrl = videoUrl.replace(/(\?|&)list=.*/, '');
                    videoUrl += (videoUrl.includes('?') ? '&' : '?') + 'autoplay=1&controls=0&modestbranding=1&rel=0&disablekb=1';
                    questionContent.innerHTML = `
                        <div class="video-container">
                            <iframe src="${videoUrl}" title="Video Question" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                            <div class="youtube-overlay"></div>
                        </div>
                    `;
                } else if (videoUrl.includes('vimeo.com')) {
                    videoUrl = videoUrl.replace(/(\?|&)title=.*/, '');
                    videoUrl += (videoUrl.includes('?') ? '&' : '?') + 'autoplay=1&title=0&byline=0&portrait=0';
                    questionContent.innerHTML = `<iframe src="${videoUrl}" title="Video Question" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>`;
                }
            } else if (question.type === 'sound') {
                questionContent.innerHTML = `
                    <audio controls autoplay>
                        <source src="${question.content}" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                `;
            }
        }, { once: true });
    }
}

// Reset all cards
resetButton.addEventListener('click', () => {
    const cells = document.querySelectorAll('td');
    cells.forEach(cell => {
        cell.classList.remove('hidden'); // Remove the hidden class
        cell.classList.add('pop-effect'); // Add pop effect
        cell.addEventListener('animationend', () => {
            cell.classList.remove('pop-effect');
        }, { once: true });
    });
});

// Close the modal when 'ESC' is pressed
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        closeModal();
    }
});

function closeModal() {
    modal.style.display = 'none';
    questionContent.innerHTML = ''; // Clear content on close
}

window.onload = loadGame; // Load game when the page loads