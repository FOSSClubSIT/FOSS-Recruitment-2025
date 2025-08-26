// Grab canvas from HTML
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Grid cell size
const cellSize = 25;

// Example Pac-Man style layout
// 1 = wall, 0 = pellet, 2 = empty space
const layout = [
  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
  1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,
  1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,
  1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,
  1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,
  1,0,0,0,0,1,0,0,0,2,2,0,0,0,0,1,0,0,0,1,
  1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,
  1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,
  1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,
  1,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,1,
  1,0,1,1,0,1,1,1,0,2,2,0,1,1,1,0,1,1,0,1,
  1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,
  1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,
  1,0,0,0,0,1,0,0,0,2,2,0,0,0,0,1,0,0,0,1,
  1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,
  1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,
  1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,
  1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
];

const cols = 20;
const rows = layout.length / cols;

// Set canvas size based on grid
canvas.width = cols * cellSize;
canvas.height = rows * cellSize;

// --- Pac-Man spawn (center of board) ---
const spawnRow = Math.floor(rows / 2);
const spawnCol = Math.floor(cols / 2);

// Pac-Man state
let pacman = {
  x: spawnCol,
  y: spawnRow,
  radius: cellSize / 2 - 3
};

// Function to draw grid
function drawGrid() {
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      let cell = layout[row * cols + col];

      if (cell === 1) {
        // Wall = blue square
        ctx.fillStyle = "blue";
        ctx.fillRect(col * cellSize, row * cellSize, cellSize, cellSize);
      } else if (cell === 0) {
        // Pellet = white circle
        ctx.beginPath();
        ctx.arc(
          col * cellSize + cellSize / 2,
          row * cellSize + cellSize / 2,
          4, 0, Math.PI * 2
        );
        ctx.fillStyle = "white";
        ctx.fill();
      } else {
        // Empty = black background
        ctx.fillStyle = "black";
        ctx.fillRect(col * cellSize, row * cellSize, cellSize, cellSize);
      }
    }
  }

  // Highlight spawn cell (so you always know where Pac-Man starts)
  ctx.fillStyle = "gray";
  ctx.lineWidth = 2;
  ctx.fillRect(spawnCol * cellSize, spawnRow * cellSize, cellSize, cellSize);
}

// Function to draw Pac-Man
function drawPacman() {
  ctx.beginPath();
  ctx.arc(
    pacman.x * cellSize + cellSize / 2,
    pacman.y * cellSize + cellSize / 2,
    pacman.radius,
    0.25 * Math.PI,   // open mouth
    1.75 * Math.PI    // open mouth
  );
  ctx.lineTo(pacman.x * cellSize + cellSize / 2, pacman.y * cellSize + cellSize / 2);
  ctx.fillStyle = "yellow";
  ctx.fill();
}

// Start game
function startGame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height); // clear old frame
  drawGrid();
  drawPacman();
}

// Run once
startGame();
