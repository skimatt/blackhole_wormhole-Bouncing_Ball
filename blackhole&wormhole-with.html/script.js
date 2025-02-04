// Select the canvas and set up context
const canvas = document.getElementById("simulationCanvas");
const ctx = canvas.getContext("2d");

// Set canvas dimensions to match the window
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Constants
const NUM_BALLS = 50;
const BLACK_HOLE_RADIUS = 50;
const WORMHOLE_RADIUS = 30;
const GRAVITY_STRENGTH = 0.5;
const SPEED_BOOST = 1.5;
const FRICTION = 0.99;

// Black hole and wormhole positions
const BLACK_HOLE_POS = { x: canvas.width / 4, y: canvas.height / 2 };
const WORMHOLE_POS = { x: (3 * canvas.width) / 4, y: canvas.height / 2 };

// Ball class
class Ball {
  constructor() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.vx = (Math.random() - 0.5) * 4;
    this.vy = (Math.random() - 0.5) * 4;
    this.radius = 10;
    this.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
  }

  update() {
    // Apply gravity towards the black hole
    const dx = BLACK_HOLE_POS.x - this.x;
    const dy = BLACK_HOLE_POS.y - this.y;
    const distance = Math.hypot(dx, dy);
    if (distance > 0) {
      const force = GRAVITY_STRENGTH / Math.max(distance, 1); // Avoid division by zero
      this.vx += (force * dx) / distance;
      this.vy += (force * dy) / distance;
    }

    // Update position
    this.x += this.vx;
    this.y += this.vy;

    // Apply friction
    this.vx *= FRICTION;
    this.vy *= FRICTION;

    // Check if the ball is inside the black hole
    if (distance < BLACK_HOLE_RADIUS) {
      this.x = WORMHOLE_POS.x;
      this.y = WORMHOLE_POS.y;
      this.vx *= SPEED_BOOST;
      this.vy *= SPEED_BOOST;
    }
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.closePath();
  }
}

// Create balls
const balls = [];
for (let i = 0; i < NUM_BALLS; i++) {
  balls.push(new Ball());
}

// Draw black hole and wormhole
function drawStaticObjects() {
  // Black hole
  ctx.beginPath();
  ctx.arc(
    BLACK_HOLE_POS.x,
    BLACK_HOLE_POS.y,
    BLACK_HOLE_RADIUS,
    0,
    Math.PI * 2
  );
  ctx.strokeStyle = "white";
  ctx.lineWidth = 2;
  ctx.stroke();
  ctx.closePath();

  // Wormhole
  ctx.beginPath();
  ctx.arc(WORMHOLE_POS.x, WORMHOLE_POS.y, WORMHOLE_RADIUS, 0, Math.PI * 2);
  ctx.strokeStyle = "green";
  ctx.lineWidth = 2;
  ctx.stroke();
  ctx.closePath();
}

// Animation loop
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Update and draw balls
  balls.forEach((ball) => {
    ball.update();
    ball.draw();
  });

  // Draw static objects
  drawStaticObjects();

  // Loop
  requestAnimationFrame(animate);
}

// Start animation
animate();

// Handle window resize
window.addEventListener("resize", () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  // Update black hole and wormhole positions
  BLACK_HOLE_POS.x = canvas.width / 4;
  BLACK_HOLE_POS.y = canvas.height / 2;
  WORMHOLE_POS.x = (3 * canvas.width) / 4;
  WORMHOLE_POS.y = canvas.height / 2;
});
