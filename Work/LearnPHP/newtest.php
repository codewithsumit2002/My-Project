<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title></title>
    <style type="text/css">
    /* Add styles for the slider container */
    .slider-container {
        width: 90%;
        margin: 10px auto;
        overflow: hidden;
    }

    /* Add styles for the slider */
    .slider {
        display: flex;
        transition: 0.5s;
    }

    /* Add styles for the slides */
    .slide {
        flex: 1;
        display: none;
    }

    /* Add styles for the active slide */
    .slide.active {
        display: block;
    }

    /* Add styles for the images */
    .slide img {
        width: 100%;
        height: 93vh;
        object-fit: cover;
    }
    </style>
</head>

<body>

    <!-- The slider container -->
    <div class="slider-container">
        <!-- The slider -->
        <div class="slider">
            <!-- The slides -->
            <div class="slide active">
                <img src="pooja.jpeg" alt="Image 1">
            </div>
            <div class="slide">
                <img src="neeraj.jpeg" alt="Image 2">
            </div>
            <div class="slide">
                <img src="sumit2.jpeg" alt="Image 3">
            </div>
            <!-- Add more slides as needed -->
        </div>
    </div>

    <script>
    // Get the slider and slides
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');

    // Set the interval for automatic sliding
    const interval = 3000; // 3 seconds

    // Set the current slide index
    let currentSlide = 0;

    // Function to slide to the next slide
    function nextSlide() {
        // Remove the active class from the current slide
        slides[currentSlide].classList.remove('active');

        // Increment the current slide index
        currentSlide = (currentSlide + 1) % slides.length;

        // Add the active class to the next slide
        slides[currentSlide].classList.add('active');
    }

    // Set the interval for automatic sliding
    setInterval(nextSlide, interval);
    </script>
</body>

</html>