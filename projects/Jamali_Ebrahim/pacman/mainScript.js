const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const cellSize = 25;


// 20x20 grid with single spawn point
const initialGrid = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
  [1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1],
  [1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1],
  [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
  [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
  [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
  [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
  [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
  [1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1],
  [1,0,0,0,0,1,0,0,0,2,0,0,0,0,0,1,0,0,0,1], // spawn point at 10th column
  [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1],
  [1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1],
  [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
  [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
];


canvas.width = initialGrid[0].length * cellSize;
canvas.height = initialGrid.length * cellSize;          // Pac-Man speed

let grid, pacman, score;
let direction = {x:0, y:0};
let lastMoveTime = 0;
const moveDelay = 200;
let gameLoopId;

// Enemies
let enemies = [];
const enemyCount = 3;
let lastEnemyMoveTime = 0;
const enemyMoveDelay = 500;
const enemyPositions = [
  {x:1, y:1},
  {x:18, y:1},
  {x:1, y:18}
];

// Draw ghost shape
function drawGhost(enemy){
  const x = enemy.x * cellSize;
  const y = enemy.y * cellSize;
  ctx.fillStyle = enemy.color;
  ctx.beginPath();
  ctx.arc(x + cellSize/2, y + cellSize/2, cellSize/2, Math.PI, 0);
  ctx.fill();
  ctx.fillRect(x, y + cellSize/2, cellSize, cellSize/2);
}

// Move enemies chasing Pac-Man
function moveEnemies(){
  enemies.forEach(e=>{
    let dx = pacman.x - e.x;
    let dy = pacman.y - e.y;

    // Decide best direction to move (prioritize axis with greater distance)
    let moveOptions = [];
    if(Math.abs(dx) > Math.abs(dy)){
      moveOptions.push({x:Math.sign(dx), y:0});
      if(dy!==0) moveOptions.push({x:0, y:Math.sign(dy)});
    } else {
      moveOptions.push({x:0, y:Math.sign(dy)});
      if(dx!==0) moveOptions.push({x:Math.sign(dx), y:0});
    }

    // Filter valid moves (not walls)
    const validMoves = moveOptions.filter(d=>{
      const nx = e.x + d.x;
      const ny = e.y + d.y;
      return ny>=0 && ny<grid.length && nx>=0 && nx<grid[0].length && grid[ny][nx]!==1;
    });

    if(validMoves.length>0){
      const move = validMoves[Math.floor(Math.random()*validMoves.length)];
      e.x += move.x;
      e.y += move.y;
    }

    // Check collision
    if(e.x === pacman.x && e.y === pacman.y) gameOver();
  });
}

// Draw grid
function drawGrid(){
  for(let row=0; row<grid.length; row++){
    for(let col=0; col<grid[0].length; col++){
      let cell = grid[row][col];
      if(cell===1){
        ctx.fillStyle="blue";
        ctx.fillRect(col*cellSize, row*cellSize, cellSize, cellSize);
      } else if(cell===0){
        ctx.fillStyle="white";
        ctx.beginPath();
        ctx.arc(col*cellSize + cellSize/2, row*cellSize + cellSize/2, 4, 0, Math.PI*2);
        ctx.fill();
      } else {
        ctx.fillStyle="black";
        ctx.fillRect(col*cellSize, row*cellSize, cellSize, cellSize);
      }
    }
  }
}

// Draw Pac-Man
function drawPacman(){
  ctx.fillStyle="yellow";
  ctx.beginPath();
  ctx.arc(pacman.x*cellSize + cellSize/2, pacman.y*cellSize + cellSize/2, cellSize/2, 0.25*Math.PI, 1.75*Math.PI);
  ctx.lineTo(pacman.x*cellSize + cellSize/2, pacman.y*cellSize + cellSize/2);
  ctx.fill();
}

// Find spawn
function findSpawn(){
  for(let y=0; y<grid.length; y++){
    for(let x=0; x<grid[0].length; x++){
      if(grid[y][x]===2) return {x,y};
    }
  }
}

// Keyboard input
document.addEventListener("keydown", e=>{
  if(e.key==="ArrowUp") direction={x:0,y:-1};
  if(e.key==="ArrowDown") direction={x:0,y:1};
  if(e.key==="ArrowLeft") direction={x:-1,y:0};
  if(e.key==="ArrowRight") direction={x:1,y:0};
});

let gameRunning = true;
function updateGame(currentTime){
  if(!gameRunning) return;
  // --- Pac-Man movement ---
  if(currentTime - lastMoveTime >= moveDelay){
    lastMoveTime = currentTime;

    const newX = pacman.x + direction.x;
    const newY = pacman.y + direction.y;

    if(newY>=0 && newY<grid.length && newX>=0 && newX<grid[0].length && grid[newY][newX]!==1){
      pacman.x=newX;
      pacman.y=newY;

      if(grid[newY][newX]===0){
        grid[newY][newX]=-1;
        score++;
        document.getElementById("score").innerText="Score: "+score;
      }
    }

    if(!grid.flat().includes(0)) gameWin();
  }

  // --- Enemy movement ---
  if(currentTime - lastEnemyMoveTime >= enemyMoveDelay){
    lastEnemyMoveTime = currentTime;
    moveEnemies();
  }
}


// Main game loop
function gameLoop(timestamp){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  drawGrid();
  drawPacman();
  enemies.forEach(drawGhost);
  updateGame(timestamp);
  requestAnimationFrame(gameLoop);
}

// Game over
function gameOver(){
  gameRunning = false;  // stop movement and scoring
  document.getElementById("game-container").style.display = "none"; // hide game
  document.getElementById("gameOverScreen").style.display = "block"; // show game over
  document.getElementById("finalScore").innerText = "Final Score: " + score;
}

function gameWin(){
  gameRunning = false; // stop everything
  document.getElementById("game-container").style.display = "none"; // hide game
  document.getElementById("gameOverScreen").style.display = "none"; // hide game over
  document.getElementById("gameWinScreen").style.display = "block"; // show win screen
  document.getElementById("winScore").innerText = "Final Score: " + score;
}

document.getElementById("winRestartBtn").onclick = startGame;


// Start / restart
function startGame(){
  gameRunning = true; // allow updates again
  document.getElementById("game-container").style.display = "flex";  // show game
  document.getElementById("gameOverScreen").style.display = "none";  // hide game over
  document.getElementById("gameWinScreen").style.display = "none";   // hide win screen
  // reset game state
  grid = initialGrid.map(row => [...row]);
  pacman = findSpawn();
  score = 0;
  direction = {x:0, y:0};
  document.getElementById("score").innerText = "Score: " + score;

  enemies = enemyPositions.map(p => ({x:p.x, y:p.y, color:"red"}));
  lastMoveTime = 0;
  lastEnemyMoveTime = 0;

  requestAnimationFrame(gameLoop);
}


document.getElementById("restartBtn").onclick=startGame;

startGame();
