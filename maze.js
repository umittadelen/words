const maze = document.getElementById("maze");
const cells = [];

for (let i = 0; i < 10; i++) {
    cells[i] = [];
    for (let j = 0; j < 10; j++) {
        cells[i][j] = document.createElement("div");
        cells[i][j].classList.add("cell");
        cells[i][j].setAttribute("data-i", i);
        cells[i][j].setAttribute("data-j", j);
        maze.appendChild(cells[i][j]);
    }
}

function getCell(i, j) {
    return cells[i][j];
}

function removeWall(current, next) {
    const currentI = parseInt(current.getAttribute("data-i"));
    const currentJ = parseInt(current.getAttribute("data-j"));
    const nextI = parseInt(next.getAttribute("data-i"));
    const nextJ = parseInt(next.getAttribute("data-j"));

    if (currentI < nextI) {
        current.style.borderBottom = "none";
        next.style.borderTop = "none";
    } else if (currentI > nextI) {
        current.style.borderTop = "none";
        next.style.borderBottom = "none";
    } else if (currentJ < nextJ) {
        current.style.borderRight = "none";
        next.style.borderLeft = "none";
    } else if (currentJ > nextJ) {
        current.style.borderLeft = "none";
        next.style.borderRight = "none";
    }
}

const start = cells[0][0];
const end = cells[9][9];
const path = [];
let current = start;

path.push(current);
current.classList.add("path");

while (current !== end) {
    const possibleDirections = [];
    const currentI = parseInt(current.getAttribute("data-i"));
    const currentJ = parseInt(current.getAttribute("data-j"));

    if (currentI > 0) {
        possibleDirections.push(getCell(currentI - 1, currentJ));
    }
    if (currentI < 9) {
        possibleDirections.push(getCell(currentI + 1, currentJ));
    }
    if (currentJ > 0) {
        possibleDirections.push(getCell(currentI, currentJ - 1));
    }
    if (currentJ < 9) {
        possibleDirections.push(getCell(currentI, currentJ + 1));
    }

    const next = possibleDirections[Math.floor(Math.random() * possibleDirections.length)];

    removeWall(current, next);
    path.push(next);
    next.classList.add("path");
    current = next;
}
