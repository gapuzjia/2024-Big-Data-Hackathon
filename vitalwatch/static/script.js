// Parse the prize data from the script tag in the HTML
const prizeDataElement = document.getElementById('prize-data');
const prizeList = JSON.parse(prizeDataElement.textContent);

// Set up the canvas and variables for the spinning wheel
const canvas = document.getElementById('wheelCanvas');
const ctx = canvas.getContext('2d');
let arcSize = (2 * Math.PI) / prizeList.length;
let startAngle = 0;
let spinAngle = 0;
let spinning = false;

// Function to draw the wheel with prizes
function drawWheel() {
    // Clear the canvas before drawing
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    for (let i = 0; i < prizeList.length; i++) {
        const angle = startAngle + i * arcSize;
        ctx.beginPath();
        ctx.arc(canvas.width / 2, canvas.height / 2, canvas.width / 2, angle, angle + arcSize);
        ctx.lineTo(canvas.width / 2, canvas.height / 2);
        ctx.fillStyle = i % 2 === 0 ? '#FFCC00' : '#FF9900';
        ctx.fill();
        ctx.stroke();

        // Draw the prize text on the wheel
        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height / 2);
        ctx.rotate(angle + arcSize / 2);
        
        // Calculate text width
        ctx.font = '16px Arial';
        const textWidth = ctx.measureText(prizeList[i]).width;

        // Adjust the position based on text width
        const textXPosition = canvas.width / 4 - textWidth / 2; // Center the text
        ctx.fillStyle = 'black';
        ctx.fillText(prizeList[i], textXPosition, 0);
        ctx.restore();
    }
}

// Function to spin the wheel
function spinWheel() {
    if (!spinning) {
        spinning = true;
        spinAngle = Math.random() * 2000 + 1000; // Random spin angle between 1000 and 3000 degrees
        animateSpin();
    }
}

// Function to animate the spinning of the wheel
function animateSpin() {
    spinAngle *= 0.97; // Slow down the spin over time
    startAngle += spinAngle * Math.PI / 180; // Rotate the wheel
    drawWheel();

    if (spinAngle > 0.1) {
        requestAnimationFrame(animateSpin);
    } else {
        spinning = false;
        determinePrize();
    }
}

// Function to determine which prize the user has won
function determinePrize() {
    const winningIndex = Math.floor((startAngle % (2 * Math.PI)) / arcSize);
    const selectedPrize = prizeList[prizeList.length - 1 - winningIndex];
    alert(`Congratulations! You won: ${selectedPrize}`);
}

// Event listener to start the spin when the button is clicked
document.getElementById('spinButton').addEventListener('click', spinWheel);

// Initial draw of the wheel when the page loads
drawWheel();
