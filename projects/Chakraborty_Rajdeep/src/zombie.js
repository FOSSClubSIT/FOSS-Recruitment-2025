const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let gameRunning = false;
let score = 0;

// Player
const player = {
  x: canvas.width / 2,
  y: canvas.height / 2,
  size: 20,
  speed: 4,
  hp: 100
};

// Bullets
let bullets = [];

// Zombies
let zombies = [];

// Input
let keys = {};
window.addEventListener("keydown", e => (keys[e.key] = true));
window.addEventListener("keyup", e => (keys[e.key] = false));

canvas.addEventListener("click", e => {
  if (!gameRunning) return;
  const angle = Math.atan2(e.clientY - player.y, e.clientX - player.x);
  bullets.push({
    x: player.x,
    y: player.y,
    dx: Math.cos(angle) * 7,
    dy: Math.sin(angle) * 7,
    size: 5
  });
});

// Start Button
document.getElementById("startBtn").addEventListener("click", () => {
  gameRunning = true;
  score = 0;
  player.hp = 100;
  bullets = [];
  zombies = [];
  document.getElementById("menu").style.display = "none";
  loop();
});

// Spawn zombies
function spawnZombie() {
  const edge = Math.floor(Math.random() * 4);
  let x, y;
  if (edge === 0) { x = 0; y = Math.random() * canvas.height; }
  if (edge === 1) { x = canvas.width; y = Math.random() * canvas.height; }
  if (edge === 2) { x = Math.random() * canvas.width; y = 0; }
  if (edge === 3) { x = Math.random() * canvas.width; y = canvas.height; }

  zombies.push({
    x,
    y,
    size: 20,
    speed: 1 + Math.random() * 1.5
  });
}
setInterval(() => { if (gameRunning) spawnZombie(); }, 1500);

// Update
function update() {
  // Move player
  if (keys["w"] || keys["ArrowUp"]) player.y -= player.speed;
  if (keys["s"] || keys["ArrowDown"]) player.y += player.speed;
  if (keys["a"] || keys["ArrowLeft"]) player.x -= player.speed;
  if (keys["d"] || keys["ArrowRight"]) player.x += player.speed;

  // Keep inside canvas
  player.x = Math.max(player.size, Math.min(canvas.width - player.size, player.x));
  player.y = Math.max(player.size, Math.min(canvas.height - player.size, player.y));

  // Move bullets
  bullets.forEach((b, i) => {
    b.x += b.dx;
    b.y += b.dy;
    if (b.x < 0 || b.y < 0 || b.x > canvas.width || b.y > canvas.height) {
      bullets.splice(i, 1);
    }
  });

  // Move zombies
  zombies.forEach((z, zi) => {
    const angle = Math.atan2(player.y - z.y, player.x - z.x);
    z.x += Math.cos(angle) * z.speed;
    z.y += Math.sin(angle) * z.speed;

    // Collision with player
    const dist = Math.hypot(player.x - z.x, player.y - z.y);
    if (dist < player.size + z.size) {
      player.hp -= 0.5;
      if (player.hp <= 0) {
        gameRunning = false;
        document.getElementById("menu").style.display = "block";
      }
    }

    // Collision with bullets
    bullets.forEach((b, bi) => {
      const d = Math.hypot(b.x - z.x, b.y - z.y);
      if (d < z.size + b.size) {
        zombies.splice(zi, 1);
        bullets.splice(bi, 1);
        score += 10;
      }
    });
  });

  // Update UI
  document.getElementById("score").innerText = "Score: " + score;
  document.getElementById("health").style.width = player.hp + "%";
}

// Draw
function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Player
  ctx.fillStyle = "cyan";
  ctx.beginPath();
  ctx.arc(player.x, player.y, player.size, 0, Math.PI * 2);
  ctx.fill();

  // Bullets
  ctx.fillStyle = "yellow";
  bullets.forEach(b => {
    ctx.beginPath();
    ctx.arc(b.x, b.y, b.size, 0, Math.PI * 2);
    ctx.fill();
  });

  // Zombies
  ctx.fillStyle = "green";
  zombies.forEach(z => {
    ctx.beginPath();
    ctx.arc(z.x, z.y, z.size, 0, Math.PI * 2);
    ctx.fill();
  });
}

// Loop
function loop() {
  if (!gameRunning) return;
  update();
  draw();
  requestAnimationFrame(loop);
}
