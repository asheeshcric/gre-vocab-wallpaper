$(document).ready(function() {

  // Helpers //

  var randBetween = function(start, end) {
    return Math.floor(Math.random() * end) + start;
  };

  var stripTags = function(html) {
    return html.replace(/(<([^>]+)>)/ig, '').split(":")[0];
  };

  // Pronunciation //

  // Prepare <audio> tag for playback
  var setupAudioPlayer = function(audioUrl) {
    var $player =  $(".audio-playback");
    var player = $player[0]
    player.src = audioUrl;
    player.load();
    player.play();

    var playerClasses = "player-ready player-playing player-error";

    $player.on("playing", function() {
      $(".player").removeClass(playerClasses);
      $(".player").addClass("player-playing");
    });

    $player.on("ended", function() {
      $(".player").removeClass(playerClasses);
      $(".player").addClass("player-ready");
    });
  }

  // Retrieve audio pronunciation URL from Wordnik and trigger player setup
  var setupAudio = function(word) {
    // developers@magoosh.com account
    apiKey = "8e5956350987aa6b0521e0c4761074eabe07f42e9d8fd1492";
    apiUrl = "http://api.wordnik.com:80/v4/word.json/" + word + "/audio?useCanonical=true&limit=3&api_key=" + apiKey;
    $.ajax({
      url: apiUrl,
      success: function(data) {
        if (data.length) {
          audioUrl = data[0].fileUrl;
          setupAudioPlayer(audioUrl);
        }
      }
    });
  }

  // Main App //

  // Retrieve random word and update HTML
  var successCallback = function(data) {
    wordCount = data.length - 1;
    wordIndex = randBetween(0, wordCount);
    wordData = data[wordIndex].back;

    $(".loading").hide();

    $("#word").text(wordData[0].content);
    $(".page-title").html(wordData[0].content + " (" + stripTags(wordData[1].content) + ")");
    $("#definition").html(wordData[1].content);
    $("#sentence").html(wordData[2].content);
    $("#pronounce").data('word', wordData[0].content)

    if (!navigator.onLine) {
      $(".player").removeClass("player-ready");
      $(".player").addClass("player-error");
      $(".player").attr("title", "Pronunciation requires an internet connection.")
    }
  };

  // Attach event listener to pronunciation button
  $("#pronounce").click(function(e) {
    var word = $(e.currentTarget).data('word');

    // Only setup audio player if they have internet
    if (navigator.onLine) {
      // TODO: add a URL cache here to avoid multiple API calls
      setupAudio(word);
    }
  });

  // Load word content from JSON file
  $.getJSON('words.json', successCallback);

});