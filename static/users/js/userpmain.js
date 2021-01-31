(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });

})(jQuery);
$(document).ready(function(){
	// Prepare the preview for profile picture
		$("#wizard-picture").change(function(){
			readURL(this);
		});
	});
	function readURL(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();
	
			reader.onload = function (e) {
				$('#wizardPicturePreview').attr('src', e.target.result).fadeIn('slow');
			}
			reader.readAsDataURL(input.files[0]);
		}
	}