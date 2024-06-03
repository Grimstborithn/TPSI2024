$(function() {
    // Initialize the slider
    $("#slider").slider({
        min: 0,
        max: 100,
        slide: function(event, ui) {
            // Calculate the color based on the slider value
            var value = ui.value;
            var colorValue = 255 - Math.round(value * 2.55);
            var color = `rgb(${colorValue}, ${colorValue}, ${colorValue})`;
            // Apply the color to the elements
            $(".change-color").css("background-color", color);
        }
    });

    // Change background color of elements with class 'change-color'
    $("#changeColorButton").click(function() {
        $(".change-color").css("background-color", "yellow");
    });

    // Toggle visibility of the element with class 'toggle-element'
    $("#toggleButton").click(function() {
        $(".toggle-element").toggle();
    });
});