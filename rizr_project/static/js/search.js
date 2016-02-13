// Your use of the YouTube API must comply with the Terms of Service:
// https://developers.google.com/youtube/terms

$(document).ready(function() {
	$('#url_submit').on("click",function() {
		var urlStr = $('#youtube_url').val();
		var linkArray = urlStr.split("=");
		var key = linkArray[1];
		var embedUrl = "http://www.youtube.com/embed/"+key+"?autoplay=0";
		$('#video_frame').prop('src', embedUrl);
		search(key);
		$("#results_wrapper").css("visibility","visible");
	});
});


function howOld(uplDateRaw) {
	var minutes = 1000 * 60;
	var hours = minutes * 60;
	var days = hours * 24;
	var years = days * 365;
	var newDate = new Date();
	var baseAge = newDate.getTime();
	var uplDate = new Date(uplDateRaw);
	console.log(uplDate);
	var uplAge = uplDate.getTime();
	var age = (baseAge-uplAge)/hours;
	return age
}

function expectedViews(ageFltHr, viewCountInt, likeCountInt, commentCountInt) {
	var viewsPerHr = viewCountInt/ageFltHr;
	//console.log(viewsPerHr);
	var likesPerHr = likeCountInt/ageFltHr;
	//console.log(likesPerHr);
	var commentsPerHr = commentCountInt/ageFltHr;
	//console.log(commentsPerHr);
	var expectedViewsCount = viewCountInt + Math.round(viewsPerHr * 3650);
	return expectedViewsCount;
	
}

// Helper function to display JavaScript value on HTML page.
function showResponse(response) {
	var titleStr = response.items[0].snippet.title;
	document.getElementById('title').innerHTML = "<b>Title: </b>" + titleStr;
	var dateStart = response.items[0].snippet.publishedAt;
	var ageFltHr = howOld(dateStart);
	var statisticsObj = response.items[0].statistics;
	var viewCountInt = parseInt(statisticsObj.viewCount);
	var likeCountInt = parseInt(statisticsObj.likeCount);
	var dislikeCountInt = parseInt(statisticsObj.dislikeCount);
	var favoriteCountInt = parseInt(statisticsObj.favoriteCount);
	var commentCountInt = parseInt(statisticsObj.commentCount);
    var expectedViewsNum = expectedViews(ageFltHr, viewCountInt, likeCountInt,commentCountInt);
	var responseString = JSON.stringify(response, '', 2);
	document.getElementById('full_response').innerHTML = responseString;
    document.getElementById('response').innerHTML = "<b>Expected Views: </b>" + expectedViewsNum;
}

// Called automatically when JavaScript client library is loaded.
function onClientLoad() {
    gapi.client.load('youtube', 'v3', onYouTubeApiLoad);
}

// Called automatically when YouTube API interface is loaded (see line 9).
function onYouTubeApiLoad() {
    // This API key is intended for use only in this lesson.
    // See https://goo.gl/PdPA1 to get a key for your own applications.
    gapi.client.setApiKey('AIzaSyD4K_G6FMUMHs-sBVQHaQDd0O_LRvJ7Whc');
    
}

function search(key) {
    // Use the JavaScript client library to create a search.list() API call.
    var request = gapi.client.youtube.videos.list({
        id: key,
        part: "snippet,statistics"
    });
    
    // Send the request to the API server,
    // and invoke onSearchRepsonse() with the response.
    request.execute(onSearchResponse);
}

// Called automatically with the response of the YouTube API request.
function onSearchResponse(response) {
    showResponse(response);
}