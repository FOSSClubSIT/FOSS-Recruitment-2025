const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const cellSize = 25;

// Bigger 20x20 grid
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
  [1,0,0,0,0,1,0,0,0,2,0,0,0,0,0,1,0,0,0,1], 
  [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1],
  [1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1],
  [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
  [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
];


canvas.width = initialGrid[0].length * cellSize;
canvas.height = initialGrid.length * cellSize;

let grid, pacman, score;
let direction = {x:0, y:0};
let lastMoveTime = 0;
const moveDelay = 200;
let gameLoopId;

function drawGrid() {
  for (let y=0; y<grid.length; y++){
    for (let x=0; x<grid[y].length; x++){
      if (grid[y][x] === 1){
        ctx.fillStyle = "blue";
        ctx.fillRect(x*cellSize, y*cellSize, cellSize, cellSize);
      } else if (grid[y][x] === 0){
        ctx.fillStyle = "white";
        ctx.beginPath();
        ctx.arc(x*cellSize + cellSize/2, y*cellSize + cellSize/2, 4, 0, 2*Math.PI);
        ctx.fill();
      } else if (grid[y][x] === 2){
        ctx.strokeStyle = "yellow";
        ctx.lineWidth = 2;
        ctx.strokeRect(x*cellSize, y*cellSize, cellSize, cellSize);
      }
    }
  }
}

function drawPacman(){
  ctx.beginPath();
  ctx.arc(pacman.x*cellSize + cellSize/2, pacman.y*cellSize + cellSize/2, cellSize/2.5, 0.2*Math.PI, 1.8*Math.PI);
  ctx.lineTo(pacman.x*cellSize + cellSize/2, pacman.y*cellSize + cellSize/2);
  ctx.fillStyle = "yellow";
  ctx.fill();
}

function findSpawn(){
  for (let y=0; y<grid.length; y++){
    for (let x=0; x<grid[y].length; x++){
      if (grid[y][x]===2) return {x,y};
    }
  }
  return {x:1,y:1};
}

document.addEventListener("keydown", e=>{
  if(e.key==="ArrowUp") direction={x:0,y:-1};
  if(e.key==="ArrowDown") direction={x:0,y:1};
  if(e.key==="ArrowLeft") direction={x:-1,y:0};
  if(e.key==="ArrowRight") direction={x:1,y:0};
});

function updateGame(currentTime){
  if(currentTime - lastMoveTime < moveDelay) return;
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

  if(!grid.flat().includes(0)) gameOver();
}

function gameLoop(timestamp){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  drawGrid();
  drawPacman();
  updateGame(timestamp);
  gameLoopId=requestAnimationFrame(gameLoop);
}

function gameOver(){
  document.getElementById("gameOverScreen").style.visibility="visible";
}

function startGame(){
  grid = initialGrid.map(row=>[...row]); // deep copy
  pacman=findSpawn();
  score=0;
  direction={x:0,y:0};
  document.getElementById("score").innerText="Score: "+score;
  document.getElementById("gameOverScreen").style.visibility="hidden";
  lastMoveTime=0;
  cancelAnimationFrame(gameLoopId);
  requestAnimationFrame(gameLoop);
}

document.getElementById("restartBtn").onclick=startGame;

startGame();
