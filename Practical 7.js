$(document).ready(function () {
  // Attach a click event handler to all paragraphs with class 'clickable'
  $("p.clickable").on("click", function () {
    // Change the background color of the clicked paragraph
    $(this).css("background-color", "#d3ffd3");

    // Display a message in the paragraph itself
    $(this).text("You clicked this paragraph!");

    // Optionally, reset the paragraph background after 1 second
    setTimeout(() => {
      $(this).css("background-color", ""); // reset background
      $(this).text(
        "This is the " + $(this).index() + 1 + " paragraph. Click me!"
      ); // reset text
    }, 2000);
  });
});
