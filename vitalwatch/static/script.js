document.addEventListener("DOMContentLoaded", () => 
{
    // Initialize the points display and set default points to 20 (home page)
    let currentPoints = 10;
    const pointsDisplay = document.getElementById('points'); 
    const homeSpinButton = document.getElementById('spinButton'); // For home page points (if applicable)
    const requiredPoints = 10;
    const progressBar = document.getElementById('progress-bar'); // Progress bar element

    // Initial points display update
    if (pointsDisplay) 
    {
        pointsDisplay.textContent = currentPoints;
    }

    // Function to update points and progress bar when checkboxes are interacted with (home page)
    function updatePoints() 
    {
        const checkboxes = document.querySelectorAll('input[type="checkbox"][data-points]');
        let pointsFromTasks = 0;
        let completedTasks = 0;

        // Calculate total points from checked checkboxes and count completed tasks
        checkboxes.forEach((checkbox) => 
        {
            let pointsValue = parseInt(checkbox.getAttribute('data-points'), 10);
            if (isNaN(pointsValue)) 
            {
                pointsValue = 0;  // Fallback to 0 if the attribute is missing or invalid
            }

            if (checkbox.checked) 
            {
                pointsFromTasks += pointsValue;
                completedTasks++; // Count the checked tasks
            }
        });

        // Update the current points
        currentPoints = currentPoints + pointsFromTasks;
        console.log("Updated Points: ", currentPoints); // Log current points for debugging

        // Update points display
        if (pointsDisplay) 
        {
            pointsDisplay.textContent = currentPoints;
        }

        // Enable or disable spin button based on points
        if (homeSpinButton) 
        {
            homeSpinButton.disabled = currentPoints < requiredPoints;
        }

        // Update progress bar based on completed tasks
        const totalTasks = checkboxes.length;
        const progressPercentage = (completedTasks / totalTasks) * 100;
        if (progressBar) 
        {
            progressBar.style.width = `${progressPercentage}%`; // Update progress bar width
        }

        console.log(`Completed ${completedTasks} out of ${totalTasks} tasks`);
    }

    // Add event listeners to checkboxes for updating points when state changes (home page)
    const checkboxes = document.querySelectorAll('input[type="checkbox"][data-points]');
    checkboxes.forEach((checkbox) => 
    {
        checkbox.addEventListener('change', updatePoints);
    });

    // Initial run to ensure the points display is set correctly
    updatePoints();
});

    // Rewards page script (wheel functionality)
    document.addEventListener("DOMContentLoaded", () => 
    {
        // Spin button for the rewards page
        const rewardsSpinButton = document.getElementById('spinButton'); 
        const pointsDisplay = document.getElementById('points'); // Points display for the rewards page
        let currentPoints = parseInt(pointsDisplay?.textContent) || 20; // Assume points carry over from the home page
        const requiredPoints = 10;

        // Parse the prize data from the script tag in the HTML (rewards page)
        const prizeDataElement = document.getElementById('prize-data');
        let prizeList = [];
        if (prizeDataElement) 
        {
            prizeList = JSON.parse(prizeDataElement.textContent);
        }

        // Set up the canvas and variables for the spinning wheel (rewards page)
        const canvas = document.getElementById('wheelCanvas');
        const ctx = canvas ? canvas.getContext('2d') : null;
        let arcSize = prizeList.length > 0 ? (2 * Math.PI) / prizeList.length : 0;
        let startAngle = 0;
        let spinAngle = 0;
        let spinning = false;

        // Function to draw the wheel with prizes (rewards page)
        function drawWheel() 
        {
            if (!ctx) return; // If canvas or context is not available, exit the function
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas before drawing

            for (let i = 0; i < prizeList.length; i++) 
            {
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

        // Function to spin the wheel (rewards page)
        function spinWheel() 
        {
            if (!spinning && currentPoints >= requiredPoints) 
            {
                spinning = true;
                spinAngle = Math.random() * 2000 + 1000; // Random spin angle between 1000 and 3000 degrees
                animateSpin();
            }
        }

        // Function to animate the spinning of the wheel (rewards page)
        function animateSpin() 
        {
            spinAngle *= 0.97; // Slow down the spin over time
            startAngle += spinAngle * Math.PI / 180; // Rotate the wheel
            drawWheel();

            if (spinAngle > 0.1) 
            {
                requestAnimationFrame(animateSpin);
            } 
            else 
            {
                spinning = false;
                determinePrize();
            }
        }

        // Function to determine which prize the user has won (rewards page)
        function determinePrize() 
        {
            const winningIndex = Math.floor((startAngle % (2 * Math.PI)) / arcSize);
            const selectedPrize = prizeList[prizeList.length - 1 - winningIndex];
            alert(`Congratulations! You won: ${selectedPrize}`);
        }

        // Event listener to start the spin when the button is clicked (rewards page)
        if (rewardsSpinButton) 
        {
            rewardsSpinButton.addEventListener('click', spinWheel);
        }

        // Initial draw of the wheel when the page loads (rewards page)
        if (ctx) 
        {
            drawWheel();
        }
});
