

// Function to fade out an element as the user scrolls
function fadeOutOnScroll(element) {
  // Check if the element exists
  if (!element) {
    return; // Exit the function if the element doesn't exist
  }
  
  // Calculate the distance from the top of the viewport to the top of the element
  var distanceToTop = window.scrollY + element.getBoundingClientRect().top;
  // Get the height of the element
  var elementHeight = element.offsetHeight;
  // Get the current vertical scroll position of the document
  var scrollTop = document.documentElement.scrollTop;
  
  // Initialize opacity to 1 (fully visible)
  var opacity = 1;
  
  // If the current scroll position is below the top of the element
  if (scrollTop > distanceToTop) {
    // Calculate the opacity based on how far the user has scrolled past the element
    opacity = 1 - (scrollTop - distanceToTop) / elementHeight;
  }
  
  // Ensure that opacity is not less than 0 (fully transparent)
  if (opacity >= 0) {
    // Set the opacity of the element
    element.style.opacity = opacity;
  }
}
