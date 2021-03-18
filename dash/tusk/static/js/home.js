$(document).ready(function() {
    $('.sidebar-button').click(function() {
        $(this).css("background-color", "#949798");
        $(this).css("color", "#2A2C2D");
        $(this).text("Requested");
    });
    $('.bi-heart').click(function() {
        $(this).css("color", "#D2452D")
    });
    $('.bi-bookmark').click(function() {
        $(this).css("color", "#5e76a1")
    });
    $('.bi-arrow-left-right').click(function() {
        $(this).css("color", "#5e76a1")
    });
});